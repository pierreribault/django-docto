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
	@docker-compose exec web pip install --no-cache-dir -r requirements.txt
	@docker-compose exec web python manage.py makemigrations apps_authentication
	@docker-compose exec web python manage.py makemigrations apps_consulting
	@docker-compose exec web python manage.py makemigrations apps_messenger
manage:
	@docker-compose exec web python manage.py
sass:
	@sass -w -q ./apps/static/assets/scss/argon.scss ./apps/static/assets/css/argon.css

deps:
	@docker-compose exec web pip install --no-cache-dir -r requirements.txt
	
seeder:
	@docker-compose exec web python manage.py seed
