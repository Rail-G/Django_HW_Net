from django.db import models

class Tag(models.Model):

    name = models.CharField(max_length=100, verbose_name='tag_name') 
    # scope_id =  models.ForeignKey('Scope', on_delete=models.CASCADE, related_name="Тег")
    # name = models.CharField(max_length=100, verbose_name='tag_name')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Tag, related_name='tags', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    
class Scope(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scope_scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scope_scopes')
    is_main = models.BooleanField(default=False)
