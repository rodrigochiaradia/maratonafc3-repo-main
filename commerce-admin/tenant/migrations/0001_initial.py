# Generated by Django 3.0.6 on 2020-06-29 16:43

from django.db import migrations, models

import common.validators
import tenant.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=255, verbose_name='empresa')),
                ('is_admin', models.BooleanField(default=False, verbose_name='administrador')),
                ('site', models.CharField(max_length=100, unique=True, validators=[
                    common.validators.simple_domain_name_validator], verbose_name='site')),
                ('fallback_subdomain', models.CharField(help_text='Este subdomínio serve para o cliente acessar quando não registrou o domínio principal', max_length=100, unique=True, validators=[
                    common.validators.simple_domain_name_validator], verbose_name='subdomínio')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
