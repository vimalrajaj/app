# 9. Create automated test cases for mobile applications using Appium and execute on emulators or real devices
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
