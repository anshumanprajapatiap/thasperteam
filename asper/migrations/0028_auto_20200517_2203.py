# Generated by Django 3.0 on 2020-05-17 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0027_auto_20200517_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designsubmit',
            name='AssignNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asper.DesignAssignment'),
        ),
    ]
