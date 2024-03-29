# Generated by Django 3.2.5 on 2021-07-04 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDL', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=10)),
                ('company', models.TextField(max_length=10)),
                ('price', models.IntegerField(max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MDL.category')),
            ],
        ),
    ]
