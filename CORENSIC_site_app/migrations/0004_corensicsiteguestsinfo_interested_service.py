# Generated by Django 4.0.5 on 2022-06-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CORENSIC_site_app', '0003_corensicsiteerrorsstatistic_record_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='corensicsiteguestsinfo',
            name='interested_service',
            field=models.TextField(null=True),
        ),
    ]
