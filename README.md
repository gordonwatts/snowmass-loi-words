# snowmass-loi-words

Source for the website hosted here: [https://gordonwatts.github.io/snowmass-loi-words/](https://gordonwatts.github.io/snowmass-loi-words/)

## Development

This is a Jekyll site. Adding and changing follows all the usual rules. As far as I know, nothing special is being done here.

## Running locally

To run locally you need to build the website first, in Jekyll. There is a `docker` container that will do this for you. If you use Visual Studio Code as your editor, there is a task configured that will start up a docker container, build your website, and serve it on port `4000`.

Note that on Windows, the auto-build feature may not work as the file systems do not always talk to each other properly.

To debug you need to first start the server. Then look for the site profile in the debugger (will start it on the default browser on your machine, if all goes well). One odd thing: Jekyll creates a copy of your website, so if you need to debug things, you'll have to look in `web/_site/xxx` for the file in which to set breakpoints.

All the above has been tested on Windows. If you want to update this for other OS', please do!
