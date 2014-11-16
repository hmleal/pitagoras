import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView

from core.models import PathWay, Gmm
from core.forms import PathWayForm


class HomeView(TemplateView):
    template_name = 'core/home.html'


class AnalyzesView(FormView):
    template_name = 'core/analyzes.html'
    form_class = PathWayForm

    def form_valid(self, form):
        self.request.session['pathways'] = form.cleaned_data['pathways']
        return redirect(reverse('core:grafo'))


class GrafoView(TemplateView):
    template_name = 'core/index.html'


def result(request):
    session_pathways = request.session.get('pathways')

    pathways = PathWay.objects.filter(pk__in=session_pathways)
    pathways_list = pathways.values_list('acronym', flat=True)

    gmms = Gmm.objects.filter(pathway__in=session_pathways).distinct()

    data = {
        'nodes': {},
        'edges': {}
    }

    # Monta as vias de ativacao
    for path in pathways_list:
        data['nodes'][path] = {'color': 'red', 'shape': 'dot', 'alpha': 1}

    # Monta os genes
    for gmm in gmms:
        data['nodes'][gmm.approved_symbol] = {
            'color': 'blue',
            'shape': 'dot', 'alpha': 1
        }

    # Monta as arestas
    for path in pathways:
        data['edges'][path.acronym] = {}
        for gmm in path.gmms.all():
            data['edges'][path.acronym][gmm.approved_symbol] = {}

    return HttpResponse(json.dumps(data), content_type=('application/json'))
