# Generated by Django 3.0 on 2020-05-17 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0026_auto_20200517_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsubmit',
            name='AssignNo',
            field=models.TextField(max_length=5, null=True),
        ),
    ]
