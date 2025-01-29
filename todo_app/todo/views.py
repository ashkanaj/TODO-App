from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from django.utils.dateparse import parse_date, parse_datetime
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ['title', 'description']


    def get_queryset(self):
        queryset = Task.objects.all()
        due_date = self.request.query_params.get('due_date', None)
        created_at = self.request.query_params.get('created_at', None)

        if due_date:
            queryset = queryset.filter(due_date=parse_date(due_date))

        if created_at:
            queryset = queryset.filter(created_at=parse_datetime(created_at))

        return queryset