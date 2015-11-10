.PHONY: build serve pdf clean deploy

build:
	jekyll build

serve:
	jekyll serve

readings.pdf:
	make -C readings readings.pdf
	cp readings/readings.pdf .

pdf: readings.pdf

clean:
	git clean -fdX

deploy: build
	git checkout gh-pages
	mv _site .site
	rm -r *
	mv .site/* .
	rmdir .site
	git add -A
	git ci -m "Generated gh-pages for `git log master -1 --pretty=short --abbrev-commit`" && git push origin gh-pages
	git checkout master