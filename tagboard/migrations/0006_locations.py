# Generated by Django 2.2.3 on 2019-08-07 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagboard', '0005_auto_20190806_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('locname', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('tags', models.TextField()),
            ],
        ),
    ]
