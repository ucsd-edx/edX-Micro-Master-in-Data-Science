#!/bin/bash
/usr/bin/yarn application -list  | awk '$6 == "RUNNING" { print $1 }' | xargs -I {} yarn application -kill {}
