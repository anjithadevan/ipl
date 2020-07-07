# ipl

1.Its an application analysing ipl result from the given csv file.

Setps for installation
1)Install requirements by pip install -r requirements.txt

2)Create databse 
  a)python manage.py makemigrations
  b)python manage.py migrate

3)Add csv file data to database by running management command.
  python manage.py add_ipl_data_to_db_from_csv
