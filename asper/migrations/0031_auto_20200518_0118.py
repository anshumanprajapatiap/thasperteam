# Generated by Django 3.0 on 2020-05-17 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asper', '0030_auto_20200518_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsubmit',
            name='AssignNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asper.AppAssignment'),
        ),
        migrations.AlterField(
            model_name='websubmit',
            name='AssignNo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asper.WebAssignment'),
        ),
    ]
