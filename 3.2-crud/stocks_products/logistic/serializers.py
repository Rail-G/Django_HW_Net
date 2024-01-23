from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']

class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)
    class Meta:
        model = Stock
        fields = ['address', 'positions']
    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        for i in positions:
            product = i.get('product')
            quantity = i.get('quantity')
            price = i.get('price')
            StockProduct.objects.create(stock=stock, product=product, quantity=quantity, price=price)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for i in positions:
            quantity = i.get('quantity')
            product = i.get('product')
            price = i.get('price')
            StockProduct.objects.update_or_create(stock=stock, product=product, defaults={'stock': stock, 'product': product, 'quantity': quantity, 'price': price})

        return stock

