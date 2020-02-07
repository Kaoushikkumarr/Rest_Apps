from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
from django.http import HttpResponse
from testapp.mixins import SerializeMixin, HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import EmployeeForm
from testapp.utils import is_json
# from django.core.serializers import serialize
import json

# Create your views here.

class EmployeeDetailCBV(HttpResponseMixin, SerializeMixin, View):
    ''' Creating ClassBaseView by extending Generic.View Class '''

    def get(self, request, id, *args, **kwargs):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg': "The request is not available"})
            return self.render_to_http_response(json_data, status=404)
        else:
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)
        # emp_data = {
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esal':emp.esal,
        #     'eaddr':emp.eaddr,
        # }

        # json_data = json.dumps(emp_data)
        # json_data = serialize('json', [emp,], fields=('eno', 'ename', 'eaddr'))

        return HttpResponse(json_data, content_type='application/json')

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCBV(HttpResponseMixin, SerializeMixin, View):
    ''' Retrieve ClassBaseView by extending Generic.View Class '''

    def get(self, request, *args, **kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data, content_type='application/json')


    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg': 'Please send valid json data only.'})
            return self.render_to_http_response(json_data, status=400)

        json_data = json.dumps({'msg': 'You have provided valid json data only.'})
        return self.render_to_http_response(json_data, status=400)

        empdata=json.loads
        form = EmployeeForm(empdata)

        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg': 'Resource created Successful.'})
            return self.render_to_http_response(json_data, status=400)

        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)
