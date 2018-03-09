# Generated by Django 2.0 on 2017-12-18 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_web', '0008_auto_20171218_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students_detail',
            old_name='age',
            new_name='father_age',
        ),
        migrations.RenameField(
            model_name='students_detail',
            old_name='name',
            new_name='father_name',
        ),
        migrations.RemoveField(
            model_name='students_detail',
            name='height',
        ),
        migrations.RemoveField(
            model_name='students_detail',
            name='weight',
        ),
        migrations.AddField(
            model_name='students_detail',
            name='mather_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='students_detail',
            name='mather_name',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='students_detail',
            name='student_id',
            field=models.IntegerField(default=0),
        ),
    ]