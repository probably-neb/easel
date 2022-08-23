list_your_courses_params = {
    "enrollment_type": {
        """When set, only return courses where the user is enrolled as this type. For example, set to âteacherâ to return only courses where the user is enrolled as a Teacher.  This argument is ignored if enrollment_role is given."""
        "type": "string",
        "required": False,
        "allowed_values": ['teacher', 'student', 'ta', 'observer', 'designer'],
    },
    "enrollment_role": {
        """Deprecated When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the Add Role API or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "enrollment_role_id": {
        """When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the Add Role API or a built_in role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "enrollment_state": {
        """When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides."""
        "type": "string",
        "required": False,
        "allowed_values": ['active', 'invited_or_pending', 'completed'],
    },
    "exclude_blueprint_courses": {
        """When set, only return courses that are not configured as blueprint courses."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "include[]": {
        """âneeds_grading_countâ: Optional information to include with each Course. When needs_grading_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned.

âsyllabus_bodyâ: Optional information to include with each Course. When syllabus_body is given the user-generated html for the course syllabus is returned.

âpublic_descriptionâ: Optional information to include with each Course. When public_description is given the user-generated text for the course public description is returned.

âtotal_scoresâ: Optional information to include with each Course. When total_scores is given, any student enrollments will also include the fields 'computed_current_score', 'computed_final_score', 'computed_current_grade', and 'computed_final_grade', as well as (if the user has permission) 'unposted_current_score', 'unposted_final_score', 'unposted_current_grade', and 'unposted_final_grade' (see Enrollment documentation for more information on these fields). This argument is ignored if the course is configured to hide final grades.

âcurrent_grading_period_scoresâ: Optional information to include with each Course. When current_grading_period_scores is given and total_scores is given, any student enrollments will also include the fields 'has_grading_periods', 'totals_for_all_grading_periods_option', 'current_grading_period_title', 'current_grading_period_id', current_period_computed_current_score', 'current_period_computed_final_score', 'current_period_computed_current_grade', and 'current_period_computed_final_grade', as well as (if the user has permission) 'current_period_unposted_current_score', 'current_period_unposted_final_score', 'current_period_unposted_current_grade', and 'current_period_unposted_final_grade' (see Enrollment documentation for more information on these fields). In addition, when this argument is passed, the course will have a 'has_grading_periods' attribute on it. This argument is ignored if the total_scores argument is not included. If the course is configured to hide final grades, the following fields are not returned: 'totals_for_all_grading_periods_option', 'current_period_computed_current_score', 'current_period_computed_final_score', 'current_period_computed_current_grade', 'current_period_computed_final_grade', 'current_period_unposted_current_score', 'current_period_unposted_final_score', 'current_period_unposted_current_grade', and 'current_period_unposted_final_grade'

âgrading_periodsâ: Optional information to include with each Course. When grading_periods is given, a list of the grading periods associated with each course is returned.

âtermâ: Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned.

âaccountâ: Optional information to include with each Course. When account is given, the account json for each course is returned.

âcourse_progressâ: Optional information to include with each Course. When course_progress is given, each course will include a 'course_progress' object with the fields: 'requirement_count', an integer specifying the total number of requirements in the course, 'requirement_completed_count', an integer specifying the total number of requirements in this course that have been completed, and 'next_requirement_url', a string url to the next requirement item, and 'completed_at', the date the course was completed (null if incomplete). 'next_requirement_url' will be null if all requirements have been completed or the current module does not require sequential progress. âcourse_progressâ will return an error message if the course is not module based or the user is not enrolled as a student in the course.

âsectionsâ: Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start_at, end_at), as well as the enrollment type (enrollment_role, e.g. 'StudentEnrollment').

âstorage_quota_used_mbâ: The amount of storage space used by the files in this course

âtotal_studentsâ: Optional information to include with each Course. Returns an integer for the total amount of active and invited students.

âpassback_statusâ: Include the grade passback_status

âfavoritesâ: Optional information to include with each Course. Indicates if the user has marked the course as a favorite course.

âteachersâ: Teacher information to include with each Course. Returns an array of hashes containing the UserDisplay information for each teacher in the course.

âobserved_usersâ: Optional information to include with each Course. Will include data for observed users if the current user has an observer enrollment.

âtabsâ: Optional information to include with each Course. Will include the list of tabs configured for each course.  See the List available tabs API for more information.

âcourse_imageâ: Optional course image data for when there is a course image and the course image feature flag has been enabled

âconcludedâ: Optional information to include with each Course. Indicates whether the course has been concluded, taking course and term dates into account."""
        "type": "string",
        "required": False,
        "allowed_values": ['needs_grading_count', 'syllabus_body', 'public_description', 'total_scores', 'current_grading_period_scores', 'grading_periods', 'term', 'account', 'course_progress', 'sections', 'storage_quota_used_mb', 'total_students', 'passback_status', 'favorites', 'teachers', 'observed_users', 'course_image', 'concluded'],
    },
    "state[]": {
        """If set, only return courses that are in the given state(s). By default, âavailableâ is returned for students and observers, and anything except âdeletedâ, for all other enrollment types"""
        "type": "string",
        "required": False,
        "allowed_values": ['unpublished', 'available', 'completed', 'deleted'],
    },
}


# GET
def list_your_courses(enrollment_type=None, enrollment_role=None, enrollment_role_id: int=None, enrollment_state=None, exclude_blueprint_courses=None, include: list=None, state: list=None):
    """Returns the paginated list of active courses for the current user."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
list_courses_for_user_params = {
    "include[]": {
        """âneeds_grading_countâ: Optional information to include with each Course. When needs_grading_count is given, and the current user has grading rights, the total number of submissions needing grading for all assignments is returned.

âsyllabus_bodyâ: Optional information to include with each Course. When syllabus_body is given the user-generated html for the course syllabus is returned.

âpublic_descriptionâ: Optional information to include with each Course. When public_description is given the user-generated text for the course public description is returned.

âtotal_scoresâ: Optional information to include with each Course. When total_scores is given, any student enrollments will also include the fields 'computed_current_score', 'computed_final_score', 'computed_current_grade', and 'computed_final_grade' (see Enrollment documentation for more information on these fields). This argument is ignored if the course is configured to hide final grades.

âcurrent_grading_period_scoresâ: Optional information to include with each Course. When current_grading_period_scores is given and total_scores is given, any student enrollments will also include the fields 'has_grading_periods', 'totals_for_all_grading_periods_option', 'current_grading_period_title', 'current_grading_period_id', current_period_computed_current_score', 'current_period_computed_final_score', 'current_period_computed_current_grade', and 'current_period_computed_final_grade', as well as (if the user has permission) 'current_period_unposted_current_score', 'current_period_unposted_final_score', 'current_period_unposted_current_grade', and 'current_period_unposted_final_grade' (see Enrollment documentation for more information on these fields). In addition, when this argument is passed, the course will have a 'has_grading_periods' attribute on it. This argument is ignored if the course is configured to hide final grades or if the total_scores argument is not included.

âgrading_periodsâ: Optional information to include with each Course. When grading_periods is given, a list of the grading periods associated with each course is returned.

âtermâ: Optional information to include with each Course. When term is given, the information for the enrollment term for each course is returned.

âaccountâ: Optional information to include with each Course. When account is given, the account json for each course is returned.

âcourse_progressâ: Optional information to include with each Course. When course_progress is given, each course will include a 'course_progress' object with the fields: 'requirement_count', an integer specifying the total number of requirements in the course, 'requirement_completed_count', an integer specifying the total number of requirements in this course that have been completed, and 'next_requirement_url', a string url to the next requirement item, and 'completed_at', the date the course was completed (null if incomplete). 'next_requirement_url' will be null if all requirements have been completed or the current module does not require sequential progress. âcourse_progressâ will return an error message if the course is not module based or the user is not enrolled as a student in the course.

âsectionsâ: Section enrollment information to include with each Course. Returns an array of hashes containing the section ID (id), section name (name), start and end dates (start_at, end_at), as well as the enrollment type (enrollment_role, e.g. 'StudentEnrollment').

âstorage_quota_used_mbâ: The amount of storage space used by the files in this course

âtotal_studentsâ: Optional information to include with each Course. Returns an integer for the total amount of active and invited students.

âpassback_statusâ: Include the grade passback_status

âfavoritesâ: Optional information to include with each Course. Indicates if the user has marked the course as a favorite course.

âteachersâ: Teacher information to include with each Course. Returns an array of hashes containing the UserDisplay information for each teacher in the course.

âobserved_usersâ: Optional information to include with each Course. Will include data for observed users if the current user has an observer enrollment.

âtabsâ: Optional information to include with each Course. Will include the list of tabs configured for each course.  See the List available tabs API for more information.

âcourse_imageâ: Optional course image data for when there is a course image and the course image feature flag has been enabled

âconcludedâ: Optional information to include with each Course. Indicates whether the course has been concluded, taking course and term dates into account."""
        "type": "string",
        "required": False,
        "allowed_values": ['needs_grading_count', 'syllabus_body', 'public_description', 'total_scores', 'current_grading_period_scores', 'grading_periods', 'term', 'account', 'course_progress', 'sections', 'storage_quota_used_mb', 'total_students', 'passback_status', 'favorites', 'teachers', 'observed_users', 'course_image', 'concluded'],
    },
    "state[]": {
        """If set, only return courses that are in the given state(s). By default, âavailableâ is returned for students and observers, and anything except âdeletedâ, for all other enrollment types"""
        "type": "string",
        "required": False,
        "allowed_values": ['unpublished', 'available', 'completed', 'deleted'],
    },
    "enrollment_state": {
        """When set, only return courses where the user has an enrollment with the given state. This will respect section/course/term date overrides."""
        "type": "string",
        "required": False,
        "allowed_values": ['active', 'invited_or_pending', 'completed'],
    },
    "homeroom": {
        """If set, only return homeroom courses."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
}


# GET
def list_courses_for_user(include: list=None, state: list=None, enrollment_state=None, homeroom=None):
    """Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/users/{user_id}/courses'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
get_user_progress_params = {
}


# GET
def get_user_progress():
    """Return progress information for the user and course"""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/users/{user_id}/progress'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
create_new_course_params = {
    "course[name]": {
        """The name of the course. If omitted, the course will be named âUnnamed Course.â"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[course_code]": {
        """The course code for the course."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[start_at]": {
        """Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true."""
        "type": "DateTime",
        "required": False,
        "allowed_values": [],
    },
    "course[end_at]": {
        """Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true."""
        "type": "DateTime",
        "required": False,
        "allowed_values": [],
    },
    "course[license]": {
        """The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference):

'private' (Private Copyrighted)

'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)

'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)

'cc_by_nc' (CC Attribution Non-Commercial)

'cc_by_nd' (CC Attribution No Derivatives)

'cc_by_sa' (CC Attribution Share Alike)

'cc_by' (CC Attribution)

'public_domain' (Public Domain)."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[is_public]": {
        """Set to true if course is public to both authenticated and unauthenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[is_public_to_auth_users]": {
        """Set to true if course is public only to authenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_syllabus]": {
        """Set to true to make the course syllabus public."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_syllabus_to_auth]": {
        """Set to true to make the course syllabus public for authenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_description]": {
        """A publicly visible description of the course."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_student_wiki_edits]": {
        """If true, students will be able to modify the course wiki."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_wiki_comments]": {
        """If true, course members will be able to comment on wiki pages."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_student_forum_attachments]": {
        """If true, students can attach files to forum posts."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[open_enrollment]": {
        """Set to true if the course is open enrollment."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[self_enrollment]": {
        """Set to true if the course is self enrollment."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[restrict_enrollments_to_course_dates]": {
        """Set to true to restrict user enrollments to the start and end dates of the course. This value must be set to true in order to specify a course start date and/or end date."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[term_id]": {
        """The unique ID of the term to create to course in."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[sis_course_id]": {
        """The unique SIS identifier."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[integration_id]": {
        """The unique Integration identifier."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[hide_final_grades]": {
        """If this option is set to true, the totals in student grades summary will be hidden."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[apply_assignment_group_weights]": {
        """Set to true to weight final grade based on assignment groups percentages."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[time_zone]": {
        """The time zone for the course. Allowed time zones are IANA time zones or friendlier Ruby on Rails time zones."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "offer": {
        """If this option is set to true, the course will be available to students immediately."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "enroll_me": {
        """Set to true to enroll the current user as the teacher."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[default_view]": {
        """The type of page that users will see when they first visit the course

'feed' Recent Activity Dashboard

'modules' Course Modules/Sections Page

'assignments' Course Assignments List

'syllabus' Course Syllabus Page

other types may be added in the future"""
        "type": "string",
        "required": False,
        "allowed_values": ['feed', 'wiki', 'modules', 'syllabus', 'assignments'],
    },
    "course[syllabus_body]": {
        """The syllabus body for the course"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[grading_standard_id]": {
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "course[grade_passback_setting]": {
        """Optional. The grade_passback_setting for the course. Only 'nightly_sync', 'disabled', and '' are allowed"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[course_format]": {
        """Optional. Specifies the format of the course. (Should be 'on_campus', 'online', or 'blended')"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "enable_sis_reactivation": {
        """When true, will first try to re-activate a deleted course with matching sis_course_id if possible."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
}


# POST
def create_new_course(course[name]=None, course[course_code]=None, course[start_at]=None, course[end_at]=None, course[license]=None, course[is_public]=None, course[is_public_to_auth_users]=None, course[public_syllabus]=None, course[public_syllabus_to_auth]=None, course[public_description]=None, course[allow_student_wiki_edits]=None, course[allow_wiki_comments]=None, course[allow_student_forum_attachments]=None, course[open_enrollment]=None, course[self_enrollment]=None, course[restrict_enrollments_to_course_dates]=None, course[term_id]: int=None, course[sis_course_id]: int=None, course[integration_id]: int=None, course[hide_final_grades]: int=None, course[apply_assignment_group_weights]=None, course[time_zone]=None, offer=None, enroll_me=None, course[default_view]=None, course[syllabus_body]=None, course[grading_standard_id]: int=None, course[grade_passback_setting]=None, course[course_format]=None, enable_sis_reactivation=None):
    """Create a new course"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/accounts/{account_id}/courses'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
upload_file_params = {
}


# POST
def upload_file():
    """Upload a file to the course."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/files'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
list_students_params = {
}


# GET
def list_students():
    """Returns the paginated list of students enrolled in this course."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/students'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
list_users_in_course_params = {
    "search_term": {
        """The partial name or full ID of the users to match and return in the results list."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "sort": {
        """When set, sort the results of the search based on the given field."""
        "type": "string",
        "required": False,
        "allowed_values": ['username', 'last_login', 'email', 'sis_id'],
    },
    "enrollment_type[]": {
        """When set, only return users where the user is enrolled as this type. âstudent_viewâ implies include[]=test_student. This argument is ignored if enrollment_role is given."""
        "type": "string",
        "required": False,
        "allowed_values": ['teacher', 'student', 'student_view', 'ta', 'observer', 'designer'],
    },
    "enrollment_role": {
        """Deprecated When set, only return users enrolled with the specified course-level role.  This can be a role created with the Add Role API or a base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "enrollment_role_id": {
        """When set, only return courses where the user is enrolled with the specified course-level role.  This can be a role created with the Add Role API or a built_in role id with type 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment', or 'DesignerEnrollment'."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "include[]": {
        """âenrollmentsâ:

Optionally include with each Course the user's current and invited enrollments. If the user is enrolled as a student, and the account has permission to manage or view all grades, each enrollment will include a 'grades' key with 'current_score', 'final_score', 'current_grade' and 'final_grade' values.

âlockedâ: Optionally include whether an enrollment is locked.

âavatar_urlâ: Optionally include avatar_url.

âbioâ: Optionally include each user's bio.

âtest_studentâ: Optionally include the course's Test Student,

if present. Default is to not include Test Student.

âcustom_linksâ: Optionally include plugin-supplied custom links for each student,

such as analytics information

âcurrent_grading_period_scoresâ: if enrollments is included as

well as this directive, the scores returned in the enrollment will be for the current grading period if there is one. A 'grading_period_id' value will also be included with the scores. if grading_period_id is nil there is no current grading period and the score is a total score.

âuuidâ: Optionally include the users uuid"""
        "type": "string",
        "required": False,
        "allowed_values": ['enrollments', 'locked', 'avatar_url', 'test_student', 'bio', 'custom_links', 'current_grading_period_scores', 'uuid'],
    },
    "user_id": {
        """If this parameter is given and it corresponds to a user in the course, the page parameter will be ignored and the page containing the specified user will be returned instead."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "user_ids[]": {
        """If included, the course users set will only include users with IDs specified by the param. Note: this will not work in conjunction with the âuser_idâ argument but multiple user_ids can be included."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "enrollment_state[]": {
        """When set, only return users where the enrollment workflow state is of one of the given types. âactiveâ and âinvitedâ enrollments are returned by default."""
        "type": "string",
        "required": False,
        "allowed_values": ['active', 'invited', 'rejected', 'completed', 'inactive'],
    },
}


# GET
def list_users_in_course(search_term=None, sort=None, enrollment_type: list=None, enrollment_role=None, enrollment_role_id: int=None, include: list=None, user_id: int=None, user_ids: list=None, enrollment_state: list=None):
    """Returns the paginated list of users in this course. And optionally the user's enrollments in the course."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/users'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
list_recently_logged_in_students_params = {
}


# GET
def list_recently_logged_in_students():
    """Returns the paginated list of users in this course, ordered by how recently they have logged in. The records include the 'last_login' field which contains a timestamp of the last time that user logged into canvas.  The querying user must have the 'View usage reports' permission."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/recent_students'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
get_single_user_params = {
}


# GET
def get_single_user():
    """Return information on a single user."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/users/{user_id}'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
search_for_content_share_users_params = {
    "search_term": {
        """Term used to find users.  Will search available share users with the search term in their name."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
}


# GET
def search_for_content_share_users(search_term=None):
    """Returns a paginated list of users you can share content with.  Requires the content share feature and the user must have the manage content permission for the course."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/content_share_users'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
preview_processed_html_params = {
    "html": {
        """The html content to process"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
}


# POST
def preview_processed_html(html=None):
    """Preview html content processed for this course"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/preview_html'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
course_activity_stream_params = {
}


# GET
def course_activity_stream():
    """Returns the current user's course-specific activity stream, paginated."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/activity_stream'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
course_activity_stream_summary_params = {
}


# GET
def course_activity_stream_summary():
    """Returns a summary of the current user's course-specific activity stream."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/activity_stream/summary'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
course_todo_items_params = {
}


# GET
def course_todo_items():
    """Returns the current user's course-specific todo items."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/todo'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
delete_or_conclude_course_params = {
    "event": {
        """The action to take on the course."""
        "type": "string",
        "required": False,
        "allowed_values": ['delete', 'conclude'],
    },
}


# DELETE
def delete_or_conclude_course(event=None):
    """Delete or conclude an existing course"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}'
    res = requests.delete(endpoint, header=header, params=params)
    return res.json()
get_course_settings_params = {
}


# GET
def get_course_settings():
    """Returns some of a course's settings."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/settings'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
update_course_settings_params = {
    "allow_student_discussion_topics": {
        """Let students create discussion topics"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "allow_student_forum_attachments": {
        """Let students attach files to discussions"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "allow_student_discussion_editing": {
        """Let students edit or delete their own discussion replies"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "allow_student_organized_groups": {
        """Let students organize their own groups"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "allow_student_discussion_reporting": {
        """Let students report offensive discussion content"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "allow_student_anonymous_discussion_topics": {
        """Let students create anonymous discussion topics"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "filter_speed_grader_by_student_group": {
        """Filter SpeedGrader to only the selected student group"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "hide_final_grades": {
        """Hide totals in student grades summary"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "hide_distribution_graphs": {
        """Hide grade distribution graphs from students"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "hide_sections_on_course_users_page": {
        """Disallow students from viewing students in sections they do not belong to"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "lock_all_announcements": {
        """Disable comments on announcements"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "usage_rights_required": {
        """Copyright and license information must be provided for files before they are published."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "restrict_student_past_view": {
        """Restrict students from viewing courses after end date"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "restrict_student_future_view": {
        """Restrict students from viewing courses before start date"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "show_announcements_on_home_page": {
        """Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home_page_announcement_limit). Canvas for Elementary subjects ignore this setting."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "home_page_announcement_limit": {
        """Limit the number of announcements on the home page if enabled via show_announcements_on_home_page"""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "syllabus_course_summary": {
        """Show the course summary (list of assignments and calendar events) on the syllabus page. Default is true."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "default_due_time": {
        """Set the default due time for assignments. This is the time that will be pre-selected in the Canvas user interface when setting a due date for an assignment. It does not change when any existing assignment is due. It should be given in 24-hour HH:MM:SS format. The default is â23:59:59â. Use âinheritâ to inherit the account setting."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "conditional_release": {
        """Enable or disable individual learning paths for students based on assessment"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
}


# PUT
def update_course_settings(allow_student_discussion_topics=None, allow_student_forum_attachments=None, allow_student_discussion_editing=None, allow_student_organized_groups=None, allow_student_discussion_reporting=None, allow_student_anonymous_discussion_topics=None, filter_speed_grader_by_student_group=None, hide_final_grades: int=None, hide_distribution_graphs: int=None, hide_sections_on_course_users_page: int=None, lock_all_announcements=None, usage_rights_required=None, restrict_student_past_view=None, restrict_student_future_view=None, show_announcements_on_home_page=None, home_page_announcement_limit=None, syllabus_course_summary=None, default_due_time=None, conditional_release=None):
    """Can update the following course settings:"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/settings'
    res = requests.put(endpoint, header=header, params=params)
    return res.json()
return_test_student_for_course_params = {
}


# GET
def return_test_student_for_course():
    """Returns information for a test student in this course. Creates a test student if one does not already exist for the course. The caller must have permission to access the course's student view."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/student_view_student'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
get_single_course_params = {
    "include[]": {
        """âall_coursesâ: Also search recently deleted courses.

âpermissionsâ: Include permissions the current user has for the course.

âobserved_usersâ: include observed users in the enrollments

âcourse_imageâ: Optional course image data for when there is a course image and the course image feature flag has been enabled

âconcludedâ: Optional information to include with each Course. Indicates whether the course has been concluded, taking course and term dates into account."""
        "type": "string",
        "required": False,
        "allowed_values": ['needs_grading_count', 'syllabus_body', 'public_description', 'total_scores', 'current_grading_period_scores', 'term', 'account', 'course_progress', 'sections', 'storage_quota_used_mb', 'total_students', 'passback_status', 'favorites', 'teachers', 'observed_users', 'all_courses', 'permissions', 'course_image', 'concluded'],
    },
    "teacher_limit": {
        """The maximum number of teacher enrollments to show. If the course contains more teachers than this, instead of giving the teacher enrollments, the count of teachers will be given under a teacher_count key."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
}


# GET
def get_single_course(include: list=None, teacher_limit=None):
    """Return information on a single course."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
update_course_params = {
    "course[account_id]": {
        """The unique ID of the account to move the course to."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "course[name]": {
        """The name of the course. If omitted, the course will be named âUnnamed Course.â"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[course_code]": {
        """The course code for the course."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[start_at]": {
        """Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true, or the course is already published."""
        "type": "DateTime",
        "required": False,
        "allowed_values": [],
    },
    "course[end_at]": {
        """Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true."""
        "type": "DateTime",
        "required": False,
        "allowed_values": [],
    },
    "course[license]": {
        """The name of the licensing. Should be one of the following abbreviations (a descriptive name is included in parenthesis for reference):

'private' (Private Copyrighted)

'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)

'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)

'cc_by_nc' (CC Attribution Non-Commercial)

'cc_by_nd' (CC Attribution No Derivatives)

'cc_by_sa' (CC Attribution Share Alike)

'cc_by' (CC Attribution)

'public_domain' (Public Domain)."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[is_public]": {
        """Set to true if course is public to both authenticated and unauthenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[is_public_to_auth_users]": {
        """Set to true if course is public only to authenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_syllabus]": {
        """Set to true to make the course syllabus public."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_syllabus_to_auth]": {
        """Set to true to make the course syllabus to public for authenticated users."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[public_description]": {
        """A publicly visible description of the course."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_student_wiki_edits]": {
        """If true, students will be able to modify the course wiki."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_wiki_comments]": {
        """If true, course members will be able to comment on wiki pages."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[allow_student_forum_attachments]": {
        """If true, students can attach files to forum posts."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[open_enrollment]": {
        """Set to true if the course is open enrollment."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[self_enrollment]": {
        """Set to true if the course is self enrollment."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[restrict_enrollments_to_course_dates]": {
        """Set to true to restrict user enrollments to the start and end dates of the course. Setting this value to false will remove the course end date (if it exists), as well as the course start date (if the course is unpublished)."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[term_id]": {
        """The unique ID of the term to create to course in."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "course[sis_course_id]": {
        """The unique SIS identifier."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[integration_id]": {
        """The unique Integration identifier."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[hide_final_grades]": {
        """If this option is set to true, the totals in student grades summary will be hidden."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[time_zone]": {
        """The time zone for the course. Allowed time zones are IANA time zones or friendlier Ruby on Rails time zones."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[apply_assignment_group_weights]": {
        """Set to true to weight final grade based on assignment groups percentages."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[storage_quota_mb]": {
        """Set the storage quota for the course, in megabytes. The caller must have the âManage storage quotasâ account permission."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "offer": {
        """If this option is set to true, the course will be available to students immediately."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[event]": {
        """The action to take on each course.

'claim' makes a course no longer visible to students. This action is also called âunpublishâ on the web site. A course cannot be unpublished if students have received graded submissions.

'offer' makes a course visible to students. This action is also called âpublishâ on the web site.

'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears in prior-enrollment lists.

'delete' completely removes the course from the web site (including course menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a future date.

'undelete' attempts to recover a course that has been deleted. This action requires account administrative rights. (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered."""
        "type": "string",
        "required": False,
        "allowed_values": ['claim', 'offer', 'conclude', 'delete', 'undelete'],
    },
    "course[default_view]": {
        """The type of page that users will see when they first visit the course

'feed' Recent Activity Dashboard

'wiki' Wiki Front Page

'modules' Course Modules/Sections Page

'assignments' Course Assignments List

'syllabus' Course Syllabus Page

other types may be added in the future"""
        "type": "string",
        "required": False,
        "allowed_values": ['feed', 'wiki', 'modules', 'syllabus', 'assignments'],
    },
    "course[syllabus_body]": {
        """The syllabus body for the course"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[syllabus_course_summary]": {
        """Optional. Indicates whether the Course Summary (consisting of the course's assignments and calendar events) is displayed on the syllabus page. Defaults to true."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[grading_standard_id]": {
        """The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "course[grade_passback_setting]": {
        """Optional. The grade_passback_setting for the course. Only 'nightly_sync' and '' are allowed"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[course_format]": {
        """Optional. Specifies the format of the course. (Should be either 'on_campus' or 'online')"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[image_id]": {
        """This is a file ID corresponding to an image file in the course that will be used as the course image. This will clear the course's image_url setting if set.  If you attempt to provide image_url and image_id in a request it will fail."""
        "type": "integer",
        "required": False,
        "allowed_values": [],
    },
    "course[image_url]": {
        """This is a URL to an image to be used as the course image. This will clear the course's image_id setting if set.  If you attempt to provide image_url and image_id in a request it will fail."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[remove_image]": {
        """If this option is set to true, the course image url and course image ID are both set to nil"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[remove_banner_image]": {
        """If this option is set to true, the course banner image url and course banner image ID are both set to nil"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[blueprint]": {
        """Sets the course as a blueprint course."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[blueprint_restrictions]": {
        """Sets a default set to apply to blueprint course objects when restricted, unless use_blueprint_restrictions_by_object_type is enabled. See the Blueprint Restriction documentation"""
        "type": "BlueprintRestriction",
        "required": False,
        "allowed_values": [],
    },
    "course[use_blueprint_restrictions_by_object_type]": {
        """When enabled, the blueprint_restrictions parameter will be ignored in favor of the blueprint_restrictions_by_object_type parameter"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[blueprint_restrictions_by_object_type]": {
        """Allows setting multiple Blueprint Restriction to apply to blueprint course objects of the matching type when restricted. The possible object types are âassignmentâ, âattachmentâ, âdiscussion_topicâ, âquizâ and âwiki_pageâ. Example usage:
course[blueprint_restrictions_by_object_type][assignment][content]=1"""
        "type": "multiple BlueprintRestrictions",
        "required": False,
        "allowed_values": [],
    },
    "course[homeroom_course]": {
        """Sets the course as a homeroom course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[sync_enrollments_from_homeroom]": {
        """Syncs enrollments from the homeroom that is set in homeroom_course_id. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[homeroom_course_id]": {
        """Sets the Homeroom Course id to be used with sync_enrollments_from_homeroom. The setting only takes effect when the course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[template]": {
        """Enable or disable the course as a template that can be selected by an account"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[course_color]": {
        """Sets a color in hex code format to be associated with the course. The setting takes effect only when the course is associated with a Canvas for Elementary-enabled account."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[friendly_name]": {
        """Set a friendly name for the course. If this is provided and the course is associated with a Canvas for Elementary account, it will be shown instead of the course name. This setting takes priority over course nicknames defined by individual users."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "course[enable_course_paces]": {
        """Enable or disable Course Pacing for the course. This setting only has an effect when the Course Pacing feature flag is enabled for the sub-account. Otherwise, Course Pacing are always disabled.
Note: Course Pacing is in active development."""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
    "course[conditional_release]": {
        """Enable or disable individual learning paths for students based on assessment"""
        "type": "boolean",
        "required": False,
        "allowed_values": [],
    },
}


# PUT
def update_course(course[account_id]: int=None, course[name]=None, course[course_code]=None, course[start_at]=None, course[end_at]=None, course[license]=None, course[is_public]=None, course[is_public_to_auth_users]=None, course[public_syllabus]=None, course[public_syllabus_to_auth]=None, course[public_description]=None, course[allow_student_wiki_edits]=None, course[allow_wiki_comments]=None, course[allow_student_forum_attachments]=None, course[open_enrollment]=None, course[self_enrollment]=None, course[restrict_enrollments_to_course_dates]=None, course[term_id]: int=None, course[sis_course_id]: int=None, course[integration_id]: int=None, course[hide_final_grades]: int=None, course[time_zone]=None, course[apply_assignment_group_weights]=None, course[storage_quota_mb]=None, offer=None, course[event]=None, course[default_view]=None, course[syllabus_body]=None, course[syllabus_course_summary]=None, course[grading_standard_id]: int=None, course[grade_passback_setting]=None, course[course_format]=None, course[image_id]: int=None, course[image_url]=None, course[remove_image]=None, course[remove_banner_image]=None, course[blueprint]=None, course[blueprint_restrictions]=None, course[use_blueprint_restrictions_by_object_type]=None, course[blueprint_restrictions_by_object_type]=None, course[homeroom_course]=None, course[sync_enrollments_from_homeroom]=None, course[homeroom_course_id]: int=None, course[template]=None, course[course_color]=None, course[friendly_name]=None, course[enable_course_paces]=None, course[conditional_release]=None):
    """Update an existing course."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}'
    res = requests.put(endpoint, header=header, params=params)
    return res.json()
update_courses_params = {
    "course_ids[]": {
        """List of ids of courses to update. At most 500 courses may be updated in one call."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "event": {
        """The action to take on each course.  Must be one of 'offer', 'conclude', 'delete', or 'undelete'.

'offer' makes a course visible to students. This action is also called âpublishâ on the web site.

'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears in prior-enrollment lists.

'delete' completely removes the course from the web site (including course menus and prior-enrollment lists). All enrollments are deleted. Course content may be physically deleted at a future date.

'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered."""
        "type": "string",
        "required": False,
        "allowed_values": ['offer', 'conclude', 'delete', 'undelete'],
    },
}


# PUT
def update_courses(course_ids: list=None, event=None):
    """Update multiple courses in an account.  Operates asynchronously; use the progress endpoint to query the status of an operation."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/accounts/{account_id}/courses'
    res = requests.put(endpoint, header=header, params=params)
    return res.json()
reset_course_params = {
}


# POST
def reset_course():
    """Deletes the current course, and creates a new equivalent course with no content, but all sections and users moved over."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/reset_content'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
get_effective_due_dates_params = {
    "assignment_ids[]": {
        """no description"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
}


# GET
def get_effective_due_dates(assignment_ids: list=None):
    """For each assignment in the course, returns each assigned student's ID and their corresponding due date along with some grading period data. Returns a collection with keys representing assignment IDs and values as a collection containing keys representing student IDs and values representing the student's effective due_at, the grading_period_id of which the due_at falls in, and whether or not the grading period is closed (in_closed_grading_period)"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/effective_due_dates'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
permissions_params = {
    "permissions[]": {
        """List of permissions to check against the authenticated user. Permission names are documented in the Create a role endpoint."""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
}


# GET
def permissions(permissions: list=None):
    """Returns permission information for the calling user in the given course. See also the Account and Group counterparts."""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/permissions'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
get_bulk_user_progress_params = {
}


# GET
def get_bulk_user_progress():
    """Returns progress information for all users enrolled in the given course."""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/bulk_user_progress'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
remove_quiz_migration_alert_params = {
}


# POST
def remove_quiz_migration_alert():
    """Remove alert about the limitations of quiz migrations that is displayed to a user in a course"""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/dismiss_migration_limitation_message'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
get_course_copy_status_params = {
}


# GET
def get_course_copy_status():
    """DEPRECATED: Please use the Content Migrations API"""
    params = locals().copy()

    endpoint = f'/api/v1/courses/{course_id}/course_copy/{course_copy_id}'
    res = requests.get(endpoint, header=header, params=params)
    return res.json()
copy_course_content_params = {
    "source_course": {
        """ID or SIS-ID of the course to copy the content from"""
        "type": "string",
        "required": False,
        "allowed_values": [],
    },
    "except[]": {
        """A list of the course content types to exclude, all areas not listed will be copied."""
        "type": "string",
        "required": False,
        "allowed_values": ['course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes'],
    },
    "only[]": {
        """A list of the course content types to copy, all areas not listed will not be copied."""
        "type": "string",
        "required": False,
        "allowed_values": ['course_settings', 'assignments', 'external_tools', 'files', 'topics', 'calendar_events', 'quizzes', 'wiki_pages', 'modules', 'outcomes'],
    },
}


# POST
def copy_course_content(source_course=None, except: list=None, only: list=None):
    """DEPRECATED: Please use the Content Migrations API"""
    params = locals().copy()
    del params[""]

    endpoint = f'/api/v1/courses/{course_id}/course_copy'
    res = requests.post(endpoint, header=header, params=params)
    return res.json()
