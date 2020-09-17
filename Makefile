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

docker-build = DOCKER_BUILDKIT=1 BUILDKIT_PROGRESS=plain docker build -t"toy_robot:$(1)" $(2) .

docker-run = docker run --rm -it -v '${PWD}:/opt/toy_robot' $(3) "toy_robot:$(1)" $(2)

install:
	$(call docker-build,local,--target prod-image)
	$(call docker-build,test,--target test)

uninstall:
	docker rmi toy_robot:local
	docker rmi toy_robot:test

start:
	$(call docker-run,local,start)

warm-up:
	$(call docker-run,local,warm-up)

test:
	$(call docker-run,test,-vvv)

console:
	$(call docker-run,local,,-w '${PWD}/toy_robot/bin' --entrypoint bash)
