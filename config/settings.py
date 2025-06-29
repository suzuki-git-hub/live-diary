"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

# 環境変数の読み込み
from decouple import config
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-c&ta4t7n7vc0&%a$^cuq#&(ojug87mve*fft&lq^xl^6)@u(ef'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []


# Application definition


#==============allauthの実装=======================
SITE_ID = 1#追加
LOGIN_REDIRECT_URL = "/" #追加(ログイン時のリダイレクトURL)
ACCOUNT_LOGOUT_REDIRECT_URL = "/"#追加(ログアウト時のリダイレクトURL)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'diary.apps.DiaryConfig', #これを追加し忘れると、bbsアプリのmodels.pyに書いた内容が、マイグレーションを実行してもDBに反映されない。
    
    'django.contrib.sites', # ←追加
    'allauth', # ←追加
    'allauth.account', # ←追加
    'allauth.socialaccount', # ←追加
    
    'django_summernote',#summernote追加
]

#=================================summernote======================================
# 画像を保存する場所の設定
MEDIA_URL   = "/media/"#クライアント側から見たurlを指定する
MEDIA_ROOT  = BASE_DIR / "media"

# summernoteの設定(エディタのサイズ調整)
# https://github.com/summernote/django-summernote
#https://stackoverflow.com/questions/74588821/how-to-change-file-upload-size-limit-django-summernote

UPLOAD_SIZE = 200 * 1000 * 1000
SUMMERNOTE_CONFIG = { 
    'attachment_filesize_limit': UPLOAD_SIZE,
    'summernote': {
        'width': '100%',
        'height': '480',
    }   
}

# 許可するHTMLタグと属性の指定(XSSに注意。scriptタグとonclick,onsubmitなどの属性は追加厳禁)
# bleachで判定する
ALLOWED_TAGS = [ 
    'a', 'div', 'p', 'span', 'img', 'em', 'i', 'li', 'ol', 'ul', 'strong', 'br',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'table', 'tbody', 'thead', 'tr', 'td',
    'abbr', 'acronym', 'b', 'blockquote', 'code', 'strike', 'u', 'sup', 'sub','font'
]
ATTRIBUTES = { 
    '*': ['style', 'align', 'title', 'style' ],
    'a': ['href', ],
    'img': ['src', ],
}
#===============================================================================


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / "templates",
                  BASE_DIR / "templates"/ "allauth" # allauthのGitHubからテンプレートをDLして配置。注意インストールするallauthとGitHubからダウンロードするtemplateのバージョンを揃えること
            ],#HTMLの保管場所を指定　プロジェクトの直下にtemplatesファイルを作らなくてはいけない。（manage.pyと同じ階層）
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'#日本語にする

TIME_ZONE = 'Asia/Tokyo'#日本時間にする

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
"""
cssを反映させるには↓このコードを追記すると良い
STATICFILES_DIRS = 〜〜〜〜〜
アプリケーション内の静的ファイルが格納されているディレクトリを指定することができる。これにより、静的ファイルの管理が簡単になる。これにより得られるメリットは複数ある。

STATICFILES_DIRS = [ BASE_DIR / "static" ]を記載しなくてもCSSga反映する理由↓
静的ファイルを処理するためにデフォルトでSTATICFILES_FINDERS設定を使用。これには、AppDirectoriesFinderが含まれている。これにより、Djangoはアプリケーション内のstaticディレクトリを自動的に検索し、静的ファイルを探す。したがって、アプリケーション内にstaticディレクトリがあり、その中にCSSファイルがある場合、デフォルト設定でDjangoが自動的にstaticディレクトリを検索し、CSSファイルを見つけることができる。ただし、アプリケーション外の別のディレクトリに静的ファイルがある場合、または複数のアプリケーションに共通の静的ファイルがある場合は、STATICFILES_DIRS設定が必要になります。
"""

STATICFILES_DIRS = [ BASE_DIR / "static" ]

"""
staticとは静的という意味
STATICFILES_DIRS = [ BASE_DIR / "static" ]はプロジェクトディレクトリ直下のstaticという名前のディレクトリを
静的ファイルを格納するディレクトリとして扱う事を意味する
設定が終わったら プロジェクトディレクトリの直下にstaticディレクトリを作る
そしてstaticディレクトリ内に直接CSSやJSを配置しても良いが より管理しやすくするために アプリごと CSS JSごとにディレクトリ構造を考慮するため staticディレクトリの中にアプリ名と同じファイルを作り その中にCSSフォルダを作り やっとその中にstyle.cssのファイルを作る
そしてHTMLに一番上に{% load static %}と追加
headタグ内にテンプレートタグのstaticを使用してstyle.cssを読み込み
<link rel="stylesheet"  type="text/css" href="{% static 'bbs/css/style.css' %}">
"""


"""
管理サイトのセキュリティーを強化する↓
今回は参考のサイトを習ってUUIDを使用する
→https://noauto-nolife.com/post/django-admin-protect/

何も設定しなければhttp://127.0.0.1:8000/admin/で誰でも管理サイトログインページを開けてしまう。
そこで、UUIDをadminのURLに割り当てる。
開発環境の段階（デバック）で書く必要はないが、デプロイする場合はかく必要がある。
※デプロイとは、ソフトウェアやアプリケーション、ウェブサイトなどの開発が完了した後、実際に稼働環境に導入することを指します。つまり、コンピューターシステム上で実行可能な形式に変換し、ユーザーがアクセスできる状態にすることです。
"""
ADMIN_PATH =""
