from django.contrib import admin

from django.db.models import Max
from .models import Sprint, SprintTask

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_id', 'start_at', 'end_at', 'created_at', 'updated_at')
    search_fields = ('id', 'display_id', 'start_at', 'end_at', 'created_at')
    ordering = ('-created_at',)
    list_editable = ('display_id', 'end_at')

    def get_changeform_initial_data(self, _):
        max_display_id = Sprint.objects.aggregate(Max('display_id'))['display_id__max'] or 0
        return {
            'display_id': 0 if max_display_id is 0 else max_display_id + 1
        }

@admin.register(SprintTask)
class SprintTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'sprint', 'user_story', 'task')
    search_fields = ('id', 'sprint', 'user_story', 'task')
    list_editable = ('sprint', 'user_story', 'task')