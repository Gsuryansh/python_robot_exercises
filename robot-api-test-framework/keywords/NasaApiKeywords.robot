*** Settings ***
Library    libraries.nasa_api_library.NasaApiLibrary




*** Keywords ***
    

Get CAD Data
    [Arguments]    ${params}=None
    ${response}    get_data    ${params}
    Return From Keyword    ${response}


    

