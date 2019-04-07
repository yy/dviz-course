MAIN := syllabus

all: $(MAIN).pdf

upload: syllabus.pdf
	scp syllabus.pdf yyahn@yongyeol.com:~/yongyeol.com/teaching/2019SU_dviz_syllabus.pdf 

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $<

monitor: $(MAIN).tex
	latexmk -pvc -pdf $<
