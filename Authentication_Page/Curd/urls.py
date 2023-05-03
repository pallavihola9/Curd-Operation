
from django.urls import path
from .views import *

urlpatterns = [
    
    path("", home),
    path("home/", home),
    path("add-user/" , add_user),
    path("Delete-curd/<int:srnumber>", Delete_curd), 
    path("Update-curd/<int:srnumber>" , Update_curd),
    path("do-Update-curd/<int:srnumber>" , do_Update_curd),


]
