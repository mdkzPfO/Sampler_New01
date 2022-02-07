from django.contrib import admin
from django.urls import path
from .views import TopPageView,ReportPageClass,ReportCheckView,ReportListView,SamplingPageClass,SamplingListView,SamplingCheckView,PreserveListView,PreserveCheckView,AnimalPageClass,AnimalListView,AnimalCheckView,signupview,loginview

urlpatterns=[
path('signup/',signupview,name='signup'),
path('login/',loginview,name='login'),
#どの操作を行うか選択するトップページ、今日の飼育履歴が画面下部に表示される
path('Top_Page',TopPageView,name='Top_Page'),
#飼育レポートを作成する為のページ
path('Report_Page/',ReportPageClass.as_view(),name='Report_Page'),
#飼育レポートリストを確認するためのページ
path('Report_List/',ReportListView,name='Report_List'),
#カレンダー形式で過去のレポートデータを確認することができる
path('Report_Check/<int:pk>/',ReportCheckView,name='Report_Check'),
#サンプリングの方法/結果の作成ページ
path('Sampling_Page/',SamplingPageClass.as_view(),name="Sampling_Page"),
#サンプリングリストの確認ページ
path('Sampling_List/',SamplingListView,name='Sampling_List'),
#サンプリングの方法/結果を確認するページ
path('Sampling_Check/<int:pk>/',SamplingCheckView,name='Sampling_Check'),
#サンプルの保存リストの確認ページ
path('Preserve_List/',PreserveListView,name="Preserve_List"),
#保存したサンプルの一覧データベース
path('Preserve_Check/',PreserveCheckView,name='Preserve_Check'),
#各動物の飼育方法、情報作成
path('Animal_Page/',AnimalPageClass.as_view(),name="Animal_Page"),
#各動物の飼育リストの閲覧
path('Animal_List/',AnimalListView,name="Animal_List"),
#各動物の飼育方法閲覧
path('Animal_Check/<int:pk>/',AnimalCheckView,name="Animal_Check"),
]
