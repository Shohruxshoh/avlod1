# Generated by Django 4.0.2 on 2022-02-07 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avlod21', '0002_courses_image_cours'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='davomiyligi',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courses',
            name='davomiyligi_ru',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='davomiyligi_uz',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='number_les',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
    ]