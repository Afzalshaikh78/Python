# ============================================================
# STATISTICS & PROBABILITY — COMPLETE PYTHON RECAP
# ============================================================

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# 1. MEAN, MEDIAN, VARIANCE, STD DEVIATION
# ============================================================

scores = np.array([72, 85, 90, 88, 76, 95, 60, 88, 74, 91])

mean     = np.mean(scores)        # 81.9  — average
median   = np.median(scores)      # 86.5  — middle value (robust to outliers)
variance = np.var(scores)         # 116.9 — average squared distance from mean
std      = np.std(scores)         # 10.81 — square root of variance (same unit as data)

print(f"Mean:     {mean:.2f}")
print(f"Median:   {median:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Std dev:  {std:.2f}")

# When to use mean vs median:
# Mean  → data has no extreme outliers (exam scores, heights)
# Median → data has outliers or is skewed (salaries, house prices)

salaries = np.array([40000, 45000, 42000, 48000, 500000])  # one CEO ruins the mean
print(f"\nSalary mean:   {np.mean(salaries):,.0f}")   # 135,000 — misleading
print(f"Salary median: {np.median(salaries):,.0f}")  #  45,000 — accurate picture

# With pandas (real workflow — you'll use this more than numpy directly)
df = pd.DataFrame({'scores': scores})
print(df['scores'].describe())   # count, mean, std, min, 25%, 50%, 75%, max in one shot


# ============================================================
# 2. DISTRIBUTIONS
# ============================================================

from scipy.stats import norm, binom, poisson

# --- Normal distribution ---
mu, sigma = 170, 10   # mean height 170cm, std 10cm

# Probability that a person is between 160 and 180cm
prob_160_180 = norm.cdf(180, mu, sigma) - norm.cdf(160, mu, sigma)
print(f"\nP(160 < height < 180): {prob_160_180:.4f}")  # ~0.6827 (68% rule)

# What height is the top 5% threshold?
top5_threshold = norm.ppf(0.95, mu, sigma)
print(f"Top 5% threshold: {top5_threshold:.1f}cm")  # ~186.4cm

# Generate samples
height_samples = np.random.normal(mu, sigma, 1000)


# --- Binomial distribution ---
n, p = 20, 0.25   # 20 MCQ questions, 0.25 chance of guessing correctly

# P(exactly 8 correct by guessing)
print(f"\nP(exactly 8 correct): {binom.pmf(8, n, p):.4f}")

# P(passing = getting 10 or more correct)
print(f"P(pass by guessing):  {1 - binom.cdf(9, n, p):.6f}")  # very small

print(f"Expected correct: {n*p:.1f}")   # 5.0


# --- Poisson distribution ---
lam = 3   # avg 3 support tickets per hour

# P(exactly 5 tickets in an hour)
print(f"\nP(5 tickets): {poisson.pmf(5, lam):.4f}")

# P(more than 6 tickets — server stress)
print(f"P(>6 tickets): {1 - poisson.cdf(6, lam):.4f}")

# Key property: mean == variance for Poisson
samples = np.random.poisson(lam, 10000)
print(f"Sample mean: {samples.mean():.2f}, Sample var: {samples.var():.2f}")  # both ~3


# ============================================================
# 3. BAYES' THEOREM & CONDITIONAL PROBABILITY
# ============================================================

# Spam filter example
# P(spam) = 0.30, P("free"|spam) = 0.90, P("free"|not_spam) = 0.10

def bayes(prior_A, likelihood_B_given_A, likelihood_B_given_not_A):
    p_not_A = 1 - prior_A
    p_B     = likelihood_B_given_A * prior_A + likelihood_B_given_not_A * p_not_A
    return (likelihood_B_given_A * prior_A) / p_B

p_spam_given_free = bayes(
    prior_A=0.30,
    likelihood_B_given_A=0.90,
    likelihood_B_given_not_A=0.10
)
print(f"\nP(spam | 'free'): {p_spam_given_free:.3f}")   # 0.794

# Naive Bayes in sklearn (the real ML use case)
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

emails = [
    "win free money now",
    "meeting at 3pm tomorrow",
    "free prize click here to claim",
    "project deadline is friday",
    "you have won a free gift",
    "quarterly review next week"
]
labels = [1, 0, 1, 0, 1, 0]   # 1 = spam, 0 = not spam

vec   = CountVectorizer()
X     = vec.fit_transform(emails)
model = MultinomialNB()
model.fit(X, labels)

test  = vec.transform(["free gift winner click now"])
print(f"Prediction:    {model.predict(test)[0]}")           # 1 (spam)
print(f"Probabilities: {model.predict_proba(test)[0]}")     # [P(ham), P(spam)]


# ============================================================
# 4. HYPOTHESIS TESTING, P-VALUES, T-TESTS
# ============================================================

np.random.seed(42)

# Scenario: did Model B actually improve over Model A?
model_a_scores = np.random.normal(loc=80, scale=5, size=50)
model_b_scores = np.random.normal(loc=83, scale=5, size=50)

# Two-sample independent t-test
t_stat, p_value = stats.ttest_ind(model_a_scores, model_b_scores)

print(f"\nModel A mean: {model_a_scores.mean():.2f}")
print(f"Model B mean: {model_b_scores.mean():.2f}")
print(f"T-statistic:  {t_stat:.3f}")
print(f"P-value:      {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject H₀ — Model B is significantly better")
else:
    print("Fail to reject H₀ — difference could be random chance")

# One-sample t-test — is our model significantly better than 75% baseline?
t2, p2 = stats.ttest_1samp(model_b_scores, popmean=75)
print(f"\nVs 75% baseline: t={t2:.3f}, p={p2:.6f}")   # very significant

# Paired t-test — same test samples evaluated by both models
t3, p3 = stats.ttest_rel(model_a_scores, model_b_scores)
print(f"Paired t-test:   t={t3:.3f}, p={p3:.4f}")


# ============================================================
# 5. CORRELATION VS CAUSATION
# ============================================================

# Correlation measures LINEAR relationship strength: -1 to +1
# +1 = perfect positive, 0 = no linear relationship, -1 = perfect negative

np.random.seed(0)
study_hours = np.random.uniform(1, 10, 50)
exam_scores = 50 + 5 * study_hours + np.random.normal(0, 5, 50)   # real relationship
ice_cream    = np.random.uniform(1, 10, 50)                        # unrelated variable

# Pearson correlation (linear)
r_study, p_study = stats.pearsonr(study_hours, exam_scores)
r_ice,   p_ice   = stats.pearsonr(ice_cream, exam_scores)

print(f"\nStudy hours vs score: r={r_study:.3f}, p={p_study:.4f}")  # strong, significant
print(f"Ice cream vs score:   r={r_ice:.3f},  p={p_ice:.4f}")       # weak, not significant

# Spearman correlation (works on non-linear / ranked data)
r_spearman, p_spearman = stats.spearmanr(study_hours, exam_scores)
print(f"Spearman r: {r_spearman:.3f}")

# Correlation matrix on a DataFrame (most common real workflow)
df = pd.DataFrame({
    'study_hours': study_hours,
    'exam_scores': exam_scores,
    'ice_cream':   ice_cream
})
print("\nCorrelation matrix:")
print(df.corr().round(3))

# Visualise (heatmap — standard in EDA before ML)
# sns.heatmap(df.corr(), annot=True, cmap='coolwarm', center=0)
# plt.show()

# ---- Correlation ≠ Causation — classic trap ----
# High correlation between:
#   drowning deaths vs Nicolas Cage movies per year    → both rise in summer
#   shoe size vs reading ability in children           → both caused by age
#   ice cream sales vs crime rate                      → both caused by hot weather
# These are CONFOUNDING VARIABLES — a hidden third variable drives both.
#
# In ML, this matters when selecting features:
#   A feature correlated with the target isn't necessarily causal.
#   Removing a confounding variable can destroy model performance.
#   Always ask: "Is there a hidden third variable explaining this?"

# Detecting confounders: partial correlation (control for a third variable)
# If correlation between A and B disappears when you control for C → C was the confounder
from scipy.stats import pearsonr

# Example: temperature drives both ice cream AND crime
temperature  = np.random.uniform(15, 40, 100)
ice_cream2   = 2 * temperature + np.random.normal(0, 3, 100)
crime_rate   = 1.5 * temperature + np.random.normal(0, 4, 100)

r_raw, _  = pearsonr(ice_cream2, crime_rate)

# Partial out temperature (residuals after regressing on temperature)
from numpy.polynomial import polynomial as P
res_ice   = ice_cream2  - np.polyval(np.polyfit(temperature, ice_cream2,  1), temperature)
res_crime = crime_rate  - np.polyval(np.polyfit(temperature, crime_rate,  1), temperature)
r_partial, _ = pearsonr(res_ice, res_crime)

print(f"\nIce cream vs crime (raw):     r={r_raw:.3f}")      # high — looks causal!
print(f"Ice cream vs crime (partial): r={r_partial:.3f}")   # near 0 — temperature was the confounder


# ============================================================
# QUICK REFERENCE CHEATSHEET
# ============================================================
#
# DESCRIPTIVE STATS
#   np.mean(x), np.median(x), np.var(x), np.std(x)
#   df.describe()                    ← all stats at once
#
# DISTRIBUTIONS
#   norm.pdf/cdf/ppf(x, mu, sigma)   ← Normal
#   binom.pmf/cdf(k, n, p)           ← Binomial
#   poisson.pmf/cdf(k, lam)          ← Poisson
#   np.random.normal/binomial/poisson ← generate samples
#
# HYPOTHESIS TESTING
#   stats.ttest_ind(a, b)            ← two independent groups
#   stats.ttest_1samp(a, mu)         ← one group vs known value
#   stats.ttest_rel(a, b)            ← paired (same subjects)
#   → check p_value < 0.05 to reject H₀
#
# CORRELATION
#   stats.pearsonr(x, y)             ← linear, continuous data
#   stats.spearmanr(x, y)            ← ranked / non-linear data
#   df.corr()                        ← full correlation matrix
#
# NAIVE BAYES (ML)
#   MultinomialNB()                  ← text / count data
#   GaussianNB()                     ← continuous features
#   BernoulliNB()                    ← binary features
#