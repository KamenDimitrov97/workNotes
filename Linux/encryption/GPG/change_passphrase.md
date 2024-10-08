# Steps to Change Your GPG Key Passphrase:

## List Your Private Keys: First, find the key ID of the private key you want to change the passphrase for by listing your private keys:
```sh
gpg --list-secret-keys
```

## Edit the Key:
```sh
gpg --edit-key <key-id>
```

## For example:
```sh
gpg --edit-key ABCDEFGH12345678
```

## Enter the Passphrase Command:
```sh
passwd
```

## Enter Your Current and New Passphrase:

You will be prompted to enter your current passphrase.
After that, you can enter your new passphrase.

## Save and Exit:
```sh
save
```
This will save your changes and exit the GPG key editing mode.
