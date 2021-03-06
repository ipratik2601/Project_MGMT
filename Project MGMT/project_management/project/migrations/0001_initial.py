# Generated by Django 4.0.3 on 2022-03-29 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('project_title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('NotStarted', 'NotStarted'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=30)),
                ('estimated_hourse', models.IntegerField()),
                ('start_date', models.DateField(auto_now_add=True)),
                ('completion_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('module_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('estimated_hours', models.IntegerField()),
                ('start_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_module',
            },
        ),
        migrations.CreateModel(
            name='ProjectTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'project_team',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('task_name', models.CharField(max_length=30)),
                ('priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=30)),
                ('description', models.TextField()),
                ('total_minutes', models.IntegerField()),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='UserTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.task')),
            ],
            options={
                'db_table': 'user_task',
            },
        ),
    ]
