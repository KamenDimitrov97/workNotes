Once the application is deployed into staging, it is common for new bugs to
be found. Unfortunately, there is often no time to fix them all because the deadline
is fast approaching and, at this stage of the project, deferring the release date is
unacceptable. So the most critical bugs are hurriedly patched up, and a list of
known defects is stored by the project manager for safekeeping, to be deprioritized
when work begins on the next release.
Sometimes it can be even worse than this. Here are a few things that can
exacerbate the problems associated with a release.

- When working on a new application, the first deployment to staging is
likely to be the most troublesome.
- The longer the release cycle, the longer the development team has to make
incorrect assumptions before the deployment occurs, and the longer it will
take to fix them.
- In large organizations where the delivery process is divided between different
groups such as development, DBA, operations, testing, etc., the cost of
coordination between these silos can be enormous, sometimes stalling the
release process in ticketing hell. In this scenario, developers, testers, and
operations personnel are constantly raising tickets (or sending emails) to
8 Chapter 1 The Problem of Delivering Software
each other to perform any given deployment—and worse, to resolve
problems that arise during deployment.
- The bigger the difference between development and production environments, the less realistic are the assumptions that have to be made during
development. This can be difficult to quantify, but it’s a good bet that
if you’re developing on a Windows machine and deploying to a Solaris
cluster, you are in for some surprises.
- If your application is installed by users or contains components that are,
you may not have much control over their environments, especially outside
of a corporate setting. In this case, a great deal of extra testing will be
required.

### Instead . . .

The remedy is to integrate the testing, deployment, and release activities into the
development process. Make them a normal and ongoing part of development so
that by the time you are ready to release your system into production there is
little to no risk, because you have rehearsed it on many different occasions in a
progressively more production-like sequence of test environments. Make sure
everybody involved in the software delivery process, from the build and release
team to testers to developers, work together from the start of the project.
We are test addicts, and the extensive use of continuous integration and continuous deployment, as a means of testing both our software and our deployment
process, is a cornerstone of the approach that we describe.