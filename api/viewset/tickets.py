from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..seralizers import *
from django.conf import settings
from django_filters.rest_framework import FilterSet

from rest_framework.permissions import IsAuthenticated


class TicketFilter(FilterSet):
    class Meta:
        model = Ticket
        fields = {
            'title': settings.FILTER_STRING_MODELS,
            'created_time': settings.FILTER_TIME_MODELS,
            'assignee': settings.FILTER_EXACT_MODELS,
            'created_by': settings.FILTER_EXACT_MODELS,
            'Status': settings.FILTER_EXACT_MODELS,
        }


class TicketViewSet(ModelViewSet):
    serializer_class = TicketSerializer
    filterset_class = TicketFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
            return Ticket.objects.all()