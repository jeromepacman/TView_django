from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class ProdView(TemplateView):
    template_name = "prod.html"


class InfosView(TemplateView):
    template_name = "infos.html"
