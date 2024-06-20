#!/bin/bash

# Set the SPARK_HOME environment variable
export SPARK_HOME=/opt/spark

# Check if the SPARK_MODE environment variable is set to "master"
if [ "$SPARK_MODE" == "master" ]; then
    echo "Starting Spark Master..."
    $SPARK_HOME/sbin/start-master.sh
else
    # If not in master mode, assume worker mode
    echo "Starting Spark Worker..."
    $SPARK_HOME/sbin/start-worker.sh $SPARK_MASTER
fi

# Keep the container running
tail -f /dev/null
