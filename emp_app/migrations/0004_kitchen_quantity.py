# Generated by Django 2.1.4 on 2019-01-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_auto_20190105_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='kitchen',
            name='quantity',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]