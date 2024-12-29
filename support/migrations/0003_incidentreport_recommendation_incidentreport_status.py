# Generated by Django 5.1.4 on 2024-12-28 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_remove_gbvcenter_latitude_remove_gbvcenter_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreport',
            name='recommendation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='incidentreport',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Closed', 'Closed')], default='Pending', max_length=10),
        ),
    ]
