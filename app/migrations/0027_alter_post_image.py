# Generated by Django 4.1.4 on 2023-11-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img'),
        ),
    ]