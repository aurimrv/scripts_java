#!/bin/bash

FILE=$1

for i in $( cat $FILE ); do
    PRJ=$(echo $i | awk 'BEGIN{FS=":"}{print $1}')
    CLAZZ=$(echo $i | awk 'BEGIN{FS=":"}{print $2}')
    
    JAVA=${CLAZZ/./\/}.java
    
    /local/tools/javancss-32.53/bin/javancss -ncss -function $PRJ/src/main/java/$JAVA > $PRJ/metricas.csv
    
    CCN=$(awk '$3=="CCN:"{print $4}' $PRJ/metricas.csv)
    NCSS=$(awk '$1=="Program"{print $3}' $PRJ/metricas.csv)
    
    echo $PRJ:$CLAZZ:$NCSS:$CCN >> metricas.csv
    echo -n .
done
echo