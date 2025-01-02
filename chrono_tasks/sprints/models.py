from django.db import models
from datetime import datetime

from shared.models import UUIDMixin, TimestampMixin
from tasks.models import Task, UserStory

class Sprint(UUIDMixin, TimestampMixin):
    """スプリントモデル

    スプリントのデータを作成する際に使用するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定する
        TimestampMixin (models.Model): 作成日時と更新日時を設定する
    """

    display_id = models.BigIntegerField(default=0)
    start_at = models.DateTimeField(blank=True, default=datetime.now)
    end_at = models.DateTimeField(blank=True)

    class Meta:
        db_table = 'sprints'

class SprintTask(UUIDMixin):
    """スプリントタスクモデル

    スプリントに所属するユーザーストーリとタスクのデータを作成するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定する
    """

    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, db_index=True)
    user_story = models.ForeignKey(UserStory, blank=True, null=True, on_delete=models.DO_NOTHING, db_index=True)
    task = models.ForeignKey(Task, blank=True, null=True, on_delete=models.DO_NOTHING, db_index=True)

    class Meta:
        db_table = 'sprint_tasks'