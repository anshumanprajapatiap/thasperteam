# Generated by Django 3.0 on 2020-05-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0035_round0'),
    ]

    operations = [
        migrations.AddField(
            model_name='round0',
            name='DT',
            field=models.DateTimeField(null=True),
        ),
    ]
