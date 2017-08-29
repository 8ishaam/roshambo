# Roshambo

## Pre-requisites
* Python 2.7

## How to
* run.py for starting the game (should be executable)
* run_test.py for running unit tests (should be executable)

## Notes
* OS porting effort was done on OS dependent stuff (clear command for instance)
* External library used for test mocking, in test/external_lib
* MVC architecture used
* Finite State Machine approach
* Externalized resources, labels, messages in configuration (conf.json) => Internationalization + Adding other moves prepared

## Remaining items
* Complete UT/coverage --> I have just put basic tests to show that I know how to test/mock ... :)
* The UI is basic, make it better (web ...)
* Adding more languages (English for now)
* Many other features to add (customizing player name/profile ...)
