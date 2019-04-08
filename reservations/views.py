from django.db.models import Q
from django.shortcuts import get_object_or_404
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
            'form': ReservationForm(),  # parent_queue=self.kwargs['pk']
        })
        return context


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data.update({
            'parent_queue': kwargs['pk'],
        })
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        start = self.request.GET['start']
        end = self.request.GET['end']
        queryset = Reservation.objects.filter(  # Q() lets you combine queries
            Q(parent_queue_id=self.kwargs['pk'])
            & Q(start__gte=start)
            & Q(end__lte=end)
        )
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
