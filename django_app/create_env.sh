#!/bin/sh


# Create the postgresql env files
create_postgresql_env() {

    cd postgresql

    # Read input from user
    echo "Enter the postgresql username: "
    read POSTGRES_USER
    echo "Enter the postgresql password: "
    read POSTGRES_PASSWORD
    echo "Enter the postgresql database name: "
    read POSTGRES_DB

    # Create the .env file and write the variables
    echo "POSTGRES_USER=$POSTGRES_USER" > $1
    echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> $1
    echo "POSTGRES_DB=$POSTGRES_DB" >> $1

}


# Create the django env files
create_django_env() {

    cd django

    # Read input from user
    echo "Enter the django secret key"
    read SECRET_KEY
    echo "Enter the allowed hosts"
    read ALLOWED_HOSTS
    echo "Enter the sql engine"
    read SQL_ENGINE
    echo "Enter the sql database"
    read SQL_DATABASE
    echo "Enter the sql user"
    read SQL_USER
    echo "Enter the sql password"
    read SQL_PASSWORD
    echo "Enter the sql host"
    read SQL_HOST
    echo "Enter the sql port"
    read SQL_PORT
    echo "Enter the database"
    read DATABASE

    if eq $1 ".env.dev"
    then
        echo "DEBUG=1" > $1
    else
        echo "DEBUG=0" > $1
    fi

    echo "SECRET_KEY=$SECRET_KEY" >> $1
    echo "DJANGO_ALLOWED_HOSTS=$ALLOWED_HOSTS" >> $1
    echo "SQL_ENGINE=$SQL_ENGINE" >> $1
    echo "SQL_DATABASE=$SQL_DATABASE" >> $1
    echo "SQL_USER=$SQL_USER" >> $1
    echo "SQL_PASSWORD=$SQL_PASSWORD" >> $1
    echo "SQL_HOST=$SQL_HOST" >> $1
    echo "SQL_PORT=$SQL_PORT" >> $1
    echo "DATABASE=$DATABASE" >> $1

}


main() {

    echo "Creating the postgresql env files"

    echo "Creating the .env.dev:"
    create_postgresql_env .env.dev

    echo "Creating the .env.prod:"
    create_postgresql_env .env.prod

    echo "Creating the django env files"

    echo "Creating the .env.dev:"
    create_django_env .env.dev

    echo "Creating the .env.prod:"
    create_django_env .env.prod

}

main
