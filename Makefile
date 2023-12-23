TARGET ?= production

build:
	docker build --file docker/Dockerfile --tag="smwatertd/viva-victoria-notifications:latest" --target=${TARGET} .

test:
	make build TARGET=testing
	docker run --rm smwatertd/viva-victoria-notifications:latest

dev:
	make build TARGET=development
	docker run --rm -p 8000:8000 smwatertd/viva-victoria-notifications:latest

prod:
	make build TARGET=production
	docker run --rm -p 8000:8000 smwatertd/viva-victoria-notifications:latest
