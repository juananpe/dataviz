import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/Users/admin/Desktop/JuananAPI-565802092fce.json', scope)
gc = gspread.authorize(credentials)
ss = gc.open('Microbios')
ss.worksheets()
ws = ss.worksheet('bugs')
ws.col_values(1)
