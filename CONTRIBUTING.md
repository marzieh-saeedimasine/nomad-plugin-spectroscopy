# Contributing to NOMAD Spectroscopy Plugin

First off, thank you for considering contributing to the NOMAD Spectroscopy Plugin! It's people like you that make this plugin such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, search the issue tracker as the problem might already be reported. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots and animated GIFs if possible**
* **Include your environment details**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and the expected behavior**

### Pull Requests

* Fill in the PR template when creating a pull request
* Follow the Python styleguides
* Include appropriate test cases
* Add documentation for any new functionality
* End all files with a newline

## Development Setup

### Prerequisites

* Python 3.10 or higher
* Git

### Getting Set Up

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/nomad-plugin-spectroscopy.git
   cd nomad-plugin-spectroscopy
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

### Running Tests

```bash
pytest
```

To run tests with coverage:

```bash
pytest --cov=src/nomad_plugin_spectroscopy
```

### Code Style

This project uses `ruff` for code formatting and linting. Format your code before submitting:

```bash
ruff format src tests
ruff check src tests --fix
```

### Building Documentation

```bash
cd docs
mkdocs serve
```

Then navigate to `http://localhost:8000` in your browser.

## Styleguides

### Python Style

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use meaningful variable and function names
* Add docstrings to functions and classes
* Keep lines under 100 characters

### Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Git Workflow

1. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
4. Create a Pull Request on GitHub

## Additional Notes

### Issue and Pull Request Labels

* `bug` - Something isn't working
* `enhancement` - New feature or request
* `documentation` - Improvements or additions to documentation
* `good first issue` - Good for newcomers
* `help wanted` - Extra attention is needed

## Recognition

Contributors will be recognized in:
* The README.md file
* Release notes
* GitHub contributors page

Thank you for contributing! 🎉
