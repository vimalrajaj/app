# 2. Automate the testing of e-commerce applications using Selenium
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
