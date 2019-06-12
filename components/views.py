from components.models import Component
from components.serializers import ComponentsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User


class ComponentsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Component.objects.all()
        serializer = ComponentsSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # print(request.data)
        # name = request.data.get('name')
        # submitter = request.data.get('submitter')
        # print(request.data)
        # print(name)
        # print(submitter)
        #
        # user = User.objects.get(username=submitter)
        # print(user)
        #
        # aa = Component.objects.create(name=name, submitter=user)
        # print(aa)
        #
        # component = Component.objects.get(name=name)
        # print(component)
        #
        # serializer = ComponentsSerializer(instance=component)
        # print(serializer)
        print(request.data)
        name = request.data.get('name')
        submitter = request.data.get('submitter')
        submitter_id = submitter.get('id')
        print(submitter_id)

        user = User.objects.get(id=submitter_id)

        serializer = ComponentsSerializer(data=request.data)

        if serializer.is_valid():
            print('ssssssssssssss')
            serializer.save()
            component = Component.objects.get(name=name)
            component.submitter = user
            component.save()

            serializer_new = ComponentsSerializer(instance=component)
            return Response(serializer_new.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # return Response(serializer.data, status=status.HTTP_201_CREATED)

        # serializer = ComponentsSerializer(instance=user, data=request.data)
        # print(serializer)


        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
