## Subtask 2. Definition generation for novel word senses.

[Codalab competition for Subtask 2](https://codalab.lisn.upsaclay.fr/competitions/18008)

This subtask challenges the participants to submit good **descriptions/definitions for the novel senses** they found in subtask 1. The definitions can be generated from scratch or retrieved from existing ontologies: this is completely up to the participants. The organizers will map the predicted definitions to the gold standard ones and evaluate their quality with the standard NLG metrics.

* **Inputs**: Same as subtask 1
* **Predictions**: Same as subtask 1 plus a **dictionary-like definition for every novel sense of the target word** (a sense not present in the dictionary entry from the first time period)
* **Metrics**: BLEU/ROUGE and BERTScore. The final score is averaged across target words
* **Ground truth**: definitions from our gold standard sense inventories
