# Generated by Django 3.2.4 on 2021-07-18 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0021_alter_borrow_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
