*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  pekka123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Minimum length of username is 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  matti  mat123
    Output Should Contain  Minimum length of password is 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  teemu  teemuncorner
    Output Should Contain  Password cannot contain only normal letters a-z

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
