# Generated by Django 4.0.4 on 2022-06-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_likes'),
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.post'),
        ),
    ]
