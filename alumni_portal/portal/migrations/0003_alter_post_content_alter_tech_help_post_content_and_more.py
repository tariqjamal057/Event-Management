# Generated by Django 4.0.2 on 2022-03-05 15:37

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_delete_authentication_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='tech_help_post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.CreateModel(
            name='Finance_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('behavior', models.CharField(choices=[('G', 'Good'), ('A', 'Average'), ('B', 'Bad')], max_length=1)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('reason', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('highschoolmark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('anyarrears', models.BooleanField()),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('currentsem', models.CharField(choices=[('1', '1st Semester'), ('2', '2nd Semester'), ('3', '3rd Semester'), ('4', '4th Semester'), ('5', '5th Semester'), ('6', '6th Semester'), ('7', '7th Semester'), ('8', '8th Semester')], max_length=1)),
                ('achievements', ckeditor_uploader.fields.RichTextUploadingField()),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='finance',
            name='studentdetails',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='portal.finance_request'),
        ),
        migrations.AlterField(
            model_name='finance',
            name='studentname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentname', to='portal.finance_request'),
        ),
        migrations.DeleteModel(
            name='StudDetails',
        ),
    ]