from django.core.management.base import BaseCommand
import paho.mqtt.client as mqtt
import json
from api.models import Device
from sensor.models import SensorData
from django.contrib.auth.models import User


def save_data(device_key, user_key, data_type, data_name, value):
    """
    Save the sensor data to the database.
    """
    try:
        print(f"Saved data: {device_key} -  {data_name}  - {data_type} - {value}")
        
        # Get or create the sensor
        device = Device.objects.get(device_key=device_key)
        user = User.objects.get(user_key = user_key)
        if not device.owner == user:
            print('device and user does not match')
            return False
        # Save the sensor data based on the type
        SensorData.objects.create(
            device=device,
            data_type=data_type,
            data_name=data_name,
            **{f"{data_type}_value": value}
        )
        print(f"Saved data: {device_key} - {data_type} - {value}")
        
    except Device.DoesNotExist:
        print('Device with this key does not exist')
        return False
    
    except User.DoesNotExist:
        print('Device with this key does not exist')
        return False
    
    except Exception as e:
        print(f"Error saving data: {e}")
        return False
        
    
class Command(BaseCommand):
    help = 'Runs the MQTT client to listen for sensor data.'

    def handle(self, *args, **options):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe("sensor", qos=1)

        def on_message(client, userdata, msg):
            try:
                # Decode and parse the JSON message
                message = msg.payload.decode('utf-8')
                data = json.loads(message)
                
                # Check if the message matches the required format
                if all(key in data for key in ['device_key', 'user_key', 'data_type', 'data_name', 'data']):
                    print("Received valid message:", data)
                else:
                    print("Invalid message format:", data)
                result = save_data(
                    device_key=data['device_key'],
                    user_key=data['user_key'],
                    data_type=data['data_type'],
                    data_name=data['data_name'],
                    value=data['data'],
                )
            except json.JSONDecodeError:
                print("Failed to decode JSON:", msg.payload.decode('utf-8'))

        # Setup MQTT client
        client = mqtt.Client()

        # Set the callbacks
        client.on_connect = on_connect
        client.on_message = on_message

        # Connect to the MQTT broker
        client.connect("nadi-co.com", 1883, 60)

        # Start processing network traffic and dispatching callbacks
        client.loop_forever()
