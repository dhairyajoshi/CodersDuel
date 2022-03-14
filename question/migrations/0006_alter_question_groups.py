# Generated by Django 4.0.3 on 2022-03-10 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_initial'),
        ('question', '0005_question_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='question_groups', to='group.group'),
        ),
    ]
