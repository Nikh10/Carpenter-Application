# Generated by Django 2.1.4 on 2019-01-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0014_auto_20190109_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=700)),
                ('address', models.CharField(max_length=1000)),
                ('state', models.CharField(max_length=280)),
                ('city', models.CharField(max_length=200)),
                ('zipp', models.IntegerField()),
                ('nameoncard', models.CharField(max_length=250)),
                ('cardnumber', models.IntegerField()),
                ('expyear', models.IntegerField()),
                ('expmonth', models.CharField(max_length=10)),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
