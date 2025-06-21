from django.contrib import admin

# Register your models here.
from .models import Folder,Diary,Artist,Setlist
from .forms import DiaryForm,ArtistForm,SetlistForm#←管理サイトでsummernoteのエディタを表示させるためにインポートする。

class DiaryAdmin(admin.ModelAdmin):
  list_display = ["title","dt","place","content"]
  form         = DiaryForm
  
class ArtistAdmin(admin.ModelAdmin):
    display      = ["name"]
    form         = ArtistForm
class SetlistAdmin(admin.ModelAdmin):
    list_display = ["artist", "song"]
    form         = SetlistForm

admin.site.register(Artist, ArtistAdmin)
admin.site.register(Setlist, SetlistAdmin)
admin.site.register(Diary,DiaryAdmin)
admin.site.register(Folder)#多対多のフィールドをadminサイトで管理するコード

