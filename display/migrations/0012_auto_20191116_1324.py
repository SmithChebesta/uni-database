# Generated by Django 2.2.6 on 2019-11-16 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0011_auto_20191116_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='system_name',
            field=models.OneToOneField(default='something', on_delete=django.db.models.deletion.CASCADE, to='display.Webapp'),
            preserve_default=False,
        ),
    ]
