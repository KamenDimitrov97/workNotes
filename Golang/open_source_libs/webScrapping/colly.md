
# Link
https://github.com/gocolly/colly

# How to

1. Create a new Go file, e.g., main.go.

2. Add the following code to scrape and print the titles of the latest news articles:

```go
package main

import (
    "fmt"
    "github.com/gocolly/colly/v2"
)

func main() {
    // Create a new collector
    c := colly.NewCollector()

    // On every <a> element which has a class attribute containing "storylink", call the callback
    c.OnHTML("a.storylink", func(e *colly.HTMLElement) {
        fmt.Println("Title:", e.Text)
    })

    // On every <a> element which has a class attribute containing "storylink", call the callback
    c.OnHTML("a.titlelink", func(e *colly.HTMLElement) {
        fmt.Println("Title:", e.Text)
    })

    // Visit the website
    c.Visit("https://news.ycombinator.com/")
}
```