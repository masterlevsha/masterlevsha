from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('remont-televizorov/', remont_televizorov, name='remont-televizorov'),
    path('remont-stiralnyh-mashin/', remont_stiralnyh_mashin, name='remont-stiralnyh-mashin'),
    path('remont-posudomoechnyh-mashin/', remont_posudomoechnyh_mashin, name='remont-posudomoechnyh-mashin'),
    path('remont-holodilnikov/', remont_holodilnikov, name='remont-holodilnikov'),
    path('remont-kofemashin/', remont_kofemashin, name='remont-kofemashin'),
    path('remont-ehlektroplit/', remont_ehlektroplit, name='remont-ehlektroplit'),
    path('remont-varochnyh-panelej/', remont_varochnyh_panelej, name='remont-varochnyh-panelej'),
    path('remont-duhovyh-shkafov/', remont_duhovyh_shkafov, name='remont-duhovyh-shkafov'),
    path('remont-mikrovolnovok/', remont_mikrovolnovok, name='remont-mikrovolnovok'),
    path('remont-shveinih-mashin/', remont_shveinih_mashin, name='remont-shveinih-mashin'),

    path('robots.txt/', robots, name='robots'),
    path('sitemap.xml/', sitemap, name='sitemap'),
]
