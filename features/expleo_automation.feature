Feature: Expleo Automation

  Scenario: Verify user could access the website
    Given launch chrome browser
    When open DOM website
    Then verify DOM website is launched successfully
    And close browser