# Generated by Django 3.0.5 on 2020-06-22 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0003_user_image'),
        ('mainpage', '0002_remove_deal_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myauth.User'),
        ),
    ]