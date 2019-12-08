from django.urls import path, include
# from .views import fbv, cbv, mainapi
# from .views import mainapi_person_generic, mainapi_house_generic
from .views import mainapi_person_viewset, mainapi_house_viewset
from rest_framework.routers import DefaultRouter # for Viewsets 

# URLPATTERNS FOR FBV, CBV, CBV WITH SERIALIZED MODELS, GENERIC CBV WITH SERIALIZED MODELS
urlpatterns = [    
    # path('fbv/', fbv, name='fbv'),
    # path('cbv/', cbv.as_view(), name='cbv'),
    # path('main/', mainapi.as_view(), name='main'),
    # path('main_person_generic/', mainapi_person_generic.as_view(), name='main_person_generic'),
    # path('main_house_generic/', mainapi_house_generic.as_view(), name='main_house_generic')
     path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),     
]

router = DefaultRouter()
router.register(r'person', mainapi_person_viewset)
router.register(r'house', mainapi_house_viewset)
urlpatterns += router.urls