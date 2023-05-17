#!/bin/bash

FILE=$1

for i in $( cat $FILE ); do
    PRJ=$(echo $i | awk 'BEGIN{FS=":"}{print $1}')
    
    java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.Marllos > $PRJ/junit-ds.Marllos
    
    java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.Evo > $PRJ/junit-ds.Evo
        
    java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.CodePro > $PRJ/junit-ds.CodePro
    
    java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.ManualEvo > $PRJ/junit-ds.ManualEvo
    
    java -cp /local/tools/junit4.11/junit-4.11.jar:/local/tools/junit4.11/hamcrest-core-1.3.jar:$PRJ/target/classes/:$PRJ/target/test-classes/ org.junit.runner.JUnitCore ds.Todos > $PRJ/junit-ds.Todos
    
    tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.Marllos)
    MARLLOS=${tmp/\(/}

    tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.Evo)
    EVO=${tmp/\(/}

    tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.CodePro)
    CODEPRO=${tmp/\(/}

    tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.ManualEvo)
    MANUALEVO=${tmp/\(/}

    tmp=$(awk '$1=="OK"{print $2}' $PRJ/junit-ds.Todos)
    TODOS=${tmp/\(/}

    echo $PRJ:$MARLLOS:$EVO:$CODEPRO:$MANUALEVO:$TODOS >> testes.csv
    echo -n .
done
echo