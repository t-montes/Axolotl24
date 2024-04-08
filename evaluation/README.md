# Evaluation scripts

## Track 1

```commandline
python3 scorer_track1.py --gold GOLD_DATA.tsv --pred PREDICTIONS.tsv
```

### Baseline results

| Language     | ARI   | Macro F1 |
|--------------|-------|----------|
| Finnish, dev | 0.022 | 0.222    |
| Russian, dev | 0.073 | 0.280    |

## Track 2

```commandline
python3 scorer_track2.py PREDICTIONS.tsv GOLD_DATA.tsv OUTPUT_FILE.txt
```

### Baseline results

| Language     | BLEU  | BERTScore |
|--------------|-------|-----------|
| Finnish, dev | 0.248 | 0.607     |
| Russian, dev | 0.886 | 0.595     |
