#!/bin/bash

source ../env/bin/activate

bin/serendipod.py $1 $2

deactivate
