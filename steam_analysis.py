import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import json

def load_steam_data(filepath):
    """Load and preprocess Steam data from JSON."""
    import json

    # Load JSON file
    with open(filepath, 'r') as f:
        steam_data = json.load(f)
    
    # Extract the games data
    games = steam_data['response']['games']
    df = pd.DataFrame(games)

    # Debug: Check initial columns
    print("Initial Steam Data Columns:", df.columns)

    # Ensure the playtime_forever column exists
    if 'playtime_forever' not in df.columns:
        raise KeyError("The column 'playtime_forever' is missing in the Steam data.")

    # Convert playtime from minutes to hours
    df['playtime_forever_hours'] = df['playtime_forever'] / 60

    # Debug: Check if playtime_forever_hours is created
    print("Columns After Adding playtime_forever_hours:", df.columns)
    print(df[['name', 'playtime_forever', 'playtime_forever_hours']].head())

    # Convert rtime_last_played to datetime (skip rows where it's 0)
    df['last_played_date'] = pd.to_datetime(df['rtime_last_played'], unit='s', errors='coerce')
    df = df[df['rtime_last_played'] > 0]  # Drop rows with no last play info

    # Debug: Check rows after dropping invalid rtime_last_played
    print("Data After Dropping Invalid rtime_last_played:")
    print(df[['name', 'rtime_last_played', 'last_played_date']].head())

    # Add year and month for grouping
    df['year_month'] = df['last_played_date'].dt.to_period('M').astype(str)

    # Debug: Confirm year_month column creation
    print("Columns After Adding year_month:", df.columns)
    print(df[['name', 'year_month']].head())

    return df



def analyze_basic_stats(df):
    """Display basic statistics about the Steam library."""
    print("Total games owned:", len(df))
    print("Total playtime (hours):", df['playtime_forever_hours'].sum())
    print("Top 5 most-played games:")
    print(df[['name', 'playtime_forever_hours']].sort_values(by='playtime_forever_hours', ascending=False).head())

    # Games with zero playtime
    zero_playtime = df[df['playtime_forever_hours'] == 0]
    print(f"Games with zero playtime: {len(zero_playtime)}")
    print(zero_playtime['name'].to_list())

    # Most recently played games
    recently_played = df[df['last_played_date'].notnull()]
    recently_played = recently_played.sort_values(by='rtime_last_played', ascending=False).head(5)
    print("Most recently played games:")
    print(recently_played[['name', 'last_played_date']])

def visualize_playtime_distribution(df):
    """Visualize the distribution of playtime."""
    plt.figure(figsize=(8, 6))
    sns.histplot(df['playtime_forever_hours'], bins=15, kde=True, color='steelblue')
    plt.title('Distribution of Total Playtime Across Games')
    plt.xlabel('Playtime (hours)')
    plt.ylabel('Frequency')
    plt.ylim(0, 5)  # Set the y-axis limits
    plt.show()


def visualize_top_games(df):
    """Visualize the top 10 most-played games with fully visible names."""
    # Safely decode game names to fix encoding issues
    df['name'] = df['name'].apply(
        lambda x: x.encode('utf-8', 'replace').decode('utf-8') if isinstance(x, str) else x
    )
    
    top_10_games = df.sort_values(by='playtime_forever_hours', ascending=False).head(10)
    plt.figure(figsize=(12, 8))  # Increased figure size for better visibility
    sns.barplot(y=top_10_games['name'], x=top_10_games['playtime_forever_hours'], color='steelblue')
    plt.title('Top 10 Most-Played Games')
    plt.xlabel('Playtime (hours)')
    plt.ylabel('Game Title')
    plt.xticks(fontsize=10)  # Adjust font size for better readability
    plt.yticks(fontsize=12)  # Adjust font size for better readability
    plt.tight_layout()  # Automatically adjust layout to prevent label clipping
    plt.show()



def visualize_playtime_trends(df):
    """Analyze and visualize playtime trends over time using monthly playtime data."""
    # Extract monthly playtime data from all games
    monthly_playtime = []
    for _, row in df.iterrows():
        if "monthly_playtime_2024" in row and isinstance(row["monthly_playtime_2024"], dict):
            for month, playtime in row["monthly_playtime_2024"].items():
                monthly_playtime.append({
                    "month": month,
                    "playtime_hours": playtime / 60  # Convert minutes to hours
                })
    
    # Create a DataFrame for the monthly playtime data
    monthly_df = pd.DataFrame(monthly_playtime)
    
    # Map month names to a standard order
    month_order = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    monthly_df["month"] = pd.Categorical(monthly_df["month"], categories=month_order, ordered=True)
    
    # Group by month and sum the playtime hours
    monthly_summary = monthly_df.groupby("month")["playtime_hours"].sum().reset_index()
    
    # Plot the updated playtime trends
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=monthly_summary, x="month", y="playtime_hours", marker="o", color="steelblue")
    plt.title("Total Monthly Playtime Trend (2024)")
    plt.xlabel("Month")
    plt.ylabel("Playtime (hours)")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


def run_analysis(filepath='steam_games_data.json'):
    """Run the full analysis."""
    df = load_steam_data(filepath)
    analyze_basic_stats(df)
    visualize_playtime_distribution(df)
    visualize_top_games(df)
    visualize_playtime_trends(df)

if __name__ == '__main__':
    run_analysis()
