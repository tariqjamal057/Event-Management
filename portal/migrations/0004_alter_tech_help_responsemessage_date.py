# Generated by Django 4.1.1 on 2023-02-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portal", "0003_alter_responsemessage_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tech_help_responsemessage",
            name="date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]