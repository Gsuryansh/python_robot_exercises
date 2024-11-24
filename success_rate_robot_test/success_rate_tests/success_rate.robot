*** Settings ***
Library     libraries/calculate_success_rate.py

*** Variables ***
${log_file_path}    config/bs_log.txt
${success_rate}    30

*** Test Cases ***
Success Rate Test
    [Documentation]    Check if the test result is successful
    ${test_result}     check_success_rate   ${log_file_path}    ${success_rate}
    Should Be True    ${test_result}  
