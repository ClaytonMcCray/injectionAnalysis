#!/usr/bin/env bash

# Resource: https://stackoverflow.com/questions/145270/calling-c-c-from-python
#  ... I was using osx and had to replace -soname with -install_name to compile
if [ -d "$OSTYPE" ]; then
	rm -r $OSTYPE
fi

mkdir $OSTYPE
cd $OSTYPE


if [[ "$OSTYPE" == "linux-gnu" ]]; then
	g++ -c -fPIC ../main.cpp -o injection.o -pthread
	g++ -shared -Wl,-soname,injection.so -o injection.so injection.o -pthread
fi
