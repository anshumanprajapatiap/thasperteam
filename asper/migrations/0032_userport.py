# Generated by Django 3.0 on 2020-05-17 23:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asper', '0031_auto_20200518_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstN', models.TextField(max_length=100, null=True)),
                ('LastN', models.TextField(max_length=100, null=True)),
                ('LinkedIn', models.TextField(max_length=100, null=True)),
                ('Behance', models.TextField(max_length=100, null=True)),
                ('Instagram', models.TextField(max_length=100, null=True)),
                ('Twitter', models.TextField(max_length=100, null=True)),
                ('Github', models.TextField(max_length=100, null=True)),
                ('usr', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
