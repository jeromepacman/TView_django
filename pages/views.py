from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class PersoView(TemplateView):
    template_name = "perso.html"


class ShopView(TemplateView):
    template_name = "shop.html"


class ProView(TemplateView):
    template_name = "pro.html"


class InfosView(TemplateView):
    template_name = "infos.html"