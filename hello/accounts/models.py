from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='Профиль пользователя', related_name='profile')
    birth_date = models.DateField(
        null=True, blank=True, verbose_name='Дата рождения'
    )
    avatar = models.ImageField(upload_to='avatars', null = True, blank=True)


    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        user = super(Profile, self).save(*args, **kwargs)
        Profile.objects.create(user=user)
        return user

    class Meta:
        db_table = 'profiles'
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
        permissions = [('view_users', 'просмотр пользователей')]