from django.contrib import admin
from django.urls import path, include
from myntraData.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r"products",ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include(router.urls)),
    path('send_otp/<phone_number>', send_otp),
    path('verify_otp/<int:got_otp>', verify_otp),
    path('carousel/', get_carousel),
    path('user_address/',user_address),
    path('user_address/<int:id>',update_user_address),
    path('user_addresss/<int:user_id>',users_userAddress),
    path('wishlist', wishlist),
    path('wishlist/<int:user_id>', user_wishlist),
    path('comment/', comment),
    path('comment/<id>', update_comment),
    path('rating/', rating),
    path('cart/', cart),
    path('bag/<int:user_id>', bag),
    path('wishlists/<int:id>', update_wishlist),
    path('bags/<int:id>', update_cart),
    path('category/', category),
    path('brand_category/', brand_category),
    path("post_bought_product/", post_bought_product),
    path("bought_product/<int:user_id>", bought_product),
    path('update_user/<user_id>', add_user_info),
    path("post_user_info",user_info ),
    path("access_user_info/<int:user_id>", access_user_info),
]
