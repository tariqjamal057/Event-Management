# Generated by Django 4.0.2 on 2022-03-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0014_finance_request_finance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_request',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
