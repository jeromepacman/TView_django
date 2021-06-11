from django.views.generic import TemplateView, FormView


class IndexView(TemplateView):
    template_name = "index.html"


class YouView(TemplateView):
    template_name = "you.html"


class ShopView(TemplateView):
    template_name = "shop.html"


class AppsView(TemplateView):
    template_name = "apps.html"


class InfosView(TemplateView):
    template_name = "infos.html"


class ContactView(TemplateView):
    template_name="contact.html"


