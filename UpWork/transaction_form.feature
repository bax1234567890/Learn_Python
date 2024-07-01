Feature: Transaction Form Submission and Payment

Scenario: Submit transaction form and make payment
    Given I navigate to the transaction form page
    When I fill out the transaction form with cashtag, name, and email
#    And I submit the transaction form
#    Then a new window with a QR code appears
#    And I scan the QR code
#    And I navigate to Cashapp with the scanned QR code
#    And I fill "For" with text from the previous page
#    And I fill "Price" with price from the previous page
#    And I make the payment