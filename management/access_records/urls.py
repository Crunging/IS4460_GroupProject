from .views import AccessRecordListView, AccessRecordDetailView, AccessRecordCreateView, AccessRecordUpdateView, AccessRecordDeleteView

urlpatterns = [
    # URL pattern for the list view of access permissions
    path('', AccessRecordListView.as_view(), name='accessrecord_list'),
    
    # URL pattern for the detail view of a specific access permission
    path('<int:pk>/', AccessRecordDetailView.as_view(), name='accessrecord_detail'),
    
    # URL pattern for creating a new access permission
    path('create/', AccessRecordCreateView.as_view(), name='accessrecord_form'),
    
    # URL pattern for updating an existing access permission
    path('<int:pk>/update/', AccessRecordUpdateView.as_view(), name='accessrecord_form'),
    
    # URL pattern for deleting an access permission
    path('<int:pk>/delete/', AccessRecordDeleteView.as_view(), name='accessrecord_confirm_delete'),
]
