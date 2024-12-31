from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'icon_color', 'created_at', 'updated_at')
  search_fields = ('id', 'name', 'email', 'created_at')
  ordering = ('-created_at',)