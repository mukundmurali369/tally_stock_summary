# Generated by Django 4.0.4 on 2022-06-21 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_createemployeegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateAttendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('typee', models.CharField(max_length=225)),
            ],
        ),
    ]
