from . import models, serializer
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.exceptions import ParseError

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
        activeSerial = serializer.sectionSerializer(request.user.sections.all(), many=True, context={'is_active': True})
        inactiveSerial = serializer.sectionSerializer(request.user.inactive_sections.all(), many=True, context={'is_active': False})
        return Response(activeSerial.data + inactiveSerial.data, status=status.HTTP_200_OK)

    def create(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        authentication_classes = (JSONWebTokenAuthentication,)
        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            section = serial.create(serial.validated_data)
        except ValueError:
            return Response({'detail': 'Not a Valid Course'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.addSection(section)
        usersectionSerializer = serializer.sectionSerializer(request.user.sections.all(), many=True)
        return Response(usersectionSerializer.data, status=status.HTTP_201_CREATED)

    def remove(self, request):
        permission_classes = (permissions.IsAuthenticated,)
        authentication_classes = (JSONWebTokenAuthentication,)
        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            section = serial.get(serial.validated_data)
        except:
            return Response({'detail': 'Course Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            request.user.removeSection(section)
        except:
            return Response({'detail': request.user + " is not related to " + section}, status=status.HTTP_400_BAD_REQUEST)

        usersectionSerializer = serializer.sectionSerializer(request.user.sections.all(), many=True)
        return Response(usersectionSerializer.data, status=status.HTTP_200_OK)

        
        