# Generated by Django 5.1.4 on 2024-12-31 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churn_app', '0002_remove_customer_name_customer_contract_1_year_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_churned',
        ),
        migrations.AddField(
            model_name='customer',
            name='confidence',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='prediction',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tenure',
            field=models.FloatField(),
        ),
    ]
