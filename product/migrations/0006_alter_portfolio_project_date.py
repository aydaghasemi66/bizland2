# Generated by Django 4.1.7 on 2023-11-14 18:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_portfolio_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='project_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 14, 22, 12, 42, 923947)),
        ),
    ]
