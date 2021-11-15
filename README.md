# wallpapr
Downloads a random picture from Unsplash and updates the desktop wallpaper every hour.

## Prerequisite
- [GNOME](https://www.gnome.org/) Desktop environment.
- [Make](https://www.gnu.org/software/make/)
- [Python 3](https://www.python.org/)

# Setup
1. [Register](https://unsplash.com/documentation#creating-a-developer-account) an Unsplash app and get the secret key and access key.
2. Export the secret key (as `UNSPLASH_SECRET_KEY`) and access key (as `UNSPLASH_ACCESS_KEY`).
```bash
$ export UNSPLASH_SECRET_KEY="secret_key"
$ export UNSPLASH_ACCESS_KEY="access_key"
```
> Note: You can add these command at the end of ~/.profile to export it globally for the current user.
> This is required in the cli.
3. Clone this repository.
```bash
$ git clone https://github.com/silwalanish/wallpapr.git
```
4. Change directory into `wallpapr`.
```bash
$ cd wallpapr
```
5. Build the project.
```bash
$ make build
```
6. Install the project.
```bash
$ make install
```

# Usage
```bash
$ wallpapr [-h] [-c] [-s] [-p {unsplash}]

optional arguments:
  -h, --help            show this help message and exit
  -c, --get-current-path
                        Get the current background path.
  -s, --only-set-current
                        Set the current background without downloading.
  -p {unsplash}, --image-provider {unsplash}
                        Set the image provider to use.
```

# Uninstalling
1. Run uninstall script.
```
$ make uninstall
```
2. Clean up.
```bash
$ cd ..
$ rm -rf wallpapr
```

# License
[MIT](./LICENSE)
