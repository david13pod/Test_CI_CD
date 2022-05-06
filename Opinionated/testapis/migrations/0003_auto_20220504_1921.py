# Generated by Django 3.0 on 2022-05-04 19:21

from django.db import migrations, models
import testapis.models


class Migration(migrations.Migration):

    dependencies = [
        ('testapis', '0002_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='average_score',
            field=models.FloatField(blank=True, null=True, validators=[testapis.models.validate_negative]),
        ),
    ]
