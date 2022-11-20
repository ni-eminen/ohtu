*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***

Register With Valid Username And Password
    Register With Credentials  kella  Kella123
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Register With Credentials  k  Kella123
    Title Should Be  Register

Register With Valid Username And Too Short Password
    Register With Credentials  kella  Kel1
    Title Should Be  Register

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Input Text  username  kella
    Input Text  password  kella123
    Input Text  password_confirmation  notpassword123
    Click Button  Register
    Title Should Be  Register

Login After Successful Registration
    Register With Credentials  kella  Kella123
    Go To Login Page
    Set Username  kella
    Set Password  Kella123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Register With Credentials  k  Kella123
    Title Should Be  Register
    Go To Login Page
    Set Username  k
    Set Password  Kella123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Create User And Go To Login Page
    Create User  kalle  kalle123

Register With Credentials
    [Arguments]  ${username}  ${password}
    Go To Register Page
    Input Text  username  ${username}
    Input Text  password  ${password}
    Input Text  password_confirmation  ${password}
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}