# Generated by Django 4.2 on 2024-06-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_contactform_contact_form_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='ranking',
            field=models.IntegerField(default=0),
        ),
    ]
