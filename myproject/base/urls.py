from django.urls import path
from .views import *

# urlpatterns = [
#     path('',home,name='home'),
#     path('add/',add,name='add'),
#     path('about/',about,name='about'),
#     path('trash/',trash,name='trash'),
#     path('complete/',complete,name='complete'),

#     path('update<int:pk>',update,name='update'),
#     path('delete/<int:pk>',delete,name='delete'), # home page delete button
#     path('complete_/<int:pk>',complete_,name='complete_'), # home page complete button
#     path('delete_all/<int:pk>',delete_all,name='delete_all'), # delete_all button for home page
#     path('complete_deleteall',complete_deleteall,name='complete_deleteall'),# delete all button on the complete page


#     path('cdelete/<int:pk',cdelete,name='cdelete'), # delete the button on the complete page
#     path('crestore/<int:pk>',crestore,name='crestore'), # restore button on the complete page
#     path('trestore/<int:pk>',trestore,name='trestore'), # restore button on the trash 
#     path('tdelete/<int:pk>',tdelete,name='tdelete'), # delete button on the trash

#     path('crestore_all/<int:pk>',crestore_all,name='crestore_all'), # restore button on the complete page


# ]


urlpatterns = [
    
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('about/', about, name='about'),
    path('trash/', trash, name='trash'),
    path('complete/', complete, name='complete'),

    
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'), # home page delete button
    path('complete_/<int:pk>/', complete_, name='complete_'),   # home page complete button
    path('cdelete/<int:pk>/', cdelete, name='cdelete'),   # delete the button on the complete page
    path('crestore/<int:pk>/', crestore, name='crestore'), # restore button on the complete page
    path('trestore/<int:pk>/', trestore, name='trestore'), # restore button on the trash 
    path('tdelete/<int:pk>/', tdelete, name='tdelete'),  # delete button on the trash

    
    path('delete_all/', delete_all, name='delete_all'),  # delete_all button for home page
    path('complete_all/', complete_all, name='complete_all'), 
    path('crestore_all/', crestore_all, name='crestore_all'), # restore button on the complete page
    path('complete_deleteall/', complete_deleteall, name='complete_deleteall'),  # delete all button on the complete page
]