# Generated by Django 4.2.4 on 2023-08-08 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrology', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zodiac',
            name='career',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='zodiac',
            name='career_2',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='zodiac',
            name='content_2',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='zodiac',
            name='content_3',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='zodiac',
            name='marriage',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
        migrations.AddField(
            model_name='zodiac',
            name='marriage_2',
            field=models.TextField(default='DEFAULT VALUE'),
        ),
    ]
