# Generated by Django 3.2.6 on 2021-08-12 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_listall_stage_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listall',
            name='Is_done',
        ),
        migrations.AddField(
            model_name='listall',
            name='State',
            field=models.IntegerField(default=102, verbose_name='Статус'),
        ),
    ]