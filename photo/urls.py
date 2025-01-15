from django.urls import path
from . import views

app_name = "photo"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("post/", views.CreatePhotoView.as_view(), name="post"),
    path("post_done/", views.PostSuccessView.as_view(), name="post_done"),
    # photos/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path("photos/<int:category>", views.CategoryView.as_view(), name="photos_cat"),
    # ユーザーの投稿一覧ページ
    # photos/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}としてCategoryViewに渡される
    path("user-list/<int:user>", views.UserView.as_view(), name="user_list"),
# 詳細ページ
# photo-detail/<Photo postsテーブルのid値>にマッチング
# <int:pk>は辞書{pk: id値(int)}としてDetailViewに渡される
    path('photo-detail/<int:pk>',
    views.DetailView.as_view(),
    name = 'photo_detail'
    ),
path('mypage/', views.MypageView.as_view(), name='mypage'),
]
