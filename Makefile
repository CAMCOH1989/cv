PROJECT_NAME ?= $(shell python3 setup.py --name)
VERSION = $(shell python3 setup.py --version | tr '+' '-')

REGISTRY ?= registry.gitlab.com
PROJECT_NAMESPACE ?= camcoh1989
REGISTRY_IMAGE ?= $(REGISTRY)/$(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make devenv	- Configure dev environment"
	@echo "make clean	- Remove generated files"
	@echo "make lint    - Run linter"
	@echo "make imports	- Fix imports with isort"
	@echo "make sdist	- Make source distribution"
	@exit 0

devenv: clean
	rm -rf env
	python3.9 -m venv env
	env/bin/pip install --upgrade pip
	env/bin/pip install -Ue '.[dev]'
	env/bin/pip install -r requirements.dev.txt -Ue
z cv

clean:
	rm -fr *.egg-info dist
	find . -iname '*.pyc' -delete

lint:
	pylama app_sharer

imports:
	isort -ca app_sharer/*/**.py

sdist: clean
	python3 setup.py sdist

docker: sdist
	docker build --target=server -t $(PROJECT_NAME):$(VERSION) .

upload: docker
	docker tag $(PROJECT_NAME):$(VERSION) $(REGISTRY_IMAGE):$(VERSION)
	docker push $(REGISTRY_IMAGE):$(VERSION)

