# Generated by Django 4.2 on 2024-06-08 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_flan_ranking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flan',
            name='ranking',
        ),
    ]