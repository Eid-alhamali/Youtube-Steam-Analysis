from scipy.stats import chi2_contingency
import numpy as np

 # YouTube video counts for cyberpunk
youtube_activity = [40, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
playtime = [30, 60, 40, 5, 0, 0, 2, 3, 2, 2, 5, 40]

# Combine bins to avoid empty categories
playtime_bins = np.digitize(playtime, bins=[0, 20])  # 0-20: Low, >20: High
youtube_bins = np.digitize(youtube_activity, bins=[0, 1])  # 0: No activity, >1: Activity

# Create contingency table
contingency_table = np.zeros((2, 2))  # 2 bins for playtime, 2 bins for YouTube activity
for p_bin, y_bin in zip(playtime_bins, youtube_bins):
    contingency_table[p_bin - 1, y_bin - 1] += 1

# Perform Chi-Square Test
chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

# Output results
print("Contingency Table:")
print(contingency_table)
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")
print(f"Degrees of Freedom: {dof}")
print("Expected Frequencies:")
print(expected)

# Interpretation
if p_value < 0.05:
    print("Reject the null hypothesis: YouTube activity depends on playtime.")
else:
    print("Fail to reject the null hypothesis: YouTube activity is independent of playtime.")
