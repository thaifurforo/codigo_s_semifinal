# Generated by Django 4.0.6 on 2022-07-08 11:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('seed', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('account_number', models.CharField(default='', editable=False, max_length=8)),
                ('account_number_no_cd', models.IntegerField(default=0, editable=False, unique=True, validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='Número da conta sem dígito verificador')),
                ('check_digit', models.IntegerField(default=0, editable=False, verbose_name='Dígito verificador do número conta')),
                ('active_account', models.BooleanField(default=True)),
                ('opening_date', models.DateField(default=datetime.datetime(2022, 7, 8, 11, 54, 58, 719343, tzinfo=utc), verbose_name='Data de abertura')),
                ('closure_date', models.DateField(blank=True, null=True, verbose_name='Data de encerramento')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(help_text='Formato: 00.000-000', max_length=10, unique=True, validators=[django.core.validators.RegexValidator('[0-9]{2}.[0-9]{3}-[0-9]{3}')])),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.CharField(choices=[('PF', 'Pessoa Física'), ('PJ', 'Pessoa Jurídica')], default='PF', max_length=2)),
                ('document_number', models.CharField(default=0, help_text='Somente números', max_length=14, unique=True, validators=[django.core.validators.RegexValidator('[0-9]{11,14}')], verbose_name='CPF/CNPJ')),
                ('name', models.CharField(default='', max_length=80, verbose_name='Nome completo ou Razão social')),
                ('phone_number', models.CharField(default='', help_text='Formato: +DI (DDD) 00000-0000', max_length=20, validators=[django.core.validators.RegexValidator('\\+[0-9]{2} \\(0[0-9]{2}\\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}', message='Telefone em formato inválido')], verbose_name='Telefone')),
                ('email', models.CharField(default='', max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('birthdate', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('zip_code', models.CharField(help_text='Formato: 00.000-000', max_length=10, validators=[django.core.validators.RegexValidator('[0-9]{2}.[0-9]{3}-[0-9]{3}')])),
                ('door_number', models.CharField(default='', max_length=10)),
                ('complement', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='virtual_bank.account')),
                ('balance', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('TI', 'Transferência entre contas do mesmo banco'), ('TE', 'Transferência de/para conta de outro banco'), ('DE', 'Depósito'), ('RE', 'Recebimento em conta'), ('PG', 'Pagamento de guia ou boleto'), ('SQ', 'Saque')], default='TI', max_length=2)),
                ('date', models.DateField(default=datetime.datetime(2022, 7, 8, 11, 54, 58, 721361, tzinfo=utc))),
                ('amount', models.FloatField(default=0)),
                ('credit_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='credit_account', to='virtual_bank.account')),
                ('debit_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='debit_account', to='virtual_bank.account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='virtual_bank.customer'),
        ),
    ]