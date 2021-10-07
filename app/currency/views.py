from currency.models import Rate

from django.http.response import HttpResponse


def rate_list(request):

    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}, created: {rate.created}, source: {rate.source}<br>')

    return HttpResponse(str(results))


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
