## Generate
```sh
gpg --full-generate-key
```

## List
```sh
gpg --list-keys
```

## Export a Public Key:
```sh
gpg --armor --export <key-id>
```
This exports the public key in ASCII-armored format for sharing. Replace <key-id> with your specific key ID.

## Export a Private Key (use carefully):
```sh
gpg --armor --export-secret-key <key-id>
```
This exports the private key. Be very cautious when doing this, as private keys should be kept secure.

## Import a Public Key:
```sh
gpg --import <public-key-file>
```
This imports a public key from a file into your keyring.

## Delete a Public Key:
```sh
gpg --delete-key <key-id>
```
This removes a public key from your keyring.

## Delete a Private Key:
```sh
gpg --delete-secret-key <key-id>
```
This removes a private key from your keyring.

## Edit a Key (for adding/removing subkeys, changing expiration, etc.):
```sh
gpg --edit-key <key-id>
```
Encrypting and Decrypting Data

## Encrypt a File with a Public Key:
```sh
gpg --encrypt --recipient <recipient-email> <file>
```
This encrypts the file for the recipient whose public key you have.

## Decrypt a File with Your Private Key:
```sh
gpg --decrypt <file.gpg>
```
This decrypts a file that was encrypted with your public key.

## Encrypt a File Symmetrically (with a passphrase):
```sh
gpg --symmetric <file>
```
This encrypts the file with a passphrase for symmetric encryption (useful when you don’t want to use a public/private key).

## Decrypt a Symmetrically Encrypted File:
```sh
gpg --decrypt <file.gpg>
```
You'll be prompted to enter the passphrase used to encrypt the file.

Signing and Verifying Data
## Sign a File (Cleartext Signature):
```sh
gpg --clearsign <file>
```
This creates a cleartext signature for the file, keeping the content readable.

## Sign a File (Detached Signature):
```sh
gpg --detach-sign <file>
```
This creates a detached signature, meaning the signature is stored in a separate file.

## Verify a Signature:
```sh
gpg --verify <signature-file> <file>
```
This verifies the integrity of a signed file.

Trust and Key Management
## Set Key Trust Level:
```sh
gpg --edit-key <key-id>
```
```sh
gpg> trust
```
This allows you to set the trust level of a specific key (e.g., how much you trust a key).

## Refresh Public Keys:
```sh
gpg --refresh-keys
```
This refreshes all public keys from the key servers.

## Search for a Key on a Keyserver:
```sh
gpg --search-keys <email>
```
This searches for a public key on a keyserver by email or key ID.

## Receive a Key from a Keyserver:
```sh
gpg --recv-keys <key-id>
```
This retrieves a public key from the keyserver and adds it to your keyring.

Exporting and Importing Keyrings
## Export All Public Keys to a File:
```sh
gpg --armor --export > public-keys.asc
```
This exports all public keys from your keyring into a file.

## Export All Private Keys to a File (Use with Caution):
```sh
gpg --armor --export-secret-keys > private-keys.asc
```
This exports all private keys into a file. Keep this file safe.

## Import a Keyring:
```sh
gpg --import <keyring-file.asc>
```
This imports all keys from a given keyring file.

Keyservers and Key Handling
## Send Your Public Key to a Keyserver:
```sh
gpg --send-keys <key-id>
```
This uploads your public key to a keyserver.

## Set the Default Keyserver:
```sh
gpg --keyserver <server-url>
```
## This sets a specific keyserver (like hkp://keys.gnupg.net) for sending/receiving keys.

Revoking a Key
## Generate a Revocation Certificate
```sh
gpg --output revoke.asc --gen-revoke <key-id>
```
This generates a revocation certificate in case you need to invalidate a key in the future.
Other Useful Commands
## Check Fingerprint of a Key:
```sh
gpg --fingerprint <key-id>
```
This shows the fingerprint of a specific key, useful for verifying the authenticity of a key.

## Change Passphrase of a Private Key:
```sh
gpg --edit-key <key-id>
```
```sh
gpg> passwd
```
This allows you to change the passphrase of your private key.

```sh
## Backup Your GPG Keys: To backup both public and private keys:
```
```sh
gpg --armor --export > public-keys-backup.asc
```
```sh
gpg --armor --export-secret-keys > private-keys-backup.asc
```
