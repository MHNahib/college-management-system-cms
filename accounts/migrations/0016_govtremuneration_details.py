# Generated by Django 3.0.2 on 2020-07-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_govtremuneration'),
    ]

    operations = [
        migrations.AddField(
            model_name='govtremuneration',
            name='details',
            field=models.CharField(max_length=250, null=True),
        ),
    ]