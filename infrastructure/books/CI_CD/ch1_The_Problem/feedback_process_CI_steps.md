# Every Change Should Trigger the Feedback Process

## Working application decomposition

A working software application can be usefully decomposed into four components:
executable code, configuration, host environment, and data. 

### Source code

Executable code changes when a change is made to the source code.
Every time a change is made to the source code, the resulting binary must be built and
tested. This is known as Continues Integration.
Code should be the same across all environments.
Never rebuilt binnary IN the pipeline!

### Configuration

Anything that changes between environments should be captured as configuration information.

### Host env
If the environments the application is to be deployed into change, the whole
system should be tested with the changes to the environment.

### Data
Finally, if the structure of the data changes, this change must also be tested. 


## Automated Feedback

What is the feedback process? It involves testing every change in a fully automated fashion, as far as possible. The tests will vary depending on the system,
but they will usually include at least the following checks.

- The process of creating the executable code must work. This verifies that
the syntax of your source code is valid.

- The software’s unit tests must pass. This checks that your application’s
code behaves as expected.

- The software should fulfill certain quality criteria such as test coverage and
other technology-specific metrics.

- The software’s functional acceptance tests must pass. This checks that your
application conforms to its business acceptance criteria—that it delivers
the business value that was intended.

- The software’s nonfunctional tests must pass. This checks that the application performs sufficiently well in terms of capacity, availability, security, and so on to meet its users’ needs. - maybe Chaos Engineering?

- The software must go through exploratory testing and a demonstration to
the customer and a selection of users. This is typically done from a manual
testing environment. In this part of the process, the product owner might
decide that there are missing features, or we might find bugs that require
fixing and automated tests that need creating to prevent regressions.

# The Feedback Must Be Received as Soon as Possible

## Commit stage of a CI pipeline

1. They run fast.

1. They are as comprehensive as possible—Mst cover more than
75%+ of the codebase, so that when they pass, we have a good level
of confidence that the application works.

1. If any of them fails, it means our application has a critical fault and should
not be released under any circumstances. That means that a test to check
the color of a UI element should not be included in this set of tests.

1. They are as environment-neutral as possible—that is, the environment does
not have to be an exact replica of production, which means it can be simpler
and cheaper

On the other hand, the tests in the later stages have the following general
characteristics.
1. They run more slowly and therefore are candidates for parallelization.

1. Some of them may fail, and we may still choose to release the application
under some circumstances (perhaps there is a critical fix in the release
candidate that causes the performance to drop below a predefined
threshold—but we might make the decision to release anyway).

1. They should run on an environment that is as similar as possible to production, so in addition to the direct focus of the test they also test the
deployment process and any changes to the production environment.