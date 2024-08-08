# Description

A renderer in `Dewret` is a component that converts internal representations of workflows into specific formats that can be used for different workflow languages e.g a renderer can convert a Dewret workflow into a Common Workflow Language (CWL) format, making it possible to execute the workflow in environments that support CWL.

# Creating a custom renderer

## ReferenceDefinition Class

### Description:
Converts internal python references to a whatever your workflow language format is. 
Modify render method to the format you're using(e.g. CWL). 

QUESTION:
### that's internal python references right?

### Code:
```python
@define
class ReferenceDefinition:
    """JSON-renderable internal reference."""

    source: str

    @classmethod
    def from_reference(cls, ref: Reference) -> "ReferenceDefinition":
        return cls(source=ref.name)

    def render(self) -> dict[str, RawType]:
        return {
            "source": self.source
        }
```

### Requirements:
1. imports:
```python
from dewret.workflow import Reference
from dewret.utils import RawType
```

## StepDefinition Class

### Description:
Converts dewret.workflow steps to JSON, also handles the inputs and outputs.

### Code:
```python
@define
class StepDefinition:
    """JSON-renderable step."""
    name: str
    run: str
    out: dict[str, "CommandInputSchema"] | list[str]
    in_: Mapping[str, ReferenceDefinition | Raw]

    @classmethod
    def from_step(cls, step: Step) -> "StepDefinition":
        return cls(
            name=step.name,
            run=step.task.name,
            out=(
                to_output_schema("out", step.return_type)["fields"]
            ) if attrs_has(step.return_type) else [
                "out"
            ],
            in_={
                key: (
                    ReferenceDefinition.from_reference(param)
                    if isinstance(param, Reference) else
                    param
                ) for key, param in step.arguments.items()
            }
        )

    def render(self) -> dict[str, RawType]:
        return {
            "run": self.run,
            "in": {
                key: (
                    ref.render()
                    if isinstance(ref, ReferenceDefinition) else
                    {"default": ref.value}
                ) for key, ref in self.in_.items()
            },
            "out": flatten(self.out)
        }
```

### Requirements:

1. Imports:
```python
from collections.abc import Mapping
from typing import Union
from dewret.workflow import Raw, step
from attrs import define, has as attrs_has
from dewret.utils import RawType, flatten
```
2. custom [CommandInputSchema](#commandinputschema-class) class created
3. custom [ReferenceDefinition](#referencedefinition-class) class created
4. custom [outputschema](#to-output-schema) method created

## to_json_type method

### Description:

Create a method to convert the python native types to the types of the workflow language you're using.

### Code:
```python
def to_json_type(typ: type) -> str | list[str]:
    if isinstance(typ, UnionType):
        return [to_json_type(item) for item in get_args(typ)]

    if typ == int:
        return "integer"
    elif typ == bool:
        return "boolean"
    elif typ == dict or attrs_has(typ):
        return "object"
    elif typ == list:
        return "array"
    elif typ == float:
        return "number"
    elif typ == str:
        return "string"
    else:
        raise TypeError(f"Cannot render complex type ({typ}) to JSON")
```

### Requirements:
1. Imports:
```python
from typing import Union
from attrs import has as attrs_has
```

## CommandInputSchema class

### Description:
Subclass of `TypedDict` this way you can specify what types of the expectede keys should be.
Basically define what the input schema is going to look like. 

### example: 

```python
input_schema = CommandInputSchema(
    type="object",
    fields={
        "name": CommandInputSchema(type="string"),
        "age": CommandInputSchema(type="integer")
    }
)

```
you can do nested cmdinputschemas -- I think?

```python
input_schema = CommandInputSchema(
    type="object",
    fields={
        "nested_object": CommandInputSchema(
            type="object",
            fields={
                "name": CommandInputSchema(type="string"),
                "age": CommandInputSchema(type="integer")
            }
),
        "age": CommandInputSchema(type="integer")
    }
)
```

### Code:

```python
class CommandInputSchema(TypedDict):
    type: InputSchemaType
    label: str
    fields: NotRequired[dict[str, "CommandInputSchema"]]
    items: NotRequired[InputSchemaType]
```

### Requirements:
1. Define the type for the input schema
```python
# Define the type for input schema
InputSchemaType = Union[str, "CommandInputSchema", list[str], list["InputSchemaType"]]
```
2. Imports:
```python
from typing import TypedDict, NotRequired, Union
```

## CommandOutputSchema class

### Description 
It's basically the same as [commandInputSchema](#commandinputschema-class)
```python
class CommandOutputSchema(CommandInputSchema):
    outputSource: NotRequired[str]
```

## Input output methods

### Description 

This method converts python raw types into the workflow language types you wanted.
Converts python raw types into the desired workflow language types.

### Code:

```python
def raw_to_command_input_schema(label: str, value: RawType) -> InputSchemaType:
    if isinstance(value, dict) or isinstance(value, list):
        return _raw_to_command_input_schema_internal(label, value)
    else:
        return to_json_type(type(value))
def to_output_schema(label: str, typ: type[RawType | AttrsInstance], output_source: str | None = None) -> CommandOutputSchema:
    if attrs_has(typ):
        output = CommandOutputSchema(
            type="object",
            label=label,
            fields={
                field.name: to_output_schema(field.name, field.type)
                for field in fields(typ)
            },
        )
    else:
        output = CommandOutputSchema(
            type=to_json_type(typ),
            label=label,
        )
    if output_source is not None:
        output["outputSource"] = output_source
    return output

def _raw_to_command_input_schema_internal(label: str, value: RawType) -> CommandInputSchema:
    typ = to_json_type(type(value))
    structure: CommandInputSchema = {"type": typ, "label": label}
    if isinstance(value, dict):
        structure["fields"] = {
            key: _raw_to_command_input_schema_internal(key, val)
            for key, val in value.items()
        }
    elif isinstance(value, list):
        typeset = set(get_args(value))
        if not typeset:
            typeset = {type(item) for item in value}
        if len(typeset) != 1:
            raise RuntimeError(
                "For JSON, an input array must have a consistent type, "
                "and we need at least one element to infer it, or an explicit type hint."
            )
        structure["items"] = to_json_type(typeset.pop())
    return structure
```

### Requirements:
1. custom [CommandInputSchema](#commandinputschema-class) class created
2. InputSchemaType
3. custom [to_json_type](#to_json_type-method) method created
4. Imports:
```python:
from typing import TypedDict, NotRequired, get_args, Union, cast, Any
from attrs import define, has as attrs_has, fields, AttrsInstance
```


## InputsDefinition class

### Description: 

Actual inputs object that's going to do the raw value input conversions of the tasks. 

### Code:

```python
@define
class InputsDefinition:
    inputs: dict[str, "CommandInputParameter"]

    @define
    class CommandInputParameter:
        type: InputSchemaType
        label: str

    @classmethod
    def from_parameters(cls, parameters: list[Parameter[RawType]]) -> "InputsDefinition":
        return cls(
            inputs={
                input.__name__: cls.CommandInputParameter(
                    label=input.__name__,
                    type=raw_to_command_input_schema(
                        label=input.__name__,
                        value=input.__default__
                    )
                ) for input in parameters
            }
        )

    def render(self) -> dict[str, RawType]:
        return {
            key: {
                "type": cast(RawType, input.type),
                "label": input.label
            } for key, input in self.inputs.items()
        }
```

### Requirements:

1. custom [InputSchemaType](#commandinputschema-class)
2. custom [raw_to_command_input_schema](#input-output-methods)
3. imports:
```python
from dewret.workflow import Reference, Raw, Workflow, Step, StepReference, Parameter
from dewret.utils import RawType, flatten
from attrs import define, has as attrs_has, fields, AttrsInstance
```

## OutputsDefinition class

### Description:

Actual outputs object that's going to do the raw value output conversions of the tasks. 
Basically the same as [InputsDefinition class](#inputsdefinition-class)

### Code:

```python
@define
class OutputsDefinition:
    outputs: dict[str, "CommandOutputSchema"]

    @classmethod
    def from_results(cls, results: dict[str, StepReference[Any]]) -> "OutputsDefinition":
        return cls(
            outputs={
                key: to_output_schema(result.field, result.return_type, output_source=result.name)
                for key, result in results.items()
            }
        )

    def render(self) -> dict[str, RawType]:
        return {
            key: flatten(output) for key, output in self.outputs.items()
        }
``` 

## WorkflowDefinition class

### Description:

From a dewret workflow object renders the code for the workflow language you've built.

### Code:

```python
@define
class WorkflowDefinition:
    steps: list[StepDefinition]
    inputs: InputsDefinition
    outputs: OutputsDefinition

    @classmethod
    def from_workflow(cls, workflow: Workflow) -> "WorkflowDefinition":
        return cls(
            steps=[
                StepDefinition.from_step(step)
                for step in workflow.steps
            ],
            inputs=InputsDefinition.from_parameters([
                reference.parameter for reference in
                workflow.find_parameters()
            ]),
            outputs=OutputsDefinition.from_results({
                workflow.result.field: workflow.result
            } if workflow.result else {})
        )

    def render(self) -> dict[str, RawType]:
        return {
            "version": "1.0",
            "class": "Workflow",
            "inputs": self.inputs.render(),
            "outputs": self.outputs.render(),
            "steps": {
                step.name: step.render()
                for step in self.steps
            }
        }

# Takes a dewret workflow object and creates a workflow based on the workflow language.  
def render(workflow: Workflow) -> str:
    """Render to a JSON string."""
    return json.dumps(WorkflowDefinition.from_workflow(workflow).render(), indent=2)

```

### Requirements:
1. All of the above
2. Imports:
```python
import json
from attrs import define, has as attrs_has, fields, AttrsInstance
from collections.abc import Mapping
from typing import TypedDict, NotRequired, get_args, Union, cast, Any
from types import UnionType

from dewret.workflow import Reference, Raw, Workflow, Step, StepReference, Parameter
from dewret.utils import RawType, flatten
```
## This is everything we need to successfully write a renderer for a specific workflow language.
