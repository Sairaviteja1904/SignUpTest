Feature: User Sign-up and Login

Scenario: Successful User Registration
    Given the user is on the sign-up page
    When the user enters valid details and clicks on Create an Account button
    Then the user should be redirected to the Account page

Scenario: Sign-Up with Existing Email
    Given the user is on the sign-up page
    When the user enters an email that is already registered
    Then the user should see an error message indicating the email already exists

  Scenario: Sign-Up with Password Mismatch
    Given the user is on the sign-up page
    When the user enters a mismatched password and confirm password
    Then the user should see an error message indicating that passwords do not match

  Scenario: Sign-Up with Invalid Email Format
    Given the user is on the sign-up page
    When the user enters an invalid email format
    Then the user should see an error message indicating invalid email format

  Scenario: Sign-Up with Missing Required Fields
    Given the user is on the sign-up page
    When the user leaves required fields (like emai or password) empty
    Then the user should see an error message indicating which fields are missing

  Scenario: Sign-Up with Weak Password
    Given the user is on the sign-up page
    When the user enters a password that doesn’t meet the criteria
    Then the user should see an error message indicating that the password is weak

  Scenario: Successful User Login
    Given the user is on the login page
    When the user enters correct credentials and clicks the "Log In" button
    Then the user should be redirected to the MyAccount page

  Scenario: Login with Incorrect Credentials
    Given the user is on the login page
    When the user enters incorrect credentials and clicks the "Log In" button
    Then the user should see an error message indicating incorrect credentials

  Scenario: User Logs Out After Logging In
    Given the user is on the login page
    When the user enters correct credentials and clicks the "Log In" button
    Then the user should be redirected to the MyAccount page
    When the user clicks the Sign out button
    Then the user should be Signed out and redirected to the Home page

  Scenario: User Updates Password Using Reset Password
    Given the user is on the login page
    When the user clicks the Forgot Password button
    Then the user should be redirected to Reset Password Page and redirected to the login page
