# Generated by Django 3.2.5 on 2022-04-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('file_updated_at', models.DateTimeField(blank=True)),
                ('title', models.CharField(max_length=512)),
                ('slug', models.CharField(blank=True, max_length=512)),
                ('path', models.CharField(max_length=1024)),
                ('share', models.TextField(blank=True)),
                ('params', models.TextField(blank=True)),
                ('state', models.CharField(blank=True, max_length=128)),
                ('default_view_path', models.CharField(blank=True, max_length=1024)),
                ('output', models.CharField(blank=True, max_length=128)),
                ('format', models.CharField(blank=True, max_length=1024)),
            ],
        ),
    ]
