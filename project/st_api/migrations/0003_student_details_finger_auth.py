# Generated by Django 4.1.3 on 2023-02-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st_api', '0002_rename_persent_student_details_present_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_details',
            name='finger_auth',
            field=models.BooleanField(default=False),
        ),
    ]
