## Subtask 1. Bridging diachronic word uses and a synchronic dictionary

[Codalab competition for Subtask 1](https://codalab.lisn.upsaclay.fr/competitions/18009)

The participants are offered two corpora, belonging to different time periods. In addition to this, they are provided with a set of **dictionary entries (sense inventories)** for the target words describing their senses in the **first** time period (accompanied by definitions). The task is to find usages of the target words belonging to **newly gained senses**, i.e., senses not covered by the provided sense inventory, as well as usages **belonging to the previously existing senses**.

The assumption is that sense definitions from the dictionary, even though not always covering all word senses even from the same time period, may still be a useful additional source of information. The goal is to map word usages to the dictionary senses. This is very similar to **Word Sense Disambiguation**, with the difference being that the usages corresponding to word senses absent from the dictionary should be grouped into novel sense clusters (this is more similar to **Word Sense Induction**). In a way, this subtask is a mixture of WSD and WSI.


* **Inputs**: a set of target words, two sets of usages for each target word (a usage is a  text fragment containing a target word); target word dictionary entries with sense ids for the **first** ("old") of two time periods.
* **Predictions**: sense id for every word usage of the **second** ("new") time period (either re-using an id from the provided dictionary or adding a novel one). 
* **Metrics**: Adjusted Rand Index (ARI) for all usages and macro-F1 for usages with existing senses
* **Ground truth**: manually annotated sense inventories
