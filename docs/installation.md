# Installation

## Prerequisites

- Python 3.10 or higher
- A running NOMAD instance (optional, for full functionality)

## Installation Methods

### From PyPI (Recommended)

Install the latest stable release from PyPI:

```bash
pip install nomad-plugin-spectroscopy
```

### From GitHub

To install the development version directly from GitHub:

```bash
pip install git+https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy.git
```

### Development Installation

For development work, clone the repository and install in editable mode:

```bash
git clone https://github.com/FAIRmat-NFDI/nomad-plugin-spectroscopy.git
cd nomad-plugin-spectroscopy
pip install -e ".[dev]"
```

With `uv`:

```bash
uv add -e ".[dev]"
```

## Using with NOMAD

To use this plugin with your NOMAD instance, add it to your NOMAD installation:

```bash
# If your NOMAD is installed via pip
pip install nomad-plugin-spectroscopy

# Or in a NOMAD distribution
# Add to your distribution's pyproject.toml:
# dependencies = [
#     "nomad-lab[infrastructure]>=1.4.1",
#     "nomad-plugin-spectroscopy",
# ]
```

After installation, restart your NOMAD instance and the plugin will be automatically registered.

## Verification

To verify the installation:

```python
import nomad_plugin_spectroscopy
print(nomad_plugin_spectroscopy.__version__)
```

## Troubleshooting

### Plugin not appearing in NOMAD

1. Ensure the plugin is installed: `pip list | grep nomad-plugin-spectroscopy`
2. Check NOMAD logs for any loading errors
3. Try restarting NOMAD: typically `docker restart nomad-app`

### Python version issues

Ensure you're using Python 3.10 or higher:

```bash
python --version
```
