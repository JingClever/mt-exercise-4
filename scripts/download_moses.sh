#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

tools=$base/tools
mkdir -p $tools

# install Moses scripts for postprocessing
pip install numpy torch sacremoses nltk

# git clone https://github.com/bricksdont/moses-scripts $tools/moses-scripts


