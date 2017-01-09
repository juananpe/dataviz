from panda_utils import *
import pandas as pd

df = pd.read_json(open('/opt/dataviz/nobel_winners/nobel_winners/spiders/nobel_winners_full.json'))
# dataframe_to_mongo(df, 'nobel_prize', 'winners')

# df = mongo_to_dataframe('nobel_prize', 'winners')

df.info()
df.describe(include=['object'])
df.head()
