# Generated by Django 3.2.7 on 2021-10-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('mail', models.TextField()),
                ('twsub', models.TextField()),
                ('twretweet', models.TextField()),
                ('telsubchannel', models.TextField()),
                ('telsubgroup', models.TextField()),
            ],
        ),
    ]
