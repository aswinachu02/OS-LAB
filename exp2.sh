#!/bin/bash

#20219025_Aswin_Subhash

echo "Shell script to print fibonacci series"

echo "Enter the total numbers in the series: "
read n

a=0
b=1
c=1

echo $a
if [ $n != 1 ]
then
    echo $b
fi
n=`expr $n - 2`

while [ $n -gt 0 ]
do
    echo $c
    a=$b
    b=$c
    c=`expr $a + $b`
    n=`expr $n - 1`
done

