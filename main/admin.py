from django.contrib import admin

from .models import SocialClub, Moderators, FormBid, Feedbacks, LegalInformation

# Register your models here.

admin.site.site_title = 'Админ система Мастермайнд'
admin.site.site_header = 'Админ система Мастермайнд'

class ChangeSocialClub(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', )
    search_fields = ('id', 'title')


class ChangeModerators(admin.ModelAdmin):
    list_display = ('id', 'name', 'social_club')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    
    
class ChangeFeedbacks(admin.ModelAdmin):
    list_display = ('id', 'name_author', 'time', 'status')
    list_display_links = ('id', 'name_author')
    search_fields = ('id', 'name_author', 'video_url')
    list_editable = ('status',)
    list_filter = ('status',)


class ChangeFormBid(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'status')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'email', 'phone')
    list_editable = ('status', )
    list_filter = ('status', )

class ChangeLegalInformation(admin.ModelAdmin):
    list_display = ('title', 'content', 'visible')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    list_editable = ('visible', )
    list_filter = ('visible', )


admin.site.register(FormBid, ChangeFormBid)
admin.site.register(SocialClub, ChangeSocialClub)
admin.site.register(Moderators, ChangeModerators)
admin.site.register(Feedbacks, ChangeFeedbacks)
admin.site.register(LegalInformation, ChangeLegalInformation)
