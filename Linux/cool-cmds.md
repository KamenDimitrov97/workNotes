## grep + sed

Greps for a string -r(recursively) -l(give only file names where it matches)
second part feeds each of the outputs of grep into sed wich removes `mystring` with `mynewstring`

```shell
grep -rl 'mystring' . | xargs sed -i 's/mystring/mynewstring/g'
```

## echo "eyJhdXRocyI6eyJyZWdpc3RyeS5naXRsYWIuY29tL2ZsYXhhbmR0ZWFsL2F1YmVyZ2luZS9wcm90b3R5cGUiOnsidXNlcm5hbWUiOiJnaXRsYWIrZGVwbG95LXRva2VuLTI0MTI1NDQiLCJwYXNzd29yZCI6IlUtYTRuNW84WTJORkQ2Q0ZkNFpvIiwiZW1haWwiOiJrYW1lbi5kaW1pdHJvdkBmbGF4YW5kdGVhbC5jby51ayIsImF1dGgiOiJaMmwwYkdGaUsyUmxjR3h2ZVMxMGIydGxiaTB5TkRFeU5UUTBPbFV0WVRSdU5XODRXVEpPUmtRMlEwWmtORnB2In19fQ==" | base64 -d

decrypts a strung and returns the result


## grep "^PORT=" .env.example | cut -d "=" -f 2 | sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' 

This finds the value of a specific varialble inside a .env file

## cmd history in percentage 

```sh
history | awk '{CMD[$2]++;count++;}END { for (a in CMD)print CMD[a] " " CMD[a]/count*100 "% " a;}' | grep -v "./" | column -c3 -s " " -t | sort -nr | nl |  head -n10
```