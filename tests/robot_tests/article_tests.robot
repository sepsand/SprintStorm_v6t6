*** Settings ***
Resource  resource.robot
Resource  reference_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Add Article With Correct Information
    Go To Add Reference Page
    Choose Reference Type  article
    Set Key  article key
    Set Author  Tester
    Set Title  Article Test
    Set Year  2000
    Set Journal  test journal
    Set Volume  12
    Set Pages  100-200
    Submit Reference
    Add Reference Should Succeed  Article Test

Add Article With Missing Field
    Go To Add Reference Page
    Choose Reference Type  article
    Set Key  article key2
    Set Title  Article Test2
    Set Year  2001
    Set Journal  test journal
    Set Volume  12
    Set Pages  100-200
    Submit Reference
    Add Reference Should Fail For Missing Field  Author

Add Article With Invalid Number Field
    Go To Add Reference Page
    Choose Reference Type  article
    Set Key  article key3
    Set Author  Tester
    Set Title  Article Test2
    Set Year  2001
    Set Journal  test journal
    Set Volume  12
    Set Pages  -12-10
    Submit Reference
    Add Reference Should Fail For Field With Message  pages  Please enter a single page or a page range (eg. 32 or 101-167).