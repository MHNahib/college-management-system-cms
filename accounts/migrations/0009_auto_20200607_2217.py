# Generated by Django 3.0.2 on 2020-06-07 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_studentpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpayment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student'),
        ),
    ]