from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import AppsDatabase
from .serializers import AppsSerializer


@api_view(['GET', 'POST'])
def apps_list(request):
    """
 List  aps, or create a new app.
 """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        apps = AppsDatabase.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(apps, 5)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = AppsSerializer(data, context={'request': request}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data, 'count': paginator.count, 'numpages': paginator.num_pages, 'nextlink': '/api/apps/?page=' + str(nextPage), 'prevlink': '/api/apps/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = AppsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def apps_detail(request, id):
    """
 Retrieve, update or delete an app by id/pk.
 """
    try:
        app = AppsDatabase.objects.get(id=id)
    except AppsDatabase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AppsSerializer(app, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AppsSerializer(app, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        app.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
