# Generated by Django 2.1.4 on 2019-01-05 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_kitchen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.FloatField()),
                ('width', models.FloatField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='accessories',
            name='wardrobe',
        ),
        migrations.DeleteModel(
            name='Closet',
        ),
        migrations.DeleteModel(
            name='Doors',
        ),
        migrations.AddField(
            model_name='wardrobe',
            name='cost',
            field=models.FloatField(default=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Accessories',
        ),
    ]
