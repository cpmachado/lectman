.POSIX:
.PHONY: install uninstall

PREFIX ?= /usr/local

install:
	rm -rf ~/.lecture-manager
	mkdir ~/.lecture-manager
	cp style.css ~/.lecture-manager/style.css
	cp lm-archive-course.py ${PREFIX}/bin/lm-archive-course
	cp lm-new-course.py     ${PREFIX}/bin/lm-new-course
	cp lm-new-lecture.py    ${PREFIX}/bin/lm-new-lecture
	chmod +x ${PREFIX}/bin/lm-archive-course\
	         ${PREFIX}/bin/lm-new-course\
	         ${PREFIX}/bin/lm-new-lecture

uninstall:
	rm -f ${PREFIX}/bin/lm-archive-course\
	      ${PREFIX}/bin/lm-new-course\
	      ${PREFIX}/bin/lm-new-lecture

