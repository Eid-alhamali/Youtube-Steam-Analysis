import requests
import json

# Replace with your actual Steam API key and Steam ID
API_KEY = 'BA19025B55523072CBB35C5E2A0BA02A'
STEAM_ID = 76561199560696871

def get_owned_games(api_key, steam_id):
    url = 'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/'
    params = {
        'key': api_key,
        'steamid': steam_id,
        'include_appinfo': True,
        'include_played_free_games': True,
        'format': 'json'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Check for HTTP errors
    return response.json()

def save_to_json(data, filename='steam_games_data.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filename}")

def main():
    try:
        data = get_owned_games(API_KEY, STEAM_ID)
        save_to_json(data)
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == '__main__':
    main()
