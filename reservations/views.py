import datetime

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import DetailView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from reservations.forms import ReservationForm
from reservations.models import Reservation, Queue
from reservations.serializers import ReservationSerializer


class QueueDetailView(DetailView):
    model = Queue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': ReservationForm()
        })
        return context


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = get_object_or_404(Reservation, pk=kwargs['pk'])
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('reservations:queue_detail', kwargs={'pk': kwargs['pk']}))

    def perform_create(self, serializer):
        parent_queue = Queue.objects.get(pk=self.kwargs['pk'])
        serializer.save(parent_queue=parent_queue, user=self.request.user)

    def get_queryset(self):
        start = datetime.datetime.strptime(self.request.GET['start'], '%Y-%m-%dT%H:%M:%S').date()
        end = datetime.datetime.strptime(self.request.GET['end'], '%Y-%m-%dT%H:%M:%S').date()
        queryset = Reservation.objects.filter(
            # Q() lets you combine queries
            Q(parent_queue_id=self.kwargs['pk'])
            & Q(start_date__gte=start)
            & Q(end_date__lte=end)
        )
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
