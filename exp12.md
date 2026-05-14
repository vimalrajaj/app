# 12. Setup test automation using Cucumber BDD framework with Selenium and generate behavior-driven reports
## Aim
To set up test automation using the Cucumber BDD framework with Selenium and generate behavior-driven reports.

## Procedure
1. Create feature file with scenarios.
2. Write step definition class.
3. Connect step definitions to Selenium code.
4. Run Cucumber test suite.
5. Generate readable HTML report.

## Sample Feature File
```cucumber
Feature: Login
Scenario: Valid login
Given user is on login page
When user enters valid credentials
Then user should reach home page
```

## Output
Behavior-driven scenarios and reports are generated through Cucumber.
