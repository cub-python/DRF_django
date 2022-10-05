from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

# from users_app.views import UserViewSet,BrendViewSet,BiographyViewSet
# from todo.view_example import BrendViewSet
# from todo.view_example import BrendListAPIView


# from todo.view_example import get
# from todo.view_example import BrendViewSet
# BrendLimitOffsetPaginatonViewSet
# from todo.view_example import get
# from todo.view_example import BrendCustomViewSet
# from todo.view_example import  BrendListAPIView
# from todo.view_example import BrendLimitOffsetPaginatonViewSet

# from todo.view_example import BrendAPIView
# from todo.view_example import BrendQuerysetFilterViewSet
# from todo.view_example import BrendDjangoFilterViewSet

router = DefaultRouter()
# from todo.view_example import BrendModelViewSet
# from todo.view_example import BrendModelViewSet
# router.register('brend_f', BrendModelViewSet)

# router = SimpleRouter()
# router.register('brend_f', BrendDjangoFilterViewSet)
# router.register('brend_p', BrendkLimitOffsetPaginatonViewSet)
# router.register('biography', BiographyViewSet)


# from todo.view_example import BrendCreateAPIView,BrendListAPIView,BrendRetrieveAPIView,BrendDestroyAPIView,BrendListAPIView,BrendUpdateAPIView


# level 3
# router.register('book', BrendViewSet,basename='book')

# level 4
# router.register('brend',BrendViewSet)

# level 5
# router.register('brend', BrendCustomViewSet)

# Filter
# router.register('brend_filter', BrendQuerysetFilterViewSet)


#
# router.register('brend',BrendViewSet)


class BrendAPIView:
    pass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    # # level 1
    path('api/brend', BrendAPIView.as_view()),
    # path('api/brend', get),

    # # level 2
    # path('api/list/', BrendListAPIView.as_view()),
    # path('api/create/', BrendCreateAPIView.as_view()),
    # path('api/update/<int:pk>/', BrendUpdateAPIView.as_view()),
    # path('api/delete/<int:pk>/', BrendDestroyAPIView.as_view()),
    # path('api/detail/<int:pk>/', BrendRetrieveAPIView.as_view()),

    # # level 3 - 5
    # path('api/', include(router.urls)),

    # filter part_2
    # path('api/<str:name>/',BrendListAPIView.as_view()),
    #
    # path('api/', include(router.urls)),

]
