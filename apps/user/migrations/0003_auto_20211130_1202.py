# Generated by Django 3.2.7 on 2021-11-30 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211129_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='numero',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]