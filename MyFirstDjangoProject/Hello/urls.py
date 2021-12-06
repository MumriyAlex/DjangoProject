from django.urls import path
from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
#     path("brian", views.brian, name="brian"),
#     path("david", views.david, name="david")
# ]
#-------------------------------------------
# urlpatterns = [
#     path("<str:name>", views.greet, name="greet")
# ]
#-----------------------------------------------
urlpatterns = [
    path("<str:name>", views.greet, name="greet")
]