from django.urls import path
from .import views


app_name    = "diary"
urlpatterns = [
    path("", views.top, name="top"),
    # path("register", views.register, name="register"),
    path("mypage/", views.mypage, name="mypage"),
    path("folder/<int:pk>/", views.folder, name="folder"),
    path("add_folder/", views.add_folder, name="add_folder"),
                                  #↑このfileは、views.pyでクラスの最後に書いた、変数名 = ビュークラス名.as_view() の変数名を入れる
    path("create/", views.create, name="create"),
    path("diary/<int:pk>/", views.diary, name="diary"),
    path("diary_delete/<int:pk>/", views.diary_delete, name="diary_delete"),
    path("diary_edit/<int:pk>/", views.diary_edit, name="diary_edit"),
    path("folder_delete/<int:pk>/", views.folder_delete, name="folder_delete"),
]