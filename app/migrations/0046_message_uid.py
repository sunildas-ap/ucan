# Generated by Django 4.1.4 on 2023-12-04 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_remove_message_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='uid',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]