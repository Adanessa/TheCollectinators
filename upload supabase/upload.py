import requests
import json

# Supabase configuration
supabase_url = 'https://oiqlwhfabpxcptnioczg.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9pcWx3aGZhYnB4Y3B0bmlvY3pnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTcxNjk2NjMwNCwiZXhwIjoyMDMyNTQyMzA0fQ.WIijwR4yrgj38xPRG5tFq5iFmwM8PeOkjItKTPX13k4'  # Use the service role key here
supabase_table_system = 'system table'
supabase_table_planet = 'planet table'
supabase_table_data = 'data table'


# Load JSON data from a file
with open('starfield_data_updated.json') as f:
    data = json.load(f)

# Function to insert data into Supabase
def insert_into_supabase(url, headers, payload):
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    print(f"Request to {url} with payload {payload}")
    print(f"Response status: {response.status_code}")
    print(f"Response text: {response.text}")

    if response.status_code == 201:
        return response.json().get('id')  # Assuming the response contains the ID
    else:
        print(f"Failed to insert data: {payload.get('name') or payload.get('planet_id')}")
        print(f"Response text: {response.text}")
        response.raise_for_status()

def upload_data():
    headers = {
        "Content-Type": "application/json",
        "apikey": supabase_key,
        "Authorization": f"Bearer {supabase_key}"
    }

    # Insert systems
    for system_name, planets in data.items():
        system_payload = {
            "system_name": system_name
        }
        system_url = f"{supabase_url}/rest/v1/{supabase_table_system}"
        try:
            system_id = insert_into_supabase(system_url, headers, system_payload)
            print(f"Successfully inserted system: {system_name} with system_id: {system_id}")
        except Exception as e:
            print(f"Failed to insert system: {system_name}")
            print(f"Error: {e}")
            continue

    # Insert planets and their data
    for system_name, planets in data.items():
        system_response = requests.get(f"{supabase_url}/rest/v1/{supabase_table_system}?system_name=eq.{system_name}", headers=headers)
        print(f"System response status: {system_response.status_code}")
        print(f"System response text: {system_response.text}")
        
        if system_response.status_code != 200 or not system_response.json():
            print(f"Failed to retrieve system_id for system: {system_name}")
            continue

        system_id = system_response.json()[0]['system_id']
        for planet_name, planet_data in planets.items():
            planet_payload = {
                "name": planet_name,
                "system_id": int(system_id)
            }
            print("Planet payload:", planet_payload)
            planet_url = f"{supabase_url}/rest/v1/{supabase_table_planet}"
            try:
                planet_id = insert_into_supabase(planet_url, headers, planet_payload)
                print(f"Successfully inserted planet: {planet_name} with planet_id: {planet_id}")

                data_payload = {
                    "planet_id": planet_id,
                    **planet_data
                }
                data_url = f"{supabase_url}/rest/v1/{supabase_table_data}"
                insert_into_supabase(data_url, headers, data_payload)
                print(f"Successfully inserted data for planet: {planet_name}")
            except Exception as e:
                print(f"Failed to insert planet: {planet_name}")
                print(f"Error: {e}")
                continue

# Run the upload function
upload_data()
