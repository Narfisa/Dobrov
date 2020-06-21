# Generated by Django 3.0.5 on 2020-06-21 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=30)),
                ('phoneNumber', models.CharField(max_length=11)),
                ('firstName', models.CharField(max_length=20, null=True)),
                ('lastName', models.CharField(max_length=20, null=True)),
                ('birthday', models.DateField(null=True)),
            ],
        ),
    ]
