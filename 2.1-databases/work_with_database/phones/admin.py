from django.contrib import admin
from .models import Phone

class MyPhoneAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Phone, MyPhoneAdmin)
