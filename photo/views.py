from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import PhotoPost
from django.views.generic import DetailView

# IndexView（インデックスページ）
class IndexView(ListView):
    template_name = "index.html"

    queryset = PhotoPost.objects.order_by("-posted_at")

    paginate_by = 9


# ログインしているユーザーのみアクセス可能
@method_decorator(login_required, name="dispatch")
class CreatePhotoView(CreateView):
    form_class = PhotoPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy("photo:post_done")  # 投稿成功後のリダイレクト先

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user  # ログインユーザーの情報を保存
        postdata.save()
        return super().form_valid(form)


# 投稿成功ページを表示するビュー
class PostSuccessView(TemplateView):
    template_name = "post_success.html"


class CategoryView(ListView):
    template_name = "index.html"
    paginate_by = 9

    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs["category"]
        # filter(フィールド名=id)で絞り込む
        categories = PhotoPost.objects.filter(category=category_id).order_by(
            "-posted_at"
        )
        return categories


class UserView(ListView):
    template_name = "index.html"
    paginate_by = 9

    def get_queryset(self):
        # self.kwargsでキーワードの辞書を取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs["user"]
        # filter(フィールド名=id)で絞り込む
        user_list = PhotoPost.objects.filter(user=user_id).order_by("-posted_at")
        return user_list
    
class DetailView(DetailView):
    template_name='detail.html'
    model = PhotoPost
class MypageView(ListView):
    template_name='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = PhotoPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return queryset
