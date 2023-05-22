from django.urls import include, path

urlpatterns_api = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

urlpatterns = [
    path('auth/', include(urlpatterns_api)),
    path('v1/', include('api.v1.urls'))
]
