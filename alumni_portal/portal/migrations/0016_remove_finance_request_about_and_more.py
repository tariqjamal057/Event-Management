# Generated by Django 4.0.2 on 2022-03-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_alter_finance_request_cgpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finance_request',
            name='about',
        ),
        migrations.RemoveField(
            model_name='finance_request',
            name='behavior',
        ),
        migrations.RemoveField(
            model_name='finance_request',
            name='cgpa',
        ),
        migrations.RemoveField(
            model_name='finance_request',
            name='highschoolmark',
        ),
        migrations.AddField(
            model_name='finance_request',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
