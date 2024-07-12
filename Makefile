define USAGE
Super awesome hand-crafted build system ⚙️

Commands:
	help		list all available commands
	install     Install Python dependencies
	getDeps   	Find dependencies from virtualenv and store it in requirements.txt
	start     	Run app in dev environment.
endef

export USAGE
help:
	@echo "$$USAGE"

getDeps:
	pip3 freeze > requirements.txt

install:
	pip3 install -r requirements.txt

start:
	FLASK_APP=app.py FLASK_DEBUG=1 FLASK_RUN_PORT=5000 flask run --reload

