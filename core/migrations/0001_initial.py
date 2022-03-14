# Generated by Django 4.0.3 on 2022-03-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('regd_no', models.CharField(max_length=25)),
                ('code', models.TextField()),
                ('subtime', models.IntegerField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
