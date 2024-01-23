from django.contrib import admin
from .models import Product, Stock, StockProduct

admin.site.register([Product, Stock, StockProduct])
