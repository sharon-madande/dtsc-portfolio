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


## Measuring Advancement

Teams received an advancement score tournament stage:

**1** Group Stage
**2** Round of 16 
**3** Quarterfinal
**4** Semifinal
**5** Runner-up
**6** Champion

Modric et al. (2022) also used measures of tournament achievement when studying UEFA Champions League teams.

---

## Key Findings

The analysis shows a **general positive association** between the number of top-performing players and tournament advancement.

| Team                                                   | Top Performers | Final Stage  |
| ------------------------------------------------------ | -------------: | ------------ |
|    **<span style="color:#b8860b;">Real Madrid</span>** |         **10** | Champion     |
| Liverpool                                              |         **10** | Runner-up    |
| Villarreal                                             |          **9** | Semifinal    |
| Bayern                                                 |          **9** | Quarterfinal |
| Manchester City                                        |          **8** | Semifinal    |

Several teams also had top-performing players across both attacking and defensive categories.

---

## Reflection

This project was one of my first opportunities to take a real dataset and turn it into a complete data science project. I enjoyed working with soccer data because it allowed me to connect something I already enjoy with the data science skills I'm learning.

One of the biggest things I learned was that the way I define and measure variables can affect the story the data tells. Using the 90th-percentile cutoff gave me a clear way to identify top performers, but I also learned that there are different ways to measure player and team performance not based on what I think make them top player. ;)

I also learned that data can show a pattern without explaining everything behind that pattern. Factors such as playing time, injuries, tactics, coaching, teamwork, and opponent strength are not fully captured in these statistics, thats where accuracy and recall may impact some results.

If I continued this project, I would compare multiple Champions League seasons and include more team and match-level information. This would help me understand whether the patterns I found are consistent over time.

Overall, this project helped me become more comfortable with **pandas, data visualization, research questions, and findings from data**. It also showed me how I can use a personal interest to create a data science project.


The complete data preparation, analysis, and visualizations are available in the Jupyter Notebook.

**[ View the Jupyter Notebook →]**


## References

Bampouras, M. T., Cronin, C., & Miller, K. P. (2012). Performance analytic processes in elite sport practice: An exploratory investigation of the perspectives of a sport scientist, coach and athlete. *International Journal of Performance Analysis in Sport, 12*(2), 468–483. https://doi.org/10.1080/24748668.2012.11868611

Modric, T., Versic, S., & Jelicic, M. (2022). Monitoring technical performance in the UEFA Champions League: Differences between successful and unsuccessful teams. *Montenegrin Journal of Sports Science and Medicine*.

Pearson, A., Webb, T., Barrow, C., Milligan, G., & Miller-Dicks, M. (2026). “What are we looking at?”: The development and implementation of a performance analysis framework for netball umpires. *International Journal of Performance Analysis in Sport, 26*(1), 118–141.

## Data & Supporting Sources

ESPN Internet Ventures. (2022). UEFA Champions League performance stats, 2021–22 season. ESPN.
Pooyanosk1382. (2022). 

POOYANOSK1382/UCL21-22: An analysis on UCL21-22 and players [GitHub repository]. GitHub.

