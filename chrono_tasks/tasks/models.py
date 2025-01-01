from django.db import models
from shared.models import TimestampMixin, UUIDMixin

class BaseTaskMixin(models.Model):
    display_id = models.BigIntegerField(default=1)
    name = models.CharField(max_length=80)
    content = models.TextField(blank=True)
    started_at = models.DateTimeField(blank=True)
    opened_merge_request_at = models.DateTimeField(blank=True)
    ended_at = models.DateTimeField(blank=True)

    class Meta:
        abstract = True

class BaseAssigneeMixin(models.Model):
    assigned_user = models.ForeignKey('users.User', on_delete=models.CASCADE, db_index=True)

    class Meta:
        abstract = True

class BaseCreatorMixin(models.Model):
    created_by_user = models.ForeignKey('users.User', on_delete=models.CASCADE, db_index=True)

    class Meta:
        abstract = True

class Epic(UUIDMixin, BaseTaskMixin, BaseCreatorMixin, TimestampMixin):
    """エピックモデル

    エピックのデータを作成する際に使用するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定する
        BaseTaskMixin (models.Model): タスクの基本情報を設定する
        BaseCreatorMixin (models.Model): タスクの作成者を設定する
        TimestampMixin (models.Model): 作成日時と更新日時を設定する
    """

    class Meta:
        db_table = 'epics'

class UserStory(UUIDMixin, BaseTaskMixin, BaseCreatorMixin, TimestampMixin):
    """ユーザーストーリーモデル

    ユーザーストーリーのデータを作成する際に使用するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定する
        BaseTaskMixin (models.Model): タスクの基本情報を設定する
        BaseCreatorMixin (models.Model): タスクの作成者を設定する
        TimestampMixin (models.Model): 作成日時と更新日時を設定する
    """

    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, db_index=True)

    class Meta:
        db_table = 'user_stories'

class Task(UUIDMixin, BaseTaskMixin, BaseCreatorMixin, TimestampMixin):
    """タスクモデル

    タスクのデータを作成する際に使用するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定する
        BaseTaskMixin (models.Model): タスクの基本情報を設定する
        BaseCreatorMixin (models.Model): タスクの作成者を設定する
        TimestampMixin (models.Model): 作成日時と更新日時を設定する
    """

    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE, db_index=True)

    class Meta:
        db_table = 'tasks'

class EpicAssignee(BaseAssigneeMixin):
    """エピック担当者モデル

    エピックの担当者のデータを作成する際に使用するモデル

    Args:
        BaseAssigneeMixin (models.Model): タスクの担当者を設定する
    """

    epic = models.ForeignKey(Epic, on_delete=models.CASCADE, db_index=True)

    class Meta:
        db_table = 'epic_assignees'

class UserStoryAssignee(BaseAssigneeMixin):
    """ユーザーストーリー担当者モデル

    ユーザーストーリーの担当者のデータを作成する際に使用するモデル

    Args:
        BaseAssigneeMixin (models.Model): タスクの担当者を設定する
    """

    user_story = models.ForeignKey(UserStory, on_delete=models.CASCADE, db_index=True)

    class Meta:
        db_table = 'user_story_assignees'

class TaskAssignee(BaseAssigneeMixin):
    """タスク担当者モデル

    タスクの担当者のデータを作成する際に使用するモデル

    Args:
        BaseAssigneeMixin (models.Model): タスクの担当者を設定する
    """

    task = models.ForeignKey(Task, on_delete=models.CASCADE, db_index=True)

    class Meta:
        db_table = 'task_assignees'