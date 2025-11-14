from django.urls import path
from .views import BoardPostListView, BoardPostDetailView

urlpatterns = [
    # 게시판 목록/작성 (예: /api/core/board/free/posts/)
    path('board/<str:board_type>/posts/', BoardPostListView.as_view(), name='board-post-list'),

    # 게시글 상세/수정/삭제 (예: /api/core/posts/123/)
   path('posts/<int:post_id>/', BoardPostDetailView.as_view(), name='post-detail'),
]