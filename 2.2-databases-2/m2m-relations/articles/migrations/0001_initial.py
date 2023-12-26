# Generated by Django 5.0 on 2023-12-26 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=256, verbose_name="Название")),
                ("text", models.TextField(verbose_name="Текст")),
                ("published_at", models.DateTimeField(verbose_name="Дата публикации")),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="", verbose_name="Изображение"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="tag_name")),
            ],
            options={
                "verbose_name": "Тег",
                "verbose_name_plural": "Теги",
            },
        ),
        migrations.CreateModel(
            name="Scope",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_main", models.BooleanField(default=False)),
                (
                    "article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="art_scopes",
                        to="articles.article",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags_scopes",
                        to="articles.tag",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="article",
            name="scopes",
            field=models.ManyToManyField(
                related_name="tags", through="articles.Scope", to="articles.tag"
            ),
        ),
    ]
