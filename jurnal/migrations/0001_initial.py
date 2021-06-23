# Generated by Django 3.1.7 on 2021-04-24 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(null=True)),
                ('keterangan', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='jurnal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(null=True)),
                ('jumlah', models.FloatField(max_length=20, null=True)),
                ('ref', models.CharField(max_length=200, null=True)),
                ('kategori', models.CharField(choices=[('Debet', 'Debet'), ('Kredit', 'Kredit')], max_length=20, null=True)),
                ('akun', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jurnal.akun')),
            ],
        ),
    ]
