# Generated by Django 3.2.9 on 2021-12-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='gallery_image',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
