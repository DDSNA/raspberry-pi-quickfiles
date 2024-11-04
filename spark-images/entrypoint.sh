#!/bin/bash

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
  start-master.sh -p 7077
  echo "Spark Master is running"
  sleep 360
  ./sbin/start-connect-server.sh --packages org.apache.spark:spark-connect_2.12:3.5.1 &
  echo "Spark Master is running with connect"
elif [ "$SPARK_WORKLOAD" == "worker" ];
then
  start-worker.sh spark://192.168.0.38:7077
  echo "Spark Worker is running";
# internal cloud master, will need updating regularly but helpful for some testing
elif [ "$SPARK_WORKLOAD" == "worker-cloud" ];
then
  start-worker.sh spark://10.132.0.2:7077:7077
  echo "Spark Worker is running"
elif [ "$SPARK_WORKLOAD" == "history" ]
then
  start-history-server.sh
fi