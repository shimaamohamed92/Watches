# Generated by Django 3.1.8 on 2021-04-20 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlists', '0003_remove_varient_waiting_list'),
        ('users', '0002_auto_20210416_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='variant_list',
            field=models.ManyToManyField(blank=True, related_name='varient_list', to='wishlists.Varient'),
        ),
    ]
