# Generated by Django 4.2.7 on 2023-11-08 13:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('file_id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(choices=[('Invoice', 'Invoice'), ('Food_Bill', 'Food'), ('Travel_Bill', 'Travel')], default='Invoice', max_length=100)),
                ('file', models.ImageField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]