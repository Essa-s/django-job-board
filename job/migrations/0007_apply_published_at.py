# Generated by Django 5.0 on 2023-12-27 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_apply_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='published_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
