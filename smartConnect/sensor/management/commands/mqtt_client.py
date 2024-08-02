from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt
import json

class Command(BaseCommand):
    help = 'Runs the MQTT client to listen for sensor data.'

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe("sensor/temperature")

        def on_message(client, userdata, msg):
            print(msg.topic + " " + str(msg.payload))
            data = json.loads(msg.payload)
            temperature = data.get('temperature')
            if temperature is not None:
                # TemperatureData.objects.create(temperature=temperature)
                print(f"Saved temperature: {temperature}°C")

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("nadi-co.com", 1883, 60)  # Replace with your broker address

        client.loop_forever()
