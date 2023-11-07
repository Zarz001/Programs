C = gcc
CF = -Wall
all: perimeter
perimeter: main.c perimeter.c
	$(C) $(CF) -o $@ $^
clean:
	rm -f perimeter
test: all
	./perimeter 5
	./perimeter 7
	./perimeter 20
	./perimeter 30

