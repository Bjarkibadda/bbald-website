# Generated by Django 3.0.3 on 2020-09-20 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200918_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='prj_or_blog',
            field=models.BooleanField(default=False),
        ),
    ]
