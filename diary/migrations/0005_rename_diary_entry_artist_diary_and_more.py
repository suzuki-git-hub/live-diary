# Generated by Django 4.2.2 on 2023-06-24 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_artist_setlist_delete_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artist',
            old_name='diary_entry',
            new_name='diary',
        ),
        migrations.RenameField(
            model_name='setlist',
            old_name='artist_entry',
            new_name='artist',
        ),
    ]
