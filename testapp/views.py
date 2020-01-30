from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from django.core.serializers import serialize
import json

# Create your views here.

class EmployeeDetailCBV(View):
    ''' Creating ClassBaseView by extending Generic.View Class '''

    def get(self, request, id, *args, **kwargs):
        emp = Employee.objects.get(id=id)
        emp_data = {
            'eno':emp.eno,
            'ename':emp.ename,
            'esal':emp.esal,
            'eaddr':emp.eaddr,
        }

        json_data = json.dumps(emp_data)
        # json_data = serialize('json', [emp,], fields=('eno', 'ename', 'eaddr'))

        return HttpResponse(json_data, content_type='application/json')
