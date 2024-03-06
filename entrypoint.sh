#!/bin/bash

set -e
source /opt/ros/melodic/setup.bash

echo "Provided arguments: $@"
exec $@
