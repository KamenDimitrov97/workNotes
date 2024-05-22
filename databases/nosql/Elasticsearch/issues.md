# Must terminate file with new line error 
```bash
kamen@MiWiFi-R4A-srv:~/dev/work/github/es-pipeline/es/es-pipeline/dp-search-data-importer/cmd/producer$ curl -XPUT "http://localhost:9200/ons/_bulk" -H "Content-Type: application/json" -d @data.json
```
```json
{
    "error": {
        "root_cause": [
            {
                "type": "illegal_argument_exception",
                "reason": "The bulk request must be terminated by a newline [\\n]"
            }
        ],
        "type": "illegal_argument_exception",
        "reason": "The bulk request must be terminated by a newline [\\n]"
    },
    "status": 400
}
```
You have to use the --data-binary flag instead of -d flag 