import pandas as pd
import streamlit as st
import io

st.title("Tech Rentals Inventory Survey Tool")

uploaded_file = st.file_uploader("Upload Connect2 CSV Export", type=['csv'])

if uploaded_file is not None:
    # Read UTF-16 tab-delimited file
    content = uploaded_file.read()
    decoded = content.decode('utf-16')
    df = pd.read_csv(io.StringIO(decoded), sep='\t', on_bad_lines='skip')
    
    # Apply filters automatically
    filtered = df[(df['Available'] == 'Yes') & (df['State'] == 'In service')]
    result = filtered[['Parent resource', 'Barcode']]
    
    # Display results
    st.success(f"Found {len(result)} available computers ready for checkout in Connect2. Please double check physical inventory on the shelves.")
    st.dataframe(result, use_container_width=True)
else:
    st.info("Upload a CSV file from Connect2 to begin. This can be found by going to Resouces > Export Data > 'Click Export Data to Excel'")