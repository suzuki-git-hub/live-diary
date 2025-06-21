"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django. conf import settings #summernoteの実装のために必要
from django.conf.urls.static import static #summernoteの実装のために必要


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("diary.urls")),
    path('accounts/', include('allauth.urls')),
    #allauthを使用するためのpath関数
    #include()関数: 他のURL設定への参照のために使用される
    path('summernote/', include('django_summernote.urls')),
    #↑django_summernote.urls を config/urls.py に組み込むことで、Summernoteの機能を有効化し、デフォルトのビュー関数やクラスが適切に動作するようになります。
]
#summernoteのパスと画像のパスを追加する↓
#settings.py で指定したNEDIA_URLと NEDIA_ROOT に倣って、urlpatterns にパスを追加している
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#このコードは、DjangoのURLパターンを設定するための変数であるurlpatternsに、静的なメディアファイルのURLを追加するための設定です。

# static()関数は、指定されたURLパスにアクセスがあった場合に、settings.MEDIA_ROOT内のメディアファイルを表示するためのURLパターンを自動的に作成します。
# 上記のコードは、urlpatterns変数にstatic()関数の返り値を追加しています。これにより、setting.pyのMEDIA_URLで指定されたURLパスにアクセスがあった場合、関連するメディアファイルがMEDIA_ROOTで指定されたディレクトリから提供されるようになります。
# この設定を追加することで、Djangoアプリケーションはメディアファイルを公開し、ウェブページなどからアクセス可能になります。
