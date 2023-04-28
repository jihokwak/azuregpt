# Generated by Django 4.2 on 2023-04-28 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100, unique=True)),
                ('api_type', models.CharField(default='open_ai', max_length=10)),
                ('api_base', models.CharField(default='https://api.openai.com/v1', max_length=100)),
                ('api_version', models.CharField(default=None, max_length=10)),
                ('token_used', models.IntegerField(default=0)),
                ('remark', models.CharField(max_length=255)),
                ('is_enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=255, verbose_name='주제')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '대화',
                'verbose_name_plural': '대화',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='이름')),
                ('value', models.CharField(max_length=255, verbose_name='값')),
            ],
            options={
                'verbose_name': '설정',
                'verbose_name_plural': '설정',
            },
        ),
        migrations.CreateModel(
            name='TokenUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokens', models.IntegerField(default=0, verbose_name='토큰')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '토큰사용량',
                'verbose_name_plural': '토큰사용량',
            },
        ),
        migrations.CreateModel(
            name='Prompt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True, verbose_name='제목')),
                ('prompt', models.TextField(verbose_name='프롬프트')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='사용자')),
            ],
            options={
                'verbose_name': '프롬프트',
                'verbose_name_plural': '프롬프트',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='메시지')),
                ('messages', models.TextField(default='', verbose_name='메시지들')),
                ('tokens', models.IntegerField(default=0, verbose_name='토큰')),
                ('is_bot', models.BooleanField(default=False, verbose_name='봇 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('conversation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.conversation', verbose_name='대화')),
            ],
            options={
                'verbose_name': '메시지',
                'verbose_name_plural': '메시지',
            },
        ),
    ]