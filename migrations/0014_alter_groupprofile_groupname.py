# Generated by Django 4.2.7 on 2023-11-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi_save_vsla_api', '0013_alter_groupprofile_countryoforigin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupprofile',
            name='groupName',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]