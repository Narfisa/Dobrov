# Generated by Django 3.0.5 on 2020-06-22 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0003_user_image'),
        ('mainpage', '0003_deal_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='address',
            field=models.CharField(blank=True, default='Отсутствует', max_length=100),
        ),
        migrations.AlterField(
            model_name='deal',
            name='by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myauth.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deal',
            name='image',
            field=models.CharField(blank=True, default='https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png', max_length=150),
        ),
        migrations.AlterField(
            model_name='deal',
            name='more',
            field=models.CharField(blank=True, default='Отсутствует', max_length=200),
        ),
        migrations.AlterField(
            model_name='deal',
            name='price',
            field=models.CharField(blank=True, default='Отсутствует', max_length=40),
        ),
        migrations.AlterField(
            model_name='deal',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]