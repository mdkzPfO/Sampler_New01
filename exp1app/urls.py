from django.contrib import admin
from django.urls import path
from .views import TopPageView,ReportList,ReportList_Create,ReportList_Delete,ReportList_Detail,ReportList_Update,SamplingList,SamplingList_Delete,SamplingList_Detail,SamplingList_Update,SamplingList_Create,AnimalList,AnimalList_Create,AnimalList_Delete,AnimalList_Detail,AnimalList_Update,Group_Create

app_name='exp1app'
urlpatterns=[
#どの操作を行うか選択するトップページ、今日の飼育履歴が画面下部に表示される
path('Top_Page',TopPageView,name='Top_Page'),
#サンプリングリスト
path('Sampling_List/',SamplingList.as_view(),name='Sampling_List'),
path('SamplingList_Create/',SamplingList_Create.as_view(),name="SamplingList_Create"),
path('SamplingList_Detail/<int:pk>/',SamplingList_Detail.as_view(),name="SamplingList_Detail"),
path('SamplingList_Delete/<int:pk>/',SamplingList_Delete.as_view(),name="SamplingList_Delete"),
path('SamplingList_Update/<int:pk>/',SamplingList_Update.as_view(),name="SamplingList_Update"),
#飼育レポート
path('Report_List/',ReportList.as_view(),name='Report_List'),
path('ReportList_Create/',ReportList_Create.as_view(),name="ReportList_Create"),
path('ReportList_Detail/<int:pk>/',ReportList_Detail.as_view(),name="ReportList_Detail"),
path('ReportList_Delete/<int:pk>/',ReportList_Delete.as_view(),name="ReportList_Delete"),
path('ReportList_Update/<int:pk>/',ReportList_Update.as_view(),name="ReportList_Update"),
#飼育生物情報
path('Animal_List/',AnimalList.as_view(),name='Animal_List'),
path('AnimalList_Create/',AnimalList_Create.as_view(),name="AnimalList_Create"),
path('AnimalList_Detail/<int:pk>/',AnimalList_Detail.as_view(),name="AnimalList_Detail"),
path('AnimalList_Delete/<int:pk>/',AnimalList_Delete.as_view(),name="AnimalList_Delete"),
path('AnimalList_Update/<int:pk>/',AnimalList_Update.as_view(),name="AnimalList_Update"),
#アカウント払い出し
path('Manager/Group_Create',Group_Create.as_view(),name="Group_Create"),

]
