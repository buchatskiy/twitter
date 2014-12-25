from django.contrib import admin
from twitter.models import Twitter, User





class TwitterAdmin(admin.ModelAdmin):
    list_display = ('text', 'name', 'date')
    list_filter = ('date',)
    ordering = ('-date',)


admin.site.register(Twitter, TwitterAdmin)
admin.site.register(User)


