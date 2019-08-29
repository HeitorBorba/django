# Generated by Django 2.2.4 on 2019-08-29 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ong', models.CharField(max_length=50, verbose_name='Nome')),
                ('resp_ong', models.CharField(max_length=30, verbose_name='Responsavel')),
                ('email_ong', models.CharField(max_length=255, unique=True, verbose_name='E-mail')),
                ('str_cep_ong', models.CharField(max_length=10, verbose_name='CEP')),
                ('str_numero_ong', models.CharField(max_length=5, verbose_name='Número Res.')),
                ('complemento_ong', models.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('hrs_ong', models.CharField(max_length=100, verbose_name='Horario de funcionamento')),
                ('telefone_ong', models.CharField(blank=True, max_length=255, null=True, verbose_name='Telefone')),
                ('trabalho_ong', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
