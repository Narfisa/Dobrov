# Generated by Django 3.0.5 on 2020-06-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_remove_deal_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='image',
            field=models.ImageField(blank=True, default='https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png', max_length=150, upload_to=''),
        ),
    ]
