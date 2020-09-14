# Generated by Django 3.1 on 2020-09-14 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='police',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policeID', models.CharField(max_length=10)),
                ('fullname', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=50)),
                ('contactNumber', models.CharField(max_length=11)),
                ('emailAddress', models.EmailField(max_length=200)),
                ('username', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
                ('confirmPassword', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
