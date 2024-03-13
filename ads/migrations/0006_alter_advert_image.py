# Generated by Django 4.2.11 on 2024-03-13 23:42

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_advert_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[300, 300], upload_to='media/'),
        ),
    ]