# Generated by Django 3.1.6 on 2021-03-20 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approve_comment',
            new_name='approved_comment',
        ),
    ]