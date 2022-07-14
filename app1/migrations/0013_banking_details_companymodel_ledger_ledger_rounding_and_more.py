# Generated by Django 4.0.4 on 2022-07-01 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_bankingdetails_ledgermodel_ledgersatutorymodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banking_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_limit', models.CharField(blank=True, default='Null', max_length=225)),
                ('holder_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('ac_number', models.CharField(blank=True, default='Null', max_length=225)),
                ('ifsc', models.CharField(blank=True, default='Null', max_length=225)),
                ('swift_code', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('branch_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('alter_chk_bks', models.CharField(blank=True, default='Null', max_length=225)),
                ('enbl_chk_printing', models.CharField(blank=True, default='Null', max_length=225)),
                ('chqconfg', models.CharField(blank=True, default='Null', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('country', models.CharField(max_length=225)),
                ('state', models.CharField(max_length=225)),
                ('pincode', models.CharField(max_length=225)),
                ('telephone', models.CharField(max_length=225)),
                ('mobile', models.CharField(max_length=225)),
                ('fax', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(max_length=225)),
                ('is_status', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=False)),
                ('currency_symbol', models.CharField(default='₹', max_length=225)),
                ('currency_formal_name', models.CharField(default='INR', max_length=225)),
                ('financial_year', models.DateField()),
                ('books_beginning_from', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_alias', models.CharField(blank=True, default='Null', max_length=225)),
                ('group_under', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_opening_bal', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('provide_banking_details', models.CharField(blank=True, default='Null', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Rounding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rounding_Method', models.CharField(blank=True, default='Null', max_length=225)),
                ('Round_limit', models.CharField(blank=True, default='Null', max_length=22)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_Satutory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessable_calculation', models.CharField(blank=True, default='Null', max_length=225)),
                ('Appropriate_to', models.CharField(blank=True, default='Null', max_length=225)),
                ('gst_applicable', models.CharField(blank=True, default='Null', max_length=225)),
                ('Set_alter_GST', models.CharField(blank=True, default='Null', max_length=225)),
                ('type_of_supply', models.CharField(blank=True, default='Null', max_length=225)),
                ('Method_of_calc', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Ledger_sundry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_balance_bill_by_bill', models.CharField(blank=True, default='Null', max_length=225)),
                ('Default_credit_period', models.CharField(blank=True, default='Null', max_length=225)),
                ('Check_for_credit_days', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='ledger_tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_duty_or_tax', models.CharField(blank=True, default='Null', max_length=225)),
                ('type_of_tax', models.CharField(blank=True, default='Null', max_length=225)),
                ('valuation_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('rate_per_unit', models.CharField(blank=True, default='Null', max_length=225)),
                ('Persentage_of_calculation', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Mailing_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Null', max_length=225)),
                ('address', models.CharField(blank=True, default='Null', max_length=225)),
                ('state', models.CharField(blank=True, default='Null', max_length=225)),
                ('country', models.CharField(blank=True, default='Null', max_length=225)),
                ('pincode', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='Tax_Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gst_uin', models.CharField(blank=True, default='Null', max_length=225)),
                ('register_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('pan_no', models.CharField(blank=True, default='Null', max_length=225)),
                ('alter_gst_details', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger')),
            ],
        ),
        migrations.DeleteModel(
            name='BankingDetails',
        ),
        migrations.DeleteModel(
            name='LedgerModel',
        ),
        migrations.DeleteModel(
            name='LedgerSatutoryModel',
        ),
        migrations.DeleteModel(
            name='MailingAddressModel',
        ),
        migrations.DeleteModel(
            name='TaxRegisterModel',
        ),
        migrations.AlterField(
            model_name='vouchermodels',
            name='prvnt_duplictes',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
        migrations.AlterField(
            model_name='vouchermodels',
            name='use_adv_conf',
            field=models.CharField(blank=True, max_length=225),
        ),
        migrations.AddField(
            model_name='banking_details',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.ledger'),
        ),
    ]