*** Settings ***
Resource    ../keywords/NasaApiKeywords.robot
Library     libraries/utility/utils.py



*** Variables ***
${date-min}=    2023-01-01    
${date-max}=    2023-01-02

*** Test Cases ***
Verify API Response Status Code and match count and data
    [Documentation]    Verify that the API response status code is 200 and count and length of data field in response matches.
    ${status_code}  ${response}=    Get CAD Data
    Should Be Equal As Numbers    ${status_code}    200
    ${status}=    utils.match_count_and_data    ${response}
    Log To Console    status is ${status}
    Should Be True    ${status}



Verify API Returns Data For Date Range
    [Documentation]    Verify that the API returns data for a specific date range
    ${params}=    Create Dictionary    date-min=${date-min}     date-max=${date-max} 
    ${status_code}  ${response}=    Get CAD Data    params=${params}
    Should Be Equal As Numbers    ${status_code}    200
    ${status}=    utils.verify_data_in_date_range    ${response}    ${date-min}    ${date-max}
    Should Be True    ${status}
    
