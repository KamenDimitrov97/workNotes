# Using params for the inputs to a function.
So the input of the
```smk
rule download_data:
  params:
    data: "1, 2, 3, 4, 5, 6, 7"
  output: "file.txt"
  run:
    def download_data(params, output):
        data_list = params.data.split(", ")
        with open(output[0], 'w') as f:
            for item in data_list:
                f.write(f"{item}\n")
  
    download_data(params, output)
```


# Q: How are the rules executed?