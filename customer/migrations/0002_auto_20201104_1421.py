# Generated by Django 3.0.8 on 2020-11-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_cust',
            name='cust_pswd',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='new_cust',
            name='cust_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]