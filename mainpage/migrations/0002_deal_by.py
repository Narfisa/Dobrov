# Generated by Django 3.0.5 on 2020-06-22 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0003_user_image'),
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='by',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.CASCADE, to='myauth.User'),
        ),
    ]