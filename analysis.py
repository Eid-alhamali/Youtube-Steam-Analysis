import pandas as pd
import matplotlib.pyplot as plt
import json

def load_steam_data(filepath):
    """Load Steam data from a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        steam_data = json.load(f)
    return steam_data["response"]["games"]

def preprocess_steam_data(games, game_name):
    """Preprocess Steam data for a specific game."""
    processed_data = []
    for game in games:
        if game["name"] == game_name:
            monthly_data = game.get("monthly_playtime_2024", {})
            for month, playtime in monthly_data.items():
                processed_data.append({
                    "month": month,
                    "playtime_hours": playtime / 60  # Convert minutes to hours
                })
    return pd.DataFrame(processed_data)

def preprocess_youtube_data(youtube_file, title_filters):
    """Filter YouTube data for videos related to the given title filters."""
    with open(youtube_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)

    youtube_data = pd.json_normalize(raw_data)
    youtube_data["time"] = pd.to_datetime(youtube_data["time"], errors="coerce")
    youtube_data["month"] = youtube_data["time"].dt.strftime("%B")
    youtube_data["related"] = youtube_data["title"].apply(
        lambda x: any(filter.lower() in x.lower() for filter in title_filters) if isinstance(x, str) else False
    )
    youtube_data = youtube_data[youtube_data["related"]]
    youtube_summary = youtube_data.groupby("month").size().reset_index(name="video_count")
    return youtube_summary

def plot_comparison(game_name, steam_df, youtube_df):
    """Plot the comparison graph for a specific game."""
    # Merge data
    merged_data = pd.merge(
        steam_df,
        youtube_df,
        on="month",
        how="outer"
    ).fillna(0)

    # Convert month to categorical for sorting
    months_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    merged_data["month"] = pd.Categorical(merged_data["month"], categories=months_order, ordered=True)
    merged_data.sort_values(by=["month"], inplace=True)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(merged_data["month"], merged_data["playtime_hours"], width=0.4, label="Playtime (hours)", align="center")
    plt.bar(merged_data["month"], merged_data["video_count"], width=0.4, label="YouTube Videos", align="edge")
    plt.title(f"Comparison of Playtime and YouTube Activity for {game_name} (2024)")
    plt.xlabel("Month")
    plt.ylabel("Count / Hours")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()  # Blocking display to view each graph manually

def run_analysis(steam_file, youtube_file):
    """Run the analysis for each game."""
    # Define games and title filters
    games_and_filters = {
        "Red Dead Redemption 2": ["Red Dead Redemption 2", "Red Dead Redemption"],
        "EA SPORTS FC™ 24": ["EA SPORTS FC 24", "FC 24", "Fifa 24"],
        "Cyberpunk 2077": ["Cyberpunk 2077", "Cyberpunk"],
        "The Witcher 3: Wild Hunt": ["The Witcher 3: Wild Hunt", "The Witcher 3", "Witcher 3"],
        "DARK SOULS™ III": ["DARK SOULS III", "DARK SOUL 3"]
    }

    # Load Steam data
    steam_games = load_steam_data(steam_file)

    # Process and plot for each game
    for game_name, title_filters in games_and_filters.items():
        steam_df = preprocess_steam_data(steam_games, game_name)
        youtube_df = preprocess_youtube_data(youtube_file, title_filters)
        plot_comparison(game_name, steam_df, youtube_df)

# Specify the file paths
steam_file = "steam_games_data.json"
youtube_file = "watch-history.json"

if __name__ == "__main__":
    run_analysis(steam_file, youtube_file)
