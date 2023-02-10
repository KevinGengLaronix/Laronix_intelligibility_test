import numpy as np

with open("wav/full_id_text_sorted.txt", "r") as f:
    for line in f.readlines():
        [id, trans] = line.split(",")
        if len(trans.split(' ')) >=15:
            print(id)
        
        
