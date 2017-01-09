from panda_utils import *
import pandas as pd

# df = pd.read_json(open('/opt/dataviz/nobel_winners/nobel_winners/spiders/nobel_winners.json'))

df = mongo_to_dataframe('nobel_prize', 'winners')
df.info()

# dataframe_to_mongo(df, 'nobel_prize', 'winners')


