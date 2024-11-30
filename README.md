# Youtube-Steam-Analysis

## Table of Contents
- [About](#about)
- [Project Overview](#project-overview)
- [Approach](#approach)
- [Datasets](#datasets)
- [Methodology](#methodology)

## About
This repository contains a project for the course DSA210 at Sabanci University. It explores the relationship between my gaming activity on Steam and YouTube watch history. The primary goal is to investigate whether there is a significant correlation between the periods when a game is actively played and when related content is consumed on YouTube.

## Project Overview

  ### Objective 
  To analyze and understand how gaming activity influences YouTube viewing habits, specifically focusing on game-related content.

  ### Hypothesis
  The majority of YouTube videos about a specific game are watched during the time I am actively playing the game.
  
  ### Side Questions 
  - Do I start watching Youtube videos about a game before I buy it? Could mean I base my purchasing decisions because of videos.
  - Do I start watching Youtube videos about a game after I buy it? Could mean that I watch the videos because I bought the game.
    
  *What comes first? The chicken or the egg?*
  
## Approach
- Collect and process personal gaming data from Steam.
- Extract and analyze YouTube watch history.
- Integrate both datasets to identify patterns and correlations.

## Datasets
### 1. Steam Gaming Data
Source: Personal Steam account data obtained through the Steam Web API and data request tools.

Contents:
- Game titles and unique identifiers.
- Detailed play session data with start and end timestamps.
- Purchase dates and last played dates for each game.

### 2. YouTube Watch History
Source: Personal YouTube watch history exported via Google Takeout.

Contents:
- Titles and URLs of watched videos.
- Timestamps of when each video was viewed.
- Channel names and video metadata.

## Methodology
### 1. Data Collection:
- Export YouTube watch history and Steam gaming data.
- Ensure all data is in a compatible format (JSON) for analysis.

### 2. Data Preprocessing:
- Clean and filter the datasets to focus on relevant information.
- Convert timestamps to a consistent timezone (UTC) and datetime format.
- Categorize YouTube videos as game-related or non-game-related using keyword matching and metadata analysis.

### 3. Data Integration:
- Merge the Steam and YouTube datasets based on timestamps.
- Create a unified timeline to visualize and analyze concurrent activities.
  
### 4. Analysis:
- Perform temporal analysis to detect patterns in YouTube viewing relative to gaming sessions.
- Conducte statistical tests to assess the strength of correlations.
- Explore the data for any leading or lagging indicators between gaming and video watching.
  
### 5. Visualization:
- Develope graphs and charts to illustrate findings.
- Use time series plots and heatmaps to represent activity levels over time.
