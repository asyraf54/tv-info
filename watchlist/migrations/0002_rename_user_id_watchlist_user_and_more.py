# Generated by Django 4.1.7 on 2023-03-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='user_id',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='show_id',
            new_name='show',
        ),
    ]
