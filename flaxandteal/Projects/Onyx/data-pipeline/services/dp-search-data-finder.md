# handler

handler recieves kafka msg with topic reindex-requested that provides 

---- get what it provides 

with 

```go
type ReindexRequested struct {
	JobID       string `avro:"job_id"`
	SearchIndex string `avro:"search_index"`
	TraceID     string `avro:"trace_id"`
}
```

1. gets and sends dataset URL and zebedee urls concurrently 

looks like this:
every url is sent one at a time from what I gather below
```go
		err := h.ContentUpdatedProducer.ContentUpdate(ctx, cfg, models.ContentUpdated{
			URI:         publishedIndex.Items[i].URI,
			JobID:       reindexReqEvent.JobID,
			TraceID:     reindexReqEvent.TraceID,
			SearchIndex: reindexReqEvent.SearchIndex,
		})
```

dataset urls look like this:

```go
		defer wgDataset.Done()
		for datasetURL := range datasetURLChan {
			log.Info(ctx, "log extracted dataset urls")
			err := h.ContentUpdatedProducer.ContentUpdate(ctx, cfg, models.ContentUpdated{
				URI:         datasetURL,
				JobID:       reindexReqEvent.JobID,
				TraceID:     reindexReqEvent.TraceID,
				SearchIndex: reindexReqEvent.SearchIndex,
			})
			if err != nil {
				log.Error(ctx, "failed to publish datasets to content update topic", err)
				return
			}
```

QUESTION: Why is the method for dataset msg produce called `logExtractedDatasetURLs` while it produces a kafka msg?
Also why the kafka msg produced includes URI JobID, TraceID, SearchIndex while the one data-extractor expects is 


```go
// ContentPublished provides an avro structure for a Content Published event
type ContentPublished struct {
	URI          string `avro:"uri"`
	DataType     string `avro:"data_type"`
	CollectionID string `avro:"collection_id"`
	JobID        string `avro:"job_id"`
	SearchIndex  string `avro:"search_index"`
	TraceID      string `avro:"trace_id"`
}
```
