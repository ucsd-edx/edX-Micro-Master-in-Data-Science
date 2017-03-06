#!/bin/env bash
REVEAL_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
# echo $REVEAL_HOME
export REVEAL_HOME
export PATH=$REVEAL_HOME/bin:$PATH
