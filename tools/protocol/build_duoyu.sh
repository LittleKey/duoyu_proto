#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname $0 )" && pwd )"
GIT_ROOT="$(git rev-parse --show-toplevel)"

cd $SCRIPT_DIR
sh build_proto.sh $GIT_ROOT $GIT_ROOT/app/duoyu/src/main/java *.proto
sh build_proto.sh $GIT_ROOT $GIT_ROOT/app/duoyu/src/main/java **/*.proto
