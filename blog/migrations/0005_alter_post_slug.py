# Generated by Django 4.2.4 on 2023-09-23 20:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date=models.DateTimeField(default=django.utils.timezone.now)),
        ),
    ]
