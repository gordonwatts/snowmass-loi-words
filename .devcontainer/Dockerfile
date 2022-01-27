# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.209.6/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic
ARG VARIANT="hirsute"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install python3-pip build-essential libpoppler-cpp-dev pkg-config python3-dev

# Make python 3 the default
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>


# Get rid of the super annoying prompt that takes seconds to update!
# It looks cool, but not at the expense of 3-4 seconds each time!
RUN echo "export PS1=\"bash$ \"" >> /home/vscode/.bashrc
