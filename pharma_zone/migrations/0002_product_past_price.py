# Generated by Django 2.0.6 on 2019-01-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharma_zone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='past_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
