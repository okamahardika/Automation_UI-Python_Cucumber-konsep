Feature: Searching ebay
    Scenario: Product showing while searching
    Given launch chrome browser
    When open ebay homepage
    And click shop by category
    And click cellphone and accesoriss
    And click cellphone & smartphone
    Then close browser