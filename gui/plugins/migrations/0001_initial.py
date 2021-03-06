# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-27 21:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repourl', models.CharField(blank=True, help_text='URL for the plugins repository', max_length=255, verbose_name='Repository URL')),
            ],
            options={
                'verbose_name': 'Configuration',
            },
        ),
        migrations.CreateModel(
            name='Kmod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.CharField(max_length=400)),
                ('within_pbi', models.BooleanField(default=False)),
                ('order', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Plugin Kernel Module',
            },
        ),
        migrations.CreateModel(
            name='Plugins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin_name', models.CharField(help_text='Name of the plugin', max_length=120, verbose_name='Plugin name')),
                ('plugin_pbiname', models.CharField(help_text='Info name of the plugin', max_length=120, verbose_name='Plugin info name')),
                ('plugin_version', models.CharField(help_text='Version of the plugin', max_length=120, verbose_name='Plugin version')),
                ('plugin_api_version', models.CharField(default=b'1', max_length=20, verbose_name='Plugin API version')),
                ('plugin_arch', models.CharField(help_text='Plugin architecture', max_length=120, verbose_name='Plugin architecture')),
                ('plugin_enabled', models.BooleanField(default=False, help_text='Plugin enabled', verbose_name='Plugin enabled')),
                ('plugin_ip', models.GenericIPAddressField(help_text='Plugin IP address', verbose_name='Plugin IP address')),
                ('plugin_port', models.IntegerField(help_text='Plugin TCP port', verbose_name='Plugin TCP port')),
                ('plugin_path', models.CharField(help_text='Path where the plugins are saved after installation', max_length=1024, verbose_name='Plugin archive path')),
                ('plugin_jail', models.CharField(help_text='Jail where the plugin is installed', max_length=120, verbose_name='Plugin jail name')),
                ('plugin_secret', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='services.RPCToken')),
            ],
            options={
                'verbose_name': 'Plugin',
                'verbose_name_plural': 'Plugins',
            },
        ),
        migrations.AddField(
            model_name='kmod',
            name='plugin',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='plugins.Plugins'),
        ),
    ]
