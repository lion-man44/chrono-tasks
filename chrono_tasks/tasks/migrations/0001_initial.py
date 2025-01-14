# Generated by Django 5.1.4 on 2024-12-31 18:30

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_id', models.BigIntegerField(default=1)),
                ('name', models.CharField(max_length=80)),
                ('content', models.TextField(blank=True, default='')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
            ],
            options={
                'db_table': 'epics',
            },
        ),
        migrations.CreateModel(
            name='EpicAssignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.epic')),
            ],
            options={
                'db_table': 'epic_assignees',
            },
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_id', models.BigIntegerField(default=1)),
                ('name', models.CharField(max_length=80)),
                ('content', models.TextField(blank=True, default='')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('opened_merge_request_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('epic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.epic')),
            ],
            options={
                'db_table': 'user_stories',
            },
        ),
        migrations.CreateModel(
            name='UserStoryAssignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('user_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.userstory')),
            ],
            options={
                'db_table': 'user_story_assignees',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('display_id', models.BigIntegerField(default=1)),
                ('name', models.CharField(max_length=80)),
                ('content', models.TextField(blank=True, default='')),
                ('started_at', models.DateTimeField(blank=True, null=True)),
                ('opened_merge_request_at', models.DateTimeField(blank=True, null=True)),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('created_by_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('user_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.userstory')),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
        migrations.CreateModel(
            name='TaskAssignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.user')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.task')),
            ],
            options={
                'db_table': 'task_assignees',
            },
        ),
    ]
