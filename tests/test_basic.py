"""
Basic tests for the spectroscopy plugin.
"""

import pytest


def test_plugin_imports():
    """Test that the plugin can be imported."""
    import nomad_plugin_spectroscopy
    assert nomad_plugin_spectroscopy.__version__ is not None


def test_sample_csv_fixture(sample_csv_data):
    """Test that the sample CSV fixture works."""
    assert "wavenumber_cm1" in sample_csv_data
    assert "absorbance" in sample_csv_data
    assert "650.4205" in sample_csv_data


def test_sample_csv_file_fixture(sample_csv_file):
    """Test that the sample CSV file fixture works."""
    assert sample_csv_file.exists()
    content = sample_csv_file.read_text()
    assert "wavenumber_cm1" in content
    assert "0.006448" in content
