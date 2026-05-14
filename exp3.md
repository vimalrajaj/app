# 3. Integrate TestNG with the above test automation
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
