from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAuthor
from .models import Advertisement, FavoriteAdvertisement, AdvertisementStatusChoices
from .serializers import AdvertisementSerializer, FavoriteAdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AdvertisementFilter
from django.db.models import Q
from rest_framework.response import Response
from django.contrib.auth.models import AnonymousUser
from rest_framework.decorators import action

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in  ["update", "partial_update", 'destroy']:
            return [IsAuthenticated(), IsAuthor()]
        return []
    
    def list(self, request):
        # status = request.GET.get('status', None)
        # created_at = request.GET.get('created_at_before', '')
        queryset = self.filter_queryset(self.get_queryset())
        user = self.request.user
        if request.user == AnonymousUser():
            queryset = queryset.filter(~Q(status=AdvertisementStatusChoices.DRAFT))
        else:
            queryset = queryset.filter(Q(status__in=[AdvertisementStatusChoices.OPEN, AdvertisementStatusChoices.CLOSED]) | (Q(status=AdvertisementStatusChoices.DRAFT) & Q(creator=user)))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
class FavoriteViewSet(ModelViewSet):
    """ViewSet для избранного."""
    queryset = FavoriteAdvertisement.objects.all()
    serializer_class = FavoriteAdvertisementSerializer
    filter_backends = [DjangoFilterBackend]

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'delete']:
            return [IsAuthenticated()]
        return []