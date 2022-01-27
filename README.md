# snowmass-loi-words

Source for the website hosted here: [https://gordonwatts.github.io/snowmass-loi-words/](https://gordonwatts.github.io/snowmass-loi-words/)

## Development

### Running the notebooks

1. Not all the packages work on Windows - you'll need to open this in WSL if you are developing in windows (use vscode, makes life *simple*).
    - Tested and run against python 3.9.
    - The PDF scanner needs `sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev`
1. `pip install -r requirements.txt`
1. Download the extraction of the summaries (see the notebook `00`)

### Website

This is a Jekyll site. Adding and changing follows all the usual rules. As far as I know, nothing special is being done here.

## Running locally

To run locally you need to build the website first, in Jekyll. There is a `docker` container that will do this for you. If you use Visual Studio Code as your editor, there is a task configured that will start up a docker container, build your website, and serve it on port `4000`. Once you have the prompt use the command `cd /gitrepo/web` and `jekyll serve` to start the webserver. The first time you run this it will take a while as it downloads everything from the web.

Note that on Windows, the auto-build feature may not work as the file systems do not always talk to each other properly.

To debug you need to first start the server. Then look for the site profile in the debugger (will start it on the default browser on your machine, if all goes well). One odd thing: Jekyll creates a copy of your website, so if you need to debug things, you'll have to look in `web/_site/xxx` for the file in which to set breakpoints.

All the above has been tested on Windows. If you want to update this for other OS', please do!

## Using the devContainer

`vscode` has a very nice feature called `devcontainers` which builds the development environment in a container, and then does all dev work from `vscode` in that container.

This repo is setup with a `devcontainer`. When you open it, use the small little green icon in the lower left hand corner to bring up the list of remote development options. Click on the `reopen in dev container` option. 

* Have the `loi` data located at the same level as the work space, and in a directory called `snowmass-lois`.
* Use the default python installation when asked for a jupyter kernel
* Use the vscode task to serve jekyll in the devcontainer. Note that vscode doesn't seem to always detect the outgoing port, you might need to click on the "ports forwarded" icon and add 4000 by hand.