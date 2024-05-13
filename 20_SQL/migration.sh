export EX=$1

mkdir -p $EX/migrations
touch $EX/migrations/__init__.py
python3 manage.py makemigrations
python3 manage.py migrate $EX
