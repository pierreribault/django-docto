makemigrations:
	@docker-compose exec web python manage.py makemigrations

migrate:
	@docker-compose exec web python manage.py migrate

admin:
	@docker-compose exec web python manage.py createsuperuser

restart:
	@docker-compose restart web

fresh:
	@rm ./*/migrations/*.py
	@docker-compose down --volumes
	@docker-compose up -d

manage:
	@docker-compose exec web python manage.py
