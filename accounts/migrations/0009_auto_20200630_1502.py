# Generated by Django 3.0.2 on 2020-06-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200630_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='parents_number',
            new_name='designation',
        ),
        migrations.AddField(
            model_name='staff',
            name='phone_number_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='post',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
