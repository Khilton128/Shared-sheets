import requests

def fetch_airtable_data(api_key, base_id, table_name):
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    records = response.json().get('records', [])
    return [record['fields'] for record in records]
