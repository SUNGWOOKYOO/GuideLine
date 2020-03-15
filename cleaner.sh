#!/bin/bash

# clean all ".ipynb*" files in this directory.
find -type d -name ".ipynb*" | xargs -d"\n" rm -rf