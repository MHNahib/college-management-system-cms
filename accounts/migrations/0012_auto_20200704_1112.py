# Generated by Django 3.0.2 on 2020-07-04 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_normalstaff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentabout',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student'),
        ),
        migrations.AlterField(
            model_name='studenteducation',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student'),
        ),
    ]
