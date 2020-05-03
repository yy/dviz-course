MAIN := syllabus

all: $(MAIN).pdf

upload: $(MAIN).pdf
	scp syllabus.pdf yyahn@yongyeol.com:~/yongyeol.com/teaching/2020SU_dviz_syllabus.pdf 
	scp syllabus.pdf yyahn@yongyeol.com:~/yongyeol.com/teaching/dviz_syllabus.pdf 

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $<

monitor: $(MAIN).tex
	latexmk -pvc -pdf $<
