# Live Diary

## アプリ概要

ライブの感想をSNSで投稿する方も多いかと思いますが、後から遡って探すのは意外と難しい。  
同じくライブ好きの友人と「あのライブのセトリなんだっけ？」「あの年のフェスの出演アーティスト誰がいたっけ？」という会話になることも。

このアプリは、そんな時に“自分だけのライブ記録”を手軽に振り返るために作成しました。  
もちろんググれば情報は出てきますが、自分の記録と一緒に読み返すことで会話がさらに広がる——そんな体験を目指しています。

---

##  機能一覧

- ユーザー登録・ログイン（Django Allauth）
- ライブ日記の作成・編集・削除
- フォルダ分けによる整理
- Summernoteによる画像つきリッチテキスト投稿
- 管理画面からのデータ管理（Django Admin）

---

##  使用技術

- Python / Django
- HTML / CSS / JavaScript
- Django Allauth
- django-summernote
- SQLite（開発用DB）
- Git / GitHub

---

##  セットアップ手順（ローカル環境）

1. このリポジトリをクローン
git clone https://github.com/suzuki-git-hub/live-diary.git
cd live-diary

２. 仮想環境を作成して起動
python3 -m venv env
source env/bin/activate

３. 必要なパッケージをインストール
pip install -r requirements.txt

４. 「.env」 ファイルを作成して以下のように設定
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

5. マイグレーション
python manage.py migrate

6. 開発用サーバーを起動
python manage.py runserver

7. ブラウザでアクセス
http://127.0.0.1:8000/
---

⚠️ 注意事項---
現在も制作途中です。
ログインユーザーごとに日記を分ける設計のはずが、すべてのユーザーに共通で表示されてしまう不具合があります（原因調査中）。
UI/UXの面でも改善が必要です。
今後、デザインの調整や不具合修正、機能追加を予定しています。

💬 今後のアップデート予定---
ユーザーごとの日記データ管理の修正
UI/UX
日記の検索・フィルター機能
お気に入り機能やタグ付け　など

🌙最後に---
お忙しい中、ここまでご覧いただきありがとうございます。
自己学習を重ねながら作成したため、至らない点や読みづらい箇所も多々あるかと思いますが、温かく見守っていただけますと幸いです。
