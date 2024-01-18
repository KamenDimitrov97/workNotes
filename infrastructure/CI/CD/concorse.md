# Description

Concourse is an open-source continuous integration and continuous delivery (CI/CD) platform that allows you to automate your software delivery pipeline. It was designed with a focus on simplicity, reproducibility, and scalability, and provides a declarative syntax for defining your pipeline as code.

At a high level, a Concourse pipeline consists of a series of jobs that define a set of steps that need to be executed to build, test, and deploy your application. Each job can have one or more tasks, which define a set of actions that need to be performed to complete the job.

Concourse also provides various resources such as Git, S3, Docker, and Kubernetes, that allow you to interact with external systems and services from within your pipeline.

One of the key features of Concourse is its ability to enforce a strict separation of concerns between the different stages of your pipeline. This means that your build, test, and deployment stages can all be defined as separate jobs, with well-defined inputs and outputs, which makes it easier to debug and troubleshoot your pipeline.

Overall, Concourse is a powerful, flexible, and easy-to-use CI/CD platform that can help you streamline and automate your software delivery pipeline.

run docker-compose up inside concourse folder dev/github

fly -t ons dp -p berlin
fly -t ons dp -p scrubber
fly -t ons dp -p category
fly -t ons dp -p search

fly -t ons unpause-pipeline -p berlin
fly -t ons unpause-pipeline -p scrubber
fly -t ons unpause-pipeline -p category
fly -t ons unpause-pipeline -p search

# pipeline triggers

    Time-based triggers: Concourse pipelines can be triggered at specific times or intervals using time-based triggers. For example, you can configure a pipeline to run every day at a specific time, or every hour, or every 30 minutes.

    Git repository triggers: Concourse pipelines can be triggered when changes are made to a Git repository. For example, you can configure a pipeline to run when a new commit is pushed to a specific branch or when a new pull request is opened.

    Webhooks: Concourse pipelines can be triggered by webhooks from external services. For example, you can configure a pipeline to run when a new issue is opened on GitHub or when a new build is triggered on Travis CI.

    Manual triggers: Concourse pipelines can be triggered manually by a user with the appropriate permissions. This can be useful for testing or for triggering a deployment when you're ready.

    Resource version changes: Concourse pipelines can be triggered when a new version of a resource is available. For example, you can configure a pipeline to run when a new Docker image is pushed to a Docker image repository or when a new release is published on GitHub.

    Slack commands: Concourse pipelines can be triggered by Slack commands. For example, you can configure a pipeline to run when a user types a specific command in a Slack channel.

    File changes: Concourse pipelines can be triggered when files are added, modified, or deleted in a directory. For example, you can configure a pipeline to run when a new file is added to a specific directory in a file system.

    