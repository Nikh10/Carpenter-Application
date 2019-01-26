# Generated by Django 2.1.4 on 2019-01-10 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0015_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='bedroom_doors',
            name='bedroom_doors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Bedroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bedroom_handles',
            name='bedroom_handles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Bedroom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doors',
            name='kitchen_doors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Kitchen'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hall_doors',
            name='hall_doors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Hall'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hall_handles',
            name='hall_handles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Hall'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='handles',
            name='kitchen_handles',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='emp_app.Kitchen'),
            preserve_default=False,
        ),
    ]
