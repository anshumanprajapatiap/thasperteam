# Generated by Django 3.0 on 2020-06-22 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0036_round0_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='firsttask',
            name='Q10',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='firsttask',
            name='Q9',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
