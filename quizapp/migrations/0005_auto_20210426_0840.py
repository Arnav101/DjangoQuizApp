# Generated by Django 3.2 on 2021-04-26 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20210426_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hardquestion',
            name='id',
        ),
        migrations.AddField(
            model_name='hardquestion',
            name='qno',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
