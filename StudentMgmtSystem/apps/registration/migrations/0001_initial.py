# Generated by Django 4.0.1 on 2022-02-23 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('collage_name', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('graduate_year', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
