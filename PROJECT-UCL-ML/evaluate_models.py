import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    roc_curve
)

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# Load the machine learning dataset
df = pd.read_csv("ml_dataset.csv")


# Features used by the models
features = [
    "previous_matches",
    "previous_wins",
    "previous_draws",
    "previous_losses",
    "previous_goals_scored",
    "previous_goals_conceded",
    "previous_goal_difference",
    "previous_win_rate",
    "previous_goals_per_match",
    "previous_goals_conceded_per_match",
    "previous_shots",
    "previous_shots_on_target",
    "previous_possession",
    "previous_passes"
]


# Separate training and testing data
train_data = df[df["dataset_type"] == "training"].copy()
test_data = df[df["dataset_type"] == "test"].copy()

X_train = train_data[features]
y_train = train_data["Winner"]

X_test = test_data[features]
y_test = test_data["Winner"]


# --------------------------------------------------
# 1. Baseline
# --------------------------------------------------

baseline = DummyClassifier(strategy="most_frequent")
baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)


# --------------------------------------------------
# 2. Logistic Regression
# --------------------------------------------------

logistic_model = LogisticRegression(max_iter=2000)
logistic_model.fit(X_train, y_train)

logistic_predictions = logistic_model.predict(X_test)


# --------------------------------------------------
# 3. Random Forest
# --------------------------------------------------

random_forest_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

random_forest_predictions = random_forest_model.predict(X_test)


# --------------------------------------------------
# Classification Metrics
# --------------------------------------------------

print("BASELINE CLASSIFICATION REPORT")
print("=" * 50)

print(
    classification_report(
        y_test,
        baseline_predictions,
        zero_division=0
    )
)


print("LOGISTIC REGRESSION CLASSIFICATION REPORT")
print("=" * 50)

print(
    classification_report(
        y_test,
        logistic_predictions,
        zero_division=0
    )
)


print("RANDOM FOREST CLASSIFICATION REPORT")
print("=" * 50)

print(
    classification_report(
        y_test,
        random_forest_predictions,
        zero_division=0
    )
)

# ROC-AUC

logistic_probabilities = (
    logistic_model.predict_proba(X_test)[:, 1]
)

random_forest_probabilities = (
    random_forest_model.predict_proba(X_test)[:, 1]
)


logistic_auc = roc_auc_score(
    y_test,
    logistic_probabilities
)

random_forest_auc = roc_auc_score(
    y_test,
    random_forest_probabilities
)


print("ROC-AUC RESULTS")
print("=" * 50)

print(
    "Logistic Regression ROC-AUC:",
    round(logistic_auc, 3)
)

print(
    "Random Forest ROC-AUC:",
    round(random_forest_auc, 3)
)

print()


# --------------------------------------------------
# Logistic Regression Feature Interpretation
# --------------------------------------------------

coefficients = pd.DataFrame({
    "feature": features,
    "coefficient": logistic_model.coef_[0]
})

coefficients["absolute_coefficient"] = (
    coefficients["coefficient"].abs()
)

coefficients = coefficients.sort_values(
    "absolute_coefficient",
    ascending=False
)


print("LOGISTIC REGRESSION FEATURE COEFFICIENTS")
print("=" * 50)

print(
    coefficients[
        ["feature", "coefficient"]
    ].to_string(index=False)
)

print()


# --------------------------------------------------
# Random Forest Feature Importance
# --------------------------------------------------

importance = pd.DataFrame({
    "feature": features,
    "importance": random_forest_model.feature_importances_
})

importance = importance.sort_values(
    "importance",
    ascending=False
)


print("RANDOM FOREST FEATURE IMPORTANCE")
print("=" * 50)

print(
    importance.to_string(index=False)
)


# --------------------------------------------------
# ROC Curve
# --------------------------------------------------

logistic_fpr, logistic_tpr, _ = roc_curve(
    y_test,
    logistic_probabilities
)

random_forest_fpr, random_forest_tpr, _ = roc_curve(
    y_test,
    random_forest_probabilities
)


plt.figure(figsize=(8, 6))

plt.plot(
    logistic_fpr,
    logistic_tpr,
    label=f"Logistic Regression (AUC = {logistic_auc:.3f})"
)

plt.plot(
    random_forest_fpr,
    random_forest_tpr,
    label=f"Random Forest (AUC = {random_forest_auc:.3f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    label="Random Guess"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve: Model Comparison")
plt.legend()
plt.grid()

plt.show()


# --------------------------------------------------
# Logistic Regression Coefficient Plot
# --------------------------------------------------

top_coefficients = coefficients.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_coefficients["feature"],
    top_coefficients["coefficient"]
)

plt.xlabel("Logistic Regression Coefficient")
plt.ylabel("Feature")
plt.title("Top Logistic Regression Feature Coefficients")

plt.gca().invert_yaxis()
plt.grid(axis="x")

plt.show()


# --------------------------------------------------
# Random Forest Feature Importance Plot
# --------------------------------------------------

top_importance = importance.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top_importance["feature"],
    top_importance["importance"]
)

plt.xlabel("Feature Importance")
plt.ylabel("Feature")
plt.title("Top Random Forest Feature Importance")

plt.gca().invert_yaxis()
plt.grid(axis="x")

plt.show()