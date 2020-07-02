.POSIX:
.PHONY: install uninstall lint

PREFIX ?= /usr/local

install:
	mkdir -p ${PREFIX}/share/lecture-manager
	cp style.css ${PREFIX}/share/lecture-manager/style.css
	cp lectman/lm_archive_course.py ${PREFIX}/bin/lm-archive-course
	cp lectman/lm_list.py ${PREFIX}/bin/lm-list
	cp lectman/lm_new_course.py     ${PREFIX}/bin/lm-new-course
	cp lectman/lm_new_lecture.py    ${PREFIX}/bin/lm-new-lecture
	chmod +x ${PREFIX}/bin/lm-archive-course\
	         ${PREFIX}/bin/lm-list\
	         ${PREFIX}/bin/lm-new-course\
	         ${PREFIX}/bin/lm-new-lecture

uninstall:
	rm -f ${PREFIX}/bin/lm-archive-course\
	      ${PREFIX}/bin/lm-list\
	      ${PREFIX}/bin/lm-new-course\
	      ${PREFIX}/bin/lm-new-lecture

lint:
	pylint setup.py
	pylint lectman
