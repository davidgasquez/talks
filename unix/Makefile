IMAGE_NAME := davidgasquez/unixtalk:latest

.PHONY: build
build:
	@docker build -t $(IMAGE_NAME) .

.PHONY: talk
talk:
	@docker run -ti --rm -v $(PWD):/talk $(IMAGE_NAME) bash -c 'TERM=xterm-256color /bin/bash'

.PHONY: version
version:
	docker run --rm -it $(IMAGE_NAME) dbt --version
