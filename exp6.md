# 6. Setup a continuous integration pipeline using Jenkins and execute automated test cases on every code commit
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
