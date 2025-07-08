cat > README.md << 'EOF'
# 🗺️ Indian Landmarks Visualization

This project provides an interactive **Folium-powered map** that displays:
- 📍 **UNESCO World Heritage Sites** in India using custom icon markers
- 🗺️ **State boundaries** from a GeoJSON file
- ℹ️ Popups showing the site's name, type (Cultural/Natural/Mixed), and inscription year

> Built with Python, Folium, and GeoJSON data for educational and visualization purposes.

---

## 📁 Project Structure

\`\`\`
Indian-Landmarks/
├── IL.py                            # Main Python script
├── IL.csv                           # CSV with site data (Name, Type, Year, Latitude, Longitude)
├── INDIA_STATES.geojson             # Indian state boundaries (with optional population data)
├── *.jpg                            # Site icons (named after UNESCO site names)
└── Map.html                         # Output interactive map
\`\`\`

---

## 🛠️ How It Works

- Reads data from \`IL.csv\`
- Places markers for each UNESCO site using corresponding \`.jpg\` images
- Loads \`INDIA_STATES.geojson\` to overlay state borders
- Allows toggling layers using Folium's LayerControl

---

## ▶️ How to Run

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/Hemanthk101/Indian-Landmarks.git
   cd Indian-Landmarks
   \`\`\`

2. Ensure required files are present:
   - \`IL.csv\`
   - \`INDIA_STATES.geojson\`
   - Image files like \`Taj Mahal.jpg\`, \`Agra Fort.jpg\`, etc.

3. Run the script:
   \`\`\`bash
   python IL.py
   \`\`\`

4. Open \`Map.html\` in your browser.

---

## 📌 Dependencies

- Python 3.x
- \`folium\`
- \`pandas\`

Install them with:
\`\`\`bash
pip install folium pandas
\`\`\`

---

## 🌐 Data Sources

- UNESCO site info: Manually curated or from [whc.unesco.org](https://whc.unesco.org)
- State boundaries: [Data.gov.in](https://data.gov.in) or [GADM.org](https://gadm.org)
- Coordinates: [LatLong.net](https://www.latlong.net/)

---

## 📷 Credits

All marker icons are \`.jpg\` images named after the UNESCO sites (e.g., \`Taj Mahal.jpg\`).

---


