# Generated by Django 2.0.7 on 2019-02-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0012_auto_20190207_1417'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tagulous_Issue_tag',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='tag',
        ),
        migrations.AddField(
            model_name='issue',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]