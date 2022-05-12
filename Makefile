makemigrations:
	@docker-compose exec web python manage.py makemigrations

migrate:
	@docker-compose exec web python manage.py migrate

admin:
	@docker-compose exec web python manage.py createsuperuser

restart:
	@docker-compose restart web

fresh:
	@rm ./apps/*/migrations/*.py | true
	@docker-compose down --volumes
	@docker-compose up -d
	@docker-compose exec web python manage.py makemigrations apps_authentication
	@docker-compose exec web python manage.py makemigrations apps_consulting
manage:
	@docker-compose exec web python manage.py
