# Generated by Django 3.2.4 on 2021-10-01 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNXProtect_Utl', '0002_auto_20210927_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='notesfile',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]
