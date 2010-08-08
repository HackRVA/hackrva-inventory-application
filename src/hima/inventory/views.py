# Create your views here.

from django.template import Context, loader
from inventory.models import Device
from django.http import HttpResponse

def index(request):
    latest_device_list = Device.objects.all().order_by('-updated')
    t=loader.get_template('index.html')
    c=Context({'latest_device_list':latest_device_list,})
    return HttpResponse(t.render(c))

def detail(request, device_id):
    device_detail = Device.objects.get(pk=device_id)
    t=loader.get_template('device.html')
    c=Context({'device_detail':device_detail})
    return HttpResponse(t.render(c))
