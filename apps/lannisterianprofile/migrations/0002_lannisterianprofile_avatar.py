# Generated by Django 3.2.9 on 2021-11-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lannisterianprofile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lannisterianprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]