from django.urls import path
from .views import AccountRegisterView, LoginView, AccountView, \
    AccountRetrieveUpdateView, AccountOwnImageUpdateView, AccountListView, \
    SetNewPasswordView


app_name = 'account'

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('get-account/', AccountView.as_view()),
    path('detail/update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
    # path('retrieve-update/<int:pk>/', AccountOwnImageUpdateView.as_view()),
    path('list/', AccountListView.as_view()),
    # path('set-password/', SetNewPasswordView.as_view()),
]