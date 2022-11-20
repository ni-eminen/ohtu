*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  newwww  new123123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  asdfasdf123
    Output Should Contain  Error

Register With Valid Username And Too Short Password
    Input Credentials  asdfasdf  a1
    Output Should Contain  Error

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  asdfa  asdfasdfs
    Output Should Contain  New user registered

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123
    Input New Command