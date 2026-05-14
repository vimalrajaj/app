# 15. Implement test automation for REST API endpoints with assertions, validations, and error handling scenarios
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
