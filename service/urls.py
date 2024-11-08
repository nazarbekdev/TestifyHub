from django.urls import path
from .views import home, pricing, subscribe, about, support, support_contact, projects, partnership, partner_request\
    , some_view, watch_demo_view, try_for_14_view,  trial_success


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('support/', support, name='support'),
    path('support/contact', support_contact, name='support_contact'),
    path('projects/', projects, name='projects'),
    path('pricing/', pricing, name='pricing'),
    path('partnership/', partnership, name='partnership'),
    path('partner_request/', partner_request, name='partner_request'),
    path('subscribe/', subscribe, name='subscribe'),
    path('some_view/', some_view, name='some_view'),
    path('watch-demo/', watch_demo_view, name='watch_demo'),
    path('try-for-14-days/', try_for_14_view, name='try_for_14_days'),
    path('trial-success/', trial_success, name='trial_success'),
]
