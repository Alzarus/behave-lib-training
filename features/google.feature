Feature: Google

    Feature to access google with selenium webdriver manager

    Scenario Outline: Access Google
        Given we access google website
        When we insert <keywords> to search
        When we click on the search button
        Then we see the results

        Examples: Test
            | keywords             |
            | brasil               |
            | fskfsdfsdlgdsgdsglds |