build:
	docker build -t countdown .
run:
	docker run -it --rm -e step=$(step) countdown
test:
	docker run -it --rm countdown ./test.sh
