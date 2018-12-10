#!/usr/bin/env bash

# Resource: https://stackoverflow.com/questions/145270/calling-c-c-from-python
#  ... I was using osx and had to replace -soname with -install_name to compile
if [ -d "lib" ]; then
    cd lib  # move into library
else
    mkdir lib
    cd lib
fi

if [ -d "bin" ]; then
    cd bin
else
    mkdir bin
    cd bin
fi


if [ -d "$OSTYPE" ]; then
	rm -r $OSTYPE
fi

mkdir $OSTYPE
cd $OSTYPE


if [[ "$OSTYPE" == "linux-gnu" ]]; then
	g++ -c -fPIC ../../src/checkInjective.cpp -o injection.o -pthread
	g++ -shared -Wl,-soname,injection.so -o injection.so injection.o -pthread

elif [[ "$OSTYPE" == "darwin17" ]]; then
    g++ -std=c++17 -c -fPIC ../../src/checkInjective.cpp -o injection.o
    g++ -shared -Wl,-install_name,injection.so -o injection.so injection.o
fi

