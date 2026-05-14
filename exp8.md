# 8. Perform API testing using REST Assured and generate HTML test reports with extent reports
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
