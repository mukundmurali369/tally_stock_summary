# Generated by Django 4.0.4 on 2022-06-22 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_createattendence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('date_join', models.DateField()),
                ('defn_sal', models.CharField(max_length=225)),
                ('emp_name', models.CharField(max_length=225)),
                ('emp_desg', models.CharField(max_length=225)),
                ('fnctn', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('blood', models.CharField(max_length=225)),
                ('parent_name', models.CharField(max_length=225)),
                ('spouse_name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('number', models.CharField(max_length=225)),
                ('emailid', models.CharField(max_length=225)),
                ('inc_tax_no', models.CharField(max_length=225)),
                ('aadhar_no', models.CharField(max_length=225)),
                ('uan', models.CharField(max_length=225)),
                ('pfn', models.CharField(max_length=225)),
                ('pran', models.CharField(max_length=225)),
                ('esin', models.CharField(max_length=225)),
                ('bankdtls', models.CharField(max_length=225)),
            ],
        ),
    ]
