# Instruction on how to use these tests

This project consists of set of Selenium auto tests written as a part of a [test assignment](https://docs.google.com/document/d/1O9JckI3mcFP1og-YrLL46Rp5VsFXZs81DALwZWv6_48/edit). The purpose of tests is checking the main features of [News360](https://news360.com) "Sign in with email" and "Sign up with email" functionality.

## Requirements and how to run tests

The tests are written in Python, so Python 2.7.* is required to run it. In order to do it effectively the following packages are required: **selenium** and **selenose**.
Therefore, the next steps will provide the fastest way to run the tests:
 1. Download the **Tests** folder somewhere on the disc and unzip it.
 2. Install **pip** in case it was not installed previously.
 3. Execute ```pip install selenium selenose```
 4. Execute ```cd /path/to/folder/Tests```
 5. Run the tests using the following command: ```nosetests -w ./ -v``` (Option -w is followed by the path to folder there Nose should search for tests. Option -v adds docstring of the main test method to log thus making log more readable)

Note that current version of tests tuned for working with local version of WebDriver that will be provided by **selenium** package so you don't have to start Selenium server manually. Ability to work with remote WebDriver server will be added later.

Next step is defining the set of tests to be run. Taking into consideration that all the tests are simple and can be run very fast, I consider that by default all the tests will be executed in one test set. The way to run such set is described above on the step 5.
In case individual test or some subset of whose test set is required to be executed, it can be done with the following command: 
 * ```nosetests --tests=TestResetPassEmpty.py,TestLogInLink.py -v```

In this particular case the set to be run consists of 2 cases: TestResetPassEmpty and TestLogInLink. More detailed description of Nose parameters can be found [here](https://nose.readthedocs.org/en/latest/man.html).

## Integration with CI services and parallel run of the tests

The easiest way to integrate these tests in the existing continues integration and delivery process can be implemented by performing the steps below:
 1. Copy tests to the server there each new build of application under test is deployed after building.
 2. On that server set up environment that met requirements provided above.
 3. Add build step "Execute shell" (Jenkins is used as CI server example here) right after the deployment step in the existing build procedure.
 4. Set ```cd /path/to/folder/Tests && nosetests -w ./ -v``` as the command to execute.

Since current test set is small enough to be run locally on the deployment server, implementing above steps will require the least amount of efforts and will give first results fast. After that the next steps like setting up separated Selenium server or even using server farm for automated testing might be implemented. Detailed instruction on integrating  Selenium-based tests with Jenkins can be found [here](http://learn-automation.com/selenium-integration-with-jenkins/)
Also, even this basic configuration can be set up to reduce test execution time by running tests in parallel.
To run several tests simultaneously use the following command: 
 * ```nosetests -w ./path/to/folder/Tests -v --processes=<number of processes run in parallel> --process-timeout=<seconds>```

For instance, on the virtual server with 1 CPU running 2 streams of tests saved about 30% of time comparing to consequent test execution.

## Test implementation details

First, tests are developed in a way so that they can be executed absolutely independently both as a part of the set and individually. Secondly, they are implemented with the Page Object pattern in mind in order to improve maintainability and despite its minor violations already introduced in code, further development also should follow this pattern.
In **test_support** package you may find files *locators.py* and *pages.py* that provide list of used locators and actions available on pages involved in tests.
In addition, please pay attention to the test filename pattern - in order to be discoverable by Nose, framework title of these files must be started with "Test". The same approach is used in naming of the main method of each test - it is started with "test_" in order to allow showing test docstring in the output log.
