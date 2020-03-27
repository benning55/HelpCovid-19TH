# HelpCovid-19TH
This project is to build help program for covid 19

# Run frontend
docker-compose exec quering-frontend-covid sh -c "npm run serve"

# Run Backend
docker-compose exec quering-django sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py initdb && python manage.py collectstatic --no-input && python manage.py runserver 0.0.0.0:8000"