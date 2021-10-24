from django.shortcuts import render, get_object_or_404

from currency.models import Rate
from currency.forms import RateForm

from django.http.response import HttpResponse, HttpResponseRedirect, Http404


# READ (list)
def rate_list(request):
    """
    MTVU
    V - view
    U - urls
    M - model
    T - template
    """

    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def rate_details(request, pk):
    rate = get_object_or_404(Rate, id=pk)
    context = {
        'rate': rate,
    }
    return render(request, 'rate_details.html', context)

# CREATE
def rate_create(request):
    if request.method == 'POST':  # 2 submit form data
        form = RateForm(request.POST)
        if form.is_valid():
            form.save()  # get validated data, save Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':  # 1 get empty form
        form = RateForm()

    context = {
        'form': form,
    }
    return render(request, 'rate_create.html', context)


# UPDATE
def update_rate(request, pk):

    '''
    BAD /rate/update/?id=101
    GOOD /rate/update/101/
    '''
    # try:
    #     rate = Rate.objects.get(id=pk)
    # except Rate.DoesNotExist:
    #     raise Http404('Object does not exist')

    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'POST':  # 2 submit form data
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()  # get validated data, save Rate.objects.create(**validated_data)
            return HttpResponseRedirect('/rate/list/')
    elif request.method == 'GET':  # 1 get empty form
        form = RateForm(instance=rate)

    context = {
        'form': form,
    }
    return render(request, 'rate_update.html', context)


# DELETE
def delete_rate(request, pk):
    rate = get_object_or_404(Rate, id=pk)

    if request.method == 'GET':
        context = {
            'object': rate,
        }
        return render(request, 'rate_delete.html', context)
    elif request.method == 'POST':
        rate.delete()
        return HttpResponseRedirect('/rate/list/')


def test_template(request):
    name = request.GET.get('name')
    context = {
        'username': name,
    }
    return render(request, 'test.html', context)


def status_code(request):
    '''
    1xx - info
    2xx - success
    200 - OK
    201 - Created
    202 - Accepted
    204 - No content
    3xx - redirect
    301 - перемещено навсегда
    302 - перемещено временно
    4xx - client error
    400 - Bad Request
    401 - Unauthorized
    402 - Payment Required
    403 - Forbidden
    404 - Not Found
    405 - Method Not Allowed
    5xx - Server fail
    500 - Code error (python)
    502
    503
    504
    '''

    # raise Http404('NF')
    # 1 + ''

    if True:
        response = HttpResponse(
            'User was created',
            status=201,
            # headers={'Location': '/rate/list/'},
        )
    else:
        response = HttpResponse(
            'Error. Invalid data',
            status=400,
            # headers={'Location': '/rate/list/'},
        )

    return response


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def request_methods(request):

    '''
    1. GET - client wants to get smth from server (read)
    http://localhost?name=Dima&age=29

    2. POST - client wants to push data to the server (create)
    http://localhost

    name=Dima&age=29

    3. PUT - client wants to update record (update) name=Dima&age=29
    4. PATCH - client wants to update record partially (partial update) name=Dima or age=29

    5. DELETE - client wants to delete record (delete)

    C - POST (create)
    R - GET (read)
    U - PUT/PATCH (update)
    D - DELETE (delete)

    6. OPTIONS - client wants to know available request methods (list methods)
    7. HEAD (GET) - client wants to know information about response (describe) (no body is sent)

    HTML - GET, POST
    '''

    if request.method == 'GET':
        message = 'Render Client Form'
        Rate.objects.all().delete()
    elif request.method == 'POST':
        message = 'Validate form data'

    return HttpResponse(message)
