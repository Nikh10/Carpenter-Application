# Generated by Django 2.1.4 on 2019-01-05 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0009_doors'),
    ]

    operations = [
        migrations.AddField(
            model_name='doors',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='handles',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
