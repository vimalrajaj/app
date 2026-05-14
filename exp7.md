# 7. Design and implement Page Object Model (POM) framework for Selenium test automation with multiple test scripts
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
