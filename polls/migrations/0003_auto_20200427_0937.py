# Generated by Django 3.0.5 on 2020-04-27 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_choice_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_data',
            new_name='pub_date',
        ),
    ]
