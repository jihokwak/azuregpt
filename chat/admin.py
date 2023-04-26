from django.contrib import admin
from django.forms import BooleanField
from django.forms.widgets import CheckboxInput
from .models import ApiKey, Conversation, Message, Setting


@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('api_key', 'api_type', 'api_version', 'api_base', 'token_used', 'remark', 'is_enabled', 'created_at')

    formfield_overrides = {
        BooleanField: {'widget': CheckboxInput},
    }

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_conversation_topic', 'message', 'is_bot', 'tokens','created_at')

    def get_conversation_topic(self, obj):
        return obj.conversation.topic

    get_conversation_topic.short_description = 'Conversation Topic'


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')