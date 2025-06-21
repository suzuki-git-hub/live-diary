from django.shortcuts import render,redirect
from django.views import View
from .models import Folder,Diary, Artist , Setlist #TODO ArtistとSetlistを追加する
from django.db.models import Q#Qオブジェクトを使ってスペース区切りの検索が出来るようにする
from django.contrib.auth.mixins import LoginRequiredMixin
#↑ログインが必要なビューを作成するために便利なLoginRequiredMixin（ログインリクワイアードミックスイン）というMixinがあります。このMixinを使用すると、ログインしていないユーザーをログインページにリダイレクトすることができます
from django.contrib.auth.forms import UserCreationForm
#UserCreationForm は、Django が提供するフォームクラスの一つであり、ユーザーアカウントの作成に必要なフィールドを持つフォームを簡単に作成するための便利なクラスです。
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import DiaryForm,ArtistForm,SetlistForm



class TopView(View):
    def get(self, request, *args, **kwargs):return render(request, "diary/top.html")
    #render 関数は、指定したテンプレートをレンダリングしてレスポンスを生成する役割。
top = TopView.as_view()


class FolderView(View):
    def get(self, request, pk, *args, **kwargs):
        
        folder = Folder.objects.filter(pk=pk).prefetch_related("diary_set__artists").first()
        #.first()メソッドを使う理由は返されるオブジェクトは単一のレコードであり、リストではなく単一のオブジェクトになるから
        
        diaries = []#diaries変数の初期化を空のリストで行い、フォルダが存在しない場合でもエラーが発生せず、空の日記リストがテンプレートに渡される
        diaries = folder.diary_set.all()# フォルダに関連する日記を取得
        
        context = { "folder": folder,"diaries": diaries }
        return render(request, "diary/folder.html", context)   
        
folder = FolderView.as_view()



class Folder_DeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        #pkを使って関連する記事を特定
        folder = Folder.objects.filter(pk=pk).prefetch_related("diary_set__artists").first()
        #.first()メソッドを使う理由は返されるオブジェクトは単一のレコードであり、リストではなく単一のオブジェクトになるから
        folder.delete()
        return redirect("diary:mypage")

folder_delete= Folder_DeleteView.as_view()  


class MypageView(View):

    def get(self, request, *args, **kwargs):
        #*args、**kwargsは引数が溢れてもエラーが起こらないようにする事ができる。https://noauto-nolife.com/post/django-args-kwargs/
      
       context = {}
       context["folders"] = Folder.objects.order_by("name")
       #folders"というキーを追加し、それに対応する値としてFolder.objects.order_by("name")を設定。
       #.order_byを使うことによって文字コードの順番になる（アイウエオ順）
       #テンプレートで{{ folders }}といった形式でデータを表示することができる。
       return render(request, 'diary/mypage.html', context)
    
mypage   = MypageView.as_view()


class Add_FolderView(View):
    
    def get(self, request,*args, **kwargs):
        return render(request,"diary/add_folder.html")

    def post(self, request, *args, **kwargs):
        folder_name = request.POST.get('add_folder')  # フォームから名前を取得
         
        if folder_name:
            folder = Folder.objects.create(name=folder_name)  #create()メソッドは、指定されたモデルのクラスの新しいオブジェクトを作成し、データベースに保存する。ここではfolderオブジェクトを作成する際にname パラメータにfolder_name を指定。
            return redirect("diary:mypage")
        else:
            messages.error(request, "フォルダ名を入力してください")
            return redirect("diary:add_folder")
add_folder = Add_FolderView.as_view()


class CreateView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["folders"]  = Folder.objects.all()#フォルダを表示させる
        context["form"]     = DiaryForm()# フォームクラスのオブジェクトをテンプレートでレンダリングするとHTMLのフォームが表示される
       #forms.pyでcontextにHTMLField()を代入していて、HTMLField()にはSummernoteWidget()を与えているため結果、summernoteのエディタが表示される
        return render(request,"diary/create.html", context)

    def post(self, request, *args, **kwargs):
        form    = DiaryForm(request.POST)
        
        
        
        # アーリーリターン
        #アーリーリターン（Early return）は、プログラム内の特定の条件を満たした場合に関数やメソッドから早期にリターン（終了）することを指す。条件が満たされた時点で残りの処理をスキップして、処理のフローを早めに終了させることで、コードの可読性や効率性を向上させる手法。
        if not form.is_valid():
            messages.error(request, "投稿エラー")
            messages.error(request, form.errors)
            return redirect("diary:create")
        
        diary = form.save()
        
        # --------artist_formの処理---------------
        # 同じname属性をリスト型で取得する
        names       = request.POST.getlist("name")

        # Setlistになるsong、紐づくArtistがわかるartist_idをそれぞれ配列で取得する
        artist_ids  = request.POST.getlist("artist_id")
        songs       = request.POST.getlist("song")
        #.getメソッドは最初の値しか取得できないが、.getlistはすべての値をリストで取得できる
        
        for index,name in enumerate(names):
        # enumerate()はインデックス番号も同時に取得できる
            dic = {}
            dic["name"]     = name
            dic["diary"]    = diary.id

            form    = ArtistForm(dic)

            if form.is_valid():
                artist  = form.save()
                print(artist)

            # 要素数が同じであればzip関数を使ってまとめてループできる
            for song,artist_id in zip(songs,artist_ids):

                if artist_id == str(index):
                    #str() を使用してindexの値を文字列に変換し、artist_id の値と比較
                    
                    #TODO: ここでartistに紐づくsetlistを作成
                    
                    print(index)
                    print(song)

                    dic = {}
                    dic["song"]     = song
                    dic["artist"]   = artist.id

                    form    = SetlistForm(dic)

                    if form.is_valid():
                        form.save()

        
        context = {'form': form}
        return redirect("diary:mypage")

create = CreateView.as_view()



class DiaryView(View):
    def get(self, request, pk, *args, **kwargs):
        context = {}
        #pkを使って関連する記事を特定
        context ["diary"] = Diary. objects.filter(id=pk).first()
        #.first()メソッドを使う理由は返されるオブジェクトは単一のレコードであり、リストではなく単一のオブジェクトになるから
        return render(request, "diary/diary.html", context)

diary= DiaryView.as_view()  

class Diary_DeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        #pkを使って関連する記事を特定
        diary = Diary. objects.filter(id=pk).first()
        #.first()メソッドを使う理由は返されるオブジェクトは単一のレコードであり、リストではなく単一のオブジェクトになるから
        print("削除成功")
        diary.delete()
        return redirect("diary:mypage")

diary_delete= Diary_DeleteView.as_view()  


class Diary_EditView(View):
    def get(self, request, pk, *args, **kwargs):
        # 編集用フォームの表示
        context = {}

        diary = Diary.objects.filter(id=pk).first()

        # instance引数を使うことで、編集対象の内容を含んだフォームを提供できる
        context["form"]     = DiaryForm(instance=diary)
        context["diary"]    = diary
        context["folders"]  = Folder.objects.all()
        # Diaryに紐づくArtist及びSetlistも編集する
        
        return render(request, "diary/diary_edit.html", context)
    
    def post(self, request, pk, *args, **kwargs):
        # 編集処理の受付
        # 編集対象を特定
        
        # 既存のモデルインスタンスを取得
        diary = Diary.objects.filter(id=pk).first()

        # 既存の diary インスタンスのデータをフォームに事前に入力し、そのインスタンスを instance 引数としてフォームを初期化します。フォームを通じて、既存のデータを編集する。instance 引数を使用しない場合、新しいモデルインスタンスが作成されてしまう。
        form    = DiaryForm(request.POST,instance=diary)

        if form.is_valid():
            form.save()
        else:
            messages.error(request, "編集エラー")
            return redirect("diary:diary", pk)

        #FIXME: ここをコメントアウトする
        """
            return redirect("diary:mypage")
        else:
            messages.error(request, "編集エラー")
            return render(request, "diary/diary.html", context)
        """
        
        #すでに記録さえていたアーティストとセットリストを編集するにはidを取得する必要がある
        edit_artist_ids  = request.POST.getlist("edit_artist_id")
                                                 # ↑name 属性
        edit_setlist_ids = request.POST.getlist("edit_setlist_id")
        
        names       = request.POST.getlist("name")
        artist_ids  = request.POST.getlist("artist_id")
        #setlist_ids = request.POST.getlist("setlist_id")

        #FIXME: ↓を追加する。
        songs       = request.POST.getlist("song")
        
        # zipとenumerateの組み合わせ。同じ要素数zipでまとめてループできる。enumerateはループでインデックス番号も取得できる https://note.nkmk.me/python-for-enumerate-zip/
        for index, (edit_artist_id, name) in enumerate(zip(edit_artist_ids,names)):
          
           # edit_artist_id が空のときは新規作成。なにか指定が有るときは編集
           
           #edit_artist_idがあり編集の場合↓
            if edit_artist_id:
               #編集対象のedit＿artist_idを取得
                artist = Artist.objects.filter(id=edit_artist_id).first()
               
                #アーティストの情報を dic という辞書に格納
                dic = {}
                dic["name"]     = name
                dic["diary"]    = diary.id

              # instanceに編集対象として取得したartistを指定する
              #instanceパラメータを通じて特定のアーティストの既存データをフォームに初期値として設定
              # これにより、フォームは初期化された状態で表示され、ユーザーは必要に応じて変更できるようになる。
                form    = ArtistForm(dic, instance=artist)
               
                 #バリデーションして保存
                if form.is_valid():
                    artist  = form.save()
                    print(artist)
             
                 
                # 要素数が同じであればzip関数を使ってまとめてループできる
                for edit_setlist_id,song,artist_id in zip(edit_setlist_ids, songs, artist_ids):
                                                         #編集対象のセットリストid・曲・セットリストの紐づいているアーティストidをループ
                    #既存のセットリストの編集                                   
                    if edit_setlist_id:

                        print("==========")
                        print(edit_setlist_id)
                        print("==========")

                        setlist = Setlist.objects.filter(id=edit_setlist_id).first()

                        if artist_id == str(index):
                            #str() を使用してindexの値を文字列に変換し、artist_id の値と比較
                            
                            #TODO: ここでartistに紐づくsetlistを作成
                            dic = {}
                            dic["song"]     = song
                            dic["artist"]   = artist.id

                            form    = SetlistForm(dic, instance=setlist)

                            if form.is_valid():
                                form.save()
                                
                    #アーティストidはあるがセットリストが新規作成の場合            
                    else:

                        if artist_id == str(index):
                            #str() を使用してindexの値を文字列に変換し、artist_id の値と比較
                            
                            #TODO: ここでartistに紐づくsetlistを作成
                            dic = {}
                            dic["song"]     = song
                            dic["artist"]   = artist.id

                            form    = SetlistForm(dic)

                            if form.is_valid():
                                form.save()
            #アーティストもセットリストも新規作成の場合
            else:
                # ↓Diaryの新規作成処理と全く同様。
                # 編集対象のArtist.idの指定がない場合は新規作成。
                # Artistの新規作成するときはSetlistも新規作成する
                dic = {}
                dic["name"]     = name
                dic["diary"]    = diary.id

                form    = ArtistForm(dic)

                if form.is_valid():
                    artist  = form.save()
                    print(artist)

                # 要素数が同じであればzip関数を使ってまとめてループできる
                for song,artist_id in zip(songs,artist_ids):

                    if artist_id == str(index):
                        #str() を使用してindexの値を文字列に変換し、artist_id の値と比較
                        
                        #TODO: ここでartistに紐づくsetlistを作成
                        print(index)
                        print(song)

                        dic = {}
                        dic["song"]     = song
                        dic["artist"]   = artist.id

                        form    = SetlistForm(dic)

                        if form.is_valid():
                            form.save()


        return redirect("diary:mypage")


diary_edit  = Diary_EditView.as_view() 
