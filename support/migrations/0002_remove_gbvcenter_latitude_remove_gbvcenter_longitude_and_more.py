# Generated by Django 5.1.4 on 2024-12-28 23:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gbvcenter',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='gbvcenter',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='gbvcenter',
            name='contact_info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='gbvcenter',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='IncidentReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
