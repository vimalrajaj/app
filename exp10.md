# 10. Implement data-driven testing using Excel/CSV files and execute parameterized test cases with TestNG
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
