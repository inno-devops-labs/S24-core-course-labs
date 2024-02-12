# Docker

## Best practices

- Used only trusted base images.
- Specified the images and packages specific versions.
- Kept the images minimal, only with needed functionality.
- Copied only the required files into the containers.
- Used multistage build - created the binary executable in `python` stage and then copied the result into `alpine` container, making the resulting container lighter and not containing the source code.
- Made the executable owned by `root` and not writable.
- Created `myuser` and running the executable using this user.
- Used the linter to assure the file readability and quality.
