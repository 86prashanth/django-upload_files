# Generated by Django 4.1.1 on 2022-10-20 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_files',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]