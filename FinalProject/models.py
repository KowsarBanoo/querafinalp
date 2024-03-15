from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Movie(models.Model):
    title = models.CharField(
        max_length = 64,
        verbose_name= "نام فیلم"
    )
    text = models.TextField(
        verbose_name= "متن درباره فیلم"
    )
    creator = models.ForeignKey(
        UserModel,
        on_delete = models.CASCADE,
        verbose_name = "کاربر"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name = "زمان ثبت فیلم"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name = "زمان بروزرسانی فیلم"
    )
    
class FeedBack(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete = models.CASCADE,
        verbose_name="نام فیلم",
        null = True
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