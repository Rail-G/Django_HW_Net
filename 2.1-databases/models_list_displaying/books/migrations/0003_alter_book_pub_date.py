# Generated by Django 5.0 on 2023-12-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_alter_book_pub_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="pub_date",
            field=models.DateField(verbose_name="Дата публикации"),
        ),
    ]