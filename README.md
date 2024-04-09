# WooperNLP solution to Axolotl24 shared task

Notebook running order:
1. `augmentation.ipynb`: Augment the dataset to create new example rows to make all senses have at least 3 examples, and create an artificial gloss for each example where gloss is missing, based on the example usage.

2. `get-embeddings.ipynb`: Generate the embeddings for a given dataset; for developing the datasets from "dev-testing" folder and for the shared task test, the "augmented" folder. Two different kind of embeddings are generated: 

- `examples`: word embeddings for the word being used in the example.
- `glosses`: sentence embeddings for the gloss of the word.

3. `concatenate-embeddings.ipynb`: Concatenate both the example and gloss embedding for each row and save them as a new kind of embedding.

4. `axolotl_solution.ipynb`: [SUBTASK 1] Given the embeddings (any of the 3 types), a clustering method and a score method for clustering, assign a cluster number (sense_id) for each row.

5. `select_sense.ipynb`: [SUBTASK 2] Given the glosses from the augmentation step, select the most proper for each cluster within the clustered rows from subtask 1, as well as prearing the data for sending for both subtasks.
