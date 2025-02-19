# Generated by Django 5.1.6 on 2025-02-19 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univer', '0006_student_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='kurs',
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='news')),
                ('context', models.TextField(blank=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_bool', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Univer.categories')),
            ],
            options={
                'verbose_name': 'NEW',
                'verbose_name_plural': 'NEWS',
                'ordering': ['-created_ed'],
            },
        ),
        migrations.DeleteModel(
            name='Kurs',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
