from django.urls import path
# ]
from rest_framework.routers import DefaultRouter

from .views import TodoViewset

# urlpatterns = [ path('', ListTodo.as_view()),
#     path('<int:pk>/', DetailTodo().as_view())

router = DefaultRouter()
router.register('',TodoViewset, basename='todos')

urlpatterns = router.urls
