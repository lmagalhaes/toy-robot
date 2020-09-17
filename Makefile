#!make

help:
	@echo 'Available actions:'
	@echo ''
	@echo '    Install'
	@echo '        Build images'
	@echo ''
	@echo '    Uninstall'
	@echo '        Delete images'
	@echo ''
	@echo '    test'
	@echo '        Run unit tests'
	@echo '        A coverage folder will be generated in the root folder.'
	@echo '        Open coverage/index.html on the browser to see full coverage.'
	@echo ''
	@echo '    console'
	@echo '        Log-in to the container. Useful for debug and access the binary directly'
	@echo ''
	@echo '    start'
	@echo '        Start application and get robot ready to receive commands'
	@echo ''
	@echo '    warm-up'
	@echo '        Start the warm-up process that sends commands to the bot automatically.'
	@echo '        THe commands that will be sent to the bot can be found in the file resources/robot_warmup.txt'


.PHONY: help
.SILENT:

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
	$(call docker-run,local,,-w '/opt/toy_robot/' --entrypoint bash)
