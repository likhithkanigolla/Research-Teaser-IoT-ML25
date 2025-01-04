import requests
import csv

def download_thingspeak_data(channel_id, api_key, results=100):
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.csv?api_key={api_key}&results={results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open('dataset.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for line in response.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))
        print("Dataset downloaded successfully.")
    else:
        print(f"Failed to download dataset. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    CHANNEL_ID = '1654489'
    API_KEY = '6UMKKV6BOREY9EZM'
    download_thingspeak_data(CHANNEL_ID, API_KEY)