from statsmodels.stats.proportion import proportions_ztest

# Total playtime in minutes for 19 games
playtime = [0, 9000, 5024, 0, 4503, 6870, 7173, 1073, 160, 2948, 494, 1995, 624, 3538, 89, 12431, 1526, 1211, 2272]

# Calculate the number of games with zero playtime
zero_playtime_count = sum(1 for x in playtime if x == 0)
total_games = len(playtime)

# Perform a one-sample z-test for proportions
# Null hypothesis: proportion of zero-playtime games = 0
stat, p_value = proportions_ztest(count=zero_playtime_count, nobs=total_games, value=0, alternative='larger')

print(f"Zero Playtime Count: {zero_playtime_count}")
print(f"Total Games: {total_games}")
print(f"Z-statistic: {stat}, P-value: {p_value}")
if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant proportion of zero-playtime games.")
else:
    print("Fail to reject the null hypothesis: There is no significant proportion of zero-playtime games.")
