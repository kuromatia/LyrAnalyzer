import json
import pandas as pd


data = pd.read_json('output.json')
print(data.drop(list(range(12)), axis=0))


'''
with open('output.json', 'r') as f:
    print(json.loads(f.read()))i

'''
