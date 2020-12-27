# Development Notes

## VS Code

- In order for VS Code to have permissions to open the camera, the editor must be opened from a terminal with permissions.

## Environment

Per recent trouble with Ruby installs on Mac, Python looks for some cryptographic libraries (`libssl.dylib` and `libcrypto.dylib`) in `/usr/local/lib/`. These don't come out of the box with the Darwin install of LibreSSL, so you have to get the latest version of `openssh` from Brew and symlink the required libraries to `/usr/local/lib/`. This is not a great solution because when Brew updates `openssh`, the symlinks will be broken.
