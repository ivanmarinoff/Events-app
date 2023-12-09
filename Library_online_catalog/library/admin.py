from django.contrib import admin
from django.utils.html import format_html

from .models import EventModel, ProfileModel


class imageAdmin(admin.ModelAdmin):
    list_display = ["event_name", "category", "description", "date", "event_image", "image_tag"]
    list_filter = ["event_name", "date"]
    search_fields = ['event_name']
    ordering = ['-date']

    def image_tag(self, obj):
        if obj.event_image:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.event_image))
        return None


class UserModelAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "profile_picture", "image_tag"]
    list_filter = ["first_name", "last_name"]
    search_fields = ['first_name']
    ordering = ['-first_name']

    def image_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" style="max-width:150px; max-height:150px"/>'.format(obj.profile_picture))
        return None


admin.site.register(EventModel, imageAdmin)
admin.site.register(ProfileModel, UserModelAdmin)
