# Generated by Django 4.1.1 on 2023-05-19 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_type', '0006_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, default='images/logo_elim.png', null=True, upload_to='images', verbose_name='foto'),
        ),
    ]
