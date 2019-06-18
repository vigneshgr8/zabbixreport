#import zabbixgetdata

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('Zabbix report auto update-83e9f35940ac.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open("Zabbix Report -Test").sheet1

wks.update_acell('B2', "this should be in b2 cell")

cell_list = wks.range('A1:B7')

print(cell_list)