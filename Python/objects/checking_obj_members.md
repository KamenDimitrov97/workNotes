```python
from module import construct

result = increment(num=3)
workflow = construct(result)
print(dir(workflow))
print(dir(workflow.steps[0].task))
print(workflow.steps[0].task.name)
print(workflow.steps[0].task.run)
```