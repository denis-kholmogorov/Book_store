# Generated by Django 2.2.4 on 2019-08-30 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_book_cover'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]