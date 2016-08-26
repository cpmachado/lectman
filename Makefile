
install:

	# Remove directory from possible previous installation
	rm -rf ~/.lecture-manager

	# Create directory 
	mkdir ~/.lecture-manager

	# Copy stylesheet to the directory
	cp style.css ~/.lecture-manager/style.css
	
	# After these lines are executed, the python scripts can 
	# be ran as if they were executables
	cp lm-new-lecture.py    /usr/local/bin/lm-new-lecture
	cp lm-new-course.py     /usr/local/bin/lm-new-course
	cp lm-archive-course.py /usr/local/bin/lm-archive-course

	# Change permissions
	chmod +x /usr/local/bin/lm-new-lecture /usr/local/bin/lm-new-course /usr/local/bin/lm-archive-course

uninstall:
	# Clean installation products
	rm /usr/local/bin/lm-new-lecture /usr/local/bin/lm-new-course /usr/local/bin/lm-archive-course
