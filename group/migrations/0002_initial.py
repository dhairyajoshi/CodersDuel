# Generated by Django 4.0.3 on 2022-03-10 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('group', '0001_initial'),
        ('question', '0005_question_groups'),
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(related_name='group_participant', to='participant.participant'),
        ),
        migrations.AddField(
            model_name='group',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='question.question'),
        ),
    ]