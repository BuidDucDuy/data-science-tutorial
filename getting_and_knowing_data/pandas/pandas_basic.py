import pandas as pd
import numpy as np
import os
file_path = os.path.join(os.path.dirname(__file__) , "chipotle.tsv")
df = pd.read_csv(file_path , sep="\t")
print(df.head(len(df)))