# PubMed-Paper-Filterer
 
PubMed is a public API developed by NCBI at USA. It is served by the E-Utilities i.e. Entrez Programming Utilities # PubMed Paper Fetcher CLI

## Overview
The PubMed Paper Fetcher CLI is a Python-based application designed to fetch and filter academic papers and articles from the PubMed database. It provides a Command Line Interface (CLI) for users to search for papers on specific topics, filter results based on criteria such as publication date or author type, and control the output with various options.

This project uses:
- **PubMed API** for fetching papers and articles.
- **Jupyter Notebook** for exploratory analysis and testing during development.
- **Poetry** for dependency management.

## Features
- Fetch papers from PubMed using a keyword-based query.
- Filter results based on:
  - Exclusion of non-academic authors.
  - Publication date.
  - Other customizable criteria.
- CLI with:
  - Help menu (`-h`) to display available commands and usage.
  - Debug mode (`-d`) for detailed logging.
  - Maximum results (`-max_results`) to limit the number of articles fetched.

## Project Structure
```
pubmed-cli/
    __init__.py         # Package initialization
    utils.py            # Utility functions for filtering papers
    fetch.py            # Fetching data from PubMed API
main.py                 # CLI entry point using argparse
```

### Directory Details
1. **`pubmed-cli/__init__.py`**
   - Initializes the `pubmed-cli` package.

2. **`pubmed-cli/utils.py`**
   - Contains functions for filtering papers based on criteria such as:
     - Excluding non-academic authors.
     - Filtering by publication date and other metadata.

3. **`pubmed-cli/fetch.py`**
   - Handles interactions with the PubMed API.
   - Fetches papers based on user-defined queries.

4. **`main.py`**
   - Entry point for the CLI.
   - Implements argument parsing using `argparse`.
   - Supports the following CLI options:
     - `-h` or `--help`: Displays help and usage details.
     - `-d` or `--debug`: Enables debug mode for detailed logging.
     - `-max_results`: Specifies the maximum number of results to fetch.
     - Query: Fetches papers based on the provided keyword or topic.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pubmed-cli.git
   cd pubmed-cli
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the Poetry environment:
   ```bash
   poetry shell
   ```

## Usage
Run the CLI using the following command:
```bash
python main.py [OPTIONS] QUERY
```

### Example Commands
1. Fetch papers with a keyword:
   ```bash
   python main.py "machine learning"
   ```

2. Limit the number of results:
   ```bash
   python main.py -max_results 10 "cancer research"
   ```

3. Enable debug mode:
   ```bash
   python main.py -d "genomics"
   ```

4. Display help menu:
   ```bash
   python main.py -h
   ```

## Development
### Jupyter Notebook
A Jupyter Notebook was used during the development phase for exploratory testing of the PubMed API and filtering logic. This notebook can be found in the project repository and provides a detailed step-by-step workflow.

### Testing
- Run unit tests to ensure functionality of `fetch.py` and `utils.py`.
- Debugging enabled via the `-d` option for enhanced troubleshooting.

## Dependencies
This project uses the following dependencies:
- `requests` for interacting with the PubMed API.
- `argparse` for CLI argument parsing.
- `loguru` (optional) for enhanced logging in debug mode.

Dependencies are managed using Poetry. To install them, run:
```bash
poetry install
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- PubMed for providing access to their database.
- Open-source contributors for their support and inspiration.

