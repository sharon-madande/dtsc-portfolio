# ⚽ <span style="color:#1d4ed8;">What Makes a Successful Soccer Team?</span>

### <span style="color:#64748b;">UEFA Champions League 2021–2022</span>


## <span style="color:#1d4ed8;">🔎 The Question</span>

> <span style="color:#b8860b;"><strong>To what extent is having top-performing players across multiple attacking and defensive categories within the same team associated with how far that team advanced in the 2021–2022 UEFA Champions League?</strong></span>

The Champions League brings together elite soccer teams and players. This project explores whether teams with stronger representation among top-performing players tended to advance further.

**Performance categories:**
 Goals ·  Assists ·  Tackles Won ·  Balls Recovered

---

## <span style="color:#1d4ed8;"> The Data</span>

The project uses the **UCL | Matches & Players Data** dataset by Azmine Toushik Wasi.

|                       |                                                                |
| --------------------- | -------------------------------------------------------------- |
|  **Season**        | 2021–2022                                                      |
| **Original unit**  | Player                                                         |
| **Analysis unit** | Team                                                           |
| **Main files**     | `goals.csv`, `attacking.csv`, `defending.csv`, `key_stats.csv` |
| **Missing values** | None in selected variables                                     |
| **Acquisition**    | Kaggle API using `kagglehub`                                   |


---

## <span style="color:#1d4ed8;"> Measuring Top Performance</span>

I wanted to classified A player as a **top performer** when their statistic was at or above the 90th percentile for that category.

| Category        |                                              |
| --------------- | -------------------------------------------: |
| Goals           |    **<span style="color:#b8860b;">4</span>** |
| Assists         |    **<span style="color:#b8860b;">3</span>** |
| Tackles Won     |    **<span style="color:#b8860b;">6</span>** |
| Balls Recovered | **<span style="color:#b8860b;">37.4</span>** |


---
