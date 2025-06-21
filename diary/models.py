from django.db import models
from django.utils import timezone

import bs4 #summernoteを解析して画像を抜き取る
# Create your models here.

# python3 manage.py makemigrations
# python3 manage.py migrate


  
#フォルダテーブル
class Folder(models.Model):
  name = models.CharField(verbose_name="フォルダ名",max_length=20)
    
  def __str__(self):#strメソッドで文字列を返すようにしている（管理サイトで見やすい）
    return self.name
 
 
 #日記テーブル
class Diary(models.Model):
  folder  = models.ManyToManyField(Folder, verbose_name="フォルダ")
  title   = models.CharField(max_length=50)
  dt      = models.DateField(verbose_name="参戦日")
  place   = models.CharField(max_length=20,verbose_name="場所")
  content = models.TextField()
  
  def __str__(self):#strメソッドで文字列を返すようにしている（管理サイトで見やすい）
    return self.title
  
  def thumbnail(self):#サムネイルの設定(bs4のインストールとインポート）
    soup = bs4. BeautifulSoup(self.content, "html.parser")#コンテントの中身を抜き取る
    img_item = soup.select ("img")#抜き取った中のimg要素を変数へ(リストになる)
    if len(img_item) > 0:#画像のセットがされていない場合があるため長さを測る（リストの場合は要素の数を数える）
      return img_item[0].get("src")#画像のソースを取得して返す
    else:
      return "https://www.shoshinsha-design.com/wp-content/uploads/2020/05/noimage-760x460.png"
    
    
  #↓↓folerのページでアーティストと曲名で検索ができるようにするために、Diaryに紐づくartistとsongを取り出すメソッドを作る↓↓
  def search_string(self):
    artists = Artist.objects.filter(diary=self.id)#開いているファイルに紐づいているもののみ取り出す
    name    = self.title
  
    for artist in artists:
      name += artist.name#ここのartistは、Artistモデルのオブジェクトのnameフィールドを変数nameに追加している
    #name = name + artist.nameと同じ意味
    
    setlists = Setlist.objects.filter (artist__diary=self.id)
  #一対多で繋がっていればアンダーバー２つでアクセスできる
    for setlist in setlists:
      name += setlist.song
    
    return name
  
  # diaryページに日記に紐付いているアーティストを表示させるための関数↓
  def get_artists(self):
    return Artist.objects.filter(diary=self.id)
  
    
#アーティストテーブル  
class Artist(models.Model):
  name  = models.CharField(verbose_name="アーティスト",max_length=20)
  diary = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name="artists")
  
   # diaryページにアーティストに紐付いている曲を表示させるための関数↓
  def get_setlists(self):
    return Setlist.objects.filter(artist=self.id)
  
  def __str__(self):
    return self.name
  
  

#セットリストテーブル
class Setlist(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)#models.CASCADEは関連するオブジェクトが消去されたら自身も消去される
  song   = models.CharField(verbose_name="曲名",max_length=30)
  
  def __str__(self):
    return self.song