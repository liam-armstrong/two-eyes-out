from . import models, serializer, tasks
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.exceptions import ParseError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('views.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, ) 
    queryset = models.customUser.objects.all()
    serializer_class = serializer.userSerializer

    def create(self, request):
        serial = serializer.userSerializer(data=request.data)

        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = serial.create(serial.validated_data)
        except ValueError:
            return Response({'detail': 'Invalid New User Data'}, status=status.HTTP_400_BAD_REQUEST)

        tasks.send_registration_email.delay(user.id)

        logger.debug("New User Created with Email: " + str(user))
        return Response({'detail': 'User Creation Successful'}, status=status.HTTP_201_CREATED)


class SectionsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    queryset = models.section.objects.all()

    def list(self, request):
        serial = serializer.subscriptionSerializer(models.subscription.objects.filter(user=request.user).order_by('id'), many=True)
        logger.debug("Section List view returned to: " + str(request.user))
        return Response(serial.data, status=status.HTTP_200_OK)

    def create(self, request):
        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            section = serial.create(serial.validated_data)
        except ValueError:
            return Response({'detail': 'Not a Valid Course'}, status=status.HTTP_400_BAD_REQUEST)

        request.user.addSection(section)

        reqSerial = serializer.subscriptionSerializer(models.subscription.objects.filter(user=request.user).order_by('id'), many=True)
        logger.debug("Section added to: " + str(request.user))
        return Response(reqSerial.data, status=status.HTTP_201_CREATED)

    def remove(self, request):
        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            section = serial.get(serial.validated_data)
        except ValueError:
            return Response({'detail': 'Course Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            request.user.removeSection(section)
        except ValueError:
            return Response({'detail': str(request.user) + " is not related to " + str(section)}, status=status.HTTP_400_BAD_REQUEST)
        
        reqSerial = serializer.subscriptionSerializer(models.subscription.objects.filter(user=request.user).order_by('id'), many=True)

        logger.debug("Section removed by: " + str(request.user))
        return Response(reqSerial.data, status=status.HTTP_200_OK)

    def flipActivation(self, request):
        serial = serializer.sectionSerializer(data=request.data)
        if serial.is_valid() is not True:
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

        try:
            section = serial.get(serial.validated_data)
        except ValueError:
            return Response({'detail': 'Course Does Not Exist'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            request.user.flipActivation(section)
        except ValueError:
            return Response({'detail': str(request.user) + " is not related to " + str(section)}, status=status.HTTP_400_BAD_REQUEST)

        reqSerial = serializer.subscriptionSerializer(models.subscription.objects.filter(user=request.user).order_by('id'), many=True)

        logger.debug("Section activation flipped by: " + str(request.user))
        return Response(reqSerial.data, status=status.HTTP_200_OK)

        
        