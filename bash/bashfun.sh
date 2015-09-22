#!/bin/bash

# this script will accept a username to remove

echo "*****Script by Patrick Daly*****"
echo -n "******** Sanitize users ********"
echo -n

read newVar
echo "you would like to clear $newVar"
echo $newVar >> sanitize-log.txt

if [ `grep $newVar sanitize-log.txt | wc -l` -eq 1]
then
    echo "something"
else
    echo "something"
fi

input=$1
input2=$2

function first_function {
	echo "this is the first fucntion"

}

first_function

function second_function {
  echo "this is the second function"

}

input_function() {
  echo "the name you gave me is: $1"
}

input_function patrick

input_function $input

case $input in
    1)
      first_function
    ;;
    2)
      second_function
    ;;
    3)
      input_function $input2
    ;;
    *)
      echo "You didn't select a valid option"
    ;;
esac

for user in `cat $file`
do
    if [ "$action" == "add" ]
      then
        echo adding user: $user
        useradd $user -m -ppassword
    fi
    if [ "$action" == "del" ]
      then
        echo deleting user: $user
        userdel -r $user
    fi
done
