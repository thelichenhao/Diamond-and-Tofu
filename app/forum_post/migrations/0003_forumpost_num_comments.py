# Generated by Django 4.1.7 on 2023-05-29 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_post', '0002_topic_forumcomment_title_forumcomment_unvotes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumpost',
            name='num_comments',
            field=models.IntegerField(default=0),
        ),
    ]