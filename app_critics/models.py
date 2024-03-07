from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class FeedBack(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    movie_name = models.CharField(
        max_length=64,
        verbose_name="نام فیلم"
    )
    personal_feedback = models.TextField(
        verbose_name="نقد",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="زمان ثبت نقد",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="زمان آخرین ویرایش"
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name="وظعیت تایید",
    )
