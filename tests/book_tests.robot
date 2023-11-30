*** Settings ***
Resource  resource.robot
Resource  reference_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Book With Correct Information
    Go To Add Reference Page
    Choose Reference Type  book
    Set Key  book key
    Set Author  Tester
    Set Title  Book Test
    Set Year  2000
    Set Publisher  testpublisher
    Submit Reference
    Add Reference Should Succeed  Book Test