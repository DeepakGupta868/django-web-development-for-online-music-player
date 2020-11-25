# Generated by Django 2.2 on 2020-04-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20200325_1955'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='a1_id',
            new_name='al_id',
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(help_text='album genre', max_length=100),
        ),
    ]