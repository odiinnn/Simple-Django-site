# Generated by Django 3.2.7 on 2021-10-01 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211001_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='mail',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='telsubchannel',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='telsubgroup',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='twretweet',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='registration',
            name='twsub',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
