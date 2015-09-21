#!/bin/bash

input=$1
input2=$2

function first_function {
	echo "this is the first fucntion"

}

first_function

function second_function {
  echo "this is the second function"

}

function input_function {
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
