# Generated by Django 4.2.13 on 2024-05-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_tag_remove_post_call_to_action_author_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
