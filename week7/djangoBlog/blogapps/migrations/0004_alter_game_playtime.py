# Generated by Django 4.2.1 on 2023-05-25 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapps', '0003_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='playtime',
            field=models.IntegerField(),
        ),
    ]