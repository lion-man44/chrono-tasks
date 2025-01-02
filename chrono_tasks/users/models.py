from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator, MinLengthValidator

from shared.models import TimestampMixin, UUIDMixin

class User(UUIDMixin, TimestampMixin):
    """ユーザモデル

    ユーザのデータを作成する際に使用するモデル

    Args:
        UUIDMixin (models.Model): UUIDを主キーに設定するミックスイン
        TimestampMixin (models.Model): 作成日時と更新日時を設定するミックイン
    """

    name = models.CharField(max_length=100, validators=[MaxLengthValidator(100)])
    email = models.EmailField(max_length=255, unique=True, validators=[EmailValidator(), MaxLengthValidator(255)])

    class Meta:
        db_table = 'users'
