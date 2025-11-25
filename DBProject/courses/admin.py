from django.contrib import admin

# Register your models here.
# user/admin.py
from .models import Class # User와 DIMC 모델을 불러옵니다.

admin.site.register(Class)
