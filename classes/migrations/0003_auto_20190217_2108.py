# Generated by Django 2.1.5 on 2019-02-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20190217_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=1),
        ),
    ]