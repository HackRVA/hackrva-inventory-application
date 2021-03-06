# Create your views here.

from hima.inventory.models import Device
from django.template import Context, loader
from django.http import HttpResponse

def index(request):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))    

def inventory(request):
    latest_device_list = Device.objects.all().order_by('-updated')
    t = loader.get_template('inventory.html')
    c = Context({'latest_device_list':latest_device_list,})
    return HttpResponse(t.render(c))

def detail(request, device_id):
    return HttpResponse("You're looking at inventory item %s" % device_id)
