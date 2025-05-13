import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_sheet(sheet_name, data, creds_json):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    with open("temp_creds.json", "w") as f:
        f.write(creds_json)

    creds = ServiceAccountCredentials.from_json_keyfile_name("temp_creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    sheet.clear()
    if data:
        headers = list(data[0].keys())
        values = [headers] + [[row.get(col, '') for col in headers] for row in data]
        sheet.append_rows(values)
