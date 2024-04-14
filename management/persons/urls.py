from django.urls import path
from .views import HomePageView, PersonList, PersonDetail, PersonCreate, PersonUpdate, PersonDelete

urlpatterns = [
    path('', PersonList.as_view(), name='person_list'),
    path('<int:uid>/', PersonDetail.as_view(), name='person_detail'),
    path('create/', PersonCreate.as_view(), name='person_create'),
    path('<int:uid>/update/', PersonUpdate.as_view(), name='person_update'),
    path('<int:uid>/delete/', PersonDelete.as_view(), name='person_delete'),
    path('home/', HomePageView.as_view(), name='home'),
]
