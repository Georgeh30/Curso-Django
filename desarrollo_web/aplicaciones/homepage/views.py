from django.views.generic import TemplateView


# LO QUE HACE EL [TempateView] ES RENDERIZAR UN TEMPLATE OSEA,
# PRESENTAR UNA PLANTILLA EL CUAL LE MANDEMOS COMO PARAMETRO EN EL [template_name]
class IndexView(TemplateView):
    template_name = 'index.html'
