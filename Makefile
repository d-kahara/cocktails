
.PHONY: help build run 

#@-- help command to show usage of make commands --@#
help:
	@echo "----------------------------------------------------------------------------"
	@echo "-                     Available docker commands                             -"
	@echo "----------------------------------------------------------------------------"
	@echo "---> make build         - To build the docker image"
	@echo "---> make run           - To start the containers in the background"
	@echo "---> make help          - To show usage commands"
	@echo "----------------------------------------------------------------------------"
	@echo "-                     Available shell commands                             -"
	@echo "----------------------------------------------------------------------------"
	@echo "---> make install        - To install the application dependencies"
	@echo "---> make migrations     - To create database migration files"
	@echo "---> make migrate 	    - To apply the migration"
	@echo "---> make superuser 	    - To create a new superuser"
	@echo "---> make collectstatic  - To create static files"
	@echo "---> make serve  	    - To run the application"


#@-- command to build the application--@#
build:
	@ echo "Building api image..."
	@ docker build -t web:latest .

#@-- command to start the container in the background --@#
run:
	@echo "Start up the api in the background after building"
	@echo ""
	@ docker run -d --name cocktails-api -e "PORT=8765" -e "DEBUG=0" -p 8007:8765 web:latest

install:
	pip install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser

collectstatic:
	python3 manage.py collectstatic

serve:
	python3 manage.py runserver