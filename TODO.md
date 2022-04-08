### TODO
	####RN
	1. jinja2 templates
	2. move from assignment_groups too assignments
		- can include assignment_group info when requesting assignments?
	2. listing upcoming assignments **[WITH API REQUEST]**
		- updating db when listing upcoming
	4. searching for item
		-pre: storing course names/ids in default table
			- assignments
			- courses
			- pages
			- modules
	3. downloading assignment attachments
		- viewing assignment descriptions / downloading
	4. submitting assignments
	5. opening item in browser when searched 
	5. displaying assignment descriptions by converting html to markdown and rendering markdown to file
	6. directories for assignments and courses, that can be used for downloading and submitting

#### Config
	- [ ] path for config file
	- [ ] auto gen course specific configs?
#### Canvas API interactions
	- [ ] preferring db or api request
			- [ ] per command (i.e. for get submission will check api request first)
			- [ ] on api request if different than db update db
	- [ ] consolidate get_{item} commands, user better ~taste~ (most if not all can be accomplished with get(courses/course_id/{type})) 
			- [ ] how to make per type differences (like adding "id" to pages or something) with good ~taste~
	- [ ] submitting files
	- [ ] getting all submissions not just most recent (maybe optional)
	###### *Far out future*
		- [ ] graphql
		- [ ] support for instructors and admins side
#### Database
	- [ ] online vs local requests?
	- [x] store courses with course_id as doc id
	- [ ] store names for courses in _default table as {courses : {key:id, names:[]}}
	### local storage
	- [ ] storing local paths in db
	- [ ] easel mv for changing path of item
	- [ ] command to get item from name/id
			- [ ] flags limit search making it faster (put this in help message)
	- [ ] output db as tree structure 
			using simplified data from type
	- [ ] search for item
			- [ ] search with regex
	- [x] update courses merges with db instead of overwriting
			- [ ] give warning before overwrite
			- then for course in favorite courses call get_item for each item in course and merge with preexisting somehow?
#### optimize
	- [ ] verify efficiency of making db requests
	- [ ] async/threads for creating documents from items and writing them to db?
		- [ ] done in api module?
#### CLI interaction 
	**- [ ] Use python code or templates for output?**
			###assignments:
	- [ ] how to submit / choose assignment 
			- [ ] choosing assignment by search term (searches assignment name and attachment name)
	- [ ] choosing course for action 
			###general:
	- [ ] using flags in base to call parsers of subcommands like courses (using _get_parser...)
	- [ ] arguments for functions
	- [ ] how to display tree and select files to download (user prompt)
	- [ ] loading bars
	- [ ] provide ability to load functions in 
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
#### testing
	- [ ] all command tests
#### Documentation
	- [ ] make docs lol
	- [ ] how to test api/db requests? just fail when no internet/db?
	- [ ] use actual db file or make a new one?
#### General
	- [ ] plugins: 
		- [ ] ability to dynamically load plugins into cement (maybe use generate command)
		- [ ] run plugins as command
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
	- [ ] "watchdog" extension config option for when assignments get moved etc
