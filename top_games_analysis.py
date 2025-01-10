from scipy.stats import chisquare

# Observed data
observed = [1, 9]
expected = [5, 5]

# Perform chi-square test
chi2_stat, p_value = chisquare(f_obs=observed, f_exp=expected)

print(f"Chi-square statistic: {chi2_stat}, P-value: {p_value}")
if p_value < 0.05:
    print("Reject null hypothesis: Observed and expected frequencies are significantly different.")
else:
    print("Fail to reject null hypothesis: Observed and expected frequencies are not significantly different.")