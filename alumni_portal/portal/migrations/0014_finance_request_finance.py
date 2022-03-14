# Generated by Django 4.0.2 on 2022-03-10 17:56

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_remove_finance_request_posted_by_delete_finance_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finance_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('behavior', models.CharField(choices=[('G', 'Good'), ('A', 'Average'), ('B', 'Bad')], max_length=1)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('highschoolmark', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('anyarrears', models.BooleanField(blank=True, null=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('currentsem', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester'), ('4', '4th Semester'), ('5', '5th Semester'), ('6', '6th Semester'), ('7', '7th Semester'), ('8', '8th Semester')], max_length=1)),
                ('achievements', ckeditor_uploader.fields.RichTextUploadingField()),
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
