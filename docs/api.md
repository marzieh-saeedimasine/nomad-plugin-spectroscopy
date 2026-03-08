# API Reference

## Module: nomad_plugin_spectroscopy

Main module for the NOMAD Spectroscopy Plugin.

### Version

```python
nomad_plugin_spectroscopy.__version__
```

Current version of the plugin.

## Parsers

### SpectroscopyParser

Main parser class for spectroscopy data files.

#### Methods

#### `parse_csv(file_path: str) -> Spectrum`

Parse a CSV file containing spectroscopy data.

**Parameters:**
- `file_path` (str): Path to the CSV file

**Returns:**
- `Spectrum`: Parsed spectrum object

**Raises:**
- `FileNotFoundError`: If the file doesn't exist
- `ValueError`: If the file format is invalid

**Example:**
```python
from nomad_plugin_spectroscopy.parser import SpectroscopyParser

parser = SpectroscopyParser()
spectrum = parser.parse_csv("data.csv")
```

## Schema Classes

### Spectrum

Represents a single spectroscopy measurement.

**Attributes:**
- `name` (str): Name of the spectrum
- `spectrum_type` (str): Type of spectroscopy (IR, Raman, UV-Vis)
- `wavenumber` (List[float]): Wavenumber values [cm⁻¹]
- `absorbance` (List[float]): Absorbance values [a.u.]
- `wavelength` (Optional[List[float]]): Wavelength values [nm]

### SpectroscopyProperties

Properties and metadata for spectroscopy data.

**Attributes:**
- `measurement_date` (Optional[str]): Date of measurement
- `instrument` (Optional[str]): Instrument used
- `operator` (Optional[str]): Person who performed measurement
- `temperature` (Optional[float]): Temperature during measurement [K]

## Utility Functions

### normalize_column_names

Normalize column names from CSV files.

```python
from nomad_plugin_spectroscopy.utils import normalize_column_names

normalized = normalize_column_names(["Wavenumber (cm-1)", "ABSORBANCE"])
# Returns: ["wavenumber", "absorbance"]
```

### detect_spectrum_type

Automatically detect the type of spectroscopy from data characteristics.

```python
from nomad_plugin_spectroscopy.utils import detect_spectrum_type

spectrum_type = detect_spectrum_type(wavenumbers, absorbances)
# Returns: "IR", "Raman", or "UV-Vis"
```

## Exceptions

### SpectrumParsingError

Raised when spectroscopy data cannot be parsed.

```python
from nomad_plugin_spectroscopy.exceptions import SpectrumParsingError

try:
    spectrum = parser.parse_csv("invalid.csv")
except SpectrumParsingError as e:
    print(f"Failed to parse spectrum: {e}")
```

## See Also

- [Usage Guide](usage.md)
- [Installation](installation.md)
- [GitHub Repository](https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy)
