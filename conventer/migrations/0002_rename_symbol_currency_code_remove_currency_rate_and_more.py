# Generated by Django 4.0.3 on 2023-08-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conventer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='symbol',
            new_name='code',
        ),
        migrations.RemoveField(
            model_name='currency',
            name='rate',
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
