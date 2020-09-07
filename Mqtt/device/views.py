from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.mixins import status
from rest_framework.views import APIView


class DeviceView(APIView):

    def put(self, request, *args, **kwargs):
        import paho.mqtt.client as paho
        import json
        from .models import Device

        try:
            device_id = kwargs.get('pk')
            print(device_id)
            print(self.request.data.get('status'))

            Device.objects.filter(id=device_id).update(status=self.request.data.get('status'))

            connecting = paho.Client()
            connecting.connect('localhost', 1883)
            print(connecting)

            message = {
                "status": True,
                "pi_id": "P-1"
            }
            string_message = json.dumps(message)
            connecting.loop_start()
            connecting.publish("P-1", string_message)

            return Response("Success", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        except Exception as e:
            return Response("Error", status=status.HTTP_400_BAD_REQUEST)
