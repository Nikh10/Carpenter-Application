# Generated by Django 2.1.4 on 2019-01-05 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0005_handles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handles',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]