# Generated by Django 5.1.6 on 2025-02-21 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univer', '0007_categories_remove_student_kurs_news_delete_kurs_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kompaniya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('birth_date', models.DateTimeField(auto_now=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.CreateModel(
            name='Avtomabil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='noun model')),
                ('color', models.TextField(blank=True)),
                ('kuchi', models.TextField(blank=True)),
                ('year', models.TextField(blank=True)),
                ('price', models.TextField(blank=True)),
                ('context', models.TextField(blank=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('kompaniyasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Univer.kompaniya')),
            ],
            options={
                'verbose_name': 'AVTOMABIL',
                'verbose_name_plural': 'AVTOMABILLAR',
                'ordering': ['-created_ed'],
            },
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
