# Generated by Django 4.0.2 on 2022-03-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_finance_request_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_request',
            name='highschoolmark',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
