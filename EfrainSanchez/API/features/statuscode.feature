Feature: API
  Scenario:
    Given I have connection to "http://www.google.com.bo"
    When I "GET"
    Then I receive status code 200
