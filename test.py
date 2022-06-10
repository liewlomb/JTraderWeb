import pandas as pd
import json

df = pd.read_csv('~/Desktop/set100_q1_2022.csv')
df = df.set_index('No')

print(df)
jsData = df.to_json(orient="index")
result = json.loads(jsData)
print(result)

#check json
parsed = json.loads(result)
test = json.dumps(parsed, indent = 4)
print(test)


