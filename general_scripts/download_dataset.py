import requests
import csv
import argparse

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
    parser = argparse.ArgumentParser(description="Download data from ThingSpeak")
    parser.add_argument("channel_id", type=int, help="ThingSpeak Channel ID")
    parser.add_argument("read_key", type=str, help="ThingSpeak Read API Key")
    args = parser.parse_args()
     
    download_thingspeak_data(args.channel_id, args.read_key)