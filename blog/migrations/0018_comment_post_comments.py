# Generated by Django 4.2.13 on 2024-05-31 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_author_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_email', models.EmailField(max_length=50)),
                ('c_comment', models.TextField()),
                ('c_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(to='blog.comment'),
        ),
    ]
