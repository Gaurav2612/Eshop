from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('singleProduct/<int:id>/',views.singleProduct),
    path('login/',views.login),
    path('signup/',views.signup),
    path('profile/',views.profilePage),
    path('logout/',views.logout),
    path('updateprofile/',views.updateSellerProfile),
    path('add-product/',views.addProduct),
    path('update-Product/<int:id>/',views.updateProduct),
    path('delete-Product/<int:id>/',views.deleteProduct),
    path('add-to-Wishlist/<int:id>/',views.addToWishlist),
    path('delete-wishlist/<int:id>/',views.deleteWishlist),
    path('add-to-cart/<int:id>/',views.addToCart),
    path('remove-from-cart/<int:id>/',views.removeFromCart),
    path('update-cart/<int:id>/<int:num>/',views.updateCart),
    path('cart/',views.cartPage),
    path('checkout/',views.checkoutPage),
    path('confirmation/',views.confirmationPage),
    path('about/',views.aboutPage),
    path('newslatter/',views.newslatterPage),
    path("contact/", views.contactpage),
    path("forget-email/",views.forgetEmail),
    path("forget-otp/",views.forgetOTP),
    path("forget-password/",views.forgetPassword),
    



]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
