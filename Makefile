.PHONY: all clean

all:
	make -C readings readings.pdf
	cp readings/readings.pdf .
	jekyll build

clean:
	git clean -fdX