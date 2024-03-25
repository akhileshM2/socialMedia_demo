from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
urlpatterns = [
               path('',views.index,name="index"),
               path('login/',views.login,name="login"),
               path('logout/',views.logout,name='logout'),
               path('password_change/',auth_view.PasswordChangeView.as_view(template_name="user/password_change.html"),name="password_change"),
               path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(template_name="user/password_done.html"),name="password_change_done"),
               path('password_reset/',auth_view.PasswordResetView.as_view(template_name="user/password_reset_form.html"),name="password_reset"),
               path('password_reset/done',auth_view.PasswordResetDoneView.as_view(template_name="user/password_reset_done.html"),name="password_reset_done"),
               path('password_reset/confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"),name="password_reset_confirm"),
               path('password_reset/complete',auth_view.PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"),name="password_reset_complete"),
               path('register/',views.register,name='register'),
               path('edit/',views.edit,name="edit")
              ]
