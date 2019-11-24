# Generated by Django 2.2.5 on 2019-11-24 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab_website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='authors',
        ),
        migrations.AddField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(to='lab_website.Person'),
        ),
    ]