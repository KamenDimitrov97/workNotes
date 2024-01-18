Helmfile:

Helmfile is a declarative configuration tool for deploying and managing Kubernetes applications using Helm charts. It allows you to define and manage multiple Helm releases and their configurations in a single YAML file, simplifying the deployment process and providing version-controlled infrastructure as code.

Common Helmfile Commands:

1. `helmfile apply`: Deploys or updates Helm releases based on the configurations defined in the Helmfile.
1. `helmfile diff`: Shows a diff of the intended changes to be applied to the Kubernetes cluster without actually deploying them.
1. `helmfile sync`: A combination of helmfile diff and helmfile apply, showing the diff and then applying changes if approved.
1. `helmfile destroy`: Deletes all the Helm releases defined in the Helmfile.
1. `helmfile template`: Generates Kubernetes manifest files without applying them to the cluster. Useful for verifying rendered templates.
1. `helmfile lint`: Checks the syntax and structure of the Helmfile and the Helm charts it references.
1. `helmfile repos`: Lists configured Helm repositories.
1. `helmfile status`: Displays the status of Helm releases defined in the Helmfile.
1. `helmfile logs`: Fetches the logs for a specified release.
1. `helmfile list`: Lists all the releases defined in the Helmfile.