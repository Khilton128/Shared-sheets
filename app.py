import streamlit as st
from services.airtable import fetch_airtable_data
from utils.sheets import upload_to_sheet

st.title("Free Coupler Clone - Airtable to Google Sheets")

with st.form("sync_form"):
    st.subheader("Airtable Details")
    api_key = st.text_input("Airtable API Key", type="password")
    base_id = st.text_input("Airtable Base ID")
    table_name = st.text_input("Table Name")

    st.subheader("Google Sheets Details")
    sheet_name = st.text_input("Google Sheet Name")
    creds_json = st.text_area("Paste Google Service Account JSON")

    submitted = st.form_submit_button("Sync Data")

    if submitted:
        try:
            st.info("Fetching data from Airtable...")
            records = fetch_airtable_data(api_key, base_id, table_name)
            st.success(f"Fetched {len(records)} records.")

            st.info("Uploading to Google Sheets...")
            upload_to_sheet(sheet_name, records, creds_json)
            st.success("Upload complete! Check your Google Sheet.")
        except Exception as e:
            st.error(f"Error: {str(e)}")
