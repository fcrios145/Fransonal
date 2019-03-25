# Makefile for building and deploying
#

PROJECT_ROOT=/home/kriz/src
PROJECT_VENV=/home/kriz/.venv/src/bin

# deploy: dependencies clean minified_static_files
deploy: stop dependencies migrations collectstatic restart

restart:
	sudo systemctl restart nginx
	sudo systemctl start gunicorn.service

stop:
	sudo systemctl stop nginx
	sudo systemctl stop gunicorn.service

# dependencies: requirements.txt
# 	( \
# 		source /home/kriz/.envs/coto_env/bin/activate; \
# 		pip install -r requirements.txt \
# 	)


dependencies:
	. $(PROJECT_VENV)/activate && $(PROJECT_VENV)/pip install -r requirements.txt

migrations:
	. $(PROJECT_VENV)/activate && python $(PROJECT_ROOT)/manage.py makemigrations
	. $(PROJECT_VENV)/activate && python $(PROJECT_ROOT)/manage.py migrate

collectstatic:
	. $(PROJECT_VENV)/activate && python $(PROJECT_ROOT)/manage.py collectstatic --noinput

clean:
	@-rm -rf static_files/
	@-find . -name '__pycache__' -exec /bin/rm -rf {} ;
	@echo 'Successfully Cleaned!'

.PHONY: clean dependencies restart stop deploy migrations collectstatic
