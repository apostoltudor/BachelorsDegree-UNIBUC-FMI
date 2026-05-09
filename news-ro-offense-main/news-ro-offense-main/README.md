# News-RO-Offense

a novel Romanian language dataset for offensive message detection with manually 
annotated comment from a local Romanian news website (stiri de cluj) into five classes:

* non-offensive
* targeted insults
* racist
* homophobic
* sexist

Resulting in 4052 annotated messages

# Corpus statistics

| Class | Label | # examples | Percentage |
|------|------|------|------|
|Non-offensive | 0 | 2682 | 66.19% |
|Targeted insult | 1 | 777 | 19.18% |
|Racist | 2 | 252 | 6.22% |
|Homophobic | 3 | 186 | 4.59% |
|Sexist | 4 | 155 | 3.82% |
| | | | |
|TOTAL | | 4052 | |

# Data structure

### comments.csv
Csv containing all annotated comments (Fields *comment_text* and *LABEL*)

additionally, all comments have the article_id for the originating article and, if they were a reply to another comment, the reply-to comment_id

### articles.csv

contains all 160 articles that were scraped for comments. The available fields are - Publishing Date, Article Title, Article Tags list and Article content



# Paper citation

```
@inproceedings{cojocaru2022news-ro-offense,
  title={News-RO-Offense - A Romanian Offensive Language Dataset and Baseline Models Centered on News Article Comments},
  author={Cojocaru, Andreea and Paraschiv, Andrei and Dascalu, Mihai},
  booktitle={Proceedings of the international conference on human-computer interaction-RoCHI 2022},
  pages={--},
  year={2022}
}

```
