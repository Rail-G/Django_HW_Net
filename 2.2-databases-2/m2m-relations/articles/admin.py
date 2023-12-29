from django.contrib import admin
from django.forms import BaseInlineFormSet, ValidationError

from .models import Article, Scope, Tag

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main'] is True:
                count += 1
        if count < 1:
            raise ValidationError('Добавьте один главный тег')
        elif count > 1:
            raise ValidationError('Только один главный тег')
        return super().clean()  # вызываем базовый код переопределяемого метода

class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


