# Generated by Django 4.1 on 2022-09-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
