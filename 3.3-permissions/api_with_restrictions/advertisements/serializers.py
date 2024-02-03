from django.contrib.auth.models import User
from rest_framework import serializers
from django_filters.filters import DateFromToRangeFilter
from advertisements.models import Advertisement, FavoriteAdvertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )
    created_at = DateFromToRangeFilter()
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )
        

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data): 
        """Метод для валидации. Вызывается при создании и обновлении."""
        if Advertisement.objects.filter(creator=self.context['request'].user, status='OPEN').count() <= 10 or data['status'] in ['CLOSED', 'DRAFT']:
            return data
        raise serializers.ValidationError('Превышен лимит в 10 открытых постов, пожалуйста, закройте одну, чтобы добавить новую')

class FavoriteAdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для избранного объявления."""
    author = UserSerializer(read_only=True)
    favorite_id = AdvertisementSerializer(read_only=True)  

    class Meta:
        model = FavoriteAdvertisement
        fields = ['id', 'author', 'favorite_id']  


    def create(self, validated_data):
        advertisement_id = self.context['request'].data.get('favorite_id')
        advertisement = Advertisement.objects.get(pk=advertisement_id)
        if self.context['request'].user == advertisement.creator:
            raise serializers.ValidationError({'error': 'This is your add'})
        validated_data['favorite_id'] = advertisement
        validated_data['author'] = self.context['request'].user
        print(self.context['request'].user)
        return super().create(validated_data)