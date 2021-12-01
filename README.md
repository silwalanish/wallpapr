# wallpapr
Downloads a random picture from Unsplash and updates the desktop wallpaper every hour.

## Prerequisite
- [GNOME](https://www.gnome.org/) Desktop environment.
- [Make](https://www.gnu.org/software/make/)
- [Python 3](https://www.python.org/)

# Setup
1. Follow the setup step for the [image provider](#image-providers) of your choice.
> Note: Currently only [`unsplash`](#unsplash) is supported as image provider.
2. Clone this repository.
```bash
$ git clone https://github.com/silwalanish/wallpapr.git
```
3. Change directory into `wallpapr`.
```bash
$ cd wallpapr
```
4. Build the project.
```bash
$ make build
```
5. Install the project.
```bash
$ make install
```

# CLI Usage
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

# Configuring wallpapr
The configurations is available at `~/.config/wallpapr/wallpapr.json`.

## Configuration
| Property | Description | Type | Default |
| :--- | :--- | :---: | :---: |
| `width` | Hints the width of the image to download from the selected `image_provider`. | Number | 1360 |
| `height` | Hints the height of the image to download from the selected `image_provider`. | Number | 768 |
| `current_wallpaper_path` | Defines the full path to the current wallpaper. If you manually update the path, run the command `$ wallpapr -c` to set the image as the wallpaper. **Note: This will only reflect correctly if the current wallpaper was set with `wallpapr`** | String | `None` |
| `download_path` | Defines the full path to the directory where the image is to be downloaded. | String | `$HOME/Pictures` |
| `image_provider` | Defines the default image provider to use. You can override the default `image_provider` in the CLI using `--image-provider` or `-p` option **Note: Currently, only [`unsplash`](#unsplash) is a valid option.** | String | [`unsplash`](#unsplash) |
| `image_provider_config` | Defines the configurations to provide to the image provider. | JSON | See [documentation](#image-providers) for the `image_provider` |

# Image Providers
* [Unsplash](#unsplash)
## Unsplash
> Note: [Unsplash](https://unsplash.com) is the default and the only (for now) image provider for `wallpapr`.

`wallpapr` uses the [`/photo/random`](https://unsplash.com/documentation#get-a-random-photo) API provided by [Unsplash](https://unsplash.com) to get the random image. The configurations are a subset of the ones described for the API in the [Unsplash official documentation](https://unsplash.com/documentation#parameters-10).

### Setup Unsplash as Image Provider
1. [Register](https://unsplash.com/documentation#creating-a-developer-account) an Unsplash app and get the secret key and access key.
2. Export the secret key (as `UNSPLASH_SECRET_KEY`) and access key (as `UNSPLASH_ACCESS_KEY`).
```bash
$ export UNSPLASH_SECRET_KEY="secret_key"
$ export UNSPLASH_ACCESS_KEY="access_key"
```
> Note: You can add these command at the end of ~/.profile to export it globally for the current user.
> This is required for wallpapr cli.
3. Once `wallpapr` is installed set `image_provider` to `unsplash` in the configuration file. See [configuring wallpapr](#configuring-wallpapr).

### Unsplash Configuration
| Property | Description | Type | Default |
| :--- | :--- | :---: | :---: |
| `orientation` | Filter by photo orientation. (Valid values: `landscape`, `portrait`, `squarish`). **Note: Multiple values are supported as either comma separated string or a list of string.** | String or Array[String] | `landscape` |
| `collections` | Public collection ID(‘s) to filter selection. The collection `id` can be found in the web url for the collection. **Note: Multiple values are supported as either comma separated string or a list of ids or a list of JSON object with `id` and `url` (optional; web url to the unsplash collection.)** | String or Array[String] or Array[Number] or Array[{id, url}] | See [Default Unsplash Collections](#default-unsplash-collections) |


### Default Unsplash Collections
```json
[
  {
    "id": "606028",
    "url": "https://unsplash.com/collections/606028/technology"
  },
  {
    "id": "11649432",
    "url": "https://unsplash.com/collections/11649432/landscape"
  },
  {
    "id": "827743",
    "url": "https://unsplash.com/collections/827743/landscape"
  },
  {
    "id": "2476111",
    "url": "https://unsplash.com/collections/2476111/retro-tech"
  }
]
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
