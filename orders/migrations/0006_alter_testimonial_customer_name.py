# Generated by Django 3.2.9 on 2022-01-15 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20220115_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='customer_name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
