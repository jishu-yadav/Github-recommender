# Generated by Django 3.2.6 on 2021-12-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0006_alter_repository_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='language',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='repository',
            name='topics',
            field=models.TextField(blank=True),
        ),
    ]