#!/bin/sh

# The purpose of this shell script is to display the real address of
# a supposedly valid bit.ly address passed as an argument.

# Usage example:
# $> ./myawesomescript.sh bit.ly/1O72s3U



# If there is no argument
if [ -z $1 ]
then
    echo "Please provide an URL as an argument."
    echo "Usage: ./myawesomescript.sh bit.ly/1O72s3U"
    exit 1
fi


# Get the real adress of the URL

# curl options :
# -s : silent mode
# -I : head request

response=$(curl -s -I $1 | grep Location | cut -d " " -f 2)


if [ $response ]
then
    echo $response
else
    echo "Error: The URL cannot be resolved."
fi
