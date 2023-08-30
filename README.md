# appium-tests-graffitecs
# Amazon App Automation Test Suite

This project demonstrates automated tests for the Amazon mobile app using Appium and Python. The tests cover various scenarios like browsing categories, applying filters, and more.

## Prerequisites

- Python (version X.X.X)
- Appium (version X.X.X)
- Android Emulator or Device
- PyCharm or any other Python IDE

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
2. Install dependencies:
  pip install -r requirements.txt
3. Set Up Appium Server:

Install Appium globally: npm install -g appium
Start the Appium server: appium


## Configuration
Running Tests
Open the test_amazon_app.py script in your preferred Python IDE.

Configure the test runner:

Update the appium_server_url to match your Appium server URL.
Run the tests:

Click on the run button for the test_amazon_app.py script.
The tests will execute on the connected Android Emulator/Device.
View Test Reports:

Test reports will be generated in the report directory in XML format.
Structure
test_amazon_app.py: Contains the test cases using the unittest framework.
amazon_app.py: Contains the Page Object Model and test actions.
apk/amazon.apk: Amazon app APK file.
