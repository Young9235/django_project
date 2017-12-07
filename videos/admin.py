from django.contrib import admin

# Register your models here.

from .models import Video

admin.site.register(Video)      #어드민 사이트에 비디오를 넣는 것