# Generated by Django 4.0 on 2022-02-26 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_rename_desc_student_support_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentor_post',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]
