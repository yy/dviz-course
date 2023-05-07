MAIN := syllabus

# Get current year
YEAR := $(shell date +%Y)

# Get current semester
MONTH := $(shell date +%m)

# Fall if month is between 8 and 11, Summer if month is between 4 and 7. 
# Fall: FA, Summer: SU
SEMESTER := $(shell if [ $(MONTH) -ge 8 -a $(MONTH) -le 11 ]; then echo FA; else echo SU; fi)

all: $(MAIN).pdf

test:
	echo $(YEAR)$(SEMESTER)

upload: $(MAIN).pdf
	scp syllabus.pdf yyahn@yongyeol.com:~/yongyeol.com/teaching/$(YEAR)$(SEMESTER)_dviz_syllabus.pdf 
	scp syllabus.pdf yyahn@yongyeol.com:~/yongyeol.com/teaching/dviz_syllabus.pdf 

$(MAIN).pdf: $(MAIN).tex
	latexmk -pdf $<

monitor: $(MAIN).tex
	latexmk -pvc -pdf $<
