# Chrome Table Exporter

A minimal Chrome extension that exports the first HTML table on the current page to CSV.

## Install Locally

1. Open `chrome://extensions`.
2. Enable Developer mode.
3. Click "Load unpacked".
4. Select this `chrome-table-exporter` folder.

## Usage

1. Open any page with an HTML table.
2. Click the extension icon.
3. Click "Export first table".

## Files

- `manifest.json` - Chrome extension manifest.
- `popup.html` - Popup UI.
- `popup.js` - Finds the active tab and runs the export script.
- `content.js` - Extracts the table and triggers a CSV download.

