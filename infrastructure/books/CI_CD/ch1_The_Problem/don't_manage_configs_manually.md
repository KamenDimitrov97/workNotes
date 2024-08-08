# Antipattern: Manual Configuration Management of Production Environments

Many organizations manage the configuration of their production environments
through a team of operations people. If a change is needed, such as a change to
database connection setting or an increase in the number of threads in a thread
pool on an application server, then it is carried out manually on the production
servers. If a record is kept of such a change, it is probably an entry in a change
management database.
Signs of this antipattern are:
- Having deployed successfully many times to staging, the deployment into
production fails.
- Different members of a cluster behave differently—for example, one node
sustaining less load or taking longer to process requests than another.
- The operations team take a long time to prepare an environment for a
release.
- You cannot step back to an earlier configuration of your system, which
may include operating system, application server, web server, RDBMS, or
other infrastructural settings.
- Servers in clusters have, unintentionally, different versions of operating
systems, third-party infrastructure, libraries, or patch levels.
- Configuration of the system is carried out by modifying the configuration
directly on production systems.

### Instead . . .

All aspects of each of your testing, staging, and production environments,
specifically the configuration of any third-party elements of your system, should
be applied from version control through an automated process.
One of the key practices that we describe in this book is configuration management, part of which means being able to repeatably re-create every piece of infrastructure used by your application. That means operating systems, patch levels,
OS configuration, your application stack, its configuration, infrastructure
configuration, and so forth should all be managed. You should be able to recreate your production environment exactly, preferably in an automated fashion.
Virtualization can help you get started with this.
You should know exactly what is in production. That means that every change
made to production should be recorded and auditable. Often, deployments fail
because somebody patched the production environment last time they deployed,
but the change was not recorded. Indeed it should not be possible to make
manual changes to testing, staging, and production environments. The only way
to make changes to these environments should be through an automated process.
Applications often depend on other applications. It should be possible to see
at a glance exactly what the currently released version of every piece of software is.
While releases can be exhilarating, they can also be exhausting and depressing.
Almost every release involves last-minute changes, such as fixing the database
login details or updating the URL for an external service. There should be a way
of introducing such changes so that they are both recorded and tested. Again,
automation is essential. Changes should be made in version control and then
propagated to production through an automated process.
It should be possible to use the same automated process to roll back to a
previous version of production if the deployment goes wrong.