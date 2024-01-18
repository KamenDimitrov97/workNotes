<h1>Meeting with Linden</h1>

Legend:
- All reviews for the NLP PRs are finished except dp-search-api as we've discussed in this weeks standups
- A/B - split testing one control group and one group will test the new feature 
- APIs configurations - in order to do the split testing we need to configure the apis in production to make sure NLP can be toggled on and off for the two groups 
maybe separate testing endpoint or a query parameter(Like the one I was told to remove before merge :D :D )
- Sandbox testing - ensuring the NLP feature is working as intended which includes errors and some basic manual testing 
- Staging testing - performance testing - which will include resource management and speed
- NLP toggled off - will be toggled off until all testing phases are complete

Steps for A/B testing and ending the project:
1. Merge all current NLP PRs - Linden will do today - without dp-search-api as I need to make chagnes there
2. We'll move everything into staging and production - Linden will hopefully do before christmass as long as it passes all automated testing and ci/cd stuff 
3. NLP will be toggled off in prod until we've done sandbox testing
3. Sandbox testing 
4. !!! Configuration is needed to start A/B testing in production - Linden doesn't know who needs to do those configurations 
5. A/B testing will be started by their analytical teams

Questions:

1. @philtweir was there any mention of the configuration of the NLP APIs in your calls with Alun.
Alun is off today so Linden can't talk to him - but will do tomorrow 
2. Who IS going to do the configurations?
3. Linden wants documents that NLP works - like the ones we have from Alana and Sarah on the Alpha
I've also asked him if my documents on testing are okay (csv, lot's of testing queries nothing special) he said Yes, but considering they're of mixed results 
I want your input on if I should send them or not @philtweir `I'm blocked on should I send it to Linden or not` - this is important


Timeframe: 
We aggreed we'd have a better idea on the standup next week but if they're doing the configurations Linden said maybe till the end of january(DOES NOT INCLUDE A/B Testing) - whichpoint I mention it'll be very hard to do anything if we have 1-2 weeks to figure shit out so we aggreed it'll be discussed again tuesday standup 19th

We're trying to get stuff in prod possibly until 21st of Dec -- not confirmed!

I'll work on dp-search-api to speed things up 
