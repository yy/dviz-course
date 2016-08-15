MAIN := syllabus

all: $(MAIN).pdf

upload: syllabus.pdf
	scp syllabus.pdf yongyeol.com:~/yongyeol.com/courses/2016F-dviz/

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $<

monitor: $(MAIN).tex
	latexmk -pvc -pdf $<
