# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-22 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('karyawan', '0001_initial'),
        ('kehadiran', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_kehadiran', models.CharField(choices=[('izin', 'Izin'), ('cuti', 'Cuti')], max_length=20)),
                ('waktu_mulai', models.DateField()),
                ('waktu_berhenti', models.DateField()),
                ('alasan', models.TextField()),
                ('disetujui', models.BooleanField(default=False)),
                ('karyawan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='karyawan.Karyawan')),
            ],
            options={
                'indexes': [],
            },
        ),
    ]