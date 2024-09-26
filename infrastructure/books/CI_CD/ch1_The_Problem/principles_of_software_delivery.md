# Create a Repeatable, Reliable Process for Releasing Software

## Deploying software ultimately involves three things:

1. Provisioning and managing the environment in which your application will
run (hardware configuration, software, infrastructure, and external services).

1. Installing the correct version of your application into it.

1. Configuring your application, including any data or state it requires.

## Automate Almost Everything

List of automations possible is extreemly big.

Try to automate almost everything. 

Always automate gradually not at once.

First always automate build, deploy, tests and release!
Then gradually automate as much as you can of the release cycle.

## Keep Everything in Version Control

Everything I need to release a product should be kept in versioned storage!
That includes but not limited to:
- Documentation
- test scripts
- database creation, upgrade, downgrade and initilization scripts
- deployment scripts
- application stack config scripts
- libraries 
- toolchains
- tech docs

It should be possible for a new team member to sit down at a new workstation,
check out the project’s revision control repository, and run a single command to
build and deploy the application to any accessible environment, including the
local development workstation.

