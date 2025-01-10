import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def preprocess_steam_data(steam_filepath):
    """Preprocess Steam data to add required columns."""
    steam_data = pd.read_json(steam_filepath)
    games = steam_data['response']['games']
    steam_df = pd.DataFrame(games)

    # Convert playtime from minutes to hours
    steam_df['playtime_forever_hours'] = steam_df['playtime_forever'] / 60

    # Convert rtime_last_played to datetime
    steam_df['last_played_date'] = pd.to_datetime(steam_df['rtime_last_played'], unit='s', errors='coerce')

    # Add year-month for grouping
    steam_df['year_month'] = steam_df['last_played_date'].dt.to_period('M').astype(str)

    return steam_df

def preprocess_youtube_data(youtube_filepath, game_name):
    """Filter YouTube data for the specified game."""
    youtube_data = pd.read_json(youtube_filepath, lines=False)

    # Ensure titles are lowercase for filtering
    youtube_data['title'] = youtube_data['title'].str.lower()

    # Filter videos related to the specified game
    youtube_data['related_game'] = youtube_data['title'].apply(
        lambda x: game_name.lower() if game_name.lower() in x else None
    )

    # Keep only videos related to the game
    related_videos = youtube_data[youtube_data['related_game'].notnull()].copy()

    # Extract year and month
    related_videos['time'] = pd.to_datetime(related_videos['time'], errors='coerce')
    related_videos['year_month'] = related_videos['time'].dt.to_period('M').astype(str)
    return related_videos

def merge_and_visualize_red_dead(steam_data, youtube_data):
    """Merge and visualize Red Dead Redemption data."""
    # Filter Steam data for Red Dead Redemption
    red_dead_steam = steam_data[steam_data['name'].str.contains('red dead redemption', case=False)]

    # Group Steam data by year-month
    red_dead_steam_grouped = red_dead_steam.groupby('year_month')['playtime_forever_hours'].sum().reset_index()
    red_dead_steam_grouped.rename(columns={'playtime_forever_hours': 'playtime_hours'}, inplace=True)

    # Group YouTube data by year-month
    red_dead_youtube_grouped = youtube_data.groupby('year_month').size().reset_index(name='video_count')

    # Merge the datasets
    merged_data = pd.merge(red_dead_steam_grouped, red_dead_youtube_grouped, on='year_month', how='outer').fillna(0)

    # Plot the merged data
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=merged_data, x='year_month', y='playtime_hours', label='Playtime (hours)', marker='o', color='orange')
    sns.lineplot(data=merged_data, x='year_month', y='video_count', label='YouTube Videos Watched', marker='o', color='blue')
    plt.title('Red Dead Redemption: Playtime vs YouTube Videos Watched')
    plt.xlabel('Year-Month')
    plt.ylabel('Count / Playtime (hours)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

    # Print merged data for debugging
    print("\nMerged Data:")
    print(merged_data)

def run_red_dead_analysis(youtube_filepath, steam_filepath):
    """Run analysis specifically for Red Dead Redemption."""
    # Preprocess Steam data
    steam_data = preprocess_steam_data(steam_filepath)

    # Preprocess YouTube data
    youtube_data = preprocess_youtube_data(youtube_filepath, "red dead redemption")

    # Merge and visualize data
    merge_and_visualize_red_dead(steam_data, youtube_data)

if __name__ == '__main__':
    run_red_dead_analysis('watch-history.json', 'steam_games_data.json')
