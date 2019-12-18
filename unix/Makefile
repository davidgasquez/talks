IMAGE_NAME := davidgasquez/unix-talk:latest

.PHONY: build
build:
	@docker build -t $(IMAGE_NAME) .

.PHONY: talk
talk: build
	@docker run -ti --rm -v $(PWD):/talk $(IMAGE_NAME) bash -c 'TERM=xterm-256color /bin/bash'

.PHONY: build
push: build
	@docker push $(IMAGE_NAME)
