# Generated by Django 3.0.2 on 2020-07-02 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('non_working_files', '0011_auto_20200501_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book_file',
            field=models.FileField(blank=True, null=True, upload_to='library/books/'),
        ),
        migrations.AlterField(
            model_name='library',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to='library/img/'),
        ),
    ]
