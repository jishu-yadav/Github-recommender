# Generated by Django 3.2.6 on 2021-12-19 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0008_repository_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repository',
            name='index',
        ),
    ]
