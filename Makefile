.PHONY: build up encode

build:
	docker-compose build

up:
	docker-compose up

encode:
	docker build -t encoder -f Dockerfile.encode --output . .
