# Generated by Django 4.0.2 on 2022-02-06 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_thubthumbnail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thubthumbnail',
            new_name='thumbnail',
        ),
    ]
