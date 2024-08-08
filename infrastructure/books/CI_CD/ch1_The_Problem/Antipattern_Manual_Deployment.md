# The problem with delivering software

## Antipattern: Deploying Software Manually

- The production of extensive, detailed documentation that describes the
steps to be taken and the ways in which the steps may go wrong
- Reliance on manual testing to confirm that the application is running
correctly
- Frequent calls to the development team to explain why a deployment is
going wrong on a release day
- Frequent corrections to the release process during the course of a release
- Environments in a cluster that differ in their configuration, for example
application servers with different connection pool settings, filesystems with
different layouts, etc.
- Releases that take more than a few minutes to perform
- Releases that are unpredictable in their outcome, that often have to be
rolled back or run into unforeseen problems
- Sitting bleary-eyed in front of a monitor at 2 A.M. the day after the release
day, trying to figure out how to make it work

instead : 


- When deployments aren’t fully automated, errors will occur every time they
are performed. The only question is whether or not the errors are significant.
Even with excellent deployment tests, bugs can be hard to track down.
- When the deployment process is not automated, it is not repeatable or
reliable, leading to time wasted on debugging deployment errors.
- A manual deployment process has to be documented. Maintaining the
documentation is a complex and time-consuming task involving collaboration between several people, so the documentation is generally incomplete
or out-of-date at any given time. A set of automated deployment scripts
serves as documentation, and it will always be up-to-date and complete,
or the deployment will not work.
- Automated deployments encourage collaboration, because everything is
explicit in a script. Documentation has to make assumptions about the
level of knowledge of the reader and in reality is usually written as an aidememoire for the person performing the deployment, making it opaque to
others.
- A corollary of the above: Manual deployments depend on the deployment
expert. If he or she is on vacation or quits work, you are in trouble.
- Performing manual deployments is boring and repetitive and yet needs
significant degree of expertise. Asking experts to do boring and repetitive,
and yet technically demanding tasks is the most certain way of ensuring
human error that we can think of, short of sleep deprivation, or inebriation.
Automating deployments frees your expensive, highly skilled, overworked
staff to work on higher-value activities.
- The only way to test a manual deployment process is to do it. This is often
time-consuming and expensive. An automated deployment process is cheap
and easy to test.
- We have heard it said that a manual process is more auditable than an
automated one. We are completely baffled by this statement. With a manual
process, there is no guarantee that the documentation has been followed.
Only an automated process is fully auditable. What is more auditable than
a working deployment script?