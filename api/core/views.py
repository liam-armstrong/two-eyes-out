from . import models, serializer
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = models.customUser.objects.all()
    serializer_class = serializer.userSerializer

class SectionsViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = models.section.objects.all()

    def list(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        authentication_classes = (JSONWebTokenAuthentication,)
        print("request: " + str(request))
        print("data: " + str(request.data))
        print("user: " + str(request.user))
        queryset = request.user.sections.all()
        serial = serializer.sectionSerializer(queryset, many=True)
        return Response(serial.data)

    def create(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        authentication_classes = (JSONWebTokenAuthentication,)

        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors,
                        status=status.HTTP_400_BAD_REQUEST)

        section = serial.create(serial.validated_data)

        print("before: " + str(request.user.sections.all()))
        request.user.addSection(section)
        print("after: " + str(request.user.sections.all()))

        return Response(serial.validated_data, status=status.HTTP_201_CREATED)