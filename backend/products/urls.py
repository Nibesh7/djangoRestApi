from django.urls import path

from . import views
urlpatterns = [
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view)
    path('',views.ProductListCreateAPIView.as_view()),
    # path('',views.ProductMixinView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    # path('<int:pk>/',views.ProductMixinView.as_view()),
    path('<int:pk>/update',views.productUpdateAPIView.as_view()),
    path('<int:pk>/delete',views.productDeleteAPIView.as_view())

]
