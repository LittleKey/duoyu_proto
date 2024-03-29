#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname $0 )" && pwd )"
GIT_ROOT="$(git rev-parse --show-toplevel)"

cd $SCRIPT_DIR
sh build_proto.sh $GIT_ROOT/proto $GIT_ROOT/app/sparkle/src/main/java models/proto/*.proto
sh build_proto.sh $GIT_ROOT/proto $GIT_ROOT/app/sparkle/src/main/java models/proto/**/*.proto
