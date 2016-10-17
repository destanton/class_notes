from django.contrib import admin
from app.models import Chirp, Vote


admin.site.register([Chirp, Vote])
# Register your models here.
