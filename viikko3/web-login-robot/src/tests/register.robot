*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  teemu
    Set Password  teemu123
    Set Password Confirmation  teemu123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  teemu123
    Set Password Confirmation  teemu123
    Submit Credentials
    Register Should Fail With Message  Minimum length of username is 3 characters

Register With Valid Username And Too Short Password
    Set Username  matti
    Set Password  mat123
    Set Password Confirmation  mat123
    Submit Credentials
    Register Should Fail With Message  Minimum length of password is 8 characters

Register With Nonmatching Password And Password Confirmation
    Set Username  marko
    Set Password  marko123
    Set Password Confirmation  marko1233
    Submit Credentials
    Register Should Fail With Message  Password does not match password confirmation

Login After Successful Registration
    Set Username  teemu
    Set Password  teemu123
    Set Password Confirmation  teemu123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  teemu
    Set Password  teemu123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Set Username  te
    Set Password  teemu123
    Set Password Confirmation  teemu123
    Submit Credentials
    Register Should Fail With Message  Minimum length of username is 3 characters
    Go To Login Page
    Set Username  te
    Set Password  teemu123
    Submit Credentials Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
