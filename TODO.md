### TODO
#### Config
	- [ ] path for config file
	- [ ] auto gen course specific configs?
#### Canvas API interactions
	- [x] assignments/grades
1.  - [ ] store assignment groups as sub dictionaries for db search
		- [ ] config option for by group or just assignments
			- not by group could miss some assignments
		- [ ] getting all submissions not just most recent (maybe optional)
	- [ ] submitting files
	###### *Far out future*
		- [ ] support for instructors and admins side
#### optimize
	- [x] parallel/async api requests
	- [ ] verify efficiency of making db requests
#### Database
	- [x] store courses with course_id as doc id
	- [ ] template for command to get item
	- [x] allow option to generate human viewable json with old method *db human readable rn*
	- [ ] output db as tree structure 
	- [ ] search for item
			- [ ] search with regex
	- [x] update courses merges with db instead of overwriting
			- [ ] maybe get favorite courses as test if should overwrite or not
				- [ ] give warning before overwrite
				- then for course in favorite courses call get_item for each item in course and merge with preexisting somehow?
	- [ ] multiple nicknames for courses
#### CLI interaction 
	- [ ] using flags in base to call parsers of subcommands like courses (using _get_parser...)
	- [ ] arguments for functions
	- [ ] how to display tree and select files to download (user prompt)
	- [ ] how to submit / choose assignment **(user prompt)**
	- [ ] loading bars
	- [ ] provide ability to load functions in 
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
	- [ ] easel mv for changing path of item
#### testing
	- [ ] make tests lol
#### Documentation
	- [ ] make docs lol
#### General
	- [ ] plugins: 
		- [ ] ability to dynamically load plugins into cement
		- [ ] run plugins as command
		- [ ] like "download_midterm2.py" which can then be run by easel and executed
