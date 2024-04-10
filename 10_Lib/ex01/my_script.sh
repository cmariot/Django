#!/bin/bash


PYTHON=python3
BLUE='\033[0;34m'
RESET='\033[0m'


function display_pip_version() {

    # Display the version of pip

    echo -e "${BLUE}Pip version:${RESET}"
    PIP_VERSION=$($PYTHON -m pip --version | cut -d ' ' -f 2)
    echo "The current version of pip is $PIP_VERSION"
    echo

}


function install_path() {

    # Install the path module using pip from its git repository
    # --pre: install development version of the package
    # --target: install the package in the local_lib directory
    # --upgrade: reinstall the package if it is already installed
    # --log: log the installation in the local_lib/install.log file
    # --verbose: display more information in the log file
    # --quiet: do not display all the installation information in the terminal

    echo -e "${BLUE}Installing the path module:${RESET}"
    $PYTHON -m pip install git+https://github.com/jaraco/path \
        --pre \
        --target=local_lib \
        --upgrade \
        --log local_lib/install.log \
        --verbose \
        --quiet
    echo

}


function check_install() {

    # Check if the path module is correctly installed
    # If the module is correctly installed, run the program my_program.py
    # Otherwise, display an error message

    echo -e "${BLUE}Checking if the path module is correctly installed:${RESET}"
    if $PYTHON -c "from local_lib.path import Path"; then
        $PYTHON my_program.py
    else
        echo "The path library is not correctly installed"
        exit 1
    fi

}


function main() {

    display_pip_version
    install_path
    check_install

}


main
