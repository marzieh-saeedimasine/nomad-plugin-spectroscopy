# NOMAD Spectroscopy Plugin

![Tests](https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy/actions/workflows/tests.yml/badge.svg)
![Docs](https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy/actions/workflows/docs.yml/badge.svg)
[![PyPI](https://img.shields.io/pypi/v/nomad-plugin-spectroscopy)](https://pypi.org/project/nomad-plugin-spectroscopy/)

A NOMAD plugin for parsing and managing spectroscopy data including IR, Raman, and UV-Vis spectroscopy.

## Features

- 📊 Parse spectroscopy CSV files with wavenumber and absorbance data
- 🔬 Support for multiple spectroscopy types (IR, Raman, UV-Vis)
- 🔧 Flexible column name matching
- ✨ Robust error handling
- 📈 Integration with NOMAD's data management platform

## Installation

### From PyPI

```bash
pip install nomad-plugin-spectroscopy
```

### Development Installation

Clone the repository and install in development mode:

```bash
git clone https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy.git
cd nomad-plugin-spectroscopy
pip install -e ".[dev]"
```

Or with `uv`:

```bash
uv add -e ".[dev]"
```

## Quick Start

### CSV File Format

Upload CSV files with the following columns:

```csv
wavenumber_cm1,absorbance
650.4205,0.006448
652.2841,0.007156
654.1478,0.008152
```

### Supported Column Names

The parser is flexible with column naming:

- **Wavenumber:** `wavenumber_cm1`, `wavenumber_cm-1`, `wavenumber [cm-1]`, `wavenumber`
- **Absorbance:** `absorbance`, `absorbance_au`, `absorbance [a.u.]`

## Usage in NOMAD

This plugin extends NOMAD with spectroscopy data parsing capabilities. Once installed in your NOMAD instance, you can:

1. Upload spectroscopy CSV files
2. The plugin automatically detects and parses spectroscopy data
3. Data is organized into the plugin's schema
4. Use NOMAD's search and analytics features on your spectroscopy data

## Documentation

For detailed documentation, visit: [https://fairmat-nfdi.github.io/nomad-plugin-spectroscopy](https://fairmat-nfdi.github.io/nomad-plugin-spectroscopy)

## Development

### Running Tests

```bash
pytest
```

### Building Documentation

```bash
cd docs
mkdocs serve
```

### Code Quality

Format code with `ruff`:

```bash
ruff format src tests
ruff check src tests --fix
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) file for details.

## Citation

If you use this plugin in your research, please cite:

```bibtex
@software{nomad_spectroscopy_plugin,
  title = {NOMAD Spectroscopy Plugin},
  author = {Saeedimasine, Marzieh},
  year = {2024},
  url = {https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy}
}
```

## Contact

For questions or issues, please open an [issue on GitHub](https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy/issues).
