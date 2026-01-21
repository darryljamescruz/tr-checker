# Tech Rentals Inventory Checker

A Streamlit application for checking available inventory from Connect2 CSV exports.

## Features

- Upload Connect2 CSV exports
- Automatically filters for available computers in service
- Displays results with parent resource and barcode information

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:
```bash
streamlit run checker.py
```

## Deployment

### Streamlit Cloud

1. Push your code to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app"
4. Connect your GitHub repository
5. Set the main file path to `checker.py`
6. Click "Deploy"

### Other Platforms

For other deployment platforms (Heroku, AWS, etc.), ensure:
- Python 3.8+ is available
- Dependencies from `requirements.txt` are installed
- The app is started with: `streamlit run checker.py --server.port=$PORT --server.address=0.0.0.0`

## Usage

1. Export data from Connect2: Resources > Export Data > "Click Export Data to Excel"
2. Upload the CSV file through the app interface
3. Review the filtered results showing available computers ready for checkout
