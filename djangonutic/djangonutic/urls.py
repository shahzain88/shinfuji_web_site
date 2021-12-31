from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views
from gaiyou import views as gaiyou_views
from shoukai import views as shoukai_views
from QandA import views as QandA_views
from contact import views as contact_veiws
from privacy import views as privacy_views
from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('articles/', include("articles.urls")),
    path('gaiyou/', include("gaiyou.urls")),
    path('shoukai/', include("shoukai.urls")),
    path('QandA/', include("QandA.urls")),
    path('contact/', include("contact.urls")),
    path('privacy/', include("privacy.urls")),
    path('home/', include("home.urls")),
    path('recruitment/', include("recruitment.urls")),
    path('about/', views.about),
    path('404/', views.view_404),

    path('robots.txt', views.view_robot_txt),
    # path('', views.homepage),
    # path('', include("articles.urls")),
    path('', home_views.home_list, name="home"),


]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
