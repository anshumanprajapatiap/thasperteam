# Generated by Django 3.0 on 2020-05-17 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0025_firsttask_ud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firsttask',
            name='ud',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
