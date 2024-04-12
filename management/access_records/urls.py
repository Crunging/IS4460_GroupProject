from django.urls import path
from .views import AccessRecordList, AccessRecordDetail, AccessRecordCreate, AccessRecordUpdate, AccessRecordDelete
   

urlpatterns = [
    path('', AccessRecordList.as_view(), name='accessrecord_list'),
    path('<int:RecordID>/', AccessRecordDetail.as_view(), name='accessrecord_detail'),
    path('create/', AccessRecordCreate.as_view(), name='accessrecord_create'),
    path('<int:RecordID>/update/', AccessRecordUpdate.as_view(), name='accessrecord_update'),
    path('<int:RecordID>/delete/', AccessRecordDelete.as_view(), name='accessrecord_delete'),
]