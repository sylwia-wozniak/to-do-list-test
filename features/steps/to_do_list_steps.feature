Feature: user adds task to do
  Scenario Outline: user types a task's name and clicks 'add'
    Given user is on https://sylwia-wozniak.github.io/works/todolist_own/
    When user types a <task_name>
    And user clicks 'add'
    Then <task_name> is created

    Examples:
    |task_name|
    |write a test|
    |buy a coffee|

  Scenario: user lefts empty input task and clicks 'add'
    Given user is on https://sylwia-wozniak.github.io/works/todolist_own/
    When user clicks 'add'
    Then user sees an alert - empty input

  Scenario Outline: user types too long task's name and click 'add'
    Given user is on https://sylwia-wozniak.github.io/works/todolist_own/
    When user types <too_long_task_name>
    Then user sees an alert - too long name

    Examples:
    |too_long_task_name|
    |write a test and write a test and write a test and write a test and write a test and write a test and write and write for the rest of my life|
