# Generated by Django 5.0.7 on 2024-07-17 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
        migrations.AlterField(
            model_name='payment',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='payments', to='base.loan'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=11),
        ),
    ]
