# -- FILE: features/example.feature
Feature: Ladder Logic
	As a Challenger
	When i win
	I want to reorder the list so i take the place of the victim and the list is reordered accordingly

  Scenario: Beat a player above 
    Given i am below another player
    When i beat that player above me
    Then i take their position

  Scenario: Beat a player below
    Given i am above another player
    When i beat that player below me
    Then nothing happens

  Scenario: Higher ranked players unaffected
    Given i am ranked above the highest ranked player
    When a match occurs
    Then nothing happens to me

  Scenario: Players unaffected within the sandwich
    Given i am ranked inbetween the active players
    When the higher ranked active player wins
    Then nothing happens to me

  Scenario: Players affected within the sandwich
    Given i am ranked inbetween the active players
    When the lower ranked active player wins
    Then my rank decreases by 1 position

  Scenario: Players below the lowest ranking player
    Given i am ranked below the lowest active players
    When a match occurs
    Then nothing happens to me

  Scenario: if the higher ranked player loses
    Given i am higher ranked of the active players
    When i lose to a lower ranked player
    Then my rank decreases by 1 position

