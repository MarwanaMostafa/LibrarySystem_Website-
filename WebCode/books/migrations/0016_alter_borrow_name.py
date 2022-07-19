# Generated by Django 3.2.4 on 2021-07-18 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0015_auto_20210718_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
