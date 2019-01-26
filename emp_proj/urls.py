
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from emp_app.views import(kitchendetails_view,
    doors_view,
    edit_door_system,
    edit_system, 
    home_view,
    login_view,
    logout_view,
    register_view,
    handle_view,
    cart_view,
    halldetails_view,
    bedroomdetails_view,
    edit_bedroom_handle,
    edit_hall_handle,
    checkout_view,
    edit_bedroom_doors,
    edit_hall_doores,
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('register', register_view, name='register'),
    path('handles/',handle_view),
    path('doors/',doors_view),
    path('cart/',cart_view),
    path('k_details/',kitchendetails_view),
    path('b_details/',bedroomdetails_view),
    path('h_details/',halldetails_view),
    path('checkout/',checkout_view),

    path('', RedirectView.as_view(url='/home')),

    path('handles/<int:id>/edit', edit_system, name='edit_system'),
    path('handles/<int:id>/bedit', edit_bedroom_handle, name='bedit_system'),
    path('handles/<int:id>/hedit', edit_hall_handle, name='hedit_system'),
    path('doors/<int:id>/bedit', edit_bedroom_doors, name='bedit_system'),
    path('doors/<int:id>/hedit', edit_hall_doores, name='hedit_system'),
    path('doors/<int:id>/edit', edit_door_system, name='edit_door_system'),

]

