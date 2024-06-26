# Generated by Django 4.1.4 on 2023-11-15 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0038_delete_job_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.BigIntegerField()),
                ('photo', models.ImageField(upload_to='job_applicants')),
                ('resume', models.FileField(upload_to='files')),
                ('job_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobs')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
