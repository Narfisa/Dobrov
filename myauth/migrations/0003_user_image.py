# Generated by Django 3.0.5 on 2020-06-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0002_auto_20200621_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.CharField(default='https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png', max_length=150),
        ),
    ]