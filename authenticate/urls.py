from .views2 import *
from authenticate import views
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'family_detail', FamilyDetailViewSet)
router.register(r'personal_detail', PersonalDetailViewSet)
router.register(r'school_detail', SchoolDetailViewSet)
router.register(r'subject_mark', SubjectMarksViewSet)
router.register(r'bank_detail', BankDetailViewSet)


urlpatterns = [
    path('', views.index),
    path('api', include(router.urls)),
    path('application', views.application),
    path('bank_detail', views.bankdetail),
    path('change_password', views.change),
    path('education', views.education),
    path('family_detail', views.familydetail),
    path('helpdesk', views.help),
    path('login', views.loginuser),
    path('logout', views.logoutuser),
    path('personal_detail', views.personaldetail),
    path('phase1', views.phase1),
    path('phase2', views.phase2),
    path('profile', views.profile),
    path('signin', views.signin),
    # path('upload', views.upload)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)