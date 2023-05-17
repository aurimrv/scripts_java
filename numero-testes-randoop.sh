#!/bin/bash

FILE=$1

rm -f testes.csv

for i in $( cat $FILE ); do
    PRJ=$(echo $i | awk 'BEGIN{FS=":"}{print $1}')
    echo -n $PRJ >> testes.csv
    for k in `seq 0 29`; do
        java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.RegressionTest${k}Maior > $PRJ/junit-ds.RegressionRandoopMaior
        
        tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.RegressionRandoopMaior)
        RANDOOP=${tmp/\(/}

        echo -n ":"$RANDOOP >> testes.csv
    done
    echo "" >> testes.csv
    echo -n .
done
echo