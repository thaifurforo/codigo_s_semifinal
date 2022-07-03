# Generated by Django 4.0.5 on 2022-07-03 21:58

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
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('PF', 'Física'), ('PJ', 'Jurídica')], default='PF', max_length=2)),
                ('cpf_cnpj', models.CharField(default=0, help_text='Somente números', max_length=14, unique=True, validators=[django.core.validators.RegexValidator('[0-9]{11,14}')], verbose_name='CPF/CNPJ')),
                ('nome_razao_social', models.CharField(default='', max_length=80, verbose_name='Nome completo ou Razão social')),
                ('endereco', models.CharField(default='', max_length=100, verbose_name='Endereço completo')),
                ('telefone', models.CharField(default='', help_text='Formato: +DI (DDD) 00000-0000', max_length=20, validators=[django.core.validators.RegexValidator('\\+[0-9]{2} \\(0[0-9]{2}\\) (?:[2-8]|9[1-9])[0-9]{3}-[0-9]{4}', message='Telefone em formato inválido')], verbose_name='Telefone')),
                ('email', models.CharField(default='', max_length=50, validators=[django.core.validators.EmailValidator()], verbose_name='E-mail')),
                ('data_nascimento', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('seed', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('numero_conta_sem_dv', models.IntegerField(default=0, editable=False, unique=True, validators=[django.core.validators.MaxValueValidator(999999)], verbose_name='Número da conta sem dígito verificador')),
                ('digito_verificador', models.IntegerField(default=0, editable=False, verbose_name='Dígito verificador do número conta')),
                ('conta_ativa', models.BooleanField(default=True)),
                ('data_abertura', models.DateField(default=datetime.datetime(2022, 7, 3, 21, 58, 2, 122369, tzinfo=utc), verbose_name='Data de abertura')),
                ('data_encerramento', models.DateField(blank=True, null=True, verbose_name='Data de encerramento')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banco_digital.cliente')),
            ],
        ),
    ]
