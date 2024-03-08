from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from accountshop.models import item_test
def index(request):
    return render(request, 'index.html')
def test(request):
    if request.method == 'POST':
        if request.POST.get('tname_item') and request.POST.get('tprice') and request.POST.get('tavailability') and request.POST.get('tpicture'):
            saveRecord = item_test()

            saveRecord.tname_item = request.POST.get('tname_item')
            saveRecord.tprice = request.POST.get('tprice')
            saveRecord.tavailability = request.POST.get('tavailability')
            saveRecord.tpicture = request.POST.get('tpicture')

            saveRecord.save()
            return HttpResponse ("added successfully!!!!!")
    else: 
        return render(request, 'test.html')

