Renderers are a function that takes a task, which can be assumed to have a __workflow__ member of type Workflow, and return a YAML-serializable nested dict structure.

CWL
The default renderer is for the Common Workflow Language. It implements a very small subset of functionality, and is not yet strictly standards compliant. It assumes that all run names can be interpreted in the context of the workflow module's global scope.