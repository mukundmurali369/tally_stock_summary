# Generated by Django 4.0 on 2022-07-14 08:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_groupmodel_under'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_name', models.CharField(max_length=225)),
                ('Item_unit', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Buy_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=10)),
                ('company', models.CharField(max_length=225)),
                ('Rate', models.IntegerField()),
                ('Value', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('month', models.CharField(default='July', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Buy_or_sell_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BorS', models.IntegerField(default=1)),
                ('Quantity', models.IntegerField(default=10)),
                ('company', models.CharField(max_length=225)),
                ('Rate', models.IntegerField()),
                ('Value', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('month', models.CharField(default='July', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Sell_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=225)),
                ('Rate', models.IntegerField()),
                ('Value', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('month', models.CharField(default='July', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Stock_Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_name', models.CharField(max_length=225)),
                ('Group_total', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='CompanyModel',
        ),
        migrations.DeleteModel(
            name='CreateAttendence',
        ),
        migrations.DeleteModel(
            name='CreateEmployeeCategory',
        ),
        migrations.DeleteModel(
            name='CreateEmployeegroup',
        ),
        migrations.RemoveField(
            model_name='currencyalter',
            name='cname',
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='GroupModel',
        ),
        migrations.RemoveField(
            model_name='ledger_banking_details',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_mailing_address',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_rounding',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_satutory',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_sundry',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_tax',
            name='ledger_id',
        ),
        migrations.RemoveField(
            model_name='ledger_tax_register',
            name='ledger_id',
        ),
        migrations.DeleteModel(
            name='VoucherModels',
        ),
        migrations.DeleteModel(
            name='CreateCurrency',
        ),
        migrations.DeleteModel(
            name='CurrencyAlter',
        ),
        migrations.DeleteModel(
            name='Ledger',
        ),
        migrations.DeleteModel(
            name='Ledger_Banking_Details',
        ),
        migrations.DeleteModel(
            name='Ledger_Mailing_Address',
        ),
        migrations.DeleteModel(
            name='Ledger_Rounding',
        ),
        migrations.DeleteModel(
            name='Ledger_Satutory',
        ),
        migrations.DeleteModel(
            name='Ledger_sundry',
        ),
        migrations.DeleteModel(
            name='ledger_tax',
        ),
        migrations.DeleteModel(
            name='Ledger_Tax_Register',
        ),
        migrations.AddField(
            model_name='sell_items',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_groups'),
        ),
        migrations.AddField(
            model_name='sell_items',
            name='Item_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_items'),
        ),
        migrations.AddField(
            model_name='buy_or_sell_items',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_groups'),
        ),
        migrations.AddField(
            model_name='buy_or_sell_items',
            name='Item_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_items'),
        ),
        migrations.AddField(
            model_name='buy_items',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_groups'),
        ),
        migrations.AddField(
            model_name='buy_items',
            name='Item_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.add_items'),
        ),
        migrations.AddField(
            model_name='add_items',
            name='Group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.stock_groups'),
        ),
    ]