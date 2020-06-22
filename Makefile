.POSIX:
.PHONY: install uninstall

PREFIX ?= /usr/local

install:
	mkdir -p ${PREFIX}/share/lecture-manager
	cp style.css ${PREFIX}/share/lecture-manager/style.css
	cp lm_archive_course.py ${PREFIX}/bin/lm-archive-course
	cp lm_new_course.py     ${PREFIX}/bin/lm-new-course
	cp lm_new_lecture.py    ${PREFIX}/bin/lm-new-lecture
	chmod +x ${PREFIX}/bin/lm-archive-course\
	         ${PREFIX}/bin/lm-new-course\
	         ${PREFIX}/bin/lm-new-lecture

uninstall:
	rm -f ${PREFIX}/bin/lm-archive-course\
	      ${PREFIX}/bin/lm-new-course\
	      ${PREFIX}/bin/lm-new-lecture

lint:
	pylint lm_archive_course.py lm_new_course.py lm_new_lecture.py
