Feature: Expleo Automation

  Scenario: Verify user could access the website
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And close browser

  Scenario: Verify there is a blue button in the website
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And verify button "1" background color is "blue"
    And close browser

  Scenario: Verify there is a red button in the website
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And verify button "2" background color is "red"
    And close browser

  Scenario: Verify there is a green button in the website
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And verify button "3" background color is "green"
    And close browser

  Scenario: Validate number of rows
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And number of "rows" in the table is "11"
    And close browser

  Scenario: Validate number of columns
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And number of "columns" in the table is "7"
    And close browser

  Scenario: Validate table has no duplicate values
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And validate table has no duplicate values
    And close browser

  Scenario: Validate the table position for specified word
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And validate table position of word "Definiebas3" is "4*4"
    And close browser

  Scenario: Validate the table position for specified word
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And validate table position of word "Phaedrum7" is "8*6"
    And close browser

  Scenario: Validate error is thrown for a word which is not available in table
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And validate error is thrown for word "Phdddrum7" which is not available in table
    And close browser

  Scenario: Verify the presence of answer and highlight it
    Given launch chrome browser
    When navigate to url
    Then verify website is launched successfully
    And verify the presence of answer and highlight it
    And close browser