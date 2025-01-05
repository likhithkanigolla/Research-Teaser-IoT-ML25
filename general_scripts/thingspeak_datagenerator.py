import requests
import random
import time

# ThingSpeak API configuration
THINGSPEAK_API_KEY = 'HF9EZ1SU90JTPI92'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def generate_random_data():
    temperature = round(random.uniform(25.0, 28.0), 1)
    humidity = round(random.uniform(48.0, 50.0), 1)
    pm25 = round(random.uniform(15.0, 40.0), 2)
    pm10 = round(random.uniform(pm25 + 1.0, pm25 + 10.0), 2)
    return temperature, humidity, pm25, pm10

def post_to_thingspeak(temperature, humidity, pm25, pm10):
    payload = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': temperature,
        'field2': humidity,
        'field3': pm25,
        'field4': pm10
    }
    response = requests.post(THINGSPEAK_URL, data=payload)
    if response.status_code == 200:
        print('Data posted successfully')
    else:
        print('Failed to post data')

if __name__ == '__main__':
    while True:
        temperature, humidity, pm25, pm10 = generate_random_data()
        post_to_thingspeak(temperature, humidity, pm25, pm10)
        time.sleep(1)