# Generated by Django 4.1.1 on 2023-05-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_type', '0002_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
