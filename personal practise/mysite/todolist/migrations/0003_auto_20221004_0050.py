# Generated by Django 3.2.9 on 2022-10-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_remove_todo_tdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donetask',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='donetask',
            name='task',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='donetask',
            name='tname',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='donetask',
            name='uid',
            field=models.IntegerField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='todo',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='todo',
            name='task',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='todo',
            name='tname',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.IntegerField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='fname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='lname',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
    ]