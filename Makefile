#!make

help:
	@echo "available actions:"
	@echo "    build"
	@echo "        Build container image"
	@echo '    test'
	@echo '        Run unit tests'
	@echo '    start'
	@echo '        Start application (It does not install the application, just start containers)'
	@echo '    warm-up'
	@echo '        Stop application (It does not uninstall the application, just stop containers)'


.PHONY: help

install:
	DOCKER_BUILDKIT=1 BUILDKIT_PROGRESS=plain docker build -t"toy_robot:local" --target prod-image .
	DOCKER_BUILDKIT=1 BUILDKIT_PROGRESS=plain docker build -t"toy_robot:test" --target test .

uninstall:
	docker rmi toy_robot:local
	docker rmi toy_robot:test

start:
	docker run --rm -v '${PWD}:/opt/toy_robot' -it toy_robot:local start

warm-up:
	docker run --rm -v '${PWD}:/opt/toy_robot' -it toy_robot:local warm-up

test:
	docker run --rm -v '${PWD}/coverage:/opt/toy_robot/coverage' toy_robot:test
