import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import pdb
import jiwer
result_dir = "./results"
import csv

transformation = jiwer.Compose(
[
    jiwer.RemovePunctuation(),
    jiwer.ToUpperCase(),
    jiwer.RemoveWhiteSpace(replace_by_space=True),
    jiwer.RemoveMultipleSpaces(),
    jiwer.ReduceToListOfListOfWords(word_delimiter=" "),
])
    
csvs = sorted(Path(result_dir).glob("**/*.csv"))

ref_txt = "./wav/full_id_text_sorted.txt"
x = pd.read_csv(ref_txt, index_col="file_name", quoting=3)

ref_dict = x['transcription'].to_dict()
# pdb.set_trace()

datalist = []
for x in csvs:
    [user, set] = x.stem.split("_")[0: 2]
    tmp = pd.read_csv(x, header=0, quotechar='\"')
    tmp['User'] = user
    tmp['set'] = set
    speech_paths = tmp['Utt'].values
    speech_ids = []
    # Get ref
    for i in speech_paths:
        speech_ids.append(Path(i).stem)
    ref = [ref_dict[x] for x in speech_ids]
    tmp['speech_id'] = speech_ids
    tmp['ref'] =ref
    datalist.append(tmp)
    # pdb.set_trace()
    
dataset = pd.concat(datalist, ignore_index=True)
wers = []
for i in dataset.itertuples():
    # print(i)
    wer= jiwer.wer(
    i.Dictation,
    i.ref,
    truth_transform=transformation,
    hypothesis_transform=transformation,
    )
    wers.append(wer)

dataset['wer'] = wers
dataset.to_csv("wav/wer.csv")

# pdb.set_trace()
user_wer = dataset.groupby("User")['wer'].mean()
print("---WER by Participants---")
print(user_wer)

set_wer = dataset.groupby("set")['wer'].mean()
print("---WER by sets---")
print(set_wer)

all_wer = dataset['wer'].mean()
print("---WER of all---")
print(all_wer)

print("Check wav/wer.csv for more details")
print("Finished")

