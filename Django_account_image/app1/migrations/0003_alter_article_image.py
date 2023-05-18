# Generated by Django 3.2.16 on 2022-12-22 02:45

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='thumbnails/'),
        ),
    ]