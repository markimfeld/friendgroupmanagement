# Generated by Django 3.1 on 2020-09-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friendgroups', '0007_auto_20200901_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='address',
            field=models.CharField(default='Centro', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='neighborhood',
            field=models.CharField(default='Centro', max_length=100),
            preserve_default=False,
        ),
    ]
