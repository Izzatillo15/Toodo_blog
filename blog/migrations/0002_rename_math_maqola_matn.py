# Generated by Django 3.2.7 on 2021-09-25 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maqola',
            old_name='math',
            new_name='matn',
        ),
    ]
