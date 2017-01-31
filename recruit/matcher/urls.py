
from django.conf.urls import url

from . import views

app_name = 'matcher'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    # ex: /matcher/5/person/
    url(r'^(?P<pk>[0-9]+)/person/$', views.PersonView.as_view(), name='persondetail'),
    url(r'^people/', views.PeopleList.as_view(), name='people_list'),
    url(r'^person/add/$', views.PersonCreate.as_view(), name='person_add'),
    url(r'^person/(?P<pk>[0-9]+)/edit/$', views.PersonUpdate.as_view(), name='person_update'),

    # ex: /matcher/5/company/
    url(r'^(?P<pk>[0-9]+)/company/$', views.CompanyDetail.as_view(), name='companydetail'),
    url(r'^companies/', views.CompanyList.as_view(), name='company_list'),
    url(r'^company/add/$', views.CompanyCreate.as_view(), name='company_add'),
    url(r'^company/(?P<pk>[0-9]+)/edit/$', views.CompanyUpdate.as_view(), name='company_update'),
   
    url(r'^(?P<position_id>[0-9]+)/position/$', views.positiondetail, name='positiondetail'),
    url(r'^positions/', views.PositionList.as_view(), name='position_list'),
    url(r'^position/add/', views.PositionCreate.as_view(), name='position_add'),
    url(r'^position/(?P<pk>[0-9]+)/edit/$', views.PositionUpdate.as_view(), name='position_update'),

    # ex: /matcher/5/match/ 
    url(r'^(?P<match_id>[0-9]+)/match/$', views.matchdetail, name='matchdetail'),
    url(r'^matches/', views.MatchList.as_view(), name='match_list'),
    url(r'^match/add/', views.MatchCreate.as_view(), name='match_add'),
    url(r'^match/(?P<pk>[0-9]+)/edit/$', views.MatchUpdate.as_view(), name='match_update'),
  # ex: /matcher/5/interview/ 
    url(r'^(?P<interview_id>[0-9]+)/interview/$', views.interviewdetail, name='interviewdetail'),
    url(r'^interview/add/', views.InterviewCreate.as_view(), name='interview_add'),
  
#    url(r'^interviews/', views.InterviewList.as_view(), name='interview_list'),
    url(r'^interview/add', views.InterviewCreate.as_view(), name='interview_add'),

]