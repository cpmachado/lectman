# lecture-manager

This was build by another person, to organize notes.

It is written with a Linux based FS and structure.

# Example use case

```shell
	$ # Create new course
	$ lm-new-course 
	Course name: network-service-management
	$ cd network-service-management/
	$ ls
	style.css
	$ # Everytime a new lecture is created, a new html file is 
	$ # generated with a basic lecture template.
	$ lm-new-lecture "Introduction"
	$ lm-new-lecture "SNMP - Simple Network Management Protocol"
	$ # When a course is archived, a new file is created containing the index of the lectures, 
	$ # with hyperlinks to each lecture.
	$ lm-archive-course
	$ ls
	lecture001.html  lecture002.html  network-service-management-archive.html  style.css
```
This is how the archive looks like:

![Image](http://i.imgur.com/4SOXvzj.png)

# Installing

Clone this repository, then use:

```shell
	# should you want install in /usr/local with a non-root user
	$ sudo make install

	# should you want to install in a local bin, example:
	$ make install PREFIX=~/.local
```

You can then delete the whole repository, since the installation is complete.


# Uninstalling

Assuming you have the Makefile.

```shell
	# With a non-root user and having installed in /usr/local
	$ sudo make uninstall

	# should you want to uninstall from a local bin, example:
	$ make uninstall PREFIX=~/.local

```

Assuming you don't, just delete the binaries, with according privilege.

```shell
	$ rm /usr/local/bin/lm-new-lecture /usr/local/bin/lm-new-course /usr/local/bin/lm-archive-course
```
