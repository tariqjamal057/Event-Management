# Generated by Django 4.0.2 on 2022-03-11 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_remove_finance_request_posted_by_delete_finance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/student_images/')),
                ('student_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('modeofpayment', models.CharField(choices=[('O', 'Online Banking'), ('N', 'Net Banking'), ('U', 'UPI'), ('C', 'Credit/Debit card'), ('A', 'Cash')], max_length=1)),
                ('studentdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='portal.finance_request')),
                ('studentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentname', to='portal.finance_request')),
            ],
        ),
    ]
