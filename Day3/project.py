import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=" * 50)
print("TITANIC DATASET — EXPLORATION REPORT")
print("=" * 50)

print(f"\nShape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# ─────────────────────────────────────────
# 2. MISSING VALUES
# ─────────────────────────────────────────
print("\n── Missing Values (before cleaning) ──")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
print(pd.DataFrame({"count": missing, "percent": missing_pct})[missing > 0])

# ─────────────────────────────────────────
# 3. CLEAN DATA
# ─────────────────────────────────────────
df["Age"]      = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df             = df.drop(columns=["Cabin"])

print("\n── Missing Values (after cleaning) ──")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("No missing values remaining ✓")

# ─────────────────────────────────────────
# 4. GROUPBY SUMMARIES
# ─────────────────────────────────────────
print("\n── Summary 1: Survival Rate by Passenger Class ──")
s1 = df.groupby("Pclass")["Survived"].agg(
    survival_rate="mean",
    total_passengers="count",
    survivors="sum"
).round(2)
print(s1)

print("\n── Summary 2: Survival Rate by Sex ──")
s2 = df.groupby("Sex")["Survived"].agg(
    survival_rate="mean",
    total="count"
).round(2)
print(s2)

print("\n── Summary 3: Survival Rate by Class + Sex ──")
s3 = df.groupby(["Pclass", "Sex"])["Survived"].mean().round(2).reset_index()
s3.columns = ["Class", "Sex", "Survival Rate"]
print(s3)

print("\n── Summary 4: Age & Fare stats by Class ──")
s4 = df.groupby("Pclass").agg(
    avg_age=("Age", "mean"),
    avg_fare=("Fare", "mean"),
    max_fare=("Fare", "max"),
).round(2)
print(s4)

# ─────────────────────────────────────────
# 5. CHARTS
# ─────────────────────────────────────────
fig = plt.figure(figsize=(14, 10))
fig.suptitle("Titanic Dataset — Exploratory Analysis", fontsize=15, fontweight="bold", y=0.98)
gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)
plt.show()

COLORS = ["#e74c3c", "#3498db", "#2ecc71"]

# Chart 1: Age distribution
ax1 = fig.add_subplot(gs[0, 0])
ax1.hist(df["Age"], bins=25, color="#3498db", edgecolor="white", linewidth=0.5)
ax1.set_title("Age Distribution", fontweight="bold")
ax1.set_xlabel("Age")
ax1.set_ylabel("Count")

# Chart 2: Survival rate by class
ax2 = fig.add_subplot(gs[0, 1])
survival_class = df.groupby("Pclass")["Survived"].mean()
bars = ax2.bar(["1st", "2nd", "3rd"], survival_class.values, color=COLORS, width=0.5)
ax2.set_title("Survival Rate by Passenger Class", fontweight="bold")
ax2.set_xlabel("Class")
ax2.set_ylabel("Survival Rate")
ax2.set_ylim(0, 1)
for bar, val in zip(bars, survival_class.values):
    ax2.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.02,
             f"{val:.0%}", ha="center", fontsize=10)

# Chart 3: Survival rate by Sex
ax3 = fig.add_subplot(gs[1, 0])
survival_sex = df.groupby("Sex")["Survived"].mean()
bars2 = ax3.bar(survival_sex.index, survival_sex.values,
                color=["#e74c3c", "#3498db"], width=0.4)
ax3.set_title("Survival Rate by Sex", fontweight="bold")
ax3.set_xlabel("Sex")
ax3.set_ylabel("Survival Rate")
ax3.set_ylim(0, 1)
for bar, val in zip(bars2, survival_sex.values):
    ax3.text(bar.get_x() + bar.get_width() / 2,
             bar.get_height() + 0.02,
             f"{val:.0%}", ha="center", fontsize=10)

# Chart 4: Age vs Fare scatter, colored by class
ax4 = fig.add_subplot(gs[1, 1])
for pclass, color, label in zip([1, 2, 3], COLORS, ["1st", "2nd", "3rd"]):
    subset = df[df["Pclass"] == pclass]
    ax4.scatter(subset["Age"], subset["Fare"],
                c=color, alpha=0.5, s=20, label=label)
ax4.set_title("Age vs Fare by Class", fontweight="bold")
ax4.set_xlabel("Age")
ax4.set_ylabel("Fare")
ax4.legend(title="Class")

