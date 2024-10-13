# Hepsiburada Web Automation

This project is a web automation script for the Hepsiburada website, developed using Selenium and Python.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project automates various tasks on the Hepsiburada website. It leverages Selenium to interact with the website's elements and perform actions such as searching for products, filtering results, and adding items to the cart.

## Features

- Search for products
- Filter search results
- Add products to the cart
- Navigate through different pages
- Extract product details

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/mtaksel/hepsiburada-web-automation-test-case.git
    ```
2. Navigate to the project directory:
    ```bash
    cd hepsiburada-web-automation-test-case
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure you have the ChromeDriver installed and its path set in the script.
2. Update the configuration settings in the `globalconstants.py` file if necessary.
3. Run the automation script:
    ```bash
    python -m pytest tests
    ```

## Configuration

You can configure the script by modifying the `globalconstants.py` file. Here, you can set parameters such as the base URL, search keywords, and other relevant settings.

### How to view HTML Report
* Go to root directory of your project and open `report.html`

![Hepsiburada Web Automation Test Result](./images/test_reports.png?raw=true "Hepsiburada Web Automation HTML Test Report")

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
