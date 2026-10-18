from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.book_detail),
    path('books/<int:book_id>/edit', views.edit_book),
    path('books/<int:book_id>/update', views.update_book),
    path('books/<int:book_id>/delete', views.delete_book),
    path('books/<int:book_id>/add_author', views.add_author_to_book),
    path('authors', views.authors_view),
    path('authors/create', views.create_author),
    path('authors/<int:author_id>', views.author_detail),
    path('authors/<int:author_id>/edit', views.edit_author),
    path('authors/<int:author_id>/update', views.update_author),
    path('authors/<int:author_id>/delete', views.delete_author),
    path('authors/<int:author_id>/add_book', views.add_book_to_author),
]