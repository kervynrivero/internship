Feature:Scenario 5 of the assignment

  Scenario: User can change the language from the page
    Given  Open the sign-in page
    When Log in to the page, email: kervynriveromujica@gmail.com password: k21471215
    Then Change the language of the page to russian
    Then Verify the language has changed to russian
