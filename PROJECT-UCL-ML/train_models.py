import pandas as pd

from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

df = pd.read_csv("ml_dataset.csv")


# define the previous-season features

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


#training and test data

train_data = df[
    df["dataset_type"] == "training"
].copy()

test_data = df[
    df["dataset_type"] == "test"
].copy()

X_train = train_data[features]
y_train = train_data["Winner"]

X_test = test_data[features]
y_test = test_data["Winner"]


print("Training observations:", len(X_train))
print("Test observations:", len(X_test))
print()

# Baseline model

baseline = DummyClassifier(
    strategy="most_frequent"
)

baseline.fit(X_train, y_train)

baseline_predictions = baseline.predict(X_test)


#Logistic Regression

logistic_model = LogisticRegression(
    max_iter=2000
)

logistic_model.fit(
    X_train,
    y_train
)

logistic_predictions = logistic_model.predict(
    X_test
)


# Random Forest

random_forest_model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

random_forest_model.fit(
    X_train,
    y_train
)

random_forest_predictions = (
    random_forest_model.predict(X_test)
)


def evaluate_model(
    name,
    actual,
    predictions
):

    accuracy = accuracy_score(
        actual,
        predictions
    )

    precision = precision_score(
        actual,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        actual,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        actual,
        predictions,
        zero_division=0
    )

    print(name)
    print("-" * len(name))

    print("Accuracy :", round(accuracy, 3))
    print("Precision:", round(precision, 3))
    print("Recall   :", round(recall, 3))
    print("F1-score :", round(f1, 3))
    print()


#Evaluate all models

print("MODEL RESULTS")
print("=" * 40)
print()

evaluate_model(
    "Baseline",
    y_test,
    baseline_predictions
)

evaluate_model(
    "Logistic Regression",
    y_test,
    logistic_predictions
)

evaluate_model(
    "Random Forest",
    y_test,
    random_forest_predictions
)


# probabilities

logistic_probabilities = (
    logistic_model.predict_proba(X_test)[:, 1]
)

random_forest_probabilities = (
    random_forest_model.predict_proba(X_test)[:, 1]
)


# results

results = test_data[
    ["season", "team", "Winner"]
].copy()

results["Logistic_Probability"] = (
    logistic_probabilities
)

results["Random_Forest_Probability"] = (
    random_forest_probabilities
)


#Logistic regression ranking

results["Logistic_Rank"] = (
    results["Logistic_Probability"]
    .rank(
        ascending=False,
        method="min"
    )
    .astype(int)
)

results = results.sort_values(
    "Logistic_Probability",
    ascending=False
)


# prediction ranking

print("2025/26 LOGISTIC REGRESSION RANKING")
print("=" * 40)

print(
    results[
        [
            "Logistic_Rank",
            "team",
            "Logistic_Probability",
            "Random_Forest_Probability"
        ]
    ].to_string(
        index=False,
        formatters={
            "Logistic_Probability":
                "{:.3f}".format,

            "Random_Forest_Probability":
                "{:.3f}".format
        }
    )
)


#prediction and actual winner

actual_winner = results[
    results["Winner"] == 1
]["team"].iloc[0]

predicted_winner = results.iloc[0]["team"]


print()
print("Actual 2025/26 champion:")
print(actual_winner)

print()
print("Logistic Regression's highest-probability prediction:")
print(predicted_winner)

print()

if predicted_winner == actual_winner:

    print(
        "The Logistic Regression model correctly "
        "identified the 2025/26 champion!"
    )

else:

    print(
        "The Logistic Regression model did not "
        "identify the 2025/26 champion."
    )


# results

results.to_csv(
    "2025_26_predictions.csv",
    index=False
)

print()
print("Predictions saved to:")
print("2025_26_predictions.csv")