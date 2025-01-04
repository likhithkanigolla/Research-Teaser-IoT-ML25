import requests
import psycopg2
import time
import argparse

# python general_scripts/ingest_to_postgres.py <channel_id> <read_key> [--continuous]

def create_table(channel_name, fields):
    conn = psycopg2.connect(
        dbname="ml25",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    columns = ", ".join([f"field{i+1} TEXT" for i in range(fields)])
    create_table_query = f"CREATE TABLE IF NOT EXISTS {channel_name} (id SERIAL PRIMARY KEY, created_at TIMESTAMP, entry_id INT, {columns});"
    
    cur.execute(create_table_query)
    conn.commit()
    cur.close()
    conn.close()

def fetch_data(channel_id, read_key):
    url = f"https://api.thingspeak.com/channels/{channel_id}/feeds.json?api_key={read_key}"
    response = requests.get(url)
    data = response.json()
    return data

def insert_data(channel_name, data):
    conn = psycopg2.connect(
        dbname="ml25",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    
    for feed in data['feeds']:
        columns = ", ".join(feed.keys())
        values = ", ".join([f"'{v}'" for v in feed.values()])
        insert_query = f"INSERT INTO {channel_name} ({columns}) VALUES ({values});"
        cur.execute(insert_query)
    
    conn.commit()
    cur.close()
    conn.close()

def main(channel_id, read_key, continuous):
    data = fetch_data(channel_id, read_key)
    fields = len(data['channel']) - 2  # Excluding 'id' and 'name'
    channel_name = data['channel']['name'].replace(" ", "_").replace("-", "_").lower()
    
    create_table(channel_name, fields)
    
    while True:
        data = fetch_data(channel_id, read_key)
        insert_data(channel_name, data)
        
        if not continuous:
            break
        
        time.sleep(60)  # Wait for 1 minute before fetching data again

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest data from ThingSpeak to PostgreSQL")
    parser.add_argument("channel_id", type=int, help="ThingSpeak Channel ID")
    parser.add_argument("read_key", type=str, help="ThingSpeak Read API Key")
    parser.add_argument("--continuous", action="store_true", help="Continuously read data")
    
    args = parser.parse_args()
    main(args.channel_id, args.read_key, args.continuous)