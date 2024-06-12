from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'index.html', context)


class MetricsView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'metrics.html', context)


class HypothesesView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'hypotheses.html', context)

class BoardView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'board.html', context)

    def get_ab_results(self,request):
        variant = request.GET.get('variant')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')


class AddMetricsView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'metrics_add.html', context)

class DesignABView(View):
    def get(self, request):
        context = {'message': 'Hello, world!'}
        return render(request, 'design.html', context)