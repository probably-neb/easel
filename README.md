# CANVAS CLI

### A WIP client for interacting with Canvas by Instructure's LMS REST API

## TODO
	-NAME at least temp name: easel
	- parse json to FileTree for reading
		- viewing files posted to course
			- modules
				- items
			- assignments
			- pages
- CLI interaction 
	- for better testing:
		- pass variables to functions
		- simple output [item id's]
	- PyInquirer
			- how to display tree and select files to download
			- how to submit / choose assignment
			- loading bars
- submitting files
- implement fuzzy finding for assignments, courses, files, etc
- optimize
	- parallel requests


Create a config file name "easel.json" in the canvas_cli folder.
```json
{
	"info" : {
		"domain": "canvas.[school].edu",
		"token" : "token"
	}
}
```



