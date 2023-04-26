from django.db import models
from django.contrib.auth.models import User
import openai


class ApiKey(models.Model):
    api_key = models.CharField(max_length=100, unique=True)
    api_type = models.CharField(max_length=10, default=openai.api_type)
    api_base = models.CharField(max_length=100, default=openai.api_base)
    api_version = models.CharField(max_length=10, default=openai.api_version)
    token_used = models.IntegerField(default=0)
    remark = models.CharField(max_length=255)
    is_enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key


# 대화 모델
class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    topic = models.CharField(max_length=255, verbose_name='주제')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '대화'
        verbose_name_plural = '대화'

# 메시지 모델
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, verbose_name='대화')
    message = models.TextField(verbose_name='메시지')
    messages = models.TextField(default='', verbose_name='메시지들')
    tokens = models.IntegerField(default=0, verbose_name='토큰')
    is_bot = models.BooleanField(default=False, verbose_name='봇 여부')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')

    class Meta:
        verbose_name = '메시지'
        verbose_name_plural = '메시지'

# 프롬프트 모델
class Prompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    title = models.TextField(null=True, blank=True, verbose_name='제목')
    prompt = models.TextField(verbose_name='프롬프트')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '프롬프트'
        verbose_name_plural = '프롬프트'

# 설정 모델
class Setting(models.Model):
    name = models.CharField(max_length=255, verbose_name='이름')
    value = models.CharField(max_length=255, verbose_name='값')

    class Meta:
        verbose_name = '설정'
        verbose_name_plural = '설정'
