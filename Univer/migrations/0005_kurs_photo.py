# Generated by Django 5.1.6 on 2025-02-17 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Univer', '0004_kurs_totalstudent'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurs',
            name='photo',
            field=models.ImageField(default=1, upload_to='photos/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
