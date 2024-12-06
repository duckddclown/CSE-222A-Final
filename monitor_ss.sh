#!/bin/bash
SERVER_IP=54.177.120.42
OUTPUT_FILE=tcp_metrics.log

# Create or clear the output file
> $OUTPUT_FILE

# Monitor TCP metrics during the test
while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "Timestamp: $TIMESTAMP" >> $OUTPUT_FILE
    ss -ti state established dst $SERVER_IP | grep -E 'cwnd|ssthresh' >> $OUTPUT_FILE
    sleep 0.1
done
