# Usage

## Basic Usage

### Uploading Spectroscopy Data

1. **Prepare your data** in CSV format:
   ```csv
   wavenumber_cm1,absorbance
   650.4205,0.006448
   652.2841,0.007156
   654.1478,0.008152
   ```

2. **Upload to NOMAD** through the web interface or API

3. **The plugin automatically**:
   - Detects the file format
   - Parses the spectroscopy data
   - Creates structured entries in NOMAD

## CSV File Format

### Supported Column Names

The parser is flexible and accepts common naming conventions:

#### Wavenumber
- `wavenumber_cm1`
- `wavenumber_cm-1`
- `wavenumber [cm-1]`
- `wavenumber`
- `frequency`

#### Absorbance
- `absorbance`
- `absorbance_au`
- `absorbance [a.u.]`
- `intensity`
- `signal`

### Example Files

#### IR Spectroscopy
```csv
wavenumber_cm-1,absorbance
4000,0.01
3800,0.02
3600,0.05
...
```

#### Raman Spectroscopy
```csv
wavenumber [cm-1],intensity [a.u.]
100,150
200,200
300,250
...
```

#### UV-Vis Spectroscopy
```csv
wavelength_nm,absorbance
200,0.1
300,0.5
400,0.8
500,0.3
```

## Accessing Data via API

### Python Client

```python
from nomad_lab_client import NOMADClient

# Initialize client
client = NOMADClient()

# Search for spectroscopy entries
results = client.search(
    query='quantities.n_atoms:[* TO *]',
    filter='spectra_search:*'
)

# Process results
for entry in results:
    print(entry.metadata.entry_type)
```

### Direct HTTP API

```bash
# Search for spectroscopy data
curl "https://your-nomad-instance/api/v1/entries?search_after=0&page_after=0&query=.data.spectrum_type%3DIR"
```

## Schema Information

The plugin uses the following schema definitions:

- **Spectrum** - Main container for spectroscopy data
- **SpectroscopyProperties** - Measured spectroscopy properties
- **MethodProperties** - Measurement method details

For detailed schema information, see the API Reference.

## Best Practices

1. **Consistent Naming** - Use standard column names for better parsing
2. **File Organization** - Keep related spectra together
3. **Metadata** - Include relevant metadata where possible
4. **Data Quality** - Ensure data values are numeric
5. **File Size** - Avoid extremely large CSV files (> 100MB)

## Examples

### Example 1: Upload and Search

```python
# Upload a spectrum file
spectrum_file = "ir_sample.csv"

# Search uploaded data
for entry in client.search(filter='data.spectrum_type:IR'):
    print(f"Found IR spectrum: {entry.metadata.name}")
```

### Example 2: Batch Processing

```python
import glob

# Process multiple spectrum files
for file in glob.glob("spectra/*.csv"):
    # Upload file
    result = client.upload_file(file)
    print(f"Uploaded {file}: {result.entry_id}")
```
