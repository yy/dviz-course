MAIN := syllabus

all: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $<

monitor: $(MAIN).tex
	latexmk -pvc -pdf $<
