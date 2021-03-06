# Generated by Django 3.1 on 2020-09-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crimeType', models.CharField(max_length=20)),
                ('crimeDescription', models.TextField(max_length=500)),
                ('dateOfCrime', models.DateField()),
                ('victims', models.TextField(max_length=200)),
                ('FIRNumber', models.CharField(max_length=20)),
                ('officerOnDuty', models.CharField(max_length=20)),
                ('fieldOfInterest', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='criminal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('height', models.CharField(max_length=7)),
                ('nationality', models.EmailField(max_length=20)),
                ('nationalID', models.CharField(max_length=20)),
                ('criminalID', models.CharField(max_length=20)),
                ('presentPrison', models.CharField(max_length=20)),
                ('previousCrimeRecord', models.CharField(max_length=20)),
                ('criminalImage', models.ImageField(upload_to=None)),
                ('fringerPrint', models.ImageField(upload_to=None)),
                ('footPrint', models.ImageField(upload_to=None)),
            ],
        ),
    ]
