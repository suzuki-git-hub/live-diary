from django import forms
from .models import Folder,Artist,Setlist

#↓summernoteのために必要===============
import bleach
from bleach.css_sanitizer import CSSSanitizer
from django_summernote.widgets import SummernoteWidget
from django.conf import settings
from .models import Diary
#========================================

class FolderForm(forms.ModelForm):#クラス名はTopicモデルを利用して作ったフォームクラスなのでFolderFormとした
  
    class Meta:#ここでのclass名はMetaが広く一般的に使われている。
      model = Folder
      fields = ["name"]
      #↑model属性とfields属性を指定する必要がある。これらの属性は、フォームがベースとなるモデルとどのフィールドを使用するかを定義するために必須
      



class HTMLField(forms.CharField):
    #コンストラクタ（クラスのオブジェクトを作る際に最初に一度だけ実行される）
    #ここではsummernoteのエディタの表示がされる処理
    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    # ここで.clean()内にstyles引数を入れるとエラー(bleachではすでにstyle引数は廃止されている)
    def to_python(self, value):
        value       = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES, css_sanitizer=CSSSanitizer())


class DiaryForm(forms.ModelForm):
    class Meta:
      model  = Diary
      fields = ["folder","title","dt","place","content"]
      
    content =   HTMLField()
    
class ArtistForm(forms.ModelForm):
    class Meta:
      model = Artist
      fields = ["name","diary"]
      
class SetlistForm(forms.ModelForm):
    class Meta:
      model = Setlist
      fields = ["artist","song"]