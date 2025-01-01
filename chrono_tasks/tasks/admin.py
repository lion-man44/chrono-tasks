from django.contrib import admin

from django.db.models import Max
from tasks.models import Epic, Task, UserStory

@admin.register(Epic)
class EpicAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'created_by_user_id', 'created_at', 'updated_at')
    search_fields = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'created_by_user_id', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('display_id', 'name', 'started_at', 'opened_merge_request_at', 'ended_at')

    def get_changeform_initial_data(self, _):
        max_display_id = Epic.objects.aggregate(Max('display_id'))['display_id__max'] or 0
        return {
            'display_id': max_display_id + 1
        }

@admin.register(UserStory)
class UserStoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'epic_id', 'created_by_user_id', 'created_at', 'updated_at')
    search_fields = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'epic_id', 'created_by_user_id', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('display_id', 'name', 'started_at', 'opened_merge_request_at', 'ended_at')

    def get_changeform_initial_data(self, _):
        max_display_id = UserStory.objects.aggregate(Max('display_id'))['display_id__max'] or 0
        return {
            'display_id': max_display_id + 1
        }

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'user_story_id', 'created_by_user_id', 'created_at', 'updated_at')
    search_fields = ('id', 'display_id', 'name', 'content', 'started_at', 'opened_merge_request_at', 'ended_at', 'user_story_id', 'created_by_user_id', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('display_id', 'name', 'started_at', 'opened_merge_request_at', 'ended_at')

    def get_changeform_initial_data(self, _):
        max_display_id = Task.objects.aggregate(Max('display_id'))['display_id__max'] or 0
        return {
            'display_id': max_display_id + 1
        }