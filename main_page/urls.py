from django.urls import path
from main_page.views import main_page, temp_page


urlpatterns = [
    path("", main_page, name="main_page"),
    path("temp/", temp_page, name="temp_page")

]
