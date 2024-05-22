# Dumb way
```bash
sudo ls /var/lib/docker/containers ## to check which container u want to remove the logs of 
sudo nano /var/lib/docker/containers/441f7b109db0c5c752c177b4899ee85cd86254929aa87254fca6627dd5a7d2c8/441f7b109db0c5c752c177b4899ee85cd86254929aa87254fca6627dd5a7d2c8-json.log
# Then go ctrl + shift + end
# ctrl + k 
```

# Easier way 

```bash
sudo truncate -s 0 $(docker inspect --format='{{.LogPath}}' name-of-container-or-id)
```
