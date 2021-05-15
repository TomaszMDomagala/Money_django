from rest_framework     import viewsets
from .serializers       import AccountSerializer, SnkrSerializer
from snkrs.models       import Account, Snkr
from django.shortcuts   import render

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class    = AccountSerializer
    queryset            = Account.objects.all()

class SnkrViewSet(viewsets.ModelViewSet):
    serializer_class    = SnkrSerializer
    queryset            = Snkr.objects.all()

def snkrs(request):
    names = Snkr.objects.all()
    context = {
        'name': names,
    }
    return render(request, 'snkrs/index.html', context=context)