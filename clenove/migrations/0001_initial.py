# Generated by Django 4.0.3 on 2022-08-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skaut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=60)),
                ('prezdivka', models.CharField(max_length=100)),
                ('vek', models.IntegerField()),
                ('slozil_zkousku', models.BooleanField()),
            ],
        ),
    ]