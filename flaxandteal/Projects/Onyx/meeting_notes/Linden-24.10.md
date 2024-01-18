Had the conversation with Linden about dp-search-api
and he says it looks good but it's practice in ONS that depednencies live elsewhere (berlin, scrubber a/u)
either dp-api-clients-go or in a separate repo which sounded very similar to the nlp_hub I spent some time writing

philtweir martin I told him I should consult with team first as we did had something like this in the beginning

As for the feature flag I've added should be changed to a config variable
and remove the nlp hub endpoint I added for testing purposes myself and change it to debug level logs