*** Automated Login Verification for OrangeHRM Site ***


Project Structure

TEST AUTOMATION/
│
├── Configuration/
│   └── config.ini
│
├── Logs/
│   └── ...
│
├── PageObjects/
│   ├── __init__.py
│   ├── DashboardPage.py
│   ├── LeavePage.py
│   └── LoginPage.py
│
├── Reports/
│   └── ...
│
├── Screenshots/
│   └── ...
│
├── TestCases/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_leave.py
│   ├── test_login.py
│   └── test_logout.py
│
├── Utilities/
│   ├── __init__.py
│   ├── Logger.py
│   ├── ReadProperties.py
│   └── WaitUtils.py
│
├── README.md
├── requirements.txt
└── Run_All_Tests.bat


*** Test Cases ***
test_login.py: Validates the login functionality.
test_leave.py: Tests leave application features.
test_logout.py: Verifies the logout process.

*** Utilities ***
Logger.py: Handles test logs.
ReadProperties.py: Reads configuration properties.
WaitUtils.py: Provides explicit wait utilities for stable automation.

*** Reporting & Screenshots ***
Reports/: Stores test execution reports.
Screenshots/: Contains screenshots captured on test failures.