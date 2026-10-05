# 🏆 <span style="color:#1d4ed8;">Can Machine Learning Predict the Next Champions League Winner?</span>

### <span style="color:#64748b;">Predicting the 2027 UEFA Champions League Winner</span>

## <span style="color:#1d4ed8;">🔎 The Question</span>

> <span style="color:#b8860b;"><strong>Can UEFA Champions League team statistics from previous seasons be used to estimate which team is most likely to win the upcoming UEFA Champions League?</strong></span>

The strongest soccer teams in Europe are competing against each other to win the trophy and be name the best team of the year. This project explores whether previous-season stats can be used to predict the outcomes of the following season.

**Performance categories:**
Matches · Wins · Goals · Goal Difference · Shots · Possession · Passes

---

## <span style="color:#1d4ed8;"> The Data</span>

The project uses the **UEFA Champions League Historical Match Statistics 2020–2026** dataset.

|                              |                                           |
| ---------------------------- | ----------------------------------------- |
| **Seasons**                  | 2020–2021 through 2025–2026               |
| **Original unit**            | Match                                     |
| **Analysis unit**            | Team                                      |
| **Team-season observations** | 477                                       |
| **Target**                   | `Winner` — 1 if the team won, 0 if not.   |
| **Model type**               | Logistic regression                       |
| **Missing values**           | None but depends ;)                       |
| **Acquisition**              | Kaggle using `kagglehub`                  |

---

## <span style="color:#1d4ed8;"> Preparing the Data</span>

The original dataset contains individual Champions League matches, so I merged them to create team-season statistics.

For each team:

* Matches
* Wins
* Draws
* Losses
* Goals Scored
* Goals Conceded
* Goal Difference
* Win Rate
* Goals per Match
* Goals Conceded per Match
* Shots
* Shots on Target
* Possession
* Passes

Then used the **previous season's statistics** to predict the following season.

For example:

**2020–2021 statistics → 2021–2022 winner**

This prevent data leakage because the model doesn't use statistics from the season it's trying to predict.

---

## <span style="color:#1d4ed8;"> Measuring Success</span>

The target variable was `Winner`.

A team received:

**1** if it won the Champions League
**0** if it did not win

The historical Champions League winners:

| Season    | Champion            |
| --------- | ------------------- |
| 2021–2022 | Real Madrid         |
| 2022–2023 | Manchester City     |
| 2023–2024 | Real Madrid         |
| 2024–2025 | Paris Saint-Germain |
| 2025–2026 | Paris Saint-Germain |

---

## Model Development

I compared three approaches:

**Baseline**

A simple model that predicts the most common outcome.

**Logistic Regression**

A classification model that estimates the probability that a team belongs to the winner class.

**Random Forest**

A tree-based model that can identify more patterns and complex relationships between team statistics and winning.

---

## Model Evaluation

I used five metrics to compare the models:

| Metric        | What it measures                                      |
| ------------- | ----------------------------------------------------- |
| **Accuracy**  | Percentage of correct predictions                     |
| **Precision** | How often predicted winners were actually winners     |
| **Recall**    | How many actual winners were identified               |
| **F1-score**  | Balance between precision and recall                  |
| **ROC-AUC**   | How well the model separates winners from non-winners |

### 2025–2026 Test Results

| Model               | Accuracy | Precision | Recall    | F1    | ROC-AUC   |
| ------------------- | -------- | --------- | --------- | ----- | --------- |
| Baseline            | 0.978    | 0.000     | 0.000     | 0.000 | —         |
| Logistic Regression | 0.889    | 0.167     | **1.000** | 0.286 | **1.000** |
| Random Forest       | 0.956    | 0.000     | 0.000     | 0.000 | 0.955     |

Although the Random Forest had higher accuracy, it did not identify the actual winner of that season.

Logistic Regression correctly identified the 2025–2026 winner, so I selected it as the final model to estimate the winner of the 2027 UEFA Champions League.

### Model Estimates

| Rank  | Team                                                        | Estimated Probability |
| ----- | ----------------------------------------------------------- | --------------------: |
| **1** | **<span style="color:#b8860b;">Paris Saint-Germain</span>** |             **57.7%** |
| 2     | Atlético Madrid                                             |                 25.0% |
| 3     | Bayern München                                              |                  5.3% |
| 4     | Club Brugge                                                 |                  3.9% |
| 5     | Manchester City                                             |                  3.8% |

### Model Estimate

> <span style="color:#b8860b;"><strong>Paris Saint-Germain ( my team btw ) received the highest estimated probability of winning the 2027 UEFA Champions League at 57.7%, which means a potential TREBLE </strong></span>

## What the Model Tells Us

The model tell us that previous-season team statistics can provide useful information about future Champions League success.

However, the model does not capture everything that happens or could happens in football.

---

## Limitations & Ethics

One of the biggest limitations is the small number of Champions League winners available for training.

Only one team wins the competition each season, so there are very few positive examples for the model to learn from.

Second, some 2026/27 teams did not play in the 2025/26 Champions League, so they did not have previous-season Champions League statistics in the dataset, which can mislead the model too.

Another limitation is **reputation**.

Historically successful clubs often have stronger players, stronger team, and consistently strong statistics. A model trained on historical performance favor established clubs.

This raises a funny question:

> **Is the model predicting future performance, or is it learning statistical patterns associated with traditionally successful teams?, I mean it is basically the same thing but not really, in a sense of, can you really predict something or read the future of something with privilege ?? **



## Reflection

My first soccer data science project looked at whether teams with more top-performing players tended to be in the final stage of the Champions League.
Now this project, I wanted to take that idea further and see collective statistics could predict future winner.

One of the biggest things I learned was about how I prepared the data, how I separated training and testing data, and whether the evaluation metrics actually showed that the model was usefu lor could it be bias or inaccurate based on what I data I was providing.

As a truly soccer fan ( FOOTBALL!!! ) I enjoyed this project since it helped me build on the skills from my first soccer data project based on my personal interest. 

The complete data preparation, modeling, evaluation, and predictions are available in the Jupyter Notebook.

**[ View the Jupyter Notebook →](ucl_ml.ipynb)**


## Data & Supporting Sources

* ESPN. (2026). *UEFA Champions League statistics*. ESPN.

* Lago-Ballesteros, J. (2011). Differences in performance indicators between winning and losing teams in the UEFA Champions League. *Journal of Human Kinetics*. https://doi.org/10.2478/V10078-011-0011-3

* Ramos, T. (2026). UEFA Champions League Historical Match Statistics 2020–2026 [https://www.kaggle.com/datasets/ramostherunning/champions-league-historical-match-20202026/data]. Kaggle.

* Saito, T., & Rehmsmeier, M. (2015). The precision-recall plot is more informative than the ROC plot when evaluating binary classifiers on imbalanced datasets. *PLOS ONE, 10*(3), e0118432. https://doi.org/10.1371/journal.pone.0118432

* Union of European Football Associations. (2026). *Meet the 2026/27 Champions League 
league phase teams*.

* Union of European Football Associations. (2026). *UEFA Champions League history*.

