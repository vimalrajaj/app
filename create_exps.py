import os

exps = {
    "exp1.md": """# 1. Test the performance of the e-commerce application
## Aim
To test the performance of an e-commerce application under normal, peak, and stress conditions and identify response-time or scalability issues.

## Procedure
1. Identify critical user journeys such as login, search, cart, and checkout.
2. Prepare a performance test environment similar to production.
3. Decide the number of virtual users and ramp-up time.
4. Create scripts in JMeter or another performance tool.
5. Execute baseline, load, and stress tests.
6. Record response time, throughput, and failures.
7. Analyze bottlenecks and prepare report.

## Sample Performance Scenarios
• 100 users browsing products simultaneously.
• 500 users searching and filtering at the same time.
• 1000 users adding items to cart and checking out.
• 2000 users running a stress test during a sale event.

## Sample Performance Output
• Average response time: 1.8 seconds
• Throughput: 250 requests/second
• Error rate: 0.5%
• CPU usage: 72%
• Memory usage: 68%

## Result
The performance of the e-commerce application was evaluated successfully using defined metrics such as response time, throughput, and error rate.
""",
    "exp2.md": """# 2. Automate the testing of e-commerce applications using Selenium
## Aim
To design and automate key test cases for an e-commerce application using Selenium WebDriver.

## Procedure
1. Install Selenium dependencies and browser driver.
2. Open the e-commerce website.
3. Identify important web elements using locators.
4. Perform actions like search, click, add to cart, and login.
5. Add assertions to verify expected results.
6. Run the automation script and review results.

## Sample Selenium Code (Java)
```java
WebDriver driver = new ChromeDriver();
driver.get("https://www.amazon.in");
driver.findElement(By.id("twotabsearchtextbox")).sendKeys("mobile");
driver.findElement(By.id("nav-search-submit-button")).click();

driver.findElement(By.cssSelector(".add-to-cart")).click();
String cartCount = driver.findElement(By.id("cart-count")).getText();
Assert.assertTrue(Integer.parseInt(cartCount) > 0);
```

## Output
Automation scripts created using Selenium should validate core e-commerce flows.

## Result
E-commerce test cases were automated successfully using Selenium WebDriver.
""",
    "exp3.md": """# 3. Integrate TestNG with the above test automation
## Aim
To integrate TestNG with Selenium automation for structured test execution, grouping, and reporting.

## Procedure
1. Add TestNG dependency to the project.
2. Create test classes for login, search, and cart.
3. Use annotations like @BeforeClass, @AfterClass, and @Test.
4. Create testng.xml to organize execution.
5. Run tests and review the HTML report.

## Sample TestNG Code
```java
import org.testng.annotations.*;
public class EcommerceTest {
    WebDriver driver;
    @BeforeClass
    public void setup() {
        driver = new ChromeDriver();
        driver.get("https://www.amazon.in");
    }
    @Test
    public void verifyHomePage() {
        Assert.assertTrue(driver.getTitle().length() > 0);
    }
    @AfterClass
    public void tearDown() {
        driver.quit();
    }
}
```

## Sample testng.xml
```xml
<suite name="EcommerceSuite">
    <test name="SmokeTests">
        <classes>
            <class name="EcommerceTest"/>
        </classes>
    </test>
</suite>
```

## Output
TestNG should execute Selenium test methods and generate a report.
""",
    "exp4.md": """# 4. Execute the test cases against a client server or desktop application and identify the defects
## Aim
To execute prepared test cases on a client-server or desktop application and identify defects.

## Procedure
1. Open the application in the test environment.
2. Execute the prepared functional test cases.
3. Observe system response and database output.
4. Compare actual result with expected result.
5. Record failed behavior as defects.

## Defect Report
Defect ID: DEF-01
Title: Quantity update mismatch
Severity: High 
Priority: High 
Expected: Updated value should be stored correctly
Actual: Wrong value saved

## Output
Execution status and defect details are recorded in the test report.
""",
    "exp5.md": """# 5. Develop the test plan and design the test cases for an inventory control system
## Aim
To develop a detailed test plan and design test cases for an inventory control system.

## Procedure
1. Prepare test data for items, suppliers, and warehouses.
2. Execute create, update, issue, transfer, and report test cases.
3. Compare stock values before and after each action.
4. Verify alerts, totals, and database records.

## Test Cases
TC ID | Module | Test Case | Expected Result
--- | --- | --- | ---
INV-01 | Item Master | Create new item | Item should be saved
INV-03 | Stock Receipt | Receive 100 units | Stock should increase by 100

## Output
The output is a complete inventory system test plan with functional test cases.
""",
    "exp6.md": """# 6. Setup a continuous integration pipeline using Jenkins and execute automated test cases on every code commit
## Aim
To set up a continuous integration pipeline using Jenkins and run automated tests on every code commit.

## Procedure
1. Install Jenkins and required plugins.
2. Connect Jenkins with Git repository.
3. Create a pipeline or freestyle job.
4. Add build and test steps.
5. Trigger execution on every commit or webhook event.
6. Publish test reports.

## Sample Jenkins Pipeline
```groovy
pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { git 'https://github.com/example/repo.git' }
        }
        stage('Test') {
            steps { sh 'mvn test' }
        }
    }
}
```

## Output
CI pipeline is configured to run tests automatically on each commit.
""",
    "exp7.md": """# 7. Design and implement Page Object Model (POM) framework for Selenium test automation with multiple test scripts
## Aim
To design and implement the Page Object Model framework for Selenium test automation with multiple scripts.

## Procedure
1. Create Base class
2. Create Page classes
3. Create Test classes
4. Create Utility class
5. Create Configuration file

## Sample POM Code
```java
public class LoginPage {
    WebDriver driver;
    By username = By.id("username");
    By password = By.id("password");
    By loginBtn = By.id("loginBtn");

    public LoginPage(WebDriver driver) {
        this.driver = driver;
    }

    public void login(String user, String pass) {
        driver.findElement(username).sendKeys(user);
        driver.findElement(password).sendKeys(pass);
        driver.findElement(loginBtn).click();
    }
}
```

## Output
A maintainable Selenium framework based on POM is created.
""",
    "exp8.md": """# 8. Perform API testing using REST Assured and generate HTML test reports with extent reports
## Aim
To perform API testing using REST Assured and generate HTML test reports using Extent Reports.

## Procedure
1. Add REST Assured and reporting dependencies.
2. Create API test methods.
3. Add assertions for response validation.
4. Integrate Extent Reports.
5. Run tests and view HTML report.

## Sample REST Assured Code
```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class ApiTest {
    @Test
    public void getUsers() {
        given()
            .baseUri("https://reqres.in/api")
        .when()
            .get("/users?page=2")
        .then()
            .statusCode(200)
            .body("data", notNullValue());
    }
}
```

## Output
REST Assured scripts and HTML report generation are prepared.
""",
    "exp9.md": """# 9. Create automated test cases for mobile applications using Appium and execute on emulators or real devices
## Aim
To create automated test cases for a mobile application using Appium and execute them on emulators or real devices.

## Procedure
1. Install Appium server and mobile driver setup.
2. Connect emulator or real device.
3. Write automation scripts.
4. Identify elements and perform actions.
5. Execute scripts and record results.

## Sample Appium Code
```java
AndroidDriver driver = new AndroidDriver(new URL("http://127.0.0.1:4723"), caps);
driver.findElement(By.id("loginField")).sendKeys("user1");
driver.findElement(By.id("loginBtn")).click();
```

## Output
Mobile automation scripts for emulator and real device testing are created.
""",
    "exp10.md": """# 10. Implement data-driven testing using Excel/CSV files and execute parameterized test cases with TestNG
## Aim
To implement data-driven testing using Excel or CSV and execute parameterized test cases using TestNG.

## Procedure
1. Prepare test data in Excel or CSV.
2. Read data using utility classes.
3. Pass data through TestNG DataProvider.
4. Run tests using multiple datasets.
5. Review pass/fail output.

## Sample TestNG DataProvider
```java
@DataProvider(name = "loginData")
public Object[][] loginData() {
    return new Object[][] {
        {"user1", "pass1"},
        {"user2", "pass2"}
    };
}

@Test(dataProvider = "loginData")
public void loginTest(String user, String pass) {
    System.out.println(user + " " + pass);
}
```

## Output
Parameterized execution using test data files is enabled.
""",
    "exp11.md": """# 11. Perform regression testing on a web application using automation tools and document defects
## Aim
To perform regression testing on a web application using automation tools and document defects.

## Procedure
1. Identify stable functional test cases.
2. Automate them using Selenium/TestNG.
3. Run the regression suite after every build.
4. Compare new results with previous runs.
5. Document any newly introduced defects.

## Defect Example
Defect ID: REG-BUG-01
Title: Search button broken after release
Severity: High
Expected: Search should run
Actual: Button click does nothing

## Output
Regression tests are executed repeatedly and defects are documented.
""",
    "exp12.md": """# 12. Setup test automation using Cucumber BDD framework with Selenium and generate behavior-driven reports
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
""",
    "exp13.md": """# 13. Configure and execute test cases on multiple browsers using Selenium Grid and document compatibility issues
## Aim
To configure Selenium Grid and execute test cases on multiple browsers to identify compatibility issues.

## Procedure
1. Set up Selenium Grid hub and nodes.
2. Register browsers on nodes.
3. Run same test across multiple browsers.
4. Compare results.
5. Document browser-specific defects.

## Sample Compatibility Defect
Defect ID: GRID-01
Browser: Safari
Description: Checkout button misaligned
Severity: High

## Output
Cross-browser execution reports and compatibility defects are recorded.
""",
    "exp14.md": """# 14. Develop automated test scripts for database validation and data integrity testing using SQL queries
## Aim
To develop automated test scripts for database validation and data integrity testing using SQL queries.

## Procedure
1. Identify tables and relationships.
2. Prepare test data and expected database state.
3. Execute application actions.
4. Run SQL queries to verify records.
5. Compare output with expected values.

## Sample SQL Queries
```sql
SELECT * FROM orders WHERE customer_id NOT IN (SELECT customer_id FROM customers);

SELECT order_id, total_amount
FROM orders
WHERE total_amount <> (
    SELECT SUM(qty * unit_price)
    FROM order_items
    WHERE order_items.order_id = orders.order_id
);
```

## Output
Automated SQL validation scripts and database integrity checks are prepared.
""",
    "exp15.md": """# 15. Implement test automation for REST API endpoints with assertions, validations, and error handling scenarios
## Aim
To implement automated test cases for REST API endpoints with assertions, validations, and error-handling scenarios.

## Procedure
1. Identify API endpoints and request methods.
2. Create positive and negative test cases.
3. Add assertions for response code and response body.
4. Handle invalid input and error response checks.
5. Execute tests and document results.

## Sample REST Assured Code
```java
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

@Test
public void invalidTokenTest() {
    given()
        .header("Authorization", "Bearer invalid")
    .when()
        .get("/users/1")
    .then()
        .statusCode(401);
}
```

## Output
Automated API tests with assertion and validation logic are implemented.
"""
}

for filename, text in exps.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Created {filename}")
