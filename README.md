# YouTube-Steam-Analysis

This repository contains a project for the course DSA210 at Sabanci University. It explores the relationship between my gaming activity on Steam and YouTube watch history. The primary goal is to investigate whether there is a significant correlation between the periods when a game is actively played and when related content is consumed on YouTube.

## Table of Contents
- [Motivation](#motivation)
- [Datasets](#datasets)
- [Data Analysis](#data-analysis)
- [Findings](#findings)
- [Future Work](#fuure-work)

## Motivation

The primary motivation for this project is to gain a deeper understanding of my gaming habits on Steam and how they correlate with my YouTube activity. By analyzing this relationship, I aim to uncover patterns in how my playtime influences my content consumption on YouTube and vice versa. This project also serves as a personal exploration to reflect on how gaming impacts my broader media engagement and to identify potential trends in my entertainment preferences.

## Datasets

### YouTube Activity Data
The YouTube history data was downloaded using Google Takeout, which allows users to export their personal data from Google products. The dataset includes information such as video titles, channels, timestamps, and associated products (e.g., YouTube Watch History). This data was processed to extract monthly counts of videos related to specific games for comparison with Steam playtime data.

### Steam Gaming Data
Gaming playtime data was collected from the Steam Web API using an API token key. This dataset provides detailed information about each game, including the total playtime, platform-specific playtime, and, where available, monthly playtime distribution. During the collection process, some improperly fetched or incomplete entries were identified and handled to ensure the accuracy and integrity of the analysis.

By integrating these two datasets, I created a structured dataset to facilitate statistical analysis and explore the relationship between playtime and YouTube activity.

## Data Analysis

The analysis involved various stages and utilized several technologies and techniques to process, analyze, and visualize the data.

### 1. Data Collection
- **APIs**: Used the Steam Web API to fetch gaming data and automate the retrieval process.
- **File Exports**: Collected YouTube activity data using Google Takeout.

### 2. Data Preprocessing
- **Data Cleaning**: Removed inconsistencies and handled improperly fetched entries.
- **Data Aggregation**: Grouped data into monthly intervals for easier comparison.
- **Data Transformation**: Converted time units, parsed timestamps, and aligned datasets for analysis.

### 3. Data Analysis Techniques
- **Exploratory Data Analysis (EDA)**:
  - Aggregated data for summarization and trend analysis.
  - Used descriptive statistics to identify patterns in playtime and YouTube activity.
- **Statistical Testing**:
  - Performed hypothesis testing to determine dependencies between datasets.
  - Applied correlation analysis and contingency testing to measure relationships.

### 4. Visualization
- **Visualization Libraries**: Used `matplotlib` and `seaborn` to create histograms, bar charts, and line plots for data trends and comparisons.
- **Trend Analysis**: Analyzed monthly activity patterns for insights into seasonal behaviors.

### 5. Tools and Technologies
- **Python Libraries**:
  - `pandas` for data manipulation and preprocessing.
  - `matplotlib` and `seaborn` for visualizations.
  - `scipy` for performing statistical tests.
- **Data Formats**:
  - `JSON` for structured data handling and processing.
  - `CSV` for exporting and sharing preprocessed datasets.

## Findings

### Hypothesis 1: Gaming Preference
**Null Hypothesis (H₀):** I play online games and story mode games equally.  
**Alternative Hypothesis (H₁):** I play story mode games more than online games.
![image](https://github.com/user-attachments/assets/0e20f209-493f-4861-a3ac-0870ee5e2131)


#### Analysis and Result
Using a Chi-Square test, the observed and expected data were as follows:
- **Observed Data:** Online Games = 1, Story Mode Games = 9  
- **Expected Data:** Online Games = 5, Story Mode Games = 5  
The test yielded the following result:
- **Chi-Square Statistic:** 6.4  
- **P-value:** 0.0114  

Since the P-value is less than 0.05, we reject the null hypothesis. This result supports the alternative hypothesis: I play story mode games more than online games.

---

### Hypothesis 2: Seasonal Playtime
**Null Hypothesis (H₀):** My playing time is uniformly distributed throughout the year.  
**Alternative Hypothesis (H₁):** My playing time is higher during January, February, July, and August (holidays).
![image](https://github.com/user-attachments/assets/30911671-08a9-4690-b440-c9f558baf836)


#### Analysis and Result
Using an independent t-test:
- **Holiday Playtime:** [140, 120, 40, 140]  
- **Non-Holiday Playtime:** [100, 80, 60, 20, 60, 80, 40, 10]  
The test yielded:
- **T-statistic:** 2.381  
- **P-value:** 0.0193  

Since the P-value is less than 0.05, we reject the null hypothesis. This result supports the alternative hypothesis: My playing time is higher during holidays.

---

### Hypothesis 3: Gaming Purchases
**Null Hypothesis (H₀):** I play all the games I buy.  
**Alternative Hypothesis (H₁):** I do not play all the games I buy.
![image](https://github.com/user-attachments/assets/dcb3187d-3b03-441f-be21-047774d34b02)


#### Analysis and Result
Using a one-sample z-test for proportions:
- **Total Games:** 19  
- **Games with Zero Playtime:** 2  
The test yielded:
- **Z-Statistic:** 1.495  
- **P-value:** 0.0674  

Since the P-value is greater than 0.05, we fail to reject the null hypothesis. This indicates that the proportion of games with zero playtime is not significantly large, meaning I generally play most of the games I buy.

---

### Hypothesis 4: Playtime vs. YouTube Activity
**Null Hypothesis (H₀):** YouTube activity is independent of playtime.  
**Alternative Hypothesis (H₁):** YouTube activity depends on playtime.

Graphs for each game:

**Cyberpunk 2077**
![image](https://github.com/user-attachments/assets/3faf0fbc-c981-48a1-a4db-1d03cd9044f3)

**Dark Souls III**
![image](https://github.com/user-attachments/assets/69ff2511-d508-4e0e-89b8-fd0e08d4272e)

**EA SPORTS FC™ 24** 
![image](https://github.com/user-attachments/assets/6ea5223f-cf13-46cb-bb2b-7a15b90b916a)

**Red Dead Redemption 2**
![image](https://github.com/user-attachments/assets/630e032c-44a8-46d2-87db-43e553a82b74)

**The Witcher 3** 
![image](https://github.com/user-attachments/assets/de424103-4cd4-463f-ad9e-0ae16edc4ac4)



#### Analysis and Results for Top 5 Games
| Game                     | P-value | Conclusion                                |
|--------------------------|---------|------------------------------------------|
| **Cyberpunk 2077**       | 0.171   | Fail to reject null hypothesis           |
| **Dark Souls III**       | 0.0153  | Reject null hypothesis                   |
| **EA SPORTS FC™ 24**     | 1.0     | Fail to reject null hypothesis           |
| **Red Dead Redemption 2**| 1.0     | Fail to reject null hypothesis           |
| **The Witcher 3**        | 1.0     | Fail to reject null hypothesis           |

#### Overall Deduction
In four out of five cases, YouTube activity was found to be independent of playtime, suggesting that I watch videos regardless of whether I am actively playing the game. Only **Dark Souls III** showed a significant dependence, indicating a closer link between gameplay and video consumption for that title.

## Limitations and Future Work

### Limitations
While this project provides valuable insights into the relationship between my gaming habits and YouTube activity, it is not without its limitations:
1. **Sample Size and Scope**: 
   - The analysis is limited to my personal data, which might not be representative of broader trends. 
   - The scope is confined to a specific period and focuses only on my top-played games, potentially overlooking trends in less-played games.

2. **Data Accuracy and Completeness**:
   - The YouTube data relies on accurate tagging of video content, which might not always reflect its relevance to specific games.
   - Some Steam data entries required manual cleaning due to improper fetching, which may have introduced minor inaccuracies.

3. **Simplified Categorization**:
   - The statistical tests grouped data into broad categories (e.g., playtime bins, YouTube activity bins), which might have obscured subtler relationships.
   - The dependency analysis assumes linear or categorical relationships, which may not capture more complex interactions.

4. **Platform and Context Limitation**:
   - The analysis only considers Steam gaming activity and YouTube videos, excluding other platforms or types of content consumption, such as Twitch streams or Reddit discussions.

5. **Seasonal Variability**:
   - External factors like academic workload, social commitments, or game release schedules were not accounted for, which could influence the observed patterns.

---

### Future Work
To build upon the insights gained in this project, the following improvements and extensions are planned:
1. **Broader Dataset**:
   - Include data from other platforms, such as PlayStation, Xbox, or Nintendo Switch, to provide a more comprehensive view of my gaming habits.
   - Incorporate data from other media consumption sources like Twitch or Spotify for a more holistic analysis.

2. **Advanced Analytics**:
   - Use machine learning models, such as clustering or regression, to predict gaming habits based on YouTube activity and vice versa.
   - Perform time-series analysis to detect seasonal trends and explore lagging effects (e.g., if gaming activity influences video consumption with a delay).

3. **Granular Analysis**:
   - Categorize YouTube content more precisely, distinguishing between gameplay guides, walkthroughs, lore videos, and reviews.
   - Analyze specific genres or gameplay styles to understand how they influence my media consumption habits.

4. **Automation and Scalability**:
   - Develop scripts to automate data retrieval, cleaning, and preprocessing for continuous analysis.
   - Extend the project to include contributions from others, enabling comparisons across users and gaming habits.

5. **Interactive Dashboards**:
   - Create an interactive dashboard for real-time visualization and exploration of trends, allowing dynamic filtering by game, month, or activity type.

6. **Behavioral Insights**:
   - Investigate the psychological and behavioral drivers behind the observed patterns, such as motivation for gaming during holidays or preferences for certain types of content.
   - Analyze how gaming habits impact productivity, mood, or social interactions.

This project lays the groundwork for a deeper understanding of my gaming and media consumption habits, and these future directions will help uncover additional patterns and insights while addressing the current limitations.

