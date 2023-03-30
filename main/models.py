from django.db import models


# Create your models here.

class SocialClubsList:

    socialClubs = (
        ('WhatsApp', 'WhatsApp'),
        ('VK', 'VK'),
        ('Telegram', 'Telegram'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('OK', 'OK'),
        ('TikTok', 'TikTok'),
        ('Twitter', 'Twitter'),
        ('YouTube', 'YouTube')
    )



class SocialClub(models.Model):
    
    
    title = models.CharField(choices=SocialClubsList.socialClubs, 
                             max_length=50, default=SocialClubsList.socialClubs[0])
    url = models.URLField()

    class Meta():
        verbose_name = 'соц. сеть'
        verbose_name_plural = 'Соц. сети'

    def __str__(self) -> str:
        return self.title
    

class Moderators(models.Model):

    name = models.TextField(max_length=100, null=False, verbose_name='Имя')
    social_club = models.CharField(choices=SocialClubsList.socialClubs, 
                                   default=SocialClubsList.socialClubs[0], 
                                   null=False,
                                   max_length=50,
                                   verbose_name='Соц. сеть')
    social_club_url = models.URLField(null=False, verbose_name='Ссылка на соцю сеть')
    media = models.ImageField(upload_to='main/images/moderators', null=False,
                              verbose_name='Фотография модератора')

    class Meta():
        verbose_name = 'модератора'
        verbose_name_plural = 'Модераторы'
    
    def __str__(self) -> str:
        return self.name
    

class FormBid(models.Model):
    
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, verbose_name='Email')
    phone = models.CharField(max_length=17, blank=True)
    status = models.BooleanField(default=False, null=False, verbose_name='Обработан')

    class Meta():
        verbose_name = "заявку"
        verbose_name_plural = 'Заявки'

    def __str__(self) -> str:
        return self.name


class Feedbacks(models.Model):

    name_author = models.CharField(max_length=100, null=False, verbose_name='Имя автора')
    video_url = models.URLField(verbose_name='URL видео с YouTube', null=False)
    time = models.DateTimeField(verbose_name='Дата и время добавления (МСК)', auto_now=True, auto_now_add=False)
    status = models.BooleanField(verbose_name='Отображать', null=False)

    class Meta():
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'    

    def __str__(self) -> str:
        return self.name_author


class LegalInformation(models.Model):

    title = models.CharField(verbose_name='Заголовок', max_length=50)
    content = models.CharField(verbose_name='Содержание', max_length=100)
    visible = models.BooleanField(verbose_name="Отображать на сайте")

    class Meta():
        verbose_name = 'информацию'
        verbose_name_plural = 'Юридическая информация'
    
    def __str__(self) -> str:
        return self.title
