# BBC Weather Scraper using Selenium <br>
This project implements a Selenium-based Python script to scrape weather data from the BBC Weather website for a given city. The main function get_weather(driver, days) extracts the weather forecast for a specified number of days, returning a list of tuples that contain weather conditions and maximum temperatures.

The project also includes unit tests to verify the functionality of the scraper.

## Table of Contents
<ol>
    <li>Features</li>
    <li>Requirements</li>
    <li>Installation</li>
    <li>Usage</li>
    <li>Running Unit Test</li>
    <li>License</li>
</ol>

## Features
Scrapes BBC Weather for a specified city.
Extracts weather conditions (e.g., Sunny, Thundery Shower, etc.) and maximum temperatures for the specified days.
Returns result as a list of tuples: (weather_description: str, max_temperature: int).
Handles invalid input cases (e.g., days < 1 or days > 10).
Comes with unit test-based test cases to validate the scraper's functionality.
## Requirements
<ul>
    <li>Python 3.x</li>
    <li>Selenium</li>
    <li>Web browser (e.g., Firefox) and corresponding WebDriver (e.g., GeckoDriver for Firefox)</li>
</ul>

## Installation
Clone the Repository
```
git clone https://github.com/Vermayugank/Selenium_AutomationWithPython.git
```

Set Up a Virtual Environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the Required Packages

bash
Copy code
pip install -r requirements.txt
The requirements.txt file should contain selenium and any other necessary dependencies.
Download the Browser Driver

If you're using Firefox, download GeckoDriver and add it to your system's PATH.
If you're using Chrome, you can download ChromeDriver and update the script accordingly.
Usage
The main function in this project is get_weather(driver, days), which scrapes weather information from the BBC Weather website.

Here's an example of how to use the function:

python
Copy code
from selenium import webdriver
from solution import get_weather

# Set up the Selenium WebDriver
driver = webdriver.Firefox()

# Navigate to the BBC Weather page for Sofia
driver.get('http://www.bbc.com/weather/727011')

# Get the weather forecast for 5 days
weather_data = get_weather(driver, 5)

# Print the scraped weather data
for weather_description, max_temp in weather_data:
    print(f"Weather: {weather_description}, Max Temp: {max_temp}°C")

# Close the driver
driver.quit()
Running Unit Tests
Unit tests are provided to ensure the scraper works correctly. These tests validate:

Correct handling of invalid inputs (e.g., negative or out-of-bound days).
Correct extraction of weather data for Sofia and New York.
To run the tests:

Make sure you have unit test (included in Python by default).

Run the following command in your terminal:

bash
Copy code
python -m unittest discover
Example Test Cases
Invalid Input Handling: Ensure the function returns None for invalid values of days such as -1, 0, and 11.
Data Extraction for Sofia: Test for the correct extraction of weather data for Sofia, Bulgaria.
Data Extraction for New York: Test for the correct extraction of weather data for New York, USA.
The unit tests can be found in test_solution.py.

License
This project is licensed under the MIT License. See the LICENSE file for details.
