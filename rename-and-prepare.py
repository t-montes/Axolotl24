import glob
import pandas as pd
import os

TRACK = 'track2'

predictions_folder = 'predictions'
files = glob.glob(f'{predictions_folder}/**/*.tsv', recursive=True)
dfs = dict()
for file in files:
    folder, filename = file.split('\\')[1:]
    if filename == "axolotl.dev.ru.tsv":
        continue
    dfs[folder] = dfs.get(folder, dict())
    dfs[folder][filename] = pd.read_csv(file, sep='\t')

for path, d in dfs.items():
    for filename, df in d.items():
        # remove all the rows where the usage_id column contains the word "augmented"
        df = df[~df.usage_id.str.contains("augmented")]
        df = df[~df.usage_id.str.contains("artificial")]
        df = df[~df.usage_id.str.contains("arificial")]
        
        filename = filename.replace('.', '_').replace('_tsv', '.tsv').replace('axolotl', TRACK)
        if not os.path.exists(f'./submission/real/{path}'):
            os.makedirs(f'./submission/real/{path}')

        df.to_csv(f'./submission/real/{path}/{filename}', sep='\t', index=False)
