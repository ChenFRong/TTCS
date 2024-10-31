# Generated by Django 3.0.3 on 2020-09-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20200917_1517'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Pending', max_length=10),
        ),
    ]
