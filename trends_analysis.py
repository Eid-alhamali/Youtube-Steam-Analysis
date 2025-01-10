from scipy.stats import ttest_ind

# Holiday and non-holiday playtimes
holiday_playtime = [140, 120, 40, 140]
non_holiday_playtime = [100, 80, 60, 20, 60, 80, 40, 10]

# Perform independent t-test
t_stat, p_value = ttest_ind(holiday_playtime, non_holiday_playtime, alternative='greater')

print(f"T-statistic: {t_stat}, P-value: {p_value}")

if p_value < 0.05:
    print("Reject null hypothesis: Holiday and non-holiday playtimes are significantly different.")
else:
    print("Fail to reject null hypothesis: Holiday and non-holiday playtimes are not significantly different.")
