# Generated by Django 4.2.13 on 2024-05-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('excerpt', models.TextField()),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('quote', models.TextField(blank=True, null=True)),
                ('quoter', models.CharField(blank=True, max_length=255, null=True)),
                ('conclusion', models.TextField()),
                ('call_to_action', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
