from django.shortcuts import render
from spending.models import Category, Spending
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
import datetime

def main_page(request):
    current_month = datetime.date.today().month
    current_year = datetime.date.today().year
    latest_spending_added = Spending.objects.all()
    latest_spending = latest_spending_added.exclude(
        date__lt=datetime.date(
            current_year, 
            current_month,
            1)).exclude(
        date__gt=datetime.date(
            current_year,
            (current_month+1),
            1
        ))
    total = 0
    for item in latest_spending:
        total += item.value

    context = {
        'latest_spending': latest_spending,
        'total': total
    }

    return render(request, 'spending/index.html', context=context)

def SpendingAboutView(request):
    return render(request, 'spending/about.html')

class SpendingDetailView(DetailView):
    model = Spending

    def get_object(self, queryset=None):
        return Spending.objects.get(uuid=self.kwargs.get("uuid"))

class CreateSpendingView(CreateView):
    model = Spending
    fields = ['title', 'value', 'description', 'category']

    def form_valid(self, form):
        return super().form_valid(form)

class SpendingUpdateView(UpdateView):
    model = Spending
    fields = ['title', 'value', 'description', 'category', 'date']

    def get_object(self, queryset=None):
        return Spending.objects.get(uuid=self.kwargs.get("uuid"))

    def form_valid(self, form):
        return super().form_valid(form)

class SpendingDeleteView(DeleteView):
    model = Spending
    success_url = '/spending/'

    def get_object(self, queryset=None):
        return Spending.objects.get(uuid=self.kwargs.get("uuid"))

