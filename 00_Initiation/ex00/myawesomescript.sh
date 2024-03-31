#!/bin/sh

# The purpose of this shell script is to display the real address of
# a supposedly valid bit.ly address passed as an argument.

# Usage example:
# $> ./myawesomescript.sh bit.ly/1O72s3U


# Parse the argument
parse_argument() {
    if [ -z $1 ]
    then
        echo "Please provide an URL as an argument."
        echo "Usage: ./myawesomescript.sh bit.ly/1O72s3U"
        exit 1
    fi
}

# Get the real address of the URL
get_location() {
    # curl options :
    # -s : silent mode
    # -I : head request

    # grep options :
    # -i : case insensitive

    # cut options :
    # -d : delimiter (space)
    # -f : field (2)

    response=$(curl -s -I $1 | grep -i Location | cut -d " " -f 2)
}

# Print the URL
print_url() {
    if [ $response ]
    then
        echo $response
    else
        echo "Error: The URL cannot be resolved."
    fi
}

# Main function
main() {
    parse_argument $1
    get_location $1
    print_url
}

# Call the main function
main $1
