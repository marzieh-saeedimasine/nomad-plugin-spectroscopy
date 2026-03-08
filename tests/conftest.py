"""
Test configuration and fixtures for the spectroscopy plugin.
"""

import pytest


@pytest.fixture
def sample_csv_data():
    """Sample spectroscopy CSV data for testing."""
    return """wavenumber_cm1,absorbance
650.4205,0.006448
652.2841,0.007156
654.1478,0.008152
656.0114,0.009341
657.8751,0.010723
"""


@pytest.fixture
def sample_csv_file(tmp_path, sample_csv_data):
    """Create a temporary CSV file with sample data."""
    csv_file = tmp_path / "sample_spectrum.csv"
    csv_file.write_text(sample_csv_data)
    return csv_file
