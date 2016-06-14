from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.contrib.auth.admin import User


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    main_content = RichTextUploadingField(blank=True)
    ingress_content = RichTextUploadingField(blank=True)

    pub_date = models.DateTimeField('Publication date', default=timezone.now)
    thumbnail = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_class():
        return "Article"

    class Meta:
        app_label = 'news'
        ordering = ('-pub_date',)


class Event(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    main_content = RichTextUploadingField(blank=True)
    ingress_content = RichTextUploadingField(blank=True)
    pub_date = models.DateTimeField('Publication date', default=timezone.now)
    thumbnail = models.CharField(max_length=200, blank=True)

    registration = models.BooleanField(default=False)
    max_limit = models.PositiveIntegerField(blank=True, default=0)
    registered_users = models.PositiveIntegerField(blank=True, default=0)

    time_start = models.DateTimeField('Start time')
    time_end = models.DateTimeField('End time')
    place = models.CharField(max_length=100, verbose_name='Place', blank=True)
    place_href = models.CharField(max_length=200, verbose_name='Place URL', blank=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_class():
        return "Event"

    def register_user(self):
        if self.registered_users < self.max_limit:
            self.registered_users += 1
            return True
        else:
            return False

    class Meta:
        app_label = 'news'
        ordering = ("-time_start",)


class Upload(models.Model):
    title = models.CharField(max_length=100, verbose_name='Filnavn')
    time = models.DateTimeField(default=timezone.now, verbose_name='Tittel')
    file = models.FileField(upload_to='uploads')
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'news'


class EventRegistration(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username + " registered on: " + self.event.title + " [{}]".format(self.event.pk)
