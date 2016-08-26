# lecture-manager

I built this tool to help me organize my lecture notes. 

(This was written, tested and used in Linux, and will not work with Windows).

# Example use case

```bash
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

```bash
$ sudo make install
```

You can then delete the whole repository, since the installation is complete.


# Uninstalling

If you still have the Makefile around, just run ```sudo make uninstall```, else run 

```bash
$ rm /usr/local/bin/lm-new-lecture /usr/local/bin/lm-new-course /usr/local/bin/lm-archive-course
```
