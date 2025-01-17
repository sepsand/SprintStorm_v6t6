*** Settings ***
Resource  resource.robot

*** Keywords ***
Add Reference Should Succeed
    View Reference Page Should Be Open
    [Arguments]  ${title}
    Page Should Contain  ${title}

Add Reference Should Fail For Field With Message
    Add Reference Page Should Be Open
    [Arguments]  ${field}  ${message}
    ${title_error}  Get Element Attribute  id=${field}  title
    Should Be Equal  ${title_error}  ${message}

Add Reference Should Fail For Missing Field
    Add Reference Page Should Be Open
    [Arguments]  ${field}
    Element Should Be Visible  css=input#${field}:required:invalid

Choose Category Type
    [Arguments]  ${type}
    Select From List By Value  id=category  ${type}
    
Submit Reference
    Click Button  Add reference

Set Key
    [Arguments]  ${key}
    Input Text  key  ${key}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}

Set Address
    [Arguments]  ${address}
    Input Text  address  ${address}

Set Journal
    [Arguments]  ${journal}
    Input Text  journal  ${journal}

Set Volume
    [Arguments]  ${volume}
    Input Text  volume  ${volume}

Set Pages
    [Arguments]  ${pages}
    Input Text  pages  ${pages}