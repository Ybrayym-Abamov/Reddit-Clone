# Generated by Django 3.0.8 on 2020-07-07 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
