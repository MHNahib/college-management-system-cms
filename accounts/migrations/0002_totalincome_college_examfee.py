# Generated by Django 3.0.2 on 2020-06-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalincome',
            name='college_examfee',
            field=models.FloatField(default=0),
        ),
    ]
