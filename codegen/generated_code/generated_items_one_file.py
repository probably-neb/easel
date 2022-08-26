
class Scope(Base):
    __tablename__ = 'scope'
    resource = Column(String)
    """The resource the scope is associated with 
        Example: courses"""
    resource_name = Column(String)
    """The localized resource name 
        Example: Courses"""
    controller = Column(String)
    """The controller the scope is associated to 
        Example: courses"""
    action = Column(String)
    """The controller action the scope is associated to 
        Example: index"""
    verb = Column(String)
    """The HTTP verb for the scope 
        Example: GET"""
    scope = Column(String)
    """The identifier for the scope 
        Example: url:GET|/api/v1/courses"""


class CalendarEvent(Base):
    __tablename__ = 'calendar_event'
    id = Column(Integer)
    """The ID of the calendar event 
        Example: 234"""
    title = Column(String)
    """The title of the calendar event 
        Example: Paintball Fight!"""
    start_at = Column(DateTime)
    """The start timestamp of the event 
        Example: 2012-07-19T15:00:00-06:00"""
    end_at = Column(DateTime)
    """The end timestamp of the event 
        Example: 2012-07-19T16:00:00-06:00"""
    description = Column(String)
    """The HTML description of the event 
        Example: <b>It's that time again!</b>"""
    location_name = Column(String)
    """The location name of the event 
        Example: Greendale Community College"""
    location_address = Column(String)
    """The address where the event is taking place 
        Example: Greendale, Colorado"""
    context_code = Column(String)
    """the context code of the calendar this event belongs to (course, user or group) 
        Example: course_123"""
    effective_context_code = Column(String)
    """if specified, it indicates which calendar this event should be displayed on. for example, a section-level event would have the course's context code here, while the section's context code would be returned above) 
        Example: None"""
    context_name = Column(String)
    """the context name of the calendar this event belongs to (course, user or group) 
        Example: Chemistry 101"""
    all_context_codes = Column(String)
    """a comma-separated list of all calendar contexts this event is part of 
        Example: course_123,course_456"""
    workflow_state = Column(String)
    """Current state of the event ('active', 'locked' or 'deleted') 'locked' indicates that start_at/end_at cannot be changed (though the event could be deleted). Normally only reservations or time slots with reservations are locked (see the Appointment Groups API) 
        Example: active"""
    hidden = Column(Boolean)
    """Whether this event should be displayed on the calendar. Only true for course-level events with section-level child events. 
        Example: None"""
    parent_event_id = Column(Integer)
    """Normally null. If this is a reservation (see the Appointment Groups API), the id will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event. 
        Example: None"""
    child_events_count = Column(Integer)
    """The number of child_events. See child_events (and parent_event_id) 
        Example: None"""
    child_events = Column(JsonObject)
"""List[int]"""
    """Included by default, but may be excluded (see include[] option). If this is a time slot (see the Appointment Groups API) this will be a list of any reservations. If this is a course-level event, this will be a list of section-level events (if any) 
        Example: None"""
    url = Column(String)
    """URL for this calendar event (to update, delete, etc.) 
        Example: https://example.com/api/v1/calendar_events/234"""
    html_url = Column(String)
    """URL for a user to view this event 
        Example: https://example.com/calendar?event_id=234&include_contexts=course_123"""
    all_day_date = Column(DateTime)
    """The date of this event 
        Example: 2012-07-19"""
    all_day = Column(Boolean)
    """Boolean indicating whether this is an all-day event (midnight to midnight) 
        Example: None"""
    created_at = Column(DateTime)
    """When the calendar event was created 
        Example: 2012-07-12T10:55:20-06:00"""
    updated_at = Column(DateTime)
    """When the calendar event was last updated 
        Example: 2012-07-12T10:55:20-06:00"""
    appointment_group_id = Column(Integer)
    """Various Appointment-Group-related fields.These fields are only pertinent to time slots (appointments) and reservations of those time slots. See the Appointment Groups API. The id of the appointment group 
        Example: None"""
    appointment_group_url = Column(String)
    """The API URL of the appointment group 
        Example: None"""
    own_reservation = Column(Boolean)
    """If the event is a reservation, this a boolean indicating whether it is the current user's reservation, or someone else's 
        Example: None"""
    reserve_url = Column(String)
    """If the event is a time slot, the API URL for reserving it 
        Example: None"""
    reserved = Column(Boolean)
    """If the event is a time slot, a boolean indicating whether the user has already made a reservation for it 
        Example: None"""
    participant_type = Column(String)
    """The type of participant to sign up for a slot: 'User' or 'Group' 
        Example: User"""
    participants_per_appointment = Column(Integer)
    """If the event is a time slot, this is the participant limit 
        Example: None"""
    available_slots = Column(Integer)
    """If the event is a time slot and it has a participant limit, an integer indicating how many slots are available 
        Example: None"""
    user = Column(String)
    """If the event is a user-level reservation, this will contain the user participant JSON (refer to the Users API). 
        Example: None"""
    group = Column(String)
    """If the event is a group-level reservation, this will contain the group participant JSON (refer to the Groups API). 
        Example: None"""
    important_dates = Column(Boolean)
    """Boolean indicating whether this has important dates. 
        Example: True"""


class AssignmentEvent(Base):
    __tablename__ = 'assignment_event'
    id = Column(String)
    """A synthetic ID for the assignment 
        Example: assignment_987"""
    title = Column(String)
    """The title of the assignment 
        Example: Essay"""
    start_at = Column(DateTime)
    """The due_at timestamp of the assignment 
        Example: 2012-07-19T23:59:00-06:00"""
    end_at = Column(DateTime)
    """The due_at timestamp of the assignment 
        Example: 2012-07-19T23:59:00-06:00"""
    description = Column(String)
    """The HTML description of the assignment 
        Example: <b>Write an essay. Whatever you want.</b>"""
    context_code = Column(String)
    """the context code of the (course) calendar this assignment belongs to 
        Example: course_123"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['published', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the assignment ('published' or 'deleted') 
        Example: published"""
    url = Column(String)
    """URL for this assignment (note that updating/deleting should be done via the Assignments API) 
        Example: https://example.com/api/v1/calendar_events/assignment_987"""
    html_url = Column(String)
    """URL for a user to view this assignment 
        Example: http://example.com/courses/123/assignments/987"""
    all_day_date = Column(DateTime)
    """The due date of this assignment 
        Example: 2012-07-19"""
    all_day = Column(Boolean)
    """Boolean indicating whether this is an all-day event (e.g. assignment due at midnight) 
        Example: True"""
    created_at = Column(DateTime)
    """When the assignment was created 
        Example: 2012-07-12T10:55:20-06:00"""
    updated_at = Column(DateTime)
    """When the assignment was last updated 
        Example: 2012-07-12T10:55:20-06:00"""
    assignment = relationship('Assignment')
    """The full assignment JSON data (See the Assignments API) 
        Example: None"""
    assignment_overrides = relationship('AssignmentOverride')
    """The list of AssignmentOverrides that apply to this event (See the Assignments API). This information is useful for determining which students or sections this assignment-due event applies to. 
        Example: None"""
    important_dates = Column(Boolean)
    """Boolean indicating whether this has important dates. 
        Example: True"""


class ProvisionalGrade(Base):
    __tablename__ = 'provisional_grade'
    provisional_grade_id = Column(Integer)
    """The identifier for the provisional grade 
        Example: 23"""
    score = Column(Integer)
    """The numeric score 
        Example: 90"""
    grade = Column(String)
    """The grade 
        Example: A-"""
    grade_matches_current_submission = Column(Boolean)
    """Whether the grade was applied to the most current submission (false if the student resubmitted after grading) 
        Example: True"""
    graded_at = Column(DateTime)
    """When the grade was given 
        Example: 2015-11-01T00:03:21-06:00"""
    final = Column(Boolean)
    """Whether this is the 'final' provisional grade created by the moderator 
        Example: None"""
    speedgrader_url = Column(String)
    """A link to view this provisional grade in SpeedGrader™ 
        Example: http://www.example.com/courses/123/gradebook/speed_grader?..."""


class FileAttachment(Base):
    """A file attachment"""
    __tablename__ = 'file_attachment'
    content_type = Column(String)
    """None 
        Example: unknown/unknown"""
    url = Column(String)
    """None 
        Example: http://www.example.com/courses/1/files/1/download"""
    filename = Column(String)
    """None 
        Example: content.txt"""
    display_name = Column(String)
    """None 
        Example: content.txt"""


class DiscussionTopic(Base):
    """A discussion topic"""
    __tablename__ = 'discussion_topic'
    id = Column(Integer)
    """The ID of this topic. 
        Example: 1"""
    title = Column(String)
    """The topic title. 
        Example: Topic 1"""
    message = Column(String)
    """The HTML content of the message body. 
        Example: <p>content here</p>"""
    html_url = Column(String)
    """The URL to the discussion topic in canvas. 
        Example: https://<canvas>/courses/1/discussion_topics/2"""
    posted_at = Column(DateTime)
    """The datetime the topic was posted. If it is null it hasn't been posted yet. (see delayed_post_at) 
        Example: 2037-07-21T13:29:31Z"""
    last_reply_at = Column(DateTime)
    """The datetime for when the last reply was in the topic. 
        Example: 2037-07-28T19:38:31Z"""
    require_initial_post = Column(Boolean)
    """If true then a user may not respond to other replies until that user has made an initial reply. Defaults to false. 
        Example: None"""
    user_can_see_posts = Column(Boolean)
    """Whether or not posts in this topic are visible to the user. 
        Example: True"""
    discussion_subentry_count = Column(Integer)
    """The count of entries in the topic. 
        Example: None"""
    readStateEnum = enum.Enum('readStateEnum', ['read', 'unread'])
    """Enum for the allowed values of the read_state field"""
    read_state = Column(Enum(readStateEnum))
    """The read_state of the topic for the current user, 'read' or 'unread'. 
        Example: read"""
    unread_count = Column(Integer)
    """The count of unread entries of this topic for the current user. 
        Example: None"""
    subscribed = Column(Boolean)
    """Whether or not the current user is subscribed to this topic. 
        Example: True"""
    subscriptionHoldEnum = enum.Enum('subscriptionHoldEnum', ['initial_post_required', 'not_in_group_set', 'not_in_group', 'topic_is_announcement'])
    """Enum for the allowed values of the subscription_hold field"""
    subscription_hold = Column(Enum(subscriptionHoldEnum))
    """(Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first; 'not_in_group_set': The user is not in the group set for this graded group discussion; 'not_in_group': The user is not in this topic's group; 'topic_is_announcement': This topic is an announcement 
        Example: not_in_group_set"""
    assignment_id = Column(Integer)
    """The unique identifier of the assignment if the topic is for grading, otherwise null. 
        Example: None"""
    delayed_post_at = Column(DateTime)
    """The datetime to publish the topic (if not right away). 
        Example: None"""
    published = Column(Boolean)
    """Whether this discussion topic is published (true) or draft state (false) 
        Example: True"""
    lock_at = Column(DateTime)
    """The datetime to lock the topic (if ever). 
        Example: None"""
    locked = Column(Boolean)
    """Whether or not the discussion is 'closed for comments'. 
        Example: None"""
    pinned = Column(Boolean)
    """Whether or not the discussion has been 'pinned' by an instructor 
        Example: None"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: True"""
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: None"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This discussion is locked until September 1 at 12:00am"""
    user_name = Column(String)
    """The username of the topic creator. 
        Example: User Name"""
    topic_children = Column(JsonObject)
"""List[int]"""
    """DEPRECATED An array of topic_ids for the group discussions the user is a part of. 
        Example: [5, 7, 10]"""
    group_topic_children = Column(JsonObject)
"""List[Unknown]"""
    """An array of group discussions the user is a part of. Fields include: id, group_id 
        Example: [{'id': 5, 'group_id': 1}, {'id': 7, 'group_id': 5}, {'id': 10, 'group_id': 4}]"""
    root_topic_id = Column(Integer)
    """If the topic is for grading and a group assignment this will point to the original topic in the course. 
        Example: None"""
    podcast_url = Column(String)
    """If the topic is a podcast topic this is the feed url for the current user. 
        Example: /feeds/topics/1/enrollment_1XAcepje4u228rt4mi7Z1oFbRpn3RAkTzuXIGOPe.rss"""
    discussionTypeEnum = enum.Enum('discussionTypeEnum', ['side_comment', 'threaded'])
    """Enum for the allowed values of the discussion_type field"""
    discussion_type = Column(Enum(discussionTypeEnum))
    """The type of discussion. Values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. 
        Example: side_comment"""
    group_category_id = Column(Integer)
    """The unique identifier of the group category if the topic is a group discussion, otherwise null. 
        Example: None"""
    attachments = Column(JsonObject)
"""List[FileAttachment]"""
    """Array of file attachments. 
        Example: None"""
    permissions = Column(JsonObject)
"""Dict[str, bool]"""
    """The current user's permissions on this topic. 
        Example: {'attach': True}"""
    allow_rating = Column(Boolean)
    """Whether or not users can rate entries in this topic. 
        Example: True"""
    only_graders_can_rate = Column(Boolean)
    """Whether or not grade permissions are required to rate entries. 
        Example: True"""
    sort_by_rating = Column(Boolean)
    """Whether or not entries should be sorted by rating. 
        Example: True"""


class GradingSchemeEntry(Base):
    __tablename__ = 'grading_scheme_entry'
    name = Column(String)
    """The name for an entry value within a GradingStandard that describes the range of the value 
        Example: A"""
    value = Column(Integer)
    """The value for the name of the entry within a GradingStandard.  The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. 
        Example: 0.9"""


class GradingStandard(Base):
    __tablename__ = 'grading_standard'
    title = Column(String)
    """the title of the grading standard 
        Example: Account Standard"""
    id = Column(Integer)
    """the id of the grading standard 
        Example: 1"""
    context_type = Column(String)
    """the context this standard is associated with, either 'Account' or 'Course' 
        Example: Account"""
    context_id = Column(Integer)
    """the id for the context either the Account or Course id 
        Example: 1"""
    grading_scheme = Column(JsonObject)
"""List[GradingSchemeEntry]"""
    """A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value 
        Example: [{'name': 'A', 'value': 0.9}, {'name': 'B', 'value': 0.8}, {'name': 'C', 'value': 0.7}, {'name': 'D', 'value': 0.6}]"""


class ePortfolio(Base):
    __tablename__ = 'e_portfolio'
    id = Column(Integer)
    """The database ID of the ePortfolio 
        Example: 1"""
    user_id = Column(Integer)
    """The user ID to which the ePortfolio belongs 
        Example: 1"""
    name = Column(String)
    """The name of the ePortfolio 
        Example: My Academic Journey"""
    public = Column(Boolean)
    """Whether or not the ePortfolio is visible without authentication 
        Example: True"""
    created_at = Column(DateTime)
    """The creation timestamp for the ePortfolio 
        Example: 2021-09-20T18:59:37Z"""
    updated_at = Column(DateTime)
    """The timestamp of the last time any of the ePortfolio attributes changed 
        Example: 2021-09-20T18:59:37Z"""
    workflow_state = Column(String)
    """The state of the ePortfolio. Either 'active' or 'deleted' 
        Example: active"""
    deleted_at = Column(DateTime)
    """The timestamp when the ePortfolio was deleted, or else null 
        Example: 2021-09-20T18:59:37Z"""
    spam_status = Column(String)
    """A flag indicating whether the ePortfolio has beenflagged or moderated as spam. One of 'flagged_as_possible_spam','marked_as_safe', 'marked_as_spam', or null 
        Example: None"""


class ePortfolioPage(Base):
    __tablename__ = 'e_portfolio_page'
    id = Column(Integer)
    """The database ID of the ePortfolio 
        Example: 1"""
    eportfolio_id = Column(Integer)
    """The ePortfolio ID to which the entry belongs 
        Example: 1"""
    position = Column(Integer)
    """The positional order of the entry in the list 
        Example: 1"""
    name = Column(String)
    """The name of the ePortfolio 
        Example: My Academic Journey"""
    content = Column(String)
    """The user entered content of the entry 
        Example: A long time ago..."""
    created_at = Column(DateTime)
    """The creation timestamp for the ePortfolio 
        Example: 2021-09-20T18:59:37Z"""
    updated_at = Column(DateTime)
    """The timestamp of the last time any of the ePortfolio attributes changed 
        Example: 2021-09-20T18:59:37Z"""


class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer)
    """ 
        Example: 1,"""
    name = Column(String)
    """ 
        Example: Default Term"""
    start_at = Column(DateTime)
    """ 
        Example: 2012-06-01T00:00:00-06:00"""
    end_at = Column(DateTime)
    """ 
        Example: null"""


class CourseProgress(Base):
    __tablename__ = 'course_progress'
    requirement_count = Column(Integer)
    """total number of requirements from all modules 
        Example: 10,"""
    requirement_completed_count = Column(Integer)
    """total number of requirements the user has completed from all modules 
        Example: 1,"""
    next_requirement_url = Column(String)
    """url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress 
        Example: http://localhost/courses/1/modules/items/2"""
    completed_at = Column(DateTime)
    """date the course was completed. null if the course has not been completed by this user 
        Example: 2013-06-01T00:00:00-06:00"""
    id = Column(Integer)
    """The unique identifier of the CourseProgress 
        Example: 123456"""


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer)
    """the unique identifier for the course 
        Example: 370663,"""
    sis_course_id = Column(String)
    """the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information. 
        Example: null,"""
    uuid = Column(String)
    """the UUID of the course 
        Example: WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5"""
    integration_id = Column(String)
    """the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information. 
        Example: null,"""
    sis_import_id = Column(Integer)
    """the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: 34,"""
    name = Column(String)
    """the full name of the course. If the requesting user has set a nickname for the course, the nickname will be shown here. 
        Example: InstructureCon 2012"""
    course_code = Column(String)
    """the course code 
        Example: INSTCON12"""
    original_name = Column(String)
    """the actual course name. This field is returned only if the requesting user has set a nickname for the course. 
        Example: InstructureCon-2012-01"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['unpublished', 'available', 'completed', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted' 
        Example: available"""
    account_id = Column(Integer)
    """the account associated with the course 
        Example: 81259,"""
    root_account_id = Column(Integer)
    """the root account associated with the course 
        Example: 81259,"""
    enrollment_term_id = Column(Integer)
    """the enrollment term associated with the course 
        Example: 34,"""
    grading_periods = Column(JsonObject)
"""List[GradingPeriod]"""
    """A list of grading periods associated with the course 
        Example: null,"""
    grading_standard_id = Column(Integer)
    """the grading standard associated with the course 
        Example: 25,"""
    grade_passback_setting = Column(String)
    """the grade_passback_setting set on the course 
        Example: nightly_sync"""
    created_at = Column(DateTime)
    """the date the course was created. 
        Example: 2012-05-01T00:00:00-06:00"""
    start_at = Column(DateTime)
    """the start date for the course, if applicable 
        Example: 2012-06-01T00:00:00-06:00"""
    end_at = Column(DateTime)
    """the end date for the course, if applicable 
        Example: 2012-09-01T00:00:00-06:00"""
    locale = Column(String)
    """the course-set locale, if applicable 
        Example: en"""
    enrollments = Column(JsonObject)
"""List[Enrollment]"""
    """A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores 
        Example: null,"""
    total_students = Column(Integer)
    """optional: the total number of active and invited students in the course 
        Example: 32,"""
    calendar = relationship('CalendarLink')
    """course calendar 
        Example: null,"""
    defaultViewEnum = enum.Enum('defaultViewEnum', ['feed', 'wiki', 'modules', 'syllabus', 'assignments'])
    """Enum for the allowed values of the default_view field"""
    default_view = Column(Enum(defaultViewEnum))
    """the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future 
        Example: feed"""
    syllabus_body = Column(String)
    """optional: user-generated HTML for the course syllabus 
        Example: <p>syllabus html goes here</p>"""
    needs_grading_count = Column(Integer)
    """optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count 
        Example: 17,"""
    term = relationship('Term')
    """optional: the enrollment term object for the course returned only if include[]=term 
        Example: null,"""
    course_progress = relationship('CourseProgress')
    """optional: information on progress through the course returned only if include[]=course_progress 
        Example: null,"""
    apply_assignment_group_weights = Column(Boolean)
    """weight final grade based on assignment group percentages 
        Example: true,"""
    permissions = Column(JsonObject)
"""Dict[str, bool]"""
    """optional: the permissions the user has for the course. returned only for a single course and include[]=permissions 
        Example: {'create_discussion_topic': True, 'create_announcement': True}"""
    is_public = Column(Boolean)
    """ 
        Example: true,"""
    is_public_to_auth_users = Column(Boolean)
    """ 
        Example: true,"""
    public_syllabus = Column(Boolean)
    """ 
        Example: true,"""
    public_syllabus_to_auth = Column(Boolean)
    """ 
        Example: true,"""
    public_description = Column(String)
    """optional: the public description of the course 
        Example: Come one, come all to InstructureCon 2012!"""
    storage_quota_mb = Column(Integer)
    """ 
        Example: 5,"""
    storage_quota_used_mb = Column(Integer)
    """ 
        Example: 5,"""
    hide_final_grades = Column(Boolean)
    """ 
        Example: false,"""
    license = Column(String)
    """ 
        Example: Creative Commons"""
    allow_student_assignment_edits = Column(Boolean)
    """ 
        Example: false,"""
    allow_wiki_comments = Column(Boolean)
    """ 
        Example: false,"""
    allow_student_forum_attachments = Column(Boolean)
    """ 
        Example: false,"""
    open_enrollment = Column(Boolean)
    """ 
        Example: true,"""
    self_enrollment = Column(Boolean)
    """ 
        Example: false,"""
    restrict_enrollments_to_course_dates = Column(Boolean)
    """ 
        Example: false,"""
    course_format = Column(String)
    """ 
        Example: online"""
    access_restricted_by_date = Column(Boolean)
    """optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings 
        Example: false,"""
    time_zone = Column(String)
    """The course's IANA time zone name. 
        Example: America/Denver"""
    blueprint = Column(Boolean)
    """optional: whether the course is set as a Blueprint Course (blueprint fields require the Blueprint Courses feature) 
        Example: true,"""
    blueprint_restrictions = relationship('Unknown')
    """optional: Set of restrictions applied to all locked course objects 
        Example: {'content': True, 'points': True, 'due_dates': False, 'availability_dates': False}"""
    blueprint_restrictions_by_object_type = relationship('Unknown')
    """optional: Sets of restrictions differentiated by object type applied to locked course objects 
        Example: {'assignment': {'content': True, 'points': True}, 'wiki_page': {'content': True}}"""
    template = Column(Boolean)
    """optional: whether the course is set as a template (requires the Course Templates feature) 
        Example: true"""


class CalendarLink(Base):
    __tablename__ = 'calendar_link'
    ics = Column(String)
    """The URL of the calendar in ICS format 
        Example: https://canvas.instructure.com/feeds/calendars/course_abcdef.ics"""
    id = Column(Integer)
    """The unique identifier of the CalendarLink 
        Example: 123456"""


class File(Base):
    __tablename__ = 'file'
    id = Column(Integer)
    """None 
        Example: 569"""
    uuid = Column(String)
    """None 
        Example: SUj23659sdfASF35h265kf352YTdnC4"""
    folder_id = Column(Integer)
    """None 
        Example: 4207"""
    display_name = Column(String)
    """None 
        Example: file.txt"""
    filename = Column(String)
    """None 
        Example: file.txt"""
    content_type = Column(String)
    """None 
        Example: text/plain"""
    url = Column(String)
    """None 
        Example: http://www.example.com/files/569/download?download_frd=1&verifier=c6HdZmxOZa0Fiin2cbvZeI8I5ry7yqD7RChQzb6P"""
    size = Column(Integer)
    """file size in bytes 
        Example: 43451"""
    created_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    updated_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    unlock_at = Column(DateTime)
    """None 
        Example: 2012-07-07T14:58:50Z"""
    locked = Column(Boolean)
    """None 
        Example: None"""
    hidden = Column(Boolean)
    """None 
        Example: None"""
    lock_at = Column(DateTime)
    """None 
        Example: 2012-07-20T14:58:50Z"""
    hidden_for_user = Column(Boolean)
    """None 
        Example: None"""
    thumbnail_url = Column(String)
    """None 
        Example: None"""
    modified_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    mime_class = Column(String)
    """simplified content-type mapping 
        Example: html"""
    media_entry_id = Column(String)
    """identifier for file in third-party transcoding service 
        Example: m-3z31gfpPf129dD3sSDF85SwSDFnwe"""
    locked_for_user = Column(Boolean)
    """None 
        Example: None"""
    lock_info = relationship('LockInfo')
    """None 
        Example: None"""
    lock_explanation = Column(String)
    """None 
        Example: This assignment is locked until September 1 at 12:00am"""
    preview_url = Column(String)
    """optional: url to the document preview. This url is specific to the user making the api call. Only included in submission endpoints. 
        Example: None"""


class ConferenceRecording(Base):
    __tablename__ = 'conference_recording'
    duration_minutes = Column(Integer)
    """None 
        Example: None"""
    title = Column(String)
    """None 
        Example: course2: Test conference 3 [170]_0"""
    updated_at = Column(DateTime)
    """None 
        Example: 2013-12-12T16:09:33.903-07:00"""
    created_at = Column(DateTime)
    """None 
        Example: 2013-12-12T16:09:09.960-07:00"""
    playback_url = Column(String)
    """None 
        Example: http://example.com/recording_url"""


class Conference(Base):
    __tablename__ = 'conference'
    id = Column(Integer)
    """The id of the conference 
        Example: 170"""
    conference_type = Column(String)
    """The type of conference 
        Example: AdobeConnect"""
    conference_key = Column(String)
    """The 3rd party's ID for the conference 
        Example: abcdjoelisgreatxyz"""
    description = Column(String)
    """The description for the conference 
        Example: Conference Description"""
    duration = Column(Integer)
    """The expected duration the conference is supposed to last 
        Example: 60"""
    ended_at = Column(DateTime)
    """The date that the conference ended at, null if it hasn't ended 
        Example: 2013-12-13T17:23:26Z"""
    started_at = Column(DateTime)
    """The date the conference started at, null if it hasn't started 
        Example: 2013-12-12T23:02:17Z"""
    title = Column(String)
    """The title of the conference 
        Example: Test conference"""
    users = Column(JsonObject)
"""List[int]"""
    """Array of user ids that are participants in the conference 
        Example: [1, 7, 8, 9, 10]"""
    has_advanced_settings = Column(Boolean)
    """True if the conference type has advanced settings. 
        Example: None"""
    long_running = Column(Boolean)
    """If true the conference is long running and has no expected end time 
        Example: None"""
    user_settings = relationship('Unknown')
    """A collection of settings specific to the conference type 
        Example: {'record': True}"""
    recordings = Column(JsonObject)
"""List[ConferenceRecording]"""
    """A List of recordings for the conference 
        Example: None"""
    url = Column(String)
    """URL for the conference, may be null if the conference type doesn't set it 
        Example: None"""
    join_url = Column(String)
    """URL to join the conference, may be null if the conference type doesn't set it 
        Example: None"""
    context_type = Column(String)
    """The type of this conference's context, typically 'Course' or 'Group'. 
        Example: None"""
    context_id = Column(Integer)
    """The ID of this conference's context. 
        Example: None"""


class Submission(Base):
    __tablename__ = 'submission'
    assignment_id = Column(Integer)
    """The submission's assignment id 
        Example: 23"""
    assignment = relationship('Assignment')
    """The submission's assignment (see the assignments API) (optional) 
        Example: None"""
    course = relationship('Course')
    """The submission's course (see the course API) (optional) 
        Example: None"""
    attempt = Column(Integer)
    """This is the submission attempt number. 
        Example: 1"""
    body = Column(String)
    """The content of the submission, if it was submitted directly in a text field. 
        Example: There are three factors too..."""
    grade = Column(String)
    """The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example). 
        Example: A-"""
    grade_matches_current_submission = Column(Boolean)
    """A boolean flag which is false if the student has re-submitted since the submission was last graded. 
        Example: True"""
    html_url = Column(String)
    """URL to the submission. This will require the user to log in. 
        Example: http://example.com/courses/255/assignments/543/submissions/134"""
    preview_url = Column(String)
    """URL to the submission preview. This will require the user to log in. 
        Example: http://example.com/courses/255/assignments/543/submissions/134?preview=1"""
    score = Column(Integer)
    """The raw score 
        Example: 13.5"""
    submission_comments = Column(JsonObject)
"""List[SubmissionComment]"""
    """Associated comments for a submission (optional) 
        Example: None"""
    submissionTypeEnum = enum.Enum('submissionTypeEnum', ['online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_type field"""
    submission_type = Column(Enum(submissionTypeEnum))
    """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation') 
        Example: online_text_entry"""
    submitted_at = Column(DateTime)
    """The timestamp when the assignment was submitted 
        Example: 2012-01-01T01:00:00Z"""
    url = Column(String)
    """The URL of the submission (for 'online_url' submissions). 
        Example: None"""
    user_id = Column(Integer)
    """The id of the user who created the submission 
        Example: 134"""
    grader_id = Column(Integer)
    """The id of the user who graded the submission. This will be null for submissions that haven't been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools).  Specifically autograded quizzes set grader_id to the negative of the quiz id.  Submissions autograded by LTI tools set grader_id to the negative of the tool id. 
        Example: 86"""
    graded_at = Column(DateTime)
    """None 
        Example: 2012-01-02T03:05:34Z"""
    user = relationship('User')
    """The submissions user (see user API) (optional) 
        Example: None"""
    late = Column(Boolean)
    """Whether the submission was made after the applicable due date 
        Example: None"""
    assignment_visible = Column(Boolean)
    """Whether the assignment is visible to the user who submitted the assignment. Submissions where `assignment_visible` is false no longer count towards the student's grade and the assignment can no longer be accessed by the student. `assignment_visible` becomes false for submissions that do not have a grade and whose assignment is no longer assigned to the student's section. 
        Example: True"""
    excused = Column(Boolean)
    """Whether the assignment is excused.  Excused assignments have no impact on a user's grade. 
        Example: True"""
    missing = Column(Boolean)
    """Whether the assignment is missing. 
        Example: True"""
    late_policy_status = Column(String)
    """The status of the submission in relation to the late policy. Can be late, missing, extended, none, or null. 
        Example: missing"""
    points_deducted = Column(Integer)
    """The amount of points automatically deducted from the score by the missing/late policy for a late or missing assignment. 
        Example: 12.3"""
    seconds_late = Column(Integer)
    """The amount of time, in seconds, that an submission is late by. 
        Example: 300"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['graded', 'submitted', 'unsubmitted', 'pending_review'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The current state of the submission 
        Example: submitted"""
    extra_attempts = Column(Integer)
    """Extra submission attempts allowed for the given user and assignment. 
        Example: 10"""
    anonymous_id = Column(String)
    """A unique short ID identifying this submission without reference to the owning user. Only included if the caller has administrator access for the current account. 
        Example: acJ4Q"""
    posted_at = Column(DateTime)
    """The date this submission was posted to the student, or nil if it has not been posted. 
        Example: 2020-01-02T11:10:30Z"""
    readStatusEnum = enum.Enum('readStatusEnum', ['read', 'unread'])
    """Enum for the allowed values of the read_status field"""
    read_status = Column(Enum(readStatusEnum))
    """The read status of this submission for the given user (optional). Including read_status will mark submission(s) as read. 
        Example: read"""
    redo_request = Column(Boolean)
    """This indicates whether the submission has been reassigned by the instructor. 
        Example: true"""


class RolePermissions(Base):
    __tablename__ = 'role_permissions'
    enabled = Column(Boolean)
    """Whether the role has the permission 
        Example: True"""
    locked = Column(Boolean)
    """Whether the permission is locked by this role 
        Example: None"""
    applies_to_self = Column(Boolean)
    """Whether the permission applies to the account this role is in. Only present if enabled is true 
        Example: True"""
    applies_to_descendants = Column(Boolean)
    """Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true 
        Example: None"""
    readonly = Column(Boolean)
    """Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role). 
        Example: None"""
    explicit = Column(Boolean)
    """Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role. 
        Example: True"""
    prior_default = Column(Boolean)
    """The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true. 
        Example: None"""


class Role(Base):
    __tablename__ = 'role'
    label = Column(String)
    """The label of the role. 
        Example: New Role"""
    role = Column(String)
    """The label of the role. (Deprecated alias for 'label') 
        Example: New Role"""
    base_role_type = Column(String)
    """The role type that is being used as a base for this role. For account-level roles, this is 'AccountMembership'. For course-level roles, it is an enrollment type. 
        Example: AccountMembership"""
    account = relationship('Account')
    """JSON representation of the account the role is in. 
        Example: {'id': 1019, 'name': 'CGNU', 'parent_account_id': 73, 'root_account_id': 1, 'sis_account_id': 'cgnu'}"""
    workflow_state = Column(String)
    """The state of the role: 'active', 'inactive', or 'built_in' 
        Example: active"""
    permissions = Column(JsonObject)
"""Dict[str, RolePermissions]"""
    """A dictionary of permissions keyed by name (see permissions input parameter in the 'Create a role' API). 
        Example: {'read_course_content': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_course_list': {'enabled': True, 'locked': True, 'readonly': True, 'explicit': False}, 'read_question_banks': {'enabled': False, 'locked': True, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_reports': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': False}}"""


class Grade(Base):
    __tablename__ = 'grade'
    html_url = Column(String)
    """The URL to the Canvas web UI page for the user's grades, if this is a student enrollment. 
        Example: None"""
    current_grade = Column(String)
    """The user's current grade in the class. Only included if user has permissions to view this grade. 
        Example: None"""
    final_grade = Column(String)
    """The user's final grade for the class. Only included if user has permissions to view this grade. 
        Example: None"""
    current_score = Column(String)
    """The user's current score in the class. Only included if user has permissions to view this score. 
        Example: None"""
    final_score = Column(String)
    """The user's final score for the class. Only included if user has permissions to view this score. 
        Example: None"""
    current_points = Column(Integer)
    """The total points the user has earned in the class. Only included if user has permissions to view this score and 'current_points' is passed in the request's 'include' parameter. 
        Example: 150"""
    unposted_current_grade = Column(String)
    """The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. 
        Example: None"""
    unposted_final_grade = Column(String)
    """The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. 
        Example: None"""
    unposted_current_score = Column(String)
    """The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: None"""
    unposted_final_score = Column(String)
    """The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: None"""
    unposted_current_points = Column(Integer)
    """The total points the user has earned in the class, including muted/unposted assignments. Only included if user has permissions to view this score (typically teachers, TAs, and admins) and 'current_points' is passed in the request's 'include' parameter. 
        Example: 150"""


class Enrollment(Base):
    __tablename__ = 'enrollment'
    id = Column(Integer)
    """The ID of the enrollment. 
        Example: 1"""
    course_id = Column(Integer)
    """The unique id of the course. 
        Example: 1"""
    sis_course_id = Column(String)
    """The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    course_integration_id = Column(String)
    """The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    course_section_id = Column(Integer)
    """The unique id of the user's section. 
        Example: 1"""
    section_integration_id = Column(String)
    """The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    sis_account_id = Column(String)
    """The SIS Account ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    sis_section_id = Column(String)
    """The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    sis_user_id = Column(String)
    """The SIS User ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    enrollment_state = Column(String)
    """The state of the user's enrollment in the course. 
        Example: active"""
    limit_privileges_to_course_section = Column(Boolean)
    """User can only access his or her own course section. 
        Example: True"""
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: 83"""
    root_account_id = Column(Integer)
    """The unique id of the user's account. 
        Example: 1"""
    type = Column(String)
    """The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'. 
        Example: StudentEnrollment"""
    user_id = Column(Integer)
    """The unique id of the user. 
        Example: 1"""
    associated_user_id = Column(Integer)
    """The unique id of the associated user. Will be null unless type is ObserverEnrollment. 
        Example: None"""
    role = Column(String)
    """The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized. 
        Example: StudentEnrollment"""
    role_id = Column(Integer)
    """The id of the enrollment role. 
        Example: 1"""
    created_at = Column(DateTime)
    """The created time of the enrollment, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    updated_at = Column(DateTime)
    """The updated time of the enrollment, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    start_at = Column(DateTime)
    """The start time of the enrollment, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    end_at = Column(DateTime)
    """The end time of the enrollment, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    last_activity_at = Column(DateTime)
    """The last activity time of the user for the enrollment, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    last_attended_at = Column(DateTime)
    """The last attended date of the user for the enrollment in a course, in ISO8601 format. 
        Example: 2012-04-18T23:08:51Z"""
    total_activity_time = Column(Integer)
    """The total activity time of the user for the enrollment, in seconds. 
        Example: 260"""
    html_url = Column(String)
    """The URL to the Canvas web UI page for this course enrollment. 
        Example: https://..."""
    grades = relationship('Grade')
    """The URL to the Canvas web UI page containing the grades associated with this enrollment. 
        Example: {'html_url': 'https://...', 'current_score': 35, 'current_grade': None, 'final_score': 6.67, 'final_grade': None}"""
    user = relationship('User')
    """A description of the user. 
        Example: {'id': 3, 'name': 'Student 1', 'sortable_name': '1, Student', 'short_name': 'Stud 1'}"""
    override_grade = Column(String)
    """The user's override grade for the course. 
        Example: A"""
    override_score = Column(Integer)
    """The user's override score for the course. 
        Example: 99.99"""
    unposted_current_grade = Column(String)
    """The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. 
        Example: None"""
    unposted_final_grade = Column(String)
    """The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. 
        Example: None"""
    unposted_current_score = Column(String)
    """The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: None"""
    unposted_final_score = Column(String)
    """The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: None"""
    has_grading_periods = Column(Boolean)
    """optional: Indicates whether the course the enrollment belongs to has grading periods set up. (applies only to student enrollments, and only available in course endpoints) 
        Example: True"""
    totals_for_all_grading_periods_option = Column(Boolean)
    """optional: Indicates whether the course the enrollment belongs to has the Display Totals for 'All Grading Periods' feature enabled. (applies only to student enrollments, and only available in course endpoints) 
        Example: True"""
    current_grading_period_title = Column(String)
    """optional: The name of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: Fall Grading Period"""
    current_grading_period_id = Column(Integer)
    """optional: The id of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: 5"""
    current_period_override_grade = Column(String)
    """The user's override grade for the current grading period. 
        Example: A"""
    current_period_override_score = Column(Integer)
    """The user's override score for the current grading period. 
        Example: 99.99"""
    current_period_unposted_current_score = Column(Integer)
    """optional: The student's score in the course for the current grading period, including muted/unposted assignments. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: 95.8"""
    current_period_unposted_final_score = Column(Integer)
    """optional: The student's score in the course for the current grading period, including muted/unposted assignments and including ungraded assignments with a score of 0. Only included if user has permission to view this score, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: 85.25"""
    current_period_unposted_current_grade = Column(String)
    """optional: The letter grade equivalent of current_period_unposted_current_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: A"""
    current_period_unposted_final_grade = Column(String)
    """optional: The letter grade equivalent of current_period_unposted_final_score, if available. Only included if user has permission to view this grade, typically teachers, TAs, and admins. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: B"""


class JWT(Base):
    __tablename__ = 'jwt'
    token = Column(String)
    """The signed, encrypted, base64 encoded JWT 
        Example: ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJSME5OSW4wLi5QbnAzS1QzLUJkZ3lQZHgtLm5JT0pOV01iZmdtQ0g3WWtybjhLeHlMbW13cl9yZExXTXF3Y0IwbXkzZDd3V1NDd0JYQkV0UTRtTVNJSVRrX0FJcG0zSU1DeThMcW5NdzA0ckdHVTkweDB3MmNJbjdHeWxOUXdveU5ZZ3UwOEN4TkZteUpCeW5FVktrdU05QlRyZXZ3Y1ZTN2hvaC1WZHRqM19PR3duRm5yUVgwSFhFVFc4R28tUGxoQVUtUnhKT0pNakx1OUxYd2NDUzZsaW9ZMno5NVU3T0hLSGNpaDBmSGVjN2FzekVJT3g4NExUeHlReGxYU3BtbFZ5LVNuYWdfbVJUeU5yNHNsMmlDWFcwSzZCNDhpWHJ1clJVVm1LUkVlVTl4ZVVJcTJPaWNpSHpfemJ0X3FrMjhkdzRyajZXRnBHSlZPNWcwTlUzVHlSWk5qdHg1S2NrTjVSQjZ1X2FzWTBScjhTY2VhNFk3Y2JFX01wcm54cFZTNDFIekVVSVRNdzVMTk1GLVpQZy52LVVDTkVJYk8zQ09EVEhPRnFXLUFR"""


class Progress(Base):
    __tablename__ = 'progress'
    id = Column(Integer)
    """the ID of the Progress object 
        Example: 1"""
    context_id = Column(Integer)
    """the context owning the job. 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Account"""
    user_id = Column(Integer)
    """the id of the user who started the job 
        Example: 123"""
    tag = Column(String)
    """the type of operation 
        Example: course_batch_update"""
    completion = Column(Integer)
    """percent completed 
        Example: 100"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['queued', 'running', 'completed', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """the state of the job one of 'queued', 'running', 'completed', 'failed' 
        Example: completed"""
    created_at = Column(DateTime)
    """the time the job was created 
        Example: 2013-01-15T15:00:00Z"""
    updated_at = Column(DateTime)
    """the time the job was last updated 
        Example: 2013-01-15T15:04:00Z"""
    message = Column(String)
    """optional details about the job 
        Example: 17 courses processed"""
    results = relationship('Unknown')
    """optional results of the job. omitted when job is still pending 
        Example: {'id': '123'}"""
    url = Column(String)
    """url where a progress update can be retrieved 
        Example: https://canvas.example.edu/api/v1/progress/1"""


class CommMessage(Base):
    __tablename__ = 'comm_message'
    id = Column(Integer)
    """The ID of the CommMessage. 
        Example: 42"""
    created_at = Column(DateTime)
    """The date and time this message was created 
        Example: 2013-03-19T21:00:00Z"""
    sent_at = Column(DateTime)
    """The date and time this message was sent 
        Example: 2013-03-20T22:42:00Z"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['created', 'staged', 'sending', 'sent', 'bounced', 'dashboard', 'cancelled', 'closed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The workflow state of the message. One of 'created', 'staged', 'sending', 'sent', 'bounced', 'dashboard', 'cancelled', or 'closed' 
        Example: sent"""
    from = Column(String)
    """The address that was put in the 'from' field of the message 
        Example: notifications@example.com"""
    from_name = Column(String)
    """The display name for the from address 
        Example: Instructure Canvas"""
    to = Column(String)
    """The address the message was sent to: 
        Example: someone@example.com"""
    reply_to = Column(String)
    """The reply_to header of the message 
        Example: notifications+specialdata@example.com"""
    subject = Column(String)
    """The message subject 
        Example: example subject line"""
    body = Column(String)
    """The plain text body of the message 
        Example: This is the body of the message"""
    html_body = Column(String)
    """The HTML body of the message. 
        Example: <html><body>This is the body of the message</body></html>"""


class Rubric(Base):
    __tablename__ = 'rubric'
    id = Column(Integer)
    """the ID of the rubric 
        Example: 1"""
    title = Column(String)
    """title of the rubric 
        Example: some title"""
    context_id = Column(Integer)
    """the context owning the rubric 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Course"""
    points_possible = Column(Integer)
    """None 
        Example: 10.0"""
    reusable = Column(Boolean)
    """None 
        Example: false"""
    read_only = Column(Boolean)
    """None 
        Example: true"""
    free_form_criterion_comments = Column(Boolean)
    """whether or not free-form comments are used 
        Example: true"""
    hide_score_total = Column(Boolean)
    """None 
        Example: true"""
    data = Column(JsonObject)
"""List[RubricCriterion]"""
    """An array with all of this Rubric's grading Criteria 
        Example: None"""
    assessments = Column(JsonObject)
"""List[RubricAssessment]"""
    """If an assessment type is included in the 'include' parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent. 
        Example: None"""
    associations = Column(JsonObject)
"""List[RubricAssociation]"""
    """If an association type is included in the 'include' parameter, includes an array of rubric association objects for a given rubric, based on the association type requested. If the user does not request an association type this key will be absent. 
        Example: None"""


class RubricCriterion(Base):
    __tablename__ = 'rubric_criterion'
    id = Column(String)
    """the ID of the criterion 
        Example: _10"""
    description = Column(String)
    """None 
        Example: None"""
    long_description = Column(String)
    """None 
        Example: None"""
    points = Column(Integer)
    """None 
        Example: 5"""
    criterion_use_range = Column(Boolean)
    """None 
        Example: false"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """the possible ratings for this Criterion 
        Example: None"""


class RubricRating(Base):
    __tablename__ = 'rubric_rating'
    points = Column(Integer)
    """None 
        Example: 10"""
    id = Column(String)
    """None 
        Example: rat1"""
    description = Column(String)
    """None 
        Example: Full marks"""
    long_description = Column(String)
    """None 
        Example: Student completed the assignment flawlessly."""


class RubricAssessment(Base):
    __tablename__ = 'rubric_assessment'
    id = Column(Integer)
    """the ID of the rubric 
        Example: 1"""
    rubric_id = Column(Integer)
    """the rubric the assessment belongs to 
        Example: 1"""
    rubric_association_id = Column(Integer)
    """None 
        Example: 2"""
    score = Column(Integer)
    """None 
        Example: 5.0"""
    artifact_type = Column(String)
    """the object of the assessment 
        Example: Submission"""
    artifact_id = Column(Integer)
    """the id of the object of the assessment 
        Example: 3"""
    artifact_attempt = Column(Integer)
    """the current number of attempts made on the object of the assessment 
        Example: 2"""
    assessment_type = Column(String)
    """the type of assessment. values will be either 'grading', 'peer_review', or 'provisional_grade' 
        Example: grading"""
    assessor_id = Column(Integer)
    """user id of the person who made the assessment 
        Example: 6"""
    data = Column(JsonObject)
"""List[Unknown]"""
    """(Optional) If 'full' is included in the 'style' parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent. 
        Example: None"""
    comments = Column(JsonObject)
"""List[str]"""
    """(Optional) If 'comments_only' is included in the 'style' parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent. 
        Example: None"""


class RubricAssociation(Base):
    __tablename__ = 'rubric_association'
    id = Column(Integer)
    """the ID of the association 
        Example: 1"""
    rubric_id = Column(Integer)
    """the ID of the rubric 
        Example: 1"""
    association_id = Column(Integer)
    """the ID of the object this association links to 
        Example: 1"""
    association_type = Column(String)
    """the type of object this association links to 
        Example: Course"""
    use_for_grading = Column(Boolean)
    """Whether or not the associated rubric is used for grade calculation 
        Example: true"""
    summary_data = Column(String)
    """None 
        Example: None"""
    purpose = Column(String)
    """Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context. Values will be grading or bookmark. 
        Example: grading"""
    hide_score_total = Column(Boolean)
    """Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. 
        Example: true"""
    hide_points = Column(Boolean)
    """None 
        Example: true"""
    hide_outcome_results = Column(Boolean)
    """None 
        Example: true"""


class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer)
    """The unique identifier for the section. 
        Example: 1"""
    name = Column(String)
    """The name of the section. 
        Example: Section A"""
    sis_section_id = Column(String)
    """The sis id of the section. This field is only included if the user has permission to view SIS information. 
        Example: s34643"""
    integration_id = Column(String)
    """Optional: The integration ID of the section. This field is only included if the user has permission to view SIS information. 
        Example: 3452342345"""
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import if created through SIS. This field is only included if the user has permission to manage SIS information. 
        Example: 47"""
    course_id = Column(Integer)
    """The unique Canvas identifier for the course in which the section belongs 
        Example: 7"""
    sis_course_id = Column(String)
    """The unique SIS identifier for the course in which the section belongs. This field is only included if the user has permission to view SIS information. 
        Example: 7"""
    start_at = Column(DateTime)
    """the start date for the section, if applicable 
        Example: 2012-06-01T00:00:00-06:00"""
    end_at = Column(DateTime)
    """the end date for the section, if applicable 
        Example: None"""
    restrict_enrollments_to_section_dates = Column(Boolean)
    """Restrict user enrollments to the start and end dates of the section 
        Example: None"""
    nonxlist_course_id = Column(Integer)
    """The unique identifier of the original course of a cross-listed section 
        Example: None"""
    total_students = Column(Integer)
    """optional: the total number of active and invited students in the section 
        Example: 13"""


class PeerReview(Base):
    __tablename__ = 'peer_review'
    assessor_id = Column(Integer)
    """The assessors user id 
        Example: 23"""
    asset_id = Column(Integer)
    """The id for the asset associated with this Peer Review 
        Example: 13"""
    asset_type = Column(String)
    """The type of the asset 
        Example: Submission"""
    id = Column(Integer)
    """The id of the Peer Review 
        Example: 1"""
    user_id = Column(Integer)
    """The user id for the owner of the asset 
        Example: 7"""
    workflow_state = Column(String)
    """The state of the Peer Review, either 'assigned' or 'completed' 
        Example: assigned"""
    user = Column(String)
    """the User object for the owner of the asset if the user include parameter is provided (see user API) (optional) 
        Example: User"""
    assessor = Column(String)
    """The User object for the assessor if the user include parameter is provided (see user API) (optional) 
        Example: User"""
    submission_comments = Column(String)
    """The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional) 
        Example: SubmissionComment"""


class Outcome(Base):
    __tablename__ = 'outcome'
    id = Column(Integer)
    """the ID of the outcome 
        Example: 1"""
    url = Column(String)
    """the URL for fetching/updating the outcome. should be treated as opaque 
        Example: /api/v1/outcomes/1"""
    context_id = Column(Integer)
    """the context owning the outcome. may be null for global outcomes 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Account"""
    title = Column(String)
    """title of the outcome 
        Example: Outcome title"""
    display_name = Column(String)
    """Optional friendly name for reporting 
        Example: My Favorite Outcome"""
    description = Column(String)
    """description of the outcome. omitted in the abbreviated form. 
        Example: Outcome description"""
    vendor_guid = Column(String)
    """A custom GUID for the learning standard. 
        Example: customid9000"""
    points_possible = Column(Integer)
    """maximum points possible. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. 
        Example: 5"""
    mastery_points = Column(Integer)
    """points necessary to demonstrate mastery outcomes. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. 
        Example: 3"""
    calculationMethodEnum = enum.Enum('calculationMethodEnum', ['decaying_average', 'n_mastery', 'latest', 'highest', 'average'])
    """Enum for the allowed values of the calculation_method field"""
    calculation_method = Column(Enum(calculationMethodEnum))
    """the method used to calculate a students score 
        Example: decaying_average"""
    calculation_int = Column(Integer)
    """this defines the variable value used by the calculation_method. included only if calculation_method uses it 
        Example: 65"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """possible ratings for this outcome. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. 
        Example: None"""
    can_edit = Column(Boolean)
    """whether the current user can update the outcome 
        Example: True"""
    can_unlink = Column(Boolean)
    """whether the outcome can be unlinked 
        Example: True"""
    assessed = Column(Boolean)
    """whether this outcome has been used to assess a student 
        Example: True"""
    has_updateable_rubrics = Column(Boolean)
    """whether updates to this outcome will propagate to unassessed rubrics that have imported it 
        Example: True"""


class OutcomeAlignment(Base):
    """An asset aligned with this outcome"""
    __tablename__ = 'outcome_alignment'
    id = Column(String)
    """A unique identifier for this alignment 
        Example: quiz_3"""
    name = Column(String)
    """The name of this alignment 
        Example: Big mid-term test"""
    html_url = Column(String)
    """(Optional) A URL for details about this alignment 
        Example: None"""


class GroupCategory(Base):
    __tablename__ = 'group_category'
    id = Column(Integer)
    """The ID of the group category. 
        Example: 17"""
    name = Column(String)
    """The display name of the group category. 
        Example: Math Groups"""
    role = Column(String)
    """Certain types of group categories have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account group categories have a role of null. 
        Example: communities"""
    selfSignupEnum = enum.Enum('selfSignupEnum', ['restricted', 'enabled'])
    """Enum for the allowed values of the self_signup field"""
    self_signup = Column(Enum(selfSignupEnum))
    """If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include 'restricted', 'enabled', and null 'enabled' allows students to assign themselves to a group 'restricted' restricts them to only joining a group in their section null disallows students from joining groups 
        Example: None"""
    autoLeaderEnum = enum.Enum('autoLeaderEnum', ['first', 'random'])
    """Enum for the allowed values of the auto_leader field"""
    auto_leader = Column(Enum(autoLeaderEnum))
    """Gives instructors the ability to automatically have group leaders assigned.  Values include 'random', 'first', and null; 'random' picks a student from the group at random as the leader, 'first' sets the first student to be assigned to the group as the leader 
        Example: None"""
    context_type = Column(String)
    """The course or account that the category group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'Course', the course_id field would be replaced by an course_id field. 
        Example: Account"""
    account_id = Column(Integer)
    """None 
        Example: 3"""
    group_limit = Column(Integer)
    """If self-signup is enabled, group_limit can be set to cap the number of users in each group. If null, there is no limit. 
        Example: None"""
    sis_group_category_id = Column(String)
    """The SIS identifier for the group category. This field is only included if the user has permission to manage or view SIS information. 
        Example: None"""
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: None"""
    progress = relationship('Progress')
    """If the group category has not yet finished a randomly student assignment request, a progress object will be attached, which will contain information related to the progress of the assignment request. Refer to the Progress API for more information 
        Example: None"""


class Collaboration(Base):
    __tablename__ = 'collaboration'
    id = Column(Integer)
    """The unique identifier for the collaboration 
        Example: 43"""
    collaboration_type = Column(String)
    """A name for the type of collaboration 
        Example: Microsoft Office"""
    document_id = Column(String)
    """The collaboration document identifier for the collaboration provider 
        Example: oinwoenfe8w8ef_onweufe89fef"""
    user_id = Column(Integer)
    """The canvas id of the user who created the collaboration 
        Example: 92"""
    context_id = Column(Integer)
    """The canvas id of the course or group to which the collaboration belongs 
        Example: 77"""
    context_type = Column(String)
    """The canvas type of the course or group to which the collaboration belongs 
        Example: Course"""
    url = Column(String)
    """The LTI launch url to view collaboration. 
        Example: None"""
    created_at = Column(DateTime)
    """The timestamp when the collaboration was created 
        Example: 2012-06-01T00:00:00-06:00"""
    updated_at = Column(DateTime)
    """The timestamp when the collaboration was last modified 
        Example: 2012-06-01T00:00:00-06:00"""
    description = Column(String)
    """None 
        Example: None"""
    title = Column(String)
    """None 
        Example: None"""
    type = Column(String)
    """Another representation of the collaboration type 
        Example: ExternalToolCollaboration"""
    update_url = Column(String)
    """The LTI launch url to edit the collaboration 
        Example: None"""
    user_name = Column(String)
    """The name of the user who owns the collaboration 
        Example: John Danger"""


class Collaborator(Base):
    __tablename__ = 'collaborator'
    id = Column(Integer)
    """The unique user or group identifier for the collaborator. 
        Example: 12345"""
    typeEnum = enum.Enum('typeEnum', ['user', 'group'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(typeEnum))
    """The type of collaborator (e.g. 'user' or 'group'). 
        Example: user"""
    name = Column(String)
    """The name of the collaborator. 
        Example: Don Draper"""


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer)
    """The ID of the group. 
        Example: 17"""
    name = Column(String)
    """The display name of the group. 
        Example: Math Group 1"""
    description = Column(String)
    """A description of the group. This is plain text. 
        Example: None"""
    is_public = Column(Boolean)
    """Whether or not the group is public.  Currently only community groups can be made public.  Also, once a group has been set to public, it cannot be changed back to private. 
        Example: None"""
    followed_by_user = Column(Boolean)
    """Whether or not the current user is following this group. 
        Example: None"""
    joinLevelEnum = enum.Enum('joinLevelEnum', ['parent_context_auto_join', 'parent_context_request', 'invitation_only'])
    """Enum for the allowed values of the join_level field"""
    join_level = Column(Enum(joinLevelEnum))
    """How people are allowed to join the group.  For all groups except for community groups, the user must share the group's parent course or account.  For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are 'parent_context_auto_join', 'parent_context_request', and 'invitation_only'.  For class groups, where students are divided up and should only be part of one group of the category, this value will always be 'invitation_only', and is not relevant. * If 'parent_context_auto_join', anyone can join and will be automatically accepted. * If 'parent_context_request', anyone  can request to join, which must be approved by a group moderator. * If 'invitation_only', only those how have received an invitation my join the group, by accepting that invitation. 
        Example: invitation_only"""
    members_count = Column(Integer)
    """The number of members currently in the group 
        Example: None"""
    avatar_url = Column(String)
    """The url of the group's avatar 
        Example: https://<canvas>/files/avatar_image.png"""
    context_type = Column(String)
    """The course or account that the group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'account', the course_id field would be replaced by an account_id field. 
        Example: Course"""
    course_id = Column(Integer)
    """None 
        Example: 3"""
    roleEnum = enum.Enum('roleEnum', ['communities', 'student_organized', 'imported'])
    """Enum for the allowed values of the role field"""
    role = Column(Enum(roleEnum))
    """Certain types of groups have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account groups have a role of null. 
        Example: None"""
    group_category_id = Column(Integer)
    """The ID of the group's category. 
        Example: 4"""
    sis_group_id = Column(String)
    """The SIS ID of the group. Only included if the user has permission to view SIS information. 
        Example: group4a"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 14"""
    storage_quota_mb = Column(Integer)
    """the storage quota for the group, in megabytes 
        Example: 50"""
    permissions = Column(JsonObject)
"""Dict[str, bool]"""
    """optional: the permissions the user has for the group. returned only for a single group and include[]=permissions 
        Example: {'create_discussion_topic': True, 'create_announcement': True}"""
    users = Column(JsonObject)
"""List[User]"""
    """optional: A list of users that are members in the group. Returned only if include[]=users. WARNING: this collection's size is capped (if there are an extremely large number of users in the group (thousands) not all of them will be returned).  If you need to capture all the users in a group with certainty consider using the paginated /api/v1/groups/<group_id>/memberships endpoint. 
        Example: None"""


class InstAccessToken(Base):
    __tablename__ = 'inst_access_token'
    token = Column(String)
    """The InstAccess token itself -- a signed, encrypted JWT 
        Example: eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.EstatUwzltksvZn4wbjHYiwleM986vzryrv4R9jqvYDGEY4rt6KPG4Q6lJ3oI0piYbH7h17i8vIWv35cqrgRbb7fzmGQ0Ptj74OEjx-1gGBMZCbZTE4W206XxPHRm9TS4qOAvIq0hsvJroE4xZsVWJFiUIKl_Wd2udbvqwF8bvnMKPAx_ooa-9mWaG1N9kd4EWC3Oxu9wi7j8ZG_TbkLSXAg1KxLaO2zXBcU5_HWrKFRxOjHmWpaOMKWkjUInt-DA6fLRszBZp9BFGoop8S9KDs6f1JebLgyM5gGrP-Gz7kSEAPO9eVXtjpd6N29wMClNI0X-Ppp_40Fp4Z3vocTKQ.c_tcevWI68RuZ0s04fDSEQ.wV8KIPHGfYwxm19MWt3K7VVGm4qqZJruPwAZ8rdUANTzJoqwafqOnYZLCyky8lV7J-m64SMVUmR-BOha_CmJEKVVw7T5x70MTP6-nv4RMVPpcViHsNgE2f1GE9HUauVePw7CrnV0PyVaNq2EZasDgdHdye4iG_-hXXQZRnGYzxl8UceTLBVkpEYHlXKdD7DyQ0IT2BYOcZSpXyW7kEIvAHpNaNbvTPCR2t0SeGbuNf8PpYVjohKDpXhNgQ-Pyl9pxs05TrdjTq1fIctzTLqIN58nfqzoqQld6rSkjcAZZXgr8bOsg8EDFMov5gTv2_Uf-YOm52yD1SbL0lJ-VdpKgXu7XtQ4UmEOj40W4uXF-KmLTjEwQmdbmtKrruhakIeth7EZa3w0Xg6RRyHLqKUheAdTgxAIer8MST8tamZlqW1b9wjMw371zSSjeksF_UjTS9p9i7eTtRPuAbf9geDhKb5e-y29MJaL1eKkhTMiEOPY3O4XGGuqRdRMrbjkNmla_RxiQhFJ3T8Dem-yDRan8gqaJLfRRrvGViz-lty96bQT-Z0hVer1uJhAtkM6RT_DgrnAUP_66LfaupZr6bLCKwnYocF1ICcAzkcYw7l5jHa4DTc2ZLgLi-yfbv2wGXpybAvLfZcO424TxHOuQykCSvbfPPuf06kkjPbYmMg6_GdM3JcQ_50VUXQFZkjH45BH5zX7y-2u0ReM8zxt65RpJAvlivrc8j2_E-u0LhlzCwEgsnd61lG4baaI86IVl4wNXkMDui4CgGvAUAf4AXW7Imw_cF0zI69z0SLfahjaYkdREGIYKStBtPAR04sfsR7o.LHBODYub4W4Vq-SXfdbk1Q"""


class Folder(Base):
    __tablename__ = 'folder'
    context_type = Column(String)
    """None 
        Example: Course"""
    context_id = Column(Integer)
    """None 
        Example: 1401"""
    files_count = Column(Integer)
    """None 
        Example: None"""
    position = Column(Integer)
    """None 
        Example: 3"""
    updated_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    folders_url = Column(String)
    """None 
        Example: https://www.example.com/api/v1/folders/2937/folders"""
    files_url = Column(String)
    """None 
        Example: https://www.example.com/api/v1/folders/2937/files"""
    full_name = Column(String)
    """None 
        Example: course files/11folder"""
    lock_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    id = Column(Integer)
    """None 
        Example: 2937"""
    folders_count = Column(Integer)
    """None 
        Example: None"""
    name = Column(String)
    """None 
        Example: 11folder"""
    parent_folder_id = Column(Integer)
    """None 
        Example: 2934"""
    created_at = Column(DateTime)
    """None 
        Example: 2012-07-06T14:58:50Z"""
    unlock_at = Column(DateTime)
    """None 
        Example: None"""
    hidden = Column(Boolean)
    """None 
        Example: None"""
    hidden_for_user = Column(Boolean)
    """None 
        Example: None"""
    locked = Column(Boolean)
    """None 
        Example: True"""
    locked_for_user = Column(Boolean)
    """None 
        Example: None"""
    for_submissions = Column(Boolean)
    """If true, indicates this is a read-only folder containing files submitted to assignments 
        Example: None"""


class SisAssignment(Base):
    """Assignments that have post_to_sis enabled with other objects for convenience"""
    __tablename__ = 'sis_assignment'
    id = Column(Integer)
    """The unique identifier for the assignment. 
        Example: 4"""
    course_id = Column(Integer)
    """The unique identifier for the course. 
        Example: 6"""
    name = Column(String)
    """the name of the assignment 
        Example: some assignment"""
    created_at = Column(DateTime)
    """The time at which this assignment was originally created 
        Example: 2012-07-01T23:59:00-06:00"""
    due_at = Column(DateTime)
    """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. 
        Example: 2012-07-01T23:59:00-06:00"""
    unlock_at = Column(DateTime)
    """(Optional) Time at which this was/will be unlocked. 
        Example: 2013-01-01T00:00:00-06:00"""
    lock_at = Column(DateTime)
    """(Optional) Time at which this was/will be locked. 
        Example: 2013-02-01T00:00:00-06:00"""
    points_possible = Column(Integer)
    """The maximum points possible for the assignment 
        Example: 12"""
    submissionTypesEnum = enum.Enum('submissionTypesEnum', ['discussion_topic', 'online_quiz', 'on_paper', 'not_graded', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_types field"""
    submission_types = Column(Enum(submissionTypesEnum))
    """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' 
        Example: ['online_text_entry']"""
    integration_id = Column(String)
    """Third Party integration id for assignment 
        Example: 12341234"""
    integration_data = Column(String)
    """(optional, Third Party integration data for assignment) 
        Example: other_data"""
    include_in_final_grade = Column(Boolean)
    """If false, the assignment will be omitted from the student's final grade 
        Example: True"""
    assignment_group = Column(JsonObject)
"""List[AssignmentGroupAttributes]"""
    """Includes attributes of a assignment_group for convenience. For more details see Assignments API. 
        Example: None"""
    sections = Column(JsonObject)
"""List[SectionAttributes]"""
    """Includes attributes of a section for convenience. For more details see Sections API. 
        Example: None"""
    user_overrides = Column(JsonObject)
"""List[UserAssignmentOverrideAttributes]"""
    """Includes attributes of a user assignment overrides. For more details see Assignments API. 
        Example: None"""


class AssignmentGroupAttributes(Base):
    """Some of the attributes of an Assignment Group. See Assignments API for more details"""
    __tablename__ = 'assignment_group_attributes'
    id = Column(Integer)
    """the id of the Assignment Group 
        Example: 1"""
    name = Column(String)
    """the name of the Assignment Group 
        Example: group2"""
    group_weight = Column(Integer)
    """the weight of the Assignment Group 
        Example: 20"""
    sis_source_id = Column(String)
    """the sis source id of the Assignment Group 
        Example: 1234"""
    integration_data = relationship('Unknown')
    """the integration data of the Assignment Group 
        Example: {'5678': '0954'}"""


class SectionAttributes(Base):
    """Some of the attributes of a section. For more details see Sections API."""
    __tablename__ = 'section_attributes'
    id = Column(Integer)
    """The unique identifier for the section. 
        Example: 1"""
    name = Column(String)
    """The name of the section. 
        Example: Section A"""
    sis_id = Column(String)
    """The sis id of the section. 
        Example: s34643"""
    integration_id = Column(String)
    """Optional: The integration ID of the section. 
        Example: 3452342345"""
    origin_course = relationship('CourseAttributes')
    """The course to which the section belongs or the course from which the section was cross-listed 
        Example: None"""
    xlist_course = relationship('CourseAttributes')
    """Optional: Attributes of the xlist course. Only present when the section has been cross-listed. See Courses API for more details 
        Example: None"""
    override = relationship('SectionAssignmentOverrideAttributes')
    """Optional: Attributes of the assignment override that apply to the section. See Assignment API for more details 
        Example: None"""


class CourseAttributes(Base):
    """Attributes of a course object.  See Courses API for more details"""
    __tablename__ = 'course_attributes'
    id = Column(Integer)
    """The unique Canvas identifier for the origin course 
        Example: 7"""
    name = Column(String)
    """The name of the origin course. 
        Example: Section A"""
    sis_id = Column(String)
    """The sis id of the origin_course. 
        Example: c34643"""
    integration_id = Column(String)
    """The integration ID of the origin_course. 
        Example: I-2"""


class SectionAssignmentOverrideAttributes(Base):
    """Attributes of an assignment override that apply to the section object.  See Assignments API for more details"""
    __tablename__ = 'section_assignment_override_attributes'
    override_title = Column(String)
    """The title for the assignment override 
        Example: some section override"""
    due_at = Column(DateTime)
    """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. 
        Example: 2012-07-01T23:59:00-06:00"""
    unlock_at = Column(DateTime)
    """(Optional) Time at which this was/will be unlocked. 
        Example: 2013-01-01T00:00:00-06:00"""
    lock_at = Column(DateTime)
    """(Optional) Time at which this was/will be locked. 
        Example: 2013-02-01T00:00:00-06:00"""


class UserAssignmentOverrideAttributes(Base):
    """Attributes of assignment overrides that apply to users.  See Assignments API for more details"""
    __tablename__ = 'user_assignment_override_attributes'
    id = Column(Integer)
    """The unique Canvas identifier for the assignment override 
        Example: 218"""
    title = Column(String)
    """The title of the assignment override. 
        Example: Override title"""
    due_at = Column(DateTime)
    """The time at which this assignment is due 
        Example: 2013-01-01T00:00:00-06:00"""
    unlock_at = Column(DateTime)
    """(Optional) Time at which this was/will be unlocked. 
        Example: 2013-01-01T00:00:00-06:00"""
    lock_at = Column(DateTime)
    """(Optional) Time at which this was/will be locked. 
        Example: 2013-02-01T00:00:00-06:00"""
    students = Column(JsonObject)
"""List[StudentAttributes]"""
    """Includes attributes of a student for convenience. For more details see Users API. 
        Example: None"""


class StudentAttributes(Base):
    """Attributes of student.  See Users API for more details"""
    __tablename__ = 'student_attributes'
    user_id = Column(Integer)
    """The unique Canvas identifier for the user 
        Example: 511"""
    sis_user_id = Column(String)
    """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: SHEL93921"""


class NotificationPreference(Base):
    __tablename__ = 'notification_preference'
    href = Column(String)
    """None 
        Example: https://canvas.instructure.com/users/1/communication_channels/email/student@example.edu/notification_preferences/new_announcement"""
    notification = Column(String)
    """The notification this preference belongs to 
        Example: new_announcement"""
    category = Column(String)
    """The category of that notification 
        Example: announcement"""
    frequencyEnum = enum.Enum('frequencyEnum', ['immediately', 'daily', 'weekly', 'never'])
    """Enum for the allowed values of the frequency field"""
    frequency = Column(Enum(frequencyEnum))
    """How often to send notifications to this communication channel for the given notification. Possible values are 'immediately', 'daily', 'weekly', and 'never' 
        Example: daily"""


class ContentMigration(Base):
    __tablename__ = 'content_migration'
    id = Column(Integer)
    """the unique identifier for the migration 
        Example: 370663"""
    migration_type = Column(String)
    """the type of content migration 
        Example: common_cartridge_importer"""
    migration_type_title = Column(String)
    """the name of the content migration type 
        Example: Canvas Cartridge Importer"""
    migration_issues_url = Column(String)
    """API url to the content migration's issues 
        Example: https://example.com/api/v1/courses/1/content_migrations/1/migration_issues"""
    attachment = Column(String)
    """attachment api object for the uploaded file may not be present for all migrations 
        Example: {"url"=>"https://example.com/api/v1/courses/1/content_migrations/1/download_archive"}"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    user_id = Column(Integer)
    """The user who started the migration 
        Example: 4"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['pre_processing', 'pre_processed', 'running', 'waiting_for_select', 'completed', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed 
        Example: running"""
    started_at = Column(DateTime)
    """timestamp 
        Example: 2012-06-01T00:00:00-06:00"""
    finished_at = Column(DateTime)
    """timestamp 
        Example: 2012-06-01T00:00:00-06:00"""
    pre_attachment = Column(String)
    """file uploading data, see {file:file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call 
        Example: {"upload_url"=>"", "message"=>"file exceeded quota", "upload_params"=>{}}"""


class Migrator(Base):
    __tablename__ = 'migrator'
    type = Column(String)
    """The value to pass to the create endpoint 
        Example: common_cartridge_importer"""
    requires_file_upload = Column(Boolean)
    """Whether this endpoint requires a file upload 
        Example: True"""
    name = Column(String)
    """Description of the package type expected 
        Example: Common Cartridge 1.0/1.1/1.2 Package"""
    required_settings = Column(JsonObject)
"""List[str]"""
    """A list of fields this system requires 
        Example: ['source_course_id']"""


class EnrollmentTerm(Base):
    __tablename__ = 'enrollment_term'
    id = Column(Integer)
    """The unique identifier for the enrollment term. 
        Example: 1"""
    sis_term_id = Column(String)
    """The SIS id of the term. Only included if the user has permission to view SIS information. 
        Example: Sp2014"""
    sis_import_id = Column(Integer)
    """the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: 34"""
    name = Column(String)
    """The name of the term. 
        Example: Spring 2014"""
    start_at = Column(DateTime)
    """The datetime of the start of the term. 
        Example: 2014-01-06T08:00:00-05:00"""
    end_at = Column(DateTime)
    """The datetime of the end of the term. 
        Example: 2014-05-16T05:00:00-04:00"""
    workflow_state = Column(String)
    """The state of the term. Can be 'active' or 'deleted'. 
        Example: active"""
    overrides = relationship('Unknown')
    """Term date overrides for specific enrollment types 
        Example: {'StudentEnrollment': {'start_at': '2014-01-07T08:00:00-05:00', 'end_at': '2014-05-14T05:00:00-04:0'}}"""
    course_count = Column(Integer)
    """The number of courses in the term (available via include) 
        Example: 80"""


class EnrollmentTermsList(Base):
    __tablename__ = 'enrollment_terms_list'
    enrollment_terms = Column(JsonObject)
"""List[EnrollmentTerm]"""
    """a paginated list of all terms in the account 
        Example: None"""


class AssignmentOverride(Base):
    __tablename__ = 'assignment_override'
    id = Column(Integer)
    """the ID of the assignment override 
        Example: 4"""
    assignment_id = Column(Integer)
    """the ID of the assignment the override applies to 
        Example: 123"""
    student_ids = Column(JsonObject)
"""List[int]"""
    """the IDs of the override's target students (present if the override targets an ad-hoc set of students) 
        Example: [1, 2, 3]"""
    group_id = Column(Integer)
    """the ID of the override's target group (present if the override targets a group and the assignment is a group assignment) 
        Example: 2"""
    course_section_id = Column(Integer)
    """the ID of the overrides's target section (present if the override targets a section) 
        Example: 1"""
    title = Column(String)
    """the title of the override 
        Example: an assignment override"""
    due_at = Column(DateTime)
    """the overridden due at (present if due_at is overridden) 
        Example: 2012-07-01T23:59:00-06:00"""
    all_day = Column(Boolean)
    """the overridden all day flag (present if due_at is overridden) 
        Example: True"""
    all_day_date = Column(DateTime)
    """the overridden all day date (present if due_at is overridden) 
        Example: 2012-07-01"""
    unlock_at = Column(DateTime)
    """the overridden unlock at (present if unlock_at is overridden) 
        Example: 2012-07-01T23:59:00-06:00"""
    lock_at = Column(DateTime)
    """the overridden lock at, if any (present if lock_at is overridden) 
        Example: 2012-07-01T23:59:00-06:00"""


class CommunicationChannel(Base):
    __tablename__ = 'communication_channel'
    id = Column(Integer)
    """The ID of the communication channel. 
        Example: 16"""
    address = Column(String)
    """The address, or path, of the communication channel. 
        Example: sheldon@caltech.example.com"""
    typeEnum = enum.Enum('typeEnum', ['email', 'push', 'sms', 'twitter'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(typeEnum))
    """The type of communcation channel being described. Possible values are: 'email', 'push', 'sms', or 'twitter'. This field determines the type of value seen in 'address'. 
        Example: email"""
    position = Column(Integer)
    """The position of this communication channel relative to the user's other channels when they are ordered. 
        Example: 1"""
    user_id = Column(Integer)
    """The ID of the user that owns this communication channel. 
        Example: 1"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['unconfirmed', 'active'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The current state of the communication channel. Possible values are: 'unconfirmed' or 'active'. 
        Example: active"""


class OutcomeGroup(Base):
    __tablename__ = 'outcome_group'
    id = Column(Integer)
    """the ID of the outcome group 
        Example: 1"""
    url = Column(String)
    """the URL for fetching/updating the outcome group. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1"""
    parent_outcome_group = relationship('OutcomeGroup')
    """an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form. 
        Example: None"""
    context_id = Column(Integer)
    """the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form. 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Account"""
    title = Column(String)
    """title of the outcome group 
        Example: Outcome group title"""
    description = Column(String)
    """description of the outcome group. omitted in the abbreviated form. 
        Example: Outcome group description"""
    vendor_guid = Column(String)
    """A custom GUID for the learning standard. 
        Example: customid9000"""
    subgroups_url = Column(String)
    """the URL for listing/creating subgroups under the outcome group. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1/subgroups"""
    outcomes_url = Column(String)
    """the URL for listing/creating outcome links under the outcome group. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1/outcomes"""
    import_url = Column(String)
    """the URL for importing another group into this outcome group. should be treated as opaque. omitted in the abbreviated form. 
        Example: /api/v1/accounts/1/outcome_groups/1/import"""
    can_edit = Column(Boolean)
    """whether the current user can update the outcome group 
        Example: True"""


class OutcomeLink(Base):
    __tablename__ = 'outcome_link'
    url = Column(String)
    """the URL for fetching/updating the outcome link. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1/outcomes/1"""
    context_id = Column(Integer)
    """the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups. 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Account"""
    outcome_group = relationship('OutcomeGroup')
    """an abbreviated OutcomeGroup object representing the group containing the outcome link. 
        Example: None"""
    outcome = relationship('Outcome')
    """an abbreviated Outcome object representing the outcome linked into the containing outcome group. 
        Example: None"""
    assessed = Column(Boolean)
    """whether this outcome has been used to assess a student in the context of this outcome link.  In other words, this will be set to true if the context is a course, and a student has been assessed with this outcome in that course. 
        Example: True"""
    can_unlink = Column(Boolean)
    """whether this outcome link is manageable and is not the last link to an aligned outcome 
        Example: None"""


class GroupMembership(Base):
    __tablename__ = 'group_membership'
    id = Column(Integer)
    """The id of the membership object 
        Example: 92"""
    group_id = Column(Integer)
    """The id of the group object to which the membership belongs 
        Example: 17"""
    user_id = Column(Integer)
    """The id of the user object to which the membership belongs 
        Example: 3"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['accepted', 'invited', 'requested'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested' 
        Example: accepted"""
    moderator = Column(Boolean)
    """Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate) 
        Example: True"""
    just_created = Column(Boolean)
    """optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member 
        Example: True"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 4"""


class UsageRights(Base):
    """Describes the copyright and license information for a File"""
    __tablename__ = 'usage_rights'
    legal_copyright = Column(String)
    """Copyright line for the file 
        Example: (C) 2014 Incom Corporation Ltd"""
    use_justification = Column(String)
    """Justification for using the file in a Canvas course. Valid values are 'own_copyright', 'public_domain', 'used_by_permission', 'fair_use', 'creative_commons' 
        Example: creative_commons"""
    license = Column(String)
    """License identifier for the file. 
        Example: cc_by_sa"""
    license_name = Column(String)
    """Readable license name 
        Example: CC Attribution Share-Alike"""
    message = Column(String)
    """Explanation of the action performed 
        Example: 4 files updated"""
    file_ids = Column(JsonObject)
"""List[int]"""
    """List of ids of files that were updated 
        Example: [1, 2, 3]"""


class License(Base):
    __tablename__ = 'license'
    id = Column(String)
    """a short string identifying the license 
        Example: cc_by_sa"""
    name = Column(String)
    """the name of the license 
        Example: CC Attribution ShareAlike"""
    url = Column(String)
    """a link to the license text 
        Example: http://creativecommons.org/licenses/by-sa/4.0"""


class MigrationIssue(Base):
    __tablename__ = 'migration_issue'
    id = Column(Integer)
    """the unique identifier for the issue 
        Example: 370663"""
    content_migration_url = Column(String)
    """API url to the content migration 
        Example: https://example.com/api/v1/courses/1/content_migrations/1"""
    description = Column(String)
    """Description of the issue for the end-user 
        Example: Questions in this quiz couldn't be converted"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['active', 'resolved'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the issue: active, resolved 
        Example: active"""
    fix_issue_html_url = Column(String)
    """HTML Url to the Canvas page to investigate the issue 
        Example: https://example.com/courses/1/quizzes/2"""
    issueTypeEnum = enum.Enum('issueTypeEnum', ['todo', 'warning', 'error'])
    """Enum for the allowed values of the issue_type field"""
    issue_type = Column(Enum(issueTypeEnum))
    """Severity of the issue: todo, warning, error 
        Example: warning"""
    error_report_html_url = Column(String)
    """Link to a Canvas error report if present (If the requesting user has permissions) 
        Example: https://example.com/error_reports/3"""
    error_message = Column(String)
    """Site administrator error message (If the requesting user has permissions) 
        Example: admin only message"""
    created_at = Column(DateTime)
    """timestamp 
        Example: 2012-06-01T00:00:00-06:00"""
    updated_at = Column(DateTime)
    """timestamp 
        Example: 2012-06-01T00:00:00-06:00"""


class AuthenticationEvent(Base):
    __tablename__ = 'authentication_event'
    created_at = Column(DateTime)
    """timestamp of the event 
        Example: 2012-07-19T15:00:00-06:00"""
    eventTypeEnum = enum.Enum('eventTypeEnum', ['login', 'logout'])
    """Enum for the allowed values of the event_type field"""
    event_type = Column(Enum(eventTypeEnum))
    """authentication event type ('login' or 'logout') 
        Example: login"""
    pseudonym_id = Column(Integer)
    """ID of the pseudonym (login) associated with the event 
        Example: 9478"""
    account_id = Column(Integer)
    """ID of the account associated with the event. will match the account_id in the associated pseudonym. 
        Example: 2319"""
    user_id = Column(Integer)
    """ID of the user associated with the event will match the user_id in the associated pseudonym. 
        Example: 362"""


class ContentShare(Base):
    """Content shared between users"""
    __tablename__ = 'content_share'
    id = Column(Integer)
    """The id of the content share for the current user 
        Example: 1"""
    name = Column(String)
    """The name of the shared content 
        Example: War of 1812 homework"""
    content_type = Column(String)
    """The type of content that was shared. Can be assignment, discussion_topic, page, quiz, module, or module_item. 
        Example: assignment"""
    created_at = Column(DateTime)
    """The datetime the content was shared with this user. 
        Example: 2017-05-09T10:12:00Z"""
    updated_at = Column(DateTime)
    """The datetime the content was updated. 
        Example: 2017-05-09T10:12:00Z"""
    user_id = Column(Integer)
    """The id of the user who sent or received the content share. 
        Example: 1578941"""
    sender = relationship('Unknown')
    """The user who shared the content. This field is provided only to receivers; it is not populated in the sender's list of sent content shares. 
        Example: {'id': 1, 'display_name': 'Matilda Vargas', 'avatar_image_url': 'http://localhost:3000/image_url', 'html_url': 'http://localhost:3000/users/1'}"""
    receivers = Column(JsonObject)
"""List[Unknown]"""
    """An Array of users the content is shared with.  This field is provided only to senders; an empty array will be returned for the receiving users. 
        Example: [{'id': 1, 'display_name': 'Jon Snow', 'avatar_image_url': 'http://localhost:3000/image_url2', 'html_url': 'http://localhost:3000/users/2'}]"""
    source_course = relationship('Unknown')
    """The course the content was originally shared from. 
        Example: {'id': 787, 'name': 'History 105'}"""
    read_state = Column(String)
    """Whether the recipient has viewed the content share. 
        Example: read"""
    content_export = relationship('ContentExport')
    """The content export record associated with this content share 
        Example: {'id': 42}"""


class PageView(Base):
    """The record of a user page view access in Canvas"""
    __tablename__ = 'page_view'
    id = Column(String)
    """A UUID representing the page view.  This is also the unique request id 
        Example: 3e246700-e305-0130-51de-02e33aa501ef"""
    app_name = Column(String)
    """If the request is from an API request, the app that generated the access token 
        Example: Canvas for iOS"""
    url = Column(String)
    """The URL requested 
        Example: https://canvas.instructure.com/conversations"""
    context_type = Column(String)
    """The type of context for the request 
        Example: Course"""
    asset_type = Column(String)
    """The type of asset in the context for the request, if any 
        Example: Discussion"""
    controller = Column(String)
    """The rails controller that handled the request 
        Example: discussions"""
    action = Column(String)
    """The rails action that handled the request 
        Example: index"""
    contributed = Column(Boolean)
    """This field is deprecated, and will always be false 
        Example: false"""
    interaction_seconds = Column(Integer)
    """An approximation of how long the user spent on the page, in seconds 
        Example: 7.21"""
    created_at = Column(DateTime)
    """When the request was made 
        Example: 2013-10-01T19:49:47Z"""
    user_request = Column(Boolean)
    """A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call) 
        Example: true"""
    render_time = Column(Integer)
    """How long the response took to render, in seconds 
        Example: 0.369"""
    user_agent = Column(String)
    """The user-agent of the browser or program that made the request 
        Example: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"""
    participated = Column(Boolean)
    """True if the request counted as participating, such as submitting homework 
        Example: false"""
    http_method = Column(String)
    """The HTTP method such as GET or POST 
        Example: GET"""
    remote_ip = Column(String)
    """The origin IP address of the request 
        Example: 173.194.46.71"""
    links = relationship('PageViewLinks')
    """The page view links to define the relationships 
        Example: {'user': 1234, 'account': 1234}"""


class PageViewLinks(Base):
    """The links of a page view access in Canvas"""
    __tablename__ = 'page_view_links'
    user = Column(Integer)
    """The ID of the user for this page view 
        Example: 1234"""
    context = Column(Integer)
    """The ID of the context for the request (course id if context_type is Course, etc) 
        Example: 1234"""
    asset = Column(Integer)
    """The ID of the asset for the request, if any 
        Example: 1234"""
    real_user = Column(Integer)
    """The ID of the actual user who made this request, if the request was made by a user who was masquerading 
        Example: 1234"""
    account = Column(Integer)
    """The ID of the account context for this page view 
        Example: 1234"""


class Grader(Base):
    __tablename__ = 'grader'
    id = Column(Integer)
    """the user_id of the user who graded the contained submissions 
        Example: 27"""
    name = Column(String)
    """the name of the user who graded the contained submissions 
        Example: Some User"""
    assignments = Column(JsonObject)
"""List[int]"""
    """the assignment groups for all submissions in this response that were graded by this user.  The details are not nested inside here, but the fact that an assignment is present here means that the grader did grade submissions for this assignment on the contextual date. You can use the id of a grader and of an assignment to make another API call to find all submissions for a grader/assignment combination on a given date. 
        Example: [1, 2, 3]"""


class Day(Base):
    __tablename__ = 'day'
    date = Column(DateTime)
    """the date represented by this entry 
        Example: 1986-08-09"""
    graders = Column(Integer)
    """an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for. 
        Example: []"""


class SubmissionVersion(Base):
    """A SubmissionVersion object contains all the fields that a Submission object does, plus additional fields prefixed with current_* new_* and previous_* described below."""
    __tablename__ = 'submission_version'
    assignment_id = Column(Integer)
    """the id of the assignment this submissions is for 
        Example: 22604"""
    assignment_name = Column(String)
    """the name of the assignment this submission is for 
        Example: some assignment"""
    body = Column(String)
    """the body text of the submission 
        Example: text from the submission"""
    current_grade = Column(String)
    """the most up to date grade for the current version of this submission 
        Example: 100"""
    current_graded_at = Column(DateTime)
    """the latest time stamp for the grading of this submission 
        Example: 2013-01-31T18:16:31Z"""
    current_grader = Column(String)
    """the name of the most recent grader for this submission 
        Example: Grader Name"""
    grade_matches_current_submission = Column(Boolean)
    """boolean indicating whether the grade is equal to the current submission grade 
        Example: True"""
    graded_at = Column(DateTime)
    """time stamp for the grading of this version of the submission 
        Example: 2013-01-31T18:16:31Z"""
    grader = Column(String)
    """the name of the user who graded this version of the submission 
        Example: Grader Name"""
    grader_id = Column(Integer)
    """the user id of the user who graded this version of the submission 
        Example: 67379"""
    id = Column(Integer)
    """the id of the submission of which this is a version 
        Example: 11607"""
    new_grade = Column(String)
    """the updated grade provided in this version of the submission 
        Example: 100"""
    new_graded_at = Column(DateTime)
    """the timestamp for the grading of this version of the submission (alias for graded_at) 
        Example: 2013-01-31T18:16:31Z"""
    new_grader = Column(String)
    """alias for 'grader' 
        Example: Grader Name"""
    previous_grade = Column(String)
    """the grade for the submission version immediately preceding this one 
        Example: 90"""
    previous_graded_at = Column(DateTime)
    """the timestamp for the grading of the submission version immediately preceding this one 
        Example: 2013-01-29T12:12:12Z"""
    previous_grader = Column(String)
    """the name of the grader who graded the version of this submission immediately preceding this one 
        Example: Graded on submission"""
    score = Column(Integer)
    """the score for this version of the submission 
        Example: 100"""
    user_name = Column(String)
    """the name of the student who created this submission 
        Example: student@example.com"""
    submission_type = Column(String)
    """the type of submission 
        Example: online"""
    url = Column(String)
    """the url of the submission, if there is one 
        Example: None"""
    user_id = Column(Integer)
    """the user ID of the student who created this submission 
        Example: 67376"""
    workflow_state = Column(String)
    """the state of the submission at this version 
        Example: unsubmitted"""


class SubmissionHistory(Base):
    __tablename__ = 'submission_history'
    submission_id = Column(Integer)
    """the id of the submission 
        Example: 4"""
    versions = Column(JsonObject)
"""List[SubmissionVersion]"""
    """an array of all the versions of this submission 
        Example: None"""


class MediaComment(Base):
    __tablename__ = 'media_comment'
    content_type = Column(String)
    """None 
        Example: audio/mp4"""
    display_name = Column(String)
    """None 
        Example: something"""
    media_id = Column(String)
    """None 
        Example: 3232"""
    media_type = Column(String)
    """None 
        Example: audio"""
    url = Column(String)
    """None 
        Example: http://example.com/media_url"""


class SubmissionComment(Base):
    __tablename__ = 'submission_comment'
    id = Column(Integer)
    """None 
        Example: 37"""
    author_id = Column(Integer)
    """None 
        Example: 134"""
    author_name = Column(String)
    """None 
        Example: Toph Beifong"""
    author = Column(String)
    """Abbreviated user object UserDisplay (see users API). 
        Example: {}"""
    comment = Column(String)
    """None 
        Example: Well here's the thing..."""
    created_at = Column(DateTime)
    """None 
        Example: 2012-01-01T01:00:00Z"""
    edited_at = Column(DateTime)
    """None 
        Example: 2012-01-02T01:00:00Z"""
    media_comment = relationship('MediaComment')
    """None 
        Example: None"""


class CourseNickname(Base):
    __tablename__ = 'course_nickname'
    course_id = Column(Integer)
    """the ID of the course 
        Example: 88"""
    name = Column(String)
    """the actual name of the course 
        Example: S1048576 DPMS1200 Intro to Newtonian Mechanics"""
    nickname = Column(String)
    """the calling user's nickname for the course 
        Example: Physics"""


class UserDisplay(Base):
    """This mini-object is used for secondary user responses, when we just want to provide enough information to display a user."""
    __tablename__ = 'user_display'
    id = Column(Integer)
    """The ID of the user. 
        Example: 2"""
    short_name = Column(String)
    """A short name the user has selected, for use in conversations or other less formal places through the site. 
        Example: Shelly"""
    avatar_image_url = Column(String)
    """If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar. 
        Example: https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g"""
    html_url = Column(String)
    """URL to access user, either nested to a context or directly. 
        Example: https://school.instructure.com/courses/:course_id/users/:user_id"""


class AnonymousUserDisplay(Base):
    """This mini-object is returned in place of UserDisplay when returning student data for anonymous assignments, and includes an anonymous ID to identify a user within the scope of a single assignment."""
    __tablename__ = 'anonymous_user_display'
    anonymous_id = Column(String)
    """A unique short ID identifying this user within the scope of a particular assignment. 
        Example: xn29Q"""
    avatar_image_url = Column(String)
    """A URL to retrieve a generic avatar. 
        Example: https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g"""
    display_name = Column(String)
    """The anonymized display name for the student. 
        Example: Student 2"""


class User(Base):
    """A Canvas user, e.g. a student, teacher, administrator, observer, etc."""
    __tablename__ = 'user'
    id = Column(Integer)
    """The ID of the user. 
        Example: 2"""
    name = Column(String)
    """The name of the user. 
        Example: Sheldon Cooper"""
    sortable_name = Column(String)
    """The name of the user that is should be used for sorting groups of users, such as in the gradebook. 
        Example: Cooper, Sheldon"""
    last_name = Column(String)
    """The last name of the user. 
        Example: Cooper"""
    first_name = Column(String)
    """The first name of the user. 
        Example: Sheldon"""
    short_name = Column(String)
    """A short name the user has selected, for use in conversations or other less formal places through the site. 
        Example: Shelly"""
    sis_user_id = Column(String)
    """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: SHEL93921"""
    sis_import_id = Column(Integer)
    """The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information. 
        Example: 18"""
    integration_id = Column(String)
    """The integration_id associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: ABC59802"""
    login_id = Column(String)
    """The unique login id for the user.  This is what the user uses to log in to Canvas. 
        Example: sheldon@caltech.example.com"""
    avatar_url = Column(String)
    """If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar. 
        Example: https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g"""
    avatar_state = Column(String)
    """Optional: If avatars are enabled and caller is admin, this field can be requested and will contain the current state of the user's avatar. 
        Example: approved"""
    enrollments = Column(JsonObject)
"""List[Enrollment]"""
    """Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records. 
        Example: None"""
    email = Column(String)
    """Optional: This field can be requested with certain API calls, and will return the users primary email address. 
        Example: sheldon@caltech.example.com"""
    locale = Column(String)
    """Optional: This field can be requested with certain API calls, and will return the users locale in RFC 5646 format. 
        Example: tlh"""
    last_login = Column(String)
    """Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas. 
        Example: 2012-05-30T17:45:25Z"""
    time_zone = Column(String)
    """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone. 
        Example: America/Denver"""
    bio = Column(String)
    """Optional: The user's bio. 
        Example: I like the Muppets."""


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer)
    """the ID of the Account object 
        Example: 2"""
    name = Column(String)
    """The display name of the account 
        Example: Canvas Account"""
    uuid = Column(String)
    """The UUID of the account 
        Example: WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5"""
    parent_account_id = Column(Integer)
    """The account's parent ID, or null if this is the root account 
        Example: 1"""
    root_account_id = Column(Integer)
    """The ID of the root account, or null if this is the root account 
        Example: 1"""
    default_storage_quota_mb = Column(Integer)
    """The storage quota for the account in megabytes, if not otherwise specified 
        Example: 500"""
    default_user_storage_quota_mb = Column(Integer)
    """The storage quota for a user in the account in megabytes, if not otherwise specified 
        Example: 50"""
    default_group_storage_quota_mb = Column(Integer)
    """The storage quota for a group in the account in megabytes, if not otherwise specified 
        Example: 50"""
    default_time_zone = Column(String)
    """The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}. 
        Example: America/Denver"""
    sis_account_id = Column(String)
    """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. 
        Example: 123xyz"""
    integration_id = Column(String)
    """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. 
        Example: 123xyz"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 12"""
    lti_guid = Column(String)
    """The account's identifier that is sent as context_id in LTI launches. 
        Example: 123xyz"""
    workflow_state = Column(String)
    """The state of the account. Can be 'active' or 'deleted'. 
        Example: active"""


class TermsOfService(Base):
    __tablename__ = 'terms_of_service'
    id = Column(Integer)
    """Terms Of Service id 
        Example: 1"""
    terms_type = Column(String)
    """The given type for the Terms of Service 
        Example: default"""
    passive = Column(Boolean)
    """Boolean dictating if the user must accept Terms of Service 
        Example: None"""
    account_id = Column(Integer)
    """The id of the root account that owns the Terms of Service 
        Example: 1"""
    content = Column(String)
    """Content of the Terms of Service 
        Example: To be or not to be that is the question"""
    self_registration_type = Column(String)
    """The type of self registration allowed 
        Example: ['none', 'observer', 'all']"""


class HelpLink(Base):
    __tablename__ = 'help_link'
    id = Column(String)
    """The ID of the help link 
        Example: instructor_question"""
    text = Column(String)
    """The name of the help link 
        Example: Ask Your Instructor a Question"""
    subtext = Column(String)
    """The description of the help link 
        Example: Questions are submitted to your instructor"""
    url = Column(String)
    """The URL of the help link 
        Example: #teacher_feedback"""
    type = Column(String)
    """The type of the help link 
        Example: default"""
    available_to = Column(JsonObject)
"""List[str]"""
    """The roles that have access to this help link 
        Example: ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled']"""


class HelpLinks(Base):
    __tablename__ = 'help_links'
    help_link_name = Column(String)
    """Help link button title 
        Example: Help And Policies"""
    help_link_icon = Column(String)
    """Help link button icon 
        Example: help"""
    custom_help_links = Column(JsonObject)
"""List[HelpLink]"""
    """Help links defined by the account. Could include default help links. 
        Example: [{'id': 'link1', 'text': 'Custom Link!', 'subtext': 'Something something.', 'url': 'https://google.com', 'type': 'custom', 'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'is_featured': True, 'is_new': False, 'feature_headline': 'Check this out!'}]"""
    default_help_links = Column(JsonObject)
"""List[HelpLink]"""
    """Default help links provided when account has not set help links of their own. 
        Example: [{'available_to': ['student'], 'text': 'Ask Your Instructor a Question', 'subtext': 'Questions are submitted to your instructor', 'url': '#teacher_feedback', 'type': 'default', 'id': 'instructor_question', 'is_featured': False, 'is_new': True, 'feature_headline': ''}, {'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'text': 'Search the Canvas Guides', 'subtext': 'Find answers to common questions', 'url': 'https://community.canvaslms.com/t5/Guides/ct-p/guides', 'type': 'default', 'id': 'search_the_canvas_guides', 'is_featured': False, 'is_new': False, 'feature_headline': ''}, {'available_to': ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled'], 'text': 'Report a Problem', 'subtext': 'If Canvas misbehaves, tell us about it', 'url': '#create_ticket', 'type': 'default', 'id': 'report_a_problem', 'is_featured': False, 'is_new': False, 'feature_headline': ''}]"""


class CourseEpubExport(Base):
    """Combination of a Course & EpubExport."""
    __tablename__ = 'course_epub_export'
    id = Column(Integer)
    """the unique identifier for the course 
        Example: 101"""
    name = Column(String)
    """the name for the course 
        Example: Maths 101"""
    epub_export = relationship('EpubExport')
    """ePub export API object 
        Example: None"""


class EpubExport(Base):
    __tablename__ = 'epub_export'
    id = Column(Integer)
    """the unique identifier for the export 
        Example: 101"""
    created_at = Column(DateTime)
    """the date and time this export was requested 
        Example: 2014-01-01T00:00:00Z"""
    attachment = relationship('File')
    """attachment api object for the export ePub (not present until the export completes) 
        Example: {'url': 'https://example.com/api/v1/attachments/789?download_frd=1&verifier=bG9sY2F0cyEh'}"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    user_id = Column(Integer)
    """The ID of the user who started the export 
        Example: 4"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['created', 'exporting', 'exported', 'generating', 'generated', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the ePub export: created exporting exported generating generated failed 
        Example: exported"""


class AssignmentExtension(Base):
    __tablename__ = 'assignment_extension'
    assignment_id = Column(Integer)
    """The ID of the Assignment the extension belongs to. 
        Example: 2"""
    user_id = Column(Integer)
    """The ID of the Student that needs the assignment extension. 
        Example: 3"""
    extra_attempts = Column(Integer)
    """Number of times the student is allowed to re-submit the assignment 
        Example: 2"""


class PlannerNote(Base):
    """A planner note"""
    __tablename__ = 'planner_note'
    id = Column(Integer)
    """The ID of the planner note 
        Example: 234"""
    title = Column(String)
    """The title for a planner note 
        Example: Bring books tomorrow"""
    description = Column(String)
    """The description of the planner note 
        Example: I need to bring books tomorrow for my course on biology"""
    user_id = Column(Integer)
    """The id of the associated user creating the planner note 
        Example: 1578941"""
    workflow_state = Column(String)
    """The current published state of the planner note 
        Example: active"""
    course_id = Column(Integer)
    """The course that the note is in relation too, if applicable 
        Example: 1578941"""
    todo_date = Column(DateTime)
    """The datetime of when the planner note should show up on their planner 
        Example: 2017-05-09T10:12:00Z"""
    linked_object_type = Column(String)
    """the type of the linked learning object 
        Example: assignment"""
    linked_object_id = Column(Integer)
    """the id of the linked learning object 
        Example: 131072"""
    linked_object_html_url = Column(String)
    """the Canvas web URL of the linked learning object 
        Example: https://canvas.example.com/courses/1578941/assignments/131072"""
    linked_object_url = Column(String)
    """the API URL of the linked learning object 
        Example: https://canvas.example.com/api/v1/courses/1578941/assignments/131072"""


class PairingCode(Base):
    """A code used for linking a user to a student to observe them."""
    __tablename__ = 'pairing_code'
    user_id = Column(Integer)
    """The ID of the user. 
        Example: 2"""
    code = Column(String)
    """The actual code to be sent to other APIs 
        Example: abc123"""
    expires_at = Column(String)
    """When the code expires 
        Example: 2012-05-30T17:45:25Z"""
    workflow_state = Column(String)
    """The current status of the code 
        Example: active"""


class GradingPeriod(Base):
    __tablename__ = 'grading_period'
    id = Column(Integer)
    """The unique identifier for the grading period. 
        Example: 1023"""
    title = Column(String)
    """The title for the grading period. 
        Example: First Block"""
    start_date = Column(String)
    """The start date of the grading period. 
        Example: 2014-01-07T15:04:00Z"""
    end_date = Column(String)
    """The end date of the grading period. 
        Example: 2014-05-07T17:07:00Z"""
    close_date = Column(String)
    """Grades can only be changed before the close date of the grading period. 
        Example: 2014-06-07T17:07:00Z"""
    weight = Column(Integer)
    """A weight value that contributes to the overall weight of a grading period set which is used to calculate how much assignments in this period contribute to the total grade 
        Example: 33.33"""
    is_closed = Column(Boolean)
    """If true, the grading period's close_date has passed. 
        Example: True"""


class JWKs(Base):
    __tablename__ = 'jw_ks'


class CompletionRequirement(Base):
    __tablename__ = 'completion_requirement'
    typeEnum = enum.Enum('typeEnum', ['must_view', 'must_submit', 'must_contribute', 'min_score', 'must_mark_done'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(typeEnum))
    """one of 'must_view', 'must_submit', 'must_contribute', 'min_score', 'must_mark_done' 
        Example: min_score"""
    min_score = Column(Integer)
    """minimum score required to complete (only present when type == 'min_score') 
        Example: 10"""
    completed = Column(Boolean)
    """whether the calling user has met this requirement (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) 
        Example: True"""


class ContentDetails(Base):
    __tablename__ = 'content_details'
    points_possible = Column(Integer)
    """None 
        Example: 20"""
    due_at = Column(DateTime)
    """None 
        Example: 2012-12-31T06:00:00-06:00"""
    unlock_at = Column(DateTime)
    """None 
        Example: 2012-12-31T06:00:00-06:00"""
    lock_at = Column(DateTime)
    """None 
        Example: 2012-12-31T06:00:00-06:00"""
    locked_for_user = Column(Boolean)
    """None 
        Example: True"""
    lock_explanation = Column(String)
    """None 
        Example: This quiz is part of an unpublished module and is not available yet."""
    lock_info = relationship('LockInfo')
    """None 
        Example: {'asset_string': 'assignment_4', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00', 'context_module': {}}"""


class ModuleItem(Base):
    __tablename__ = 'module_item'
    id = Column(Integer)
    """the unique identifier for the module item 
        Example: 768"""
    module_id = Column(Integer)
    """the id of the Module this item appears in 
        Example: 123"""
    position = Column(Integer)
    """the position of this item in the module (1-based) 
        Example: 1"""
    title = Column(String)
    """the title of this item 
        Example: Square Roots: Irrational numbers or boxy vegetables?"""
    indent = Column(Integer)
    """0-based indent level; module items may be indented to show a hierarchy 
        Example: None"""
    typeEnum = enum.Enum('typeEnum', ['File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(typeEnum))
    """the type of object referred to one of 'File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool' 
        Example: Assignment"""
    content_id = Column(Integer)
    """the id of the object referred to applies to 'File', 'Discussion', 'Assignment', 'Quiz', 'ExternalTool' types 
        Example: 1337"""
    html_url = Column(String)
    """link to the item in Canvas 
        Example: https://canvas.example.edu/courses/222/modules/items/768"""
    url = Column(String)
    """(Optional) link to the Canvas API object, if applicable 
        Example: https://canvas.example.edu/api/v1/courses/222/assignments/987"""
    page_url = Column(String)
    """(only for 'Page' type) unique locator for the linked wiki page 
        Example: my-page-title"""
    external_url = Column(String)
    """(only for 'ExternalUrl' and 'ExternalTool' types) external url that the item points to 
        Example: https://www.example.com/externalurl"""
    new_tab = Column(Boolean)
    """(only for 'ExternalTool' type) whether the external tool opens in a new tab 
        Example: None"""
    completion_requirement = relationship('CompletionRequirement')
    """Completion requirement for this module item 
        Example: {'type': 'min_score', 'min_score': 10, 'completed': True}"""
    content_details = relationship('ContentDetails')
    """(Present only if requested through include[]=content_details) If applicable, returns additional details specific to the associated object 
        Example: {'points_possible': 20, 'due_at': '2012-12-31T06:00:00-06:00', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00'}"""
    published = Column(Boolean)
    """(Optional) Whether this module item is published. This field is present only if the caller has permission to view unpublished items. 
        Example: True"""


class ModuleItemSequenceNode(Base):
    __tablename__ = 'module_item_sequence_node'
    prev = relationship('ModuleItem')
    """The previous ModuleItem in the sequence 
        Example: None"""
    current = relationship('ModuleItem')
    """The ModuleItem being queried 
        Example: {'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}"""
    next = relationship('ModuleItem')
    """The next ModuleItem in the sequence 
        Example: {'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}"""
    mastery_path = relationship('Unknown')
    """The conditional release rule for the module item, if applicable 
        Example: {'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}"""


class ModuleItemSequence(Base):
    __tablename__ = 'module_item_sequence'
    items = Column(JsonObject)
"""List[ModuleItemSequenceNode]"""
    """an array containing one ModuleItemSequenceNode for each appearence of the asset in the module sequence (up to 10 total) 
        Example: [{'prev': None, 'current': {'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}, 'next': {'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}, 'mastery_path': {'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}}]"""
    modules = Column(JsonObject)
"""List[Module]"""
    """an array containing each Module referenced above 
        Example: [{'id': 123, 'name': 'Overview'}, {'id': 127, 'name': 'Imaginary Numbers'}]"""


class SisImportError(Base):
    __tablename__ = 'sis_import_error'
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. 
        Example: 1"""
    file = Column(String)
    """The file where the error message occurred. 
        Example: courses.csv"""
    message = Column(String)
    """The error message that from the record. 
        Example: No short_name given for course C001"""
    row_info = Column(String)
    """The contents of the line that had the error. 
        Example: account_1, Sub account 1,, active """
    row = Column(Integer)
    """The line number where the error occurred. Some Importers do not yet support this. This is a 1 based index starting with the header row. 
        Example: 34"""


class AuthenticationProvider(Base):
    __tablename__ = 'authentication_provider'
    identifier_format = Column(String)
    """Valid for SAML providers. 
        Example: urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"""
    auth_type = Column(String)
    """Valid for all providers. 
        Example: saml"""
    id = Column(Integer)
    """Valid for all providers. 
        Example: 1649"""
    log_out_url = Column(String)
    """Valid for SAML providers. 
        Example: http://example.com/saml1/slo"""
    log_in_url = Column(String)
    """Valid for SAML and CAS providers. 
        Example: http://example.com/saml1/sli"""
    certificate_fingerprint = Column(String)
    """Valid for SAML providers. 
        Example: 111222"""
    requested_authn_context = Column(String)
    """Valid for SAML providers. 
        Example: None"""
    auth_host = Column(String)
    """Valid for LDAP providers. 
        Example: 127.0.0.1"""
    auth_filter = Column(String)
    """Valid for LDAP providers. 
        Example: filter1"""
    auth_over_tls = Column(Integer)
    """Valid for LDAP providers. 
        Example: None"""
    auth_base = Column(String)
    """Valid for LDAP and CAS providers. 
        Example: None"""
    auth_username = Column(String)
    """Valid for LDAP providers. 
        Example: username1"""
    auth_port = Column(Integer)
    """Valid for LDAP providers. 
        Example: None"""
    position = Column(Integer)
    """Valid for all providers. 
        Example: 1"""
    idp_entity_id = Column(String)
    """Valid for SAML providers. 
        Example: http://example.com/saml1"""
    login_attribute = Column(String)
    """Valid for SAML providers. 
        Example: nameid"""
    sig_alg = Column(String)
    """Valid for SAML providers. 
        Example: http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"""
    jit_provisioning = Column(Boolean)
    """Just In Time provisioning. Valid for all providers except Canvas (which has the similar in concept self_registration setting). 
        Example: None"""
    federated_attributes = relationship('FederatedAttributesConfig')
    """None 
        Example: None"""
    mfa_required = Column(Boolean)
    """If multi-factor authentication is required when logging in with this authentication provider. The account must not have MFA disabled. 
        Example: None"""


class SSOSettings(Base):
    """Settings that are applicable across an account's authentication configuration, even if there are multiple individual providers"""
    __tablename__ = 'sso_settings'
    login_handle_name = Column(String)
    """The label used for unique login identifiers. 
        Example: Username"""
    change_password_url = Column(String)
    """The url to redirect users to for password resets. Leave blank for default Canvas behavior 
        Example: https://example.com/reset_password"""
    auth_discovery_url = Column(String)
    """If a discovery url is set, canvas will forward all users to that URL when they need to be authenticated. That page will need to then help the user figure out where they need to go to log in. If no discovery url is configured, the first configuration will be used to attempt to authenticate the user. 
        Example: https://example.com/which_account"""
    unknown_user_url = Column(String)
    """If an unknown user url is set, Canvas will forward to that url when a service authenticates a user, but that user does not exist in Canvas. The default behavior is to present an error. 
        Example: https://example.com/register_for_canvas"""


class FederatedAttributesConfig(Base):
    """A mapping of Canvas attribute names to attribute names that a provider may send, in order to update the value of these attributes when a user logs in. The values can be a FederatedAttributeConfig, or a raw string corresponding to the "attribute" property of a FederatedAttributeConfig. In responses, full FederatedAttributeConfig objects are returned if JIT provisioning is enabled, otherwise just the attribute names are returned."""
    __tablename__ = 'federated_attributes_config'
    admin_roles = Column(String)
    """A comma separated list of role names to grant to the user. Note that these only apply at the root account level, and not sub-accounts. If the attribute is not marked for provisioning only, the user will also be removed from any other roles they currently hold that are not still specified by the IdP. 
        Example: None"""
    display_name = Column(String)
    """The full display name of the user 
        Example: None"""
    email = Column(String)
    """The user's e-mail address 
        Example: None"""
    given_name = Column(String)
    """The first, or given, name of the user 
        Example: None"""
    integration_id = Column(String)
    """The secondary unique identifier for SIS purposes 
        Example: None"""
    locale = Column(String)
    """The user's preferred locale/language 
        Example: None"""
    name = Column(String)
    """The full name of the user 
        Example: None"""
    sis_user_id = Column(String)
    """The unique SIS identifier 
        Example: None"""
    sortable_name = Column(String)
    """The full name of the user for sorting purposes 
        Example: None"""
    surname = Column(String)
    """The surname, or last name, of the user 
        Example: None"""
    timezone = Column(String)
    """The user's preferred time zone 
        Example: None"""


class FederatedAttributeConfig(Base):
    """A single attribute name to be federated when a user logs in"""
    __tablename__ = 'federated_attribute_config'
    attribute = Column(String)
    """The name of the attribute as it will be sent from the authentication provider 
        Example: mail"""
    provisioning_only = Column(Boolean)
    """If the attribute should be applied only when provisioning a new user, rather than all logins 
        Example: None"""


class ProficiencyRating(Base):
    __tablename__ = 'proficiency_rating'
    description = Column(String)
    """The description of the rating 
        Example: Exceeds Mastery"""
    points = Column(Integer)
    """A non-negative number of points for the rating 
        Example: 4"""
    mastery = Column(Boolean)
    """Indicates the rating where mastery is first achieved 
        Example: None"""
    color = Column(String)
    """The hex color code of the rating 
        Example: 127A1B"""


class Proficiency(Base):
    __tablename__ = 'proficiency'
    ratings = Column(JsonObject(List))
    """An array of proficiency ratings. See the ProficiencyRating specification above. 
        Example: None"""


class Tab(Base):
    __tablename__ = 'tab'
    html_url = Column(String)
    """None 
        Example: /courses/1/external_tools/4"""
    id = Column(String)
    """None 
        Example: context_external_tool_4"""
    label = Column(String)
    """None 
        Example: WordPress"""
    type = Column(String)
    """None 
        Example: external"""
    hidden = Column(Boolean)
    """only included if true 
        Example: True"""
    visibility = Column(String)
    """possible values are: public, members, admins, and none 
        Example: public"""
    position = Column(Integer)
    """1 based 
        Example: 2"""


class GradeChangeEventLinks(Base):
    __tablename__ = 'grade_change_event_links'
    assignment = Column(Integer)
    """ID of the assignment associated with the event 
        Example: 2319"""
    course = Column(Integer)
    """ID of the course associated with the event. will match the context_id in the associated assignment if the context type for the assignment is a course 
        Example: 2319"""
    student = Column(Integer)
    """ID of the student associated with the event. will match the user_id in the associated submission. 
        Example: 2319"""
    grader = Column(Integer)
    """ID of the grader associated with the event. will match the grader_id in the associated submission. 
        Example: 2319"""
    page_view = Column(String)
    """ID of the page view during the event if it exists. 
        Example: e2b76430-27a5-0131-3ca1-48e0eb13f29b"""


class GradeChangeEvent(Base):
    __tablename__ = 'grade_change_event'
    id = Column(String)
    """ID of the event. 
        Example: e2b76430-27a5-0131-3ca1-48e0eb13f29b"""
    created_at = Column(DateTime)
    """timestamp of the event 
        Example: 2012-07-19T15:00:00-06:00"""
    event_type = Column(String)
    """GradeChange event type 
        Example: grade_change"""
    excused_after = Column(Boolean)
    """Boolean indicating whether the submission was excused after the change. 
        Example: True"""
    excused_before = Column(Boolean)
    """Boolean indicating whether the submission was excused before the change. 
        Example: None"""
    grade_after = Column(String)
    """The grade after the change. 
        Example: 8"""
    grade_before = Column(String)
    """The grade before the change. 
        Example: 8"""
    graded_anonymously = Column(Boolean)
    """Boolean indicating whether the student name was visible when the grade was given. Could be null if the grade change record was created before this feature existed. 
        Example: True"""
    version_number = Column(String)
    """Version Number of the grade change submission. 
        Example: 1"""
    request_id = Column(String)
    """The unique request id of the request during the grade change. 
        Example: e2b76430-27a5-0131-3ca1-48e0eb13f29b"""
    links = relationship('GradeChangeEventLinks')
    """None 
        Example: None"""


class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer)
    """The unique identifier for the report. 
        Example: 1"""
    report = Column(String)
    """The type of report. 
        Example: sis_export_csv"""
    file_url = Column(String)
    """The url to the report download. 
        Example: https://example.com/some/path"""
    attachment = relationship('File')
    """The attachment api object of the report. Only available after the report has completed. 
        Example: None"""
    status = Column(String)
    """The status of the report 
        Example: complete"""
    created_at = Column(DateTime)
    """The date and time the report was created. 
        Example: 2013-12-01T23:59:00-06:00"""
    started_at = Column(DateTime)
    """The date and time the report started processing. 
        Example: 2013-12-02T00:03:21-06:00"""
    ended_at = Column(DateTime)
    """The date and time the report finished processing. 
        Example: 2013-12-02T00:03:21-06:00"""
    parameters = relationship('ReportParameters')
    """The report parameters 
        Example: {'course_id': 2, 'start_at': '2012-07-13T10:55:20-06:00', 'end_at': '2012-07-13T10:55:20-06:00'}"""
    progress = Column(Integer)
    """The progress of the report 
        Example: 100"""
    current_line = Column(Integer)
    """This is the current line count being written to the report. It updates every 1000 records. 
        Example: 12000"""


class ReportParameters(Base):
    """The parameters returned will vary for each report."""
    __tablename__ = 'report_parameters'
    enrollment_term_id = Column(Integer)
    """The canvas id of the term to get grades from 
        Example: 2"""
    include_deleted = Column(Boolean)
    """If true, deleted objects will be included. If false, deleted objects will be omitted. 
        Example: None"""
    course_id = Column(Integer)
    """The id of the course to report on 
        Example: 2"""
    orderEnum = enum.Enum('orderEnum', ['users', 'courses', 'outcomes'])
    """Enum for the allowed values of the order field"""
    order = Column(Enum(orderEnum))
    """The sort order for the csv, Options: 'users', 'courses', 'outcomes'. 
        Example: users"""
    users = Column(Boolean)
    """If true, user data will be included. If false, user data will be omitted. 
        Example: None"""
    accounts = Column(Boolean)
    """If true, account data will be included. If false, account data will be omitted. 
        Example: None"""
    terms = Column(Boolean)
    """If true, term data will be included. If false, term data will be omitted. 
        Example: None"""
    courses = Column(Boolean)
    """If true, course data will be included. If false, course data will be omitted. 
        Example: None"""
    sections = Column(Boolean)
    """If true, section data will be included. If false, section data will be omitted. 
        Example: None"""
    enrollments = Column(Boolean)
    """If true, enrollment data will be included. If false, enrollment data will be omitted. 
        Example: None"""
    groups = Column(Boolean)
    """If true, group data will be included. If false, group data will be omitted. 
        Example: None"""
    xlist = Column(Boolean)
    """If true, data for crosslisted courses will be included. If false, data for crosslisted courses will be omitted. 
        Example: None"""
    sis_terms_csv = Column(Integer)
    """None 
        Example: 1"""
    sis_accounts_csv = Column(Integer)
    """None 
        Example: 1"""
    include_enrollment_state = Column(Boolean)
    """If true, enrollment state will be included. If false, enrollment state will be omitted. Defaults to false. 
        Example: None"""
    enrollment_state = Column(JsonObject)
"""List[str]"""
    """Include enrollment state. Defaults to 'all' Options: ['active'| 'invited'| 'creation_pending'| 'deleted'| 'rejected'| 'completed'| 'inactive'| 'all'] 
        Example: ['all']"""
    start_at = Column(DateTime)
    """The beginning date for submissions. Max time range is 2 weeks. 
        Example: 2012-07-13T10:55:20-06:00"""
    end_at = Column(DateTime)
    """The end date for submissions. Max time range is 2 weeks. 
        Example: 2012-07-13T10:55:20-06:00"""


class Profile(Base):
    """Profile details for a Canvas user."""
    __tablename__ = 'profile'
    id = Column(Integer)
    """The ID of the user. 
        Example: 1234"""
    name = Column(String)
    """Sample User 
        Example: Sample User"""
    short_name = Column(String)
    """Sample User 
        Example: Sample User"""
    sortable_name = Column(String)
    """user, sample 
        Example: user, sample"""
    title = Column(String)
    """None 
        Example: None"""
    bio = Column(String)
    """None 
        Example: None"""
    primary_email = Column(String)
    """sample_user@example.com 
        Example: sample_user@example.com"""
    login_id = Column(String)
    """sample_user@example.com 
        Example: sample_user@example.com"""
    sis_user_id = Column(String)
    """sis1 
        Example: sis1"""
    lti_user_id = Column(String)
    """None 
        Example: None"""
    avatar_url = Column(String)
    """The avatar_url can change over time, so we recommend not caching it for more than a few hours 
        Example: ..url.."""
    calendar = relationship('CalendarLink')
    """None 
        Example: None"""
    time_zone = Column(String)
    """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone. 
        Example: America/Denver"""
    locale = Column(String)
    """The users locale. 
        Example: None"""
    k5_user = Column(Boolean)
    """Optional: Whether or not the user is a K5 user. This field is nil if the user settings are not for the user making the request. 
        Example: True"""


class Avatar(Base):
    """Possible avatar for a user."""
    __tablename__ = 'avatar'
    type = Column(String)
    """['gravatar'|'attachment'|'no_pic'] The type of avatar record, for categorization purposes. 
        Example: gravatar"""
    url = Column(String)
    """The url of the avatar 
        Example: https://secure.gravatar.com/avatar/2284..."""
    token = Column(String)
    """A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client. 
        Example: <opaque_token>"""
    display_name = Column(String)
    """A textual description of the avatar record. 
        Example: user, sample"""
    id = Column(Integer)
    """['attachment' type only] the internal id of the attachment 
        Example: 12"""
    content_type = Column(String)
    """['attachment' type only] the content-type of the attachment. 
        Example: image/jpeg"""
    filename = Column(String)
    """['attachment' type only] the filename of the attachment 
        Example: profile.jpg"""
    size = Column(Integer)
    """['attachment' type only] the size of the attachment 
        Example: 32649"""


class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer)
    """The unique identifier for the account role/user assignment. 
        Example: 1023"""
    role = Column(String)
    """The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API. 
        Example: AccountAdmin"""
    user = relationship('User')
    """The user the role is assigned to. See the Users API for details. 
        Example: None"""
    workflow_state = Column(String)
    """The status of the account role/user assignment. 
        Example: deleted"""


class OutcomeResult(Base):
    """A student's result for an outcome"""
    __tablename__ = 'outcome_result'
    id = Column(Integer)
    """A unique identifier for this result 
        Example: 42"""
    score = Column(Integer)
    """The student's score 
        Example: 6"""
    submitted_or_assessed_at = Column(DateTime)
    """The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed. 
        Example: 2013-02-01T00:00:00-06:00"""
    links = relationship('Unknown')
    """Unique identifiers of objects associated with this result 
        Example: {'user': '3', 'learning_outcome': '97', 'alignment': '53'}"""
    percent = Column(Integer)
    """score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome 
        Example: 0.65"""


class OutcomeRollupScoreLinks(Base):
    __tablename__ = 'outcome_rollup_score_links'
    outcome = Column(Integer)
    """The id of the related outcome 
        Example: 42"""


class OutcomeRollupScore(Base):
    __tablename__ = 'outcome_rollup_score'
    score = Column(Integer)
    """The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores. 
        Example: 3"""
    count = Column(Integer)
    """The number of alignment scores included in this rollup. 
        Example: 6"""
    links = relationship('OutcomeRollupScoreLinks')
    """None 
        Example: {'outcome': '42'}"""


class OutcomeRollupLinks(Base):
    __tablename__ = 'outcome_rollup_links'
    course = Column(Integer)
    """If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to 
        Example: 42"""
    user = Column(Integer)
    """(Optional) The id of the user that this rollup applies to 
        Example: 42"""
    section = Column(Integer)
    """(Optional) The id of the section the user is in 
        Example: 57"""


class OutcomeRollup(Base):
    __tablename__ = 'outcome_rollup'
    scores = relationship('OutcomeRollupScore')
    """an array of OutcomeRollupScore objects 
        Example: None"""
    name = Column(String)
    """The name of the resource for this rollup. For example, the user name. 
        Example: John Doe"""
    links = relationship('OutcomeRollupLinks')
    """None 
        Example: {'course': 42, 'user': 42, 'section': 57}"""


class OutcomePath(Base):
    """The full path to an outcome"""
    __tablename__ = 'outcome_path'
    id = Column(Integer)
    """A unique identifier for this outcome 
        Example: 42"""
    parts = relationship('OutcomePathPart')
    """an array of OutcomePathPart objects 
        Example: None"""


class OutcomePathPart(Base):
    """An outcome or outcome group"""
    __tablename__ = 'outcome_path_part'
    name = Column(String)
    """The title of the outcome or outcome group 
        Example: Spelling out numbers"""


class SharedBrandConfig(Base):
    __tablename__ = 'shared_brand_config'
    id = Column(Integer)
    """The shared_brand_config identifier. 
        Example: 987"""
    account_id = Column(String)
    """The id of the account it should be shared within. 
        Example: None"""
    brand_config_md5 = Column(String)
    """The md5 (since BrandConfigs are identified by MD5 and not numeric id) of the BrandConfig to share. 
        Example: 1d31002c95842f8fe16da7dfcc0d1f39"""
    name = Column(String)
    """The name to share this theme as 
        Example: Crimson and Gold Verson 1"""
    created_at = Column(DateTime)
    """When this was created 
        Example: 2012-07-13T10:55:20-06:00"""
    updated_at = Column(DateTime)
    """When this was last updated 
        Example: 2012-07-13T10:55:20-06:00"""


class HistoryEntry(Base):
    """Information about a recently visited item or page in Canvas"""
    __tablename__ = 'history_entry'
    asset_code = Column(String)
    """The asset string for the item viewed 
        Example: assignment_123"""
    asset_name = Column(String)
    """The name of the item 
        Example: Test Assignment"""
    asset_icon = Column(String)
    """The icon type shown for the item. One of 'icon-announcement', 'icon-assignment', 'icon-calendar-month', 'icon-discussion', 'icon-document', 'icon-download', 'icon-gradebook', 'icon-home', 'icon-message', 'icon-module', 'icon-outcomes', 'icon-quiz', 'icon-user', 'icon-syllabus' 
        Example: icon-assignment"""
    asset_readable_category = Column(String)
    """The associated category describing the asset_icon 
        Example: Assignment"""
    context_type = Column(String)
    """The type of context of the item visited. One of 'Course', 'Group', 'User', or 'Account' 
        Example: Course"""
    context_id = Column(Integer)
    """The id of the context, if applicable 
        Example: 123"""
    context_name = Column(String)
    """The name of the context 
        Example: Something 101"""
    visited_url = Column(String)
    """The URL of the item 
        Example: https://canvas.example.com/courses/123/assignments/456"""
    visited_at = Column(DateTime)
    """When the page was visited 
        Example: 2019-08-01T19:49:47Z"""
    interaction_seconds = Column(Integer)
    """The estimated time spent on the page in seconds 
        Example: 400"""


class OutcomeImportData(Base):
    __tablename__ = 'outcome_import_data'
    import_type = Column(String)
    """The type of outcome import 
        Example: instructure_csv"""


class OutcomeImport(Base):
    __tablename__ = 'outcome_import'
    id = Column(Integer)
    """The unique identifier for the outcome import. 
        Example: 1"""
    learning_outcome_group_id = Column(Integer)
    """The unique identifier for the group into which the outcomes will be imported to, or NULL. 
        Example: 1"""
    created_at = Column(DateTime)
    """The date the outcome import was created. 
        Example: 2013-12-01T23:59:00-06:00"""
    ended_at = Column(DateTime)
    """The date the outcome import finished. Returns null if not finished. 
        Example: 2013-12-02T00:03:21-06:00"""
    updated_at = Column(DateTime)
    """The date the outcome import was last updated. 
        Example: 2013-12-02T00:03:21-06:00"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['created', 'importing', 'succeeded', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The current state of the outcome import.
 - 'created': The outcome import has been created.
 - 'importing': The outcome import is currently processing.
 - 'succeeded': The outcome import has completed successfully.
 - 'failed': The outcome import failed. 
        Example: imported"""
    data = relationship('OutcomeImportData')
    """See the OutcomeImportData specification above. 
        Example: None"""
    progress = Column(String)
    """The progress of the outcome import. 
        Example: 100"""
    user = relationship('User')
    """The user that initiated the outcome_import. See the Users API for details. 
        Example: None"""
    processing_errors = Column(JsonObject)
"""List[List[Unknown]]"""
    """An array of row number / error message pairs. Returns the first 25 errors. 
        Example: [[1, 'Missing required fields: title']]"""


class ErrorReport(Base):
    """A collection of information around a specific notification of a problem"""
    __tablename__ = 'error_report'
    subject = Column(String)
    """The users problem summary, like an email subject line 
        Example: File upload breaking"""
    comments = Column(String)
    """long form documentation of what was witnessed 
        Example: When I went to upload a .mov file to my files page, I got an error.  Retrying didn't help, other file types seem ok"""
    user_perceived_severity = Column(String)
    """categorization of how bad the user thinks the problem is.  Should be one of [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do, extreme_critical_emergency]. 
        Example: just_a_comment"""
    email = Column(String)
    """the email address of the reporting user 
        Example: name@example.com"""
    url = Column(String)
    """URL of the page on which the error was reported 
        Example: https://canvas.instructure.com/courses/1"""
    context_asset_string = Column(String)
    """string describing the asset being interacted with at the time of error.  Formatted '[type]_[id]' 
        Example: user_1"""
    user_roles = Column(String)
    """comma seperated list of roles the reporting user holds.  Can be one [student], or many [teacher,admin] 
        Example: user,teacher,admin"""


class Appointment(Base):
    """Date and time for an appointment"""
    __tablename__ = 'appointment'
    id = Column(Integer)
    """The appointment identifier. 
        Example: 987"""
    start_at = Column(DateTime)
    """Start time for the appointment 
        Example: 2012-07-20T15:00:00-06:00"""
    end_at = Column(DateTime)
    """End time for the appointment 
        Example: 2012-07-20T15:00:00-06:00"""


class AppointmentGroup(Base):
    __tablename__ = 'appointment_group'
    id = Column(Integer)
    """The ID of the appointment group 
        Example: 543"""
    title = Column(String)
    """The title of the appointment group 
        Example: Final Presentation"""
    start_at = Column(DateTime)
    """The start of the first time slot in the appointment group 
        Example: 2012-07-20T15:00:00-06:00"""
    end_at = Column(DateTime)
    """The end of the last time slot in the appointment group 
        Example: 2012-07-20T17:00:00-06:00"""
    description = Column(String)
    """The text description of the appointment group 
        Example: Es muy importante"""
    location_name = Column(String)
    """The location name of the appointment group 
        Example: El Tigre Chino's office"""
    location_address = Column(String)
    """The address of the appointment group's location 
        Example: Room 234"""
    participant_count = Column(Integer)
    """The number of participant who have reserved slots (see include[] argument) 
        Example: 2"""
    reserved_times = Column(JsonObject)
"""List[Appointment]"""
    """The start and end times of slots reserved by the current user as well as the id of the calendar event for the reservation (see include[] argument) 
        Example: [{'id': 987, 'start_at': '2012-07-20T15:00:00-06:00', 'end_at': '2012-07-20T15:00:00-06:00'}]"""
    context_codes = Column(JsonObject)
"""List[str]"""
    """The context codes (i.e. courses) this appointment group belongs to. Only people in these courses will be eligible to sign up. 
        Example: ['course_123']"""
    sub_context_codes = Column(JsonObject)
"""List[int]"""
    """The sub-context codes (i.e. course sections and group categories) this appointment group is restricted to 
        Example: ['course_section_234']"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['pending', 'active', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the appointment group ('pending', 'active' or 'deleted'). 'pending' indicates that it has not been published yet and is invisible to participants. 
        Example: active"""
    requiring_action = Column(Boolean)
    """Boolean indicating whether the current user needs to sign up for this appointment group (i.e. it's reservable and the min_appointments_per_participant limit has not been met by this user). 
        Example: True"""
    appointments_count = Column(Integer)
    """Number of time slots in this appointment group 
        Example: 2"""
    appointments = Column(JsonObject)
"""List[CalendarEvent]"""
    """Calendar Events representing the time slots (see include[] argument) Refer to the Calendar Events API for more information 
        Example: None"""
    new_appointments = Column(JsonObject)
"""List[CalendarEvent]"""
    """Newly created time slots (same format as appointments above). Only returned in Create/Update responses where new time slots have been added 
        Example: None"""
    max_appointments_per_participant = Column(Integer)
    """Maximum number of time slots a user may register for, or null if no limit 
        Example: 1"""
    min_appointments_per_participant = Column(Integer)
    """Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots 
        Example: 1"""
    participants_per_appointment = Column(Integer)
    """Maximum number of participants that may register for each time slot, or null if no limit 
        Example: 1"""
    participantVisibilityEnum = enum.Enum('participantVisibilityEnum', ['private', 'protected'])
    """Enum for the allowed values of the participant_visibility field"""
    participant_visibility = Column(Enum(participantVisibilityEnum))
    """'private' means participants cannot see who has signed up for a particular time slot, 'protected' means that they can 
        Example: private"""
    participantTypeEnum = enum.Enum('participantTypeEnum', ['User', 'Group'])
    """Enum for the allowed values of the participant_type field"""
    participant_type = Column(Enum(participantTypeEnum))
    """Indicates how participants sign up for the appointment group, either as individuals ('User') or in student groups ('Group'). Related to sub_context_codes (i.e. 'Group' signups always have a single group category) 
        Example: User"""
    url = Column(String)
    """URL for this appointment group (to update, delete, etc.) 
        Example: https://example.com/api/v1/appointment_groups/543"""
    html_url = Column(String)
    """URL for a user to view this appointment group 
        Example: http://example.com/appointment_groups/1"""
    created_at = Column(DateTime)
    """When the appointment group was created 
        Example: 2012-07-13T10:55:20-06:00"""
    updated_at = Column(DateTime)
    """When the appointment group was last updated 
        Example: 2012-07-13T10:55:20-06:00"""


class ColumnDatum(Base):
    """ColumnDatum objects contain the entry for a column for each user."""
    __tablename__ = 'column_datum'
    content = Column(String)
    """None 
        Example: Nut allergy"""
    user_id = Column(Integer)
    """None 
        Example: 2"""


class BlackoutDate(Base):
    """Blackout dates are used to prevent scheduling assignments on a given date in course pacing."""
    __tablename__ = 'blackout_date'
    id = Column(Integer)
    """the ID of the blackout date 
        Example: 1"""
    context_id = Column(Integer)
    """the context owning the blackout date 
        Example: 1"""
    context_type = Column(String)
    """None 
        Example: Course"""
    start_date = Column(DateTime)
    """the start date of the blackout date 
        Example: 2022-01-01"""
    end_date = Column(DateTime)
    """the end date of the blackout date 
        Example: 2022-01-02"""
    event_title = Column(String)
    """title of the blackout date 
        Example: some title"""


class WebZipExport(Base):
    __tablename__ = 'web_zip_export'
    id = Column(Integer)
    """the unique identifier for the export 
        Example: 101"""
    created_at = Column(DateTime)
    """the date and time this export was requested 
        Example: 2014-01-01T00:00:00Z"""
    updated_at = Column(DateTime)
    """the date and time this export was last updated 
        Example: 2014-01-01T00:01:00Z"""
    zip_attachment = relationship('File')
    """attachment api object for the export web zip (not present until the export completes) 
        Example: {'url': 'https://example.com/api/v1/attachments/789?download_frd=1&verifier=bG9sY2F0cyEh'}"""
    progress_id = Column(Integer)
    """the unique identifier for the progress object 
        Example: 5"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    user_id = Column(Integer)
    """The ID of the user who started the export 
        Example: 4"""
    course_id = Column(Integer)
    """The ID of the course the export is for 
        Example: 2"""
    content_export_id = Column(Integer)
    """The ID of the content export used in the offline export 
        Example: 5"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['created', 'exporting', 'exported', 'generating', 'generated', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the web zip export: created exporting exported generating generated failed 
        Example: exported"""


class PlannerOverride(Base):
    """User-controlled setting for whether an item should be displayed on the planner or not"""
    __tablename__ = 'planner_override'
    id = Column(Integer)
    """The ID of the planner override 
        Example: 234"""
    plannable_type = Column(String)
    """The type of the associated object for the planner override 
        Example: Assignment"""
    plannable_id = Column(Integer)
    """The id of the associated object for the planner override 
        Example: 1578941"""
    user_id = Column(Integer)
    """The id of the associated user for the planner override 
        Example: 1578941"""
    assignment_id = Column(Integer)
    """The id of the plannable's associated assignment, if it has one 
        Example: 1578941"""
    workflow_state = Column(String)
    """The current published state of the item, synced with the associated object 
        Example: published"""
    marked_complete = Column(Boolean)
    """Controls whether or not the associated plannable item is marked complete on the planner 
        Example: None"""
    dismissed = Column(Boolean)
    """Controls whether or not the associated plannable item shows up in the opportunities list 
        Example: None"""
    created_at = Column(DateTime)
    """The datetime of when the planner override was created 
        Example: 2017-05-09T10:12:00Z"""
    updated_at = Column(DateTime)
    """The datetime of when the planner override was updated 
        Example: 2017-05-09T10:12:00Z"""
    deleted_at = Column(DateTime)
    """The datetime of when the planner override was deleted, if applicable 
        Example: 2017-05-15T12:12:00Z"""


class ContentExport(Base):
    __tablename__ = 'content_export'
    id = Column(Integer)
    """the unique identifier for the export 
        Example: 101"""
    created_at = Column(DateTime)
    """the date and time this export was requested 
        Example: 2014-01-01T00:00:00Z"""
    exportTypeEnum = enum.Enum('exportTypeEnum', ['common_cartridge', 'qti'])
    """Enum for the allowed values of the export_type field"""
    export_type = Column(Enum(exportTypeEnum))
    """the type of content migration: 'common_cartridge' or 'qti' 
        Example: common_cartridge"""
    attachment = relationship('File')
    """attachment api object for the export package (not present before the export completes or after it becomes unavailable for download.) 
        Example: {'url': 'https://example.com/api/v1/attachments/789?download_frd=1&verifier=bG9sY2F0cyEh'}"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    user_id = Column(Integer)
    """The ID of the user who started the export 
        Example: 4"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['created', 'exporting', 'exported', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """Current state of the content migration: created exporting exported failed 
        Example: exported"""


class GradingRules(Base):
    __tablename__ = 'grading_rules'
    drop_lowest = Column(Integer)
    """Number of lowest scores to be dropped for each user. 
        Example: 1"""
    drop_highest = Column(Integer)
    """Number of highest scores to be dropped for each user. 
        Example: 1"""
    never_drop = Column(JsonObject)
"""List[int]"""
    """Assignment IDs that should never be dropped. 
        Example: [33, 17, 24]"""


class AssignmentGroup(Base):
    __tablename__ = 'assignment_group'
    id = Column(Integer)
    """the id of the Assignment Group 
        Example: 1"""
    name = Column(String)
    """the name of the Assignment Group 
        Example: group2"""
    position = Column(Integer)
    """the position of the Assignment Group 
        Example: 7"""
    group_weight = Column(Integer)
    """the weight of the Assignment Group 
        Example: 20"""
    sis_source_id = Column(String)
    """the sis source id of the Assignment Group 
        Example: 1234"""
    integration_data = relationship('Unknown')
    """the integration data of the Assignment Group 
        Example: {'5678': '0954'}"""
    assignments = Column(JsonObject)
"""List[int]"""
    """the assignments in this Assignment Group (see the Assignment API for a detailed list of fields) 
        Example: None"""
    rules = relationship('GradingRules')
    """the grading rules that this Assignment Group has 
        Example: None"""


class ExternalToolTagAttributes(Base):
    __tablename__ = 'external_tool_tag_attributes'
    url = Column(String)
    """URL to the external tool 
        Example: http://instructure.com"""
    new_tab = Column(Boolean)
    """Whether or not there is a new tab for the external tool 
        Example: None"""
    resource_link_id = Column(String)
    """the identifier for this tool_tag 
        Example: ab81173af98b8c33e66a"""


class LockInfo(Base):
    __tablename__ = 'lock_info'
    asset_string = Column(String)
    """Asset string for the object causing the lock 
        Example: assignment_4"""
    unlock_at = Column(DateTime)
    """(Optional) Time at which this was/will be unlocked. Must be before the due date. 
        Example: 2013-01-01T00:00:00-06:00"""
    lock_at = Column(DateTime)
    """(Optional) Time at which this was/will be locked. Must be after the due date. 
        Example: 2013-02-01T00:00:00-06:00"""
    context_module = Column(String)
    """(Optional) Context module causing the lock. 
        Example: {}"""
    manually_locked = Column(Boolean)
    """None 
        Example: True"""


class RubricCriteria(Base):
    __tablename__ = 'rubric_criteria'
    points = Column(Integer)
    """None 
        Example: 10"""
    id = Column(String)
    """The id of rubric criteria. 
        Example: crit1"""
    learning_outcome_id = Column(String)
    """(Optional) The id of the learning outcome this criteria uses, if any. 
        Example: 1234"""
    vendor_guid = Column(String)
    """(Optional) The 3rd party vendor's GUID for the outcome this criteria references, if any. 
        Example: abdsfjasdfne3jsdfn2"""
    description = Column(String)
    """None 
        Example: Criterion 1"""
    long_description = Column(String)
    """None 
        Example: Criterion 1 more details"""
    criterion_use_range = Column(Boolean)
    """None 
        Example: True"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """None 
        Example: None"""
    ignore_for_scoring = Column(Boolean)
    """None 
        Example: True"""


class AssignmentDate(Base):
    """Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field."""
    __tablename__ = 'assignment_date'
    id = Column(Integer)
    """(Optional, missing if 'base' is present) id of the assignment override this date represents 
        Example: 1"""
    base = Column(Boolean)
    """(Optional, present if 'id' is missing) whether this date represents the assignment's or quiz's default due date 
        Example: True"""
    title = Column(String)
    """None 
        Example: Summer Session"""
    due_at = Column(DateTime)
    """The due date for the assignment. Must be between the unlock date and the lock date if there are lock dates 
        Example: 2013-08-28T23:59:00-06:00"""
    unlock_at = Column(DateTime)
    """The unlock date for the assignment. Must be before the due date if there is a due date. 
        Example: 2013-08-01T00:00:00-06:00"""
    lock_at = Column(DateTime)
    """The lock date for the assignment. Must be after the due date if there is a due date. 
        Example: 2013-08-31T23:59:00-06:00"""


class TurnitinSettings(Base):
    __tablename__ = 'turnitin_settings'
    originality_report_visibility = Column(String)
    """None 
        Example: after_grading"""
    s_paper_check = Column(Boolean)
    """None 
        Example: None"""
    internet_check = Column(Boolean)
    """None 
        Example: None"""
    journal_check = Column(Boolean)
    """None 
        Example: None"""
    exclude_biblio = Column(Boolean)
    """None 
        Example: None"""
    exclude_quoted = Column(Boolean)
    """None 
        Example: None"""
    exclude_small_matches_type = Column(String)
    """None 
        Example: percent"""
    exclude_small_matches_value = Column(Integer)
    """None 
        Example: 50"""


class NeedsGradingCount(Base):
    """Used by Assignment model"""
    __tablename__ = 'needs_grading_count'
    section_id = Column(String)
    """The section ID 
        Example: 123456"""
    needs_grading_count = Column(Integer)
    """Number of submissions that need grading 
        Example: 5"""


class ScoreStatistic(Base):
    """Used by Assignment model"""
    __tablename__ = 'score_statistic'
    min = Column(Integer)
    """Min score 
        Example: 1"""
    max = Column(Integer)
    """Max score 
        Example: 10"""
    mean = Column(Integer)
    """Mean score 
        Example: 6"""


class Assignment(Base):
    __tablename__ = 'assignment'
    id = Column(Integer)
    """the ID of the assignment 
        Example: 4"""
    name = Column(String)
    """the name of the assignment 
        Example: some assignment"""
    description = Column(String)
    """the assignment description, in an HTML fragment 
        Example: <p>Do the following:</p>..."""
    created_at = Column(DateTime)
    """The time at which this assignment was originally created 
        Example: 2012-07-01T23:59:00-06:00"""
    updated_at = Column(DateTime)
    """The time at which this assignment was last modified in any way 
        Example: 2012-07-01T23:59:00-06:00"""
    due_at = Column(DateTime)
    """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API. 
        Example: 2012-07-01T23:59:00-06:00"""
    lock_at = Column(DateTime)
    """the lock date (assignment is locked after this date). returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the lock date as it applies to the user requesting information from the API. 
        Example: 2012-07-01T23:59:00-06:00"""
    unlock_at = Column(DateTime)
    """the unlock date (assignment is unlocked after this date) returns null if not present NOTE: If this assignment has assignment overrides, this field will be the unlock date as it applies to the user requesting information from the API. 
        Example: 2012-07-01T23:59:00-06:00"""
    has_overrides = Column(Boolean)
    """whether this assignment has overrides 
        Example: True"""
    all_dates = Column(JsonObject)
"""List[AssignmentDate]"""
    """(Optional) all dates associated with the assignment, if applicable 
        Example: None"""
    course_id = Column(Integer)
    """the ID of the course the assignment belongs to 
        Example: 123"""
    html_url = Column(String)
    """the URL to the assignment's web page 
        Example: https://..."""
    submissions_download_url = Column(String)
    """the URL to download all submissions as a zip 
        Example: https://example.com/courses/:course_id/assignments/:id/submissions?zip=1"""
    assignment_group_id = Column(Integer)
    """the ID of the assignment's group 
        Example: 2"""
    due_date_required = Column(Boolean)
    """Boolean flag indicating whether the assignment requires a due date based on the account level setting 
        Example: True"""
    allowed_extensions = Column(JsonObject)
"""List[str]"""
    """Allowed file extensions, which take effect if submission_types includes 'online_upload'. 
        Example: ['docx', 'ppt']"""
    max_name_length = Column(Integer)
    """An integer indicating the maximum length an assignment's name may be 
        Example: 15"""
    turnitin_enabled = Column(Boolean)
    """Boolean flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available 
        Example: True"""
    vericite_enabled = Column(Boolean)
    """Boolean flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available 
        Example: True"""
    turnitin_settings = relationship('TurnitinSettings')
    """Settings to pass along to turnitin to control what kinds of matches should be considered. originality_report_visibility can be 'immediate', 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can be null, 'percent', 'words' exclude_small_matches_value: - if type is null, this will be null also - if type is 'percent', this will be a number between 0 and 100 representing match size to exclude as a percentage of the document size. - if type is 'words', this will be number > 0 representing how many words a match must contain for it to be considered NOTE: This flag will not appear unless your account has the Turnitin plugin available 
        Example: None"""
    grade_group_students_individually = Column(Boolean)
    """If this is a group assignment, boolean flag indicating whether or not students will be graded individually. 
        Example: None"""
    external_tool_tag_attributes = relationship('ExternalToolTagAttributes')
    """(Optional) assignment's settings for external tools if submission_types include 'external_tool'. Only url and new_tab are included (new_tab defaults to false).  Use the 'External Tools' API if you need more information about an external tool. 
        Example: None"""
    peer_reviews = Column(Boolean)
    """Boolean indicating if peer reviews are required for this assignment 
        Example: None"""
    automatic_peer_reviews = Column(Boolean)
    """Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews. 
        Example: None"""
    peer_review_count = Column(Integer)
    """Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. 
        Example: None"""
    peer_reviews_assign_at = Column(DateTime)
    """String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment's due date, the assignment's due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. 
        Example: 2012-07-01T23:59:00-06:00"""
    intra_group_peer_reviews = Column(Boolean)
    """Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work 
        Example: false"""
    group_category_id = Column(Integer)
    """The ID of the assignment’s group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment. 
        Example: 1"""
    needs_grading_count = Column(Integer)
    """if the requesting user has grading rights, the number of submissions that need grading. 
        Example: 17"""
    needs_grading_count_by_section = Column(JsonObject)
"""List[NeedsGradingCount]"""
    """if the requesting user has grading rights and the 'needs_grading_count_by_section' flag is specified, the number of submissions that need grading split out by section. NOTE: This key is NOT present unless you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER NOTE: it's possible to be enrolled in multiple sections, and if a student is setup that way they will show an assignment that needs grading in multiple sections (effectively the count will be duplicated between sections) 
        Example: [{'section_id': '123456', 'needs_grading_count': 5}, {'section_id': '654321', 'needs_grading_count': 0}]"""
    position = Column(Integer)
    """the sorting order of the assignment in the group 
        Example: 1"""
    post_to_sis = Column(Boolean)
    """(optional, present if Sync Grades to SIS feature is enabled) 
        Example: True"""
    integration_id = Column(String)
    """(optional, Third Party unique identifier for Assignment) 
        Example: 12341234"""
    integration_data = relationship('Unknown')
    """(optional, Third Party integration data for assignment) 
        Example: {'5678': '0954'}"""
    points_possible = Column(Integer)
    """the maximum points possible for the assignment 
        Example: 12.0"""
    submissionTypesEnum = enum.Enum('submissionTypesEnum', ['discussion_topic', 'online_quiz', 'on_paper', 'not_graded', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_types field"""
    submission_types = Column(Enum(submissionTypesEnum))
    """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' 
        Example: ['online_text_entry']"""
    has_submitted_submissions = Column(Boolean)
    """If true, the assignment has been submitted to by at least one student 
        Example: True"""
    gradingTypeEnum = enum.Enum('gradingTypeEnum', ['pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'])
    """Enum for the allowed values of the grading_type field"""
    grading_type = Column(Enum(gradingTypeEnum))
    """The type of grading the assignment receives; one of 'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points' 
        Example: points"""
    grading_standard_id = Column(Integer)
    """The id of the grading standard being applied to this assignment. Valid if grading_type is 'letter_grade' or 'gpa_scale'. 
        Example: None"""
    published = Column(Boolean)
    """Whether the assignment is published 
        Example: True"""
    unpublishable = Column(Boolean)
    """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the assignment. 
        Example: None"""
    only_visible_to_overrides = Column(Boolean)
    """Whether the assignment is only visible to overrides. 
        Example: None"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: None"""
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: None"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This assignment is locked until September 1 at 12:00am"""
    quiz_id = Column(Integer)
    """(Optional) id of the associated quiz (applies only when submission_types is ['online_quiz']) 
        Example: 620"""
    anonymous_submissions = Column(Boolean)
    """(Optional) whether anonymous submissions are accepted (applies only to quiz assignments) 
        Example: None"""
    discussion_topic = relationship('DiscussionTopic')
    """(Optional) the DiscussionTopic associated with the assignment, if applicable 
        Example: None"""
    freeze_on_copy = Column(Boolean)
    """(Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: None"""
    frozen = Column(Boolean)
    """(Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: None"""
    frozen_attributes = Column(JsonObject)
"""List[str]"""
    """(Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: ['title']"""
    submission = relationship('Submission')
    """(Optional) If 'submission' is included in the 'include' parameter, includes a Submission object that represents the current user's (user who is requesting information from the api) current submission for the assignment. See the Submissions API for an example response. If the user does not have a submission, this key will be absent. 
        Example: None"""
    use_rubric_for_grading = Column(Boolean)
    """(Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric. 
        Example: True"""
    rubric_settings = Column(String)
    """(Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric. 
        Example: {"points_possible"=>12}"""
    rubric = Column(JsonObject)
"""List[RubricCriteria]"""
    """(Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric. 
        Example: None"""
    assignment_visibility = Column(JsonObject)
"""List[int]"""
    """(Optional) If 'assignment_visibility' is included in the 'include' parameter, includes an array of student IDs who can see this assignment. 
        Example: [137, 381, 572]"""
    overrides = Column(JsonObject)
"""List[AssignmentOverride]"""
    """(Optional) If 'overrides' is included in the 'include' parameter, includes an array of assignment override objects. 
        Example: None"""
    omit_from_final_grade = Column(Boolean)
    """(Optional) If true, the assignment will be omitted from the student's final grade 
        Example: True"""
    moderated_grading = Column(Boolean)
    """Boolean indicating if the assignment is moderated. 
        Example: True"""
    grader_count = Column(Integer)
    """The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. 
        Example: 3"""
    final_grader_id = Column(Integer)
    """The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. 
        Example: 3"""
    grader_comments_visible_to_graders = Column(Boolean)
    """Boolean indicating if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments. 
        Example: True"""
    graders_anonymous_to_graders = Column(Boolean)
    """Boolean indicating if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments with grader_comments_visible_to_graders set to true. 
        Example: True"""
    grader_names_visible_to_final_grader = Column(Boolean)
    """Boolean indicating if provisional grader identities are visible to the final grader. Only relevant for moderated assignments. 
        Example: True"""
    anonymous_grading = Column(Boolean)
    """Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities. 
        Example: True"""
    allowed_attempts = Column(Integer)
    """The number of submission attempts a student can make for this assignment. -1 is considered unlimited. 
        Example: 2"""
    post_manually = Column(Boolean)
    """Whether the assignment has manual posting enabled. Only relevant for courses using New Gradebook. 
        Example: True"""
    score_statistics = relationship('ScoreStatistic')
    """(Optional) If 'score_statistics' and 'submission' are included in the 'include' parameter and statistics are available, includes the min, max, and mode for this assignment 
        Example: None"""
    can_submit = Column(Boolean)
    """(Optional) If retrieving a single assignment and 'can_submit' is included in the 'include' parameter, flags whether user has the right to submit the assignment (i.e. checks enrollment dates, submission types, locked status, attempts remaining, etc...). Including 'can submit' automatically includes 'submission' in the include parameter. Not available when observed_users are included. 
        Example: True"""
    annotatable_attachment_id = Column(Integer)
    """The id of the attachment to be annotated by students. Relevant only if submission_types includes 'student_annotation'. 
        Example: None"""
    anonymize_students = Column(Boolean)
    """(Optional) Boolean indicating whether student names are anonymized 
        Example: None"""
    require_lockdown_browser = Column(Boolean)
    """(Optional) Boolean indicating whether the Respondus LockDown Browser® is required for this assignment. 
        Example: None"""
    important_dates = Column(Boolean)
    """(Optional) Boolean indicating whether this assignment has important dates. 
        Example: None"""
    muted = Column(Boolean)
    """(Optional, Deprecated) Boolean indicating whether notifications are muted for this assignment. 
        Example: None"""


class SisImportData(Base):
    __tablename__ = 'sis_import_data'
    import_type = Column(String)
    """The type of SIS import 
        Example: instructure_csv"""
    supplied_batches = Column(JsonObject)
"""List[str]"""
    """Which files were included in the SIS import 
        Example: ['term', 'course', 'section', 'user', 'enrollment']"""
    counts = relationship('SisImportCounts')
    """The number of rows processed for each type of import 
        Example: None"""


class SisImportStatistic(Base):
    __tablename__ = 'sis_import_statistic'
    created = Column(Integer)
    """This is the number of items that were created. 
        Example: 18"""
    concluded = Column(Integer)
    """This is the number of items that marked as completed. This only applies to courses and enrollments. 
        Example: 3"""
    deactivated = Column(Integer)
    """This is the number of Enrollments that were marked as 'inactive'. This only applies to enrollments. 
        Example: 1"""
    restored = Column(Integer)
    """This is the number of items that were set to an active state from a completed, inactive, or deleted state. 
        Example: 2"""
    deleted = Column(Integer)
    """This is the number of items that were deleted. 
        Example: 40"""


class SisImportStatistics(Base):
    __tablename__ = 'sis_import_statistics'
    total_state_changes = Column(Integer)
    """This is the total number of items that were changed in the sis import. There are a few caveats that can cause this number to not add up to the individual counts. There are some state changes that happen that have no impact to the object. An example would be changing a course from 'created' to 'claimed'. Both of these would be considered an active course, but would increment this counter. In this example the course would not increment the created or restored counters for course statistic. 
        Example: 382"""
    Account = relationship('SisImportStatistic')
    """This contains that statistics for accounts. 
        Example: None"""
    EnrollmentTerm = relationship('SisImportStatistic')
    """This contains that statistics for terms. 
        Example: None"""
    CommunicationChannel = relationship('SisImportStatistic')
    """This contains that statistics for communication channels. This is an indirect effect from creating or deleting a user. 
        Example: None"""
    AbstractCourse = relationship('SisImportStatistic')
    """This contains that statistics for abstract courses. 
        Example: None"""
    Course = relationship('SisImportStatistic')
    """This contains that statistics for courses. 
        Example: None"""
    CourseSection = relationship('SisImportStatistic')
    """This contains that statistics for course sections. 
        Example: None"""
    Enrollment = relationship('SisImportStatistic')
    """This contains that statistics for enrollments. 
        Example: None"""
    GroupCategory = relationship('SisImportStatistic')
    """This contains that statistics for group categories. 
        Example: None"""
    Group = relationship('SisImportStatistic')
    """This contains that statistics for groups. 
        Example: None"""
    GroupMembership = relationship('SisImportStatistic')
    """This contains that statistics for group memberships. This can be a direct impact from the import or indirect from an enrollment being deleted. 
        Example: None"""
    Pseudonym = relationship('SisImportStatistic')
    """This contains that statistics for pseudonyms. Pseudonyms are logins for users, and are the object that ties an enrollment to a user. This would be impacted from the user importer.  
        Example: None"""
    UserObserver = relationship('SisImportStatistic')
    """This contains that statistics for user observers. 
        Example: None"""
    AccountUser = relationship('SisImportStatistic')
    """This contains that statistics for account users. 
        Example: None"""


class SisImportCounts(Base):
    __tablename__ = 'sis_import_counts'
    accounts = Column(Integer)
    """None 
        Example: None"""
    terms = Column(Integer)
    """None 
        Example: 3"""
    abstract_courses = Column(Integer)
    """None 
        Example: None"""
    courses = Column(Integer)
    """None 
        Example: 121"""
    sections = Column(Integer)
    """None 
        Example: 278"""
    xlists = Column(Integer)
    """None 
        Example: None"""
    users = Column(Integer)
    """None 
        Example: 346"""
    enrollments = Column(Integer)
    """None 
        Example: 1542"""
    groups = Column(Integer)
    """None 
        Example: None"""
    group_memberships = Column(Integer)
    """None 
        Example: None"""
    grade_publishing_results = Column(Integer)
    """None 
        Example: None"""
    batch_courses_deleted = Column(Integer)
    """the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted 
        Example: 11"""
    batch_sections_deleted = Column(Integer)
    """the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted 
        Example: None"""
    batch_enrollments_deleted = Column(Integer)
    """the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted 
        Example: 150"""
    error_count = Column(Integer)
    """None 
        Example: None"""
    warning_count = Column(Integer)
    """None 
        Example: None"""


class SisImport(Base):
    __tablename__ = 'sis_import'
    id = Column(Integer)
    """The unique identifier for the SIS import. 
        Example: 1"""
    created_at = Column(DateTime)
    """The date the SIS import was created. 
        Example: 2013-12-01T23:59:00-06:00"""
    ended_at = Column(DateTime)
    """The date the SIS import finished. Returns null if not finished. 
        Example: 2013-12-02T00:03:21-06:00"""
    updated_at = Column(DateTime)
    """The date the SIS import was last updated. 
        Example: 2013-12-02T00:03:21-06:00"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['initializing', 'created', 'importing', 'cleanup_batch', 'imported', 'imported_with_messages', 'aborted', 'failed', 'failed_with_messages', 'restoring', 'partially_restored', 'restored'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """The current state of the SIS import.
 - 'initializing': The SIS import is being created, if this gets stuck in initializing, it will not import and will continue on to next import.
 - 'created': The SIS import has been created.
 - 'importing': The SIS import is currently processing.
 - 'cleanup_batch': The SIS import is currently cleaning up courses, sections, and enrollments not included in the batch for batch_mode imports.
 - 'imported': The SIS import has completed successfully.
 - 'imported_with_messages': The SIS import completed with errors or warnings.
 - 'aborted': The SIS import was aborted.
 - 'failed_with_messages': The SIS import failed with errors.
 - 'failed': The SIS import failed.
 - 'restoring': The SIS import is restoring states of imported items.
 - 'partially_restored': The SIS import is restored some of the states of imported items. This is generally due to passing a param like undelete only.
 - 'restored': The SIS import is restored all of the states of imported items. 
        Example: imported"""
    data = relationship('SisImportData')
    """data 
        Example: None"""
    statistics = relationship('SisImportStatistics')
    """statistics 
        Example: None"""
    progress = Column(String)
    """The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage 
        Example: 100"""
    errors_attachment = relationship('File')
    """The errors_attachment api object of the SIS import. Only available if there are errors or warning and import has completed. 
        Example: None"""
    user = relationship('User')
    """The user that initiated the sis_batch. See the Users API for details. 
        Example: None"""
    processing_warnings = Column(JsonObject)
"""List[List[str]]"""
    """Only imports that are complete will get this data. An array of CSV_file/warning_message pairs. 
        Example: [['students.csv', "user John Doe has already claimed john_doe's requested login information, skipping"]]"""
    processing_errors = Column(JsonObject)
"""List[List[str]]"""
    """An array of CSV_file/error_message pairs. 
        Example: [['students.csv', 'Error while importing CSV. Please contact support.']]"""
    batch_mode = Column(Boolean)
    """Whether the import was run in batch mode. 
        Example: true"""
    batch_mode_term_id = Column(String)
    """The term the batch was limited to. 
        Example: 1234"""
    multi_term_batch_mode = Column(Boolean)
    """Enables batch mode against all terms in term file. Requires change_threshold to be set. 
        Example: false"""
    skip_deletes = Column(Boolean)
    """When set the import will skip any deletes. 
        Example: false"""
    override_sis_stickiness = Column(Boolean)
    """Whether UI changes were overridden. 
        Example: false"""
    add_sis_stickiness = Column(Boolean)
    """Whether stickiness was added to the batch changes. 
        Example: false"""
    clear_sis_stickiness = Column(Boolean)
    """Whether stickiness was cleared. 
        Example: false"""
    diffing_threshold_exceeded = Column(Boolean)
    """Whether a diffing job failed because the threshold limit got exceeded. 
        Example: true"""
    diffing_data_set_identifier = Column(String)
    """The identifier of the data set that this SIS batch diffs against 
        Example: account-5-enrollments"""
    diffing_remaster = Column(Boolean)
    """Whether diffing remaster data was enabled. 
        Example: false"""
    diffed_against_import_id = Column(Integer)
    """The ID of the SIS Import that this import was diffed against 
        Example: 1"""
    csv_attachments = Column(JsonObject)
"""List[List[File]]"""
    """An array of CSV files for processing 
        Example: None"""

class Feature(Base):
    __tablename__ = 'feature'
    feature = Column(String)
    """The symbolic name of the feature, used in FeatureFlags 
        Example: fancy_wickets"""
    display_name = Column(String)
    """The user-visible name of the feature 
        Example: Fancy Wickets"""
    appliesToEnum = enum.Enum('appliesToEnum', ['Course', 'RootAccount', 'Account', 'User'])
    """Enum for the allowed values of the applies_to field"""
    applies_to = Column(Enum(appliesToEnum))
    """The type of object the feature applies to (RootAccount, Account, Course, or User):
 * RootAccount features may only be controlled by flags on root accounts.
 * Account features may be controlled by flags on accounts and their parent accounts.
 * Course features may be controlled by flags on courses and their parent accounts.
 * User features may be controlled by flags on users and site admin only. 
        Example: Course"""
    feature_flag = relationship('FeatureFlag')
    """The FeatureFlag that applies to the caller 
        Example: {'feature': 'fancy_wickets', 'state': 'allowed'}"""
    root_opt_in = Column(Boolean)
    """If true, a feature that is 'allowed' globally will be 'off' by default in root accounts. Otherwise, root accounts inherit the global 'allowed' setting, which allows sub-accounts and courses to turn features on with no root account action. 
        Example: True"""
    beta = Column(Boolean)
    """Whether the feature is a feature preview. If true, opting in includes ongoing updates outside the regular release schedule. 
        Example: True"""
    autoexpand = Column(Boolean)
    """Whether the details of the feature are autoexpanded on page load vs. the user clicking to expand. 
        Example: True"""
    release_notes_url = Column(String)
    """A URL to the release notes describing the feature 
        Example: http://canvas.example.com/release_notes#fancy_wickets"""


class FeatureFlag(Base):
    __tablename__ = 'feature_flag'
    contextTypeEnum = enum.Enum('contextTypeEnum', ['Course', 'Account', 'User'])
    """Enum for the allowed values of the context_type field"""
    context_type = Column(Enum(contextTypeEnum))
    """The type of object to which this flag applies (Account, Course, or User). (This field is not present if this FeatureFlag represents the global Canvas default) 
        Example: Account"""
    context_id = Column(Integer)
    """The id of the object to which this flag applies (This field is not present if this FeatureFlag represents the global Canvas default) 
        Example: 1038"""
    feature = Column(String)
    """The feature this flag controls 
        Example: fancy_wickets"""
    stateEnum = enum.Enum('stateEnum', ['off', 'allowed', 'allowed_on', 'on'])
    """Enum for the allowed values of the state field"""
    state = Column(Enum(stateEnum))
    """The policy for the feature at this context.  can be 'off', 'allowed', 'allowed_on', or 'on'. 
        Example: allowed"""
    locked = Column(Boolean)
    """If set, this feature flag cannot be changed in the caller's context because the flag is set 'off' or 'on' in a higher context 
        Example: None"""


class AccountNotification(Base):
    __tablename__ = 'account_notification'
    subject = Column(String)
    """The subject of the notifications 
        Example: Attention Students"""
    message = Column(String)
    """The message to be sent in the notification. 
        Example: This is a test of the notification system."""
    start_at = Column(DateTime)
    """When to send out the notification. 
        Example: 2013-08-28T23:59:00-06:00"""
    end_at = Column(DateTime)
    """When to expire the notification. 
        Example: 2013-08-29T23:59:00-06:00"""
    iconEnum = enum.Enum('iconEnum', ['warning', 'information', 'question', 'error', 'calendar'])
    """Enum for the allowed values of the icon field"""
    icon = Column(Enum(iconEnum))
    """The icon to display with the message.  Defaults to warning. 
        Example: information"""
    roles = Column(JsonObject)
"""List[str]"""
    """(Deprecated) The roles to send the notification to.  If roles is not passed it defaults to all roles 
        Example: ['StudentEnrollment']"""
    role_ids = Column(JsonObject)
"""List[int]"""
    """The roles to send the notification to.  If roles is not passed it defaults to all roles 
        Example: [1]"""


class DeveloperKeyAccountBinding(Base):
    __tablename__ = 'developer_key_account_binding'
    id = Column(Integer)
    """The Canvas ID of the binding 
        Example: 1"""
    account_id = Column(Integer)
    """The global Canvas ID of the account in the binding 
        Example: 10000000000001"""
    developer_key_id = Column(Integer)
    """The global Canvas ID of the developer key in the binding 
        Example: 10000000000008"""
    workflow_state = Column(Integer)
    """The workflow state of the binding. Will be one of 'on', 'off', or 'allow.' 
        Example: on"""
    account_owns_binding = Column(Boolean)
    """True if the requested context owns the binding 
        Example: true"""


class LatePolicy(Base):
    __tablename__ = 'late_policy'
    id = Column(Integer)
    """the unique identifier for the late policy 
        Example: 123"""
    course_id = Column(Integer)
    """the unique identifier for the course 
        Example: 123"""
    missing_submission_deduction_enabled = Column(Boolean)
    """whether to enable missing submission deductions 
        Example: True"""
    missing_submission_deduction = Column(Integer)
    """amount of percentage points to deduct 
        Example: 12.34"""
    late_submission_deduction_enabled = Column(Boolean)
    """whether to enable late submission deductions 
        Example: True"""
    late_submission_deduction = Column(Integer)
    """amount of percentage points to deduct per late_submission_interval 
        Example: 12.34"""
    late_submission_interval = Column(String)
    """time interval for late submission deduction 
        Example: hour"""
    late_submission_minimum_percent_enabled = Column(Boolean)
    """whether to enable late submission minimum percent 
        Example: True"""
    late_submission_minimum_percent = Column(Integer)
    """the minimum score a submission can receive in percentage points 
        Example: 12.34"""
    created_at = Column(DateTime)
    """the time at which this late policy was originally created 
        Example: 2012-07-01T23:59:00-06:00"""
    updated_at = Column(DateTime)
    """the time at which this late policy was last modified in any way 
        Example: 2012-07-01T23:59:00-06:00"""


class Conversation(Base):
    __tablename__ = 'conversation'
    id = Column(Integer)
    """the unique identifier for the conversation. 
        Example: 2"""
    subject = Column(String)
    """the subject of the conversation. 
        Example: 2"""
    workflow_state = Column(String)
    """The current state of the conversation (read, unread or archived). 
        Example: unread"""
    last_message = Column(String)
    """A <=100 character preview from the most recent message. 
        Example: sure thing, here's the file"""
    start_at = Column(DateTime)
    """the date and time at which the last message was sent. 
        Example: 2011-09-02T12:00:00Z"""
    message_count = Column(Integer)
    """the number of messages in the conversation. 
        Example: 2"""
    subscribed = Column(Boolean)
    """whether the current user is subscribed to the conversation. 
        Example: True"""
    private = Column(Boolean)
    """whether the conversation is private. 
        Example: True"""
    starred = Column(Boolean)
    """whether the conversation is starred. 
        Example: True"""
    properties = Column(JsonObject)
"""List[str]"""
    """Additional conversation flags (last_author, attachments, media_objects). Each listed property means the flag is set to true (i.e. the current user is the most recent author, there are attachments, or there are media objects) 
        Example: None"""
    audience = Column(JsonObject)
"""List[int]"""
    """Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue. 
        Example: None"""
    audience_contexts = Column(JsonObject)
"""List[str]"""
    """Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user's enrollment(s)/ membership type(s) in each course/group. 
        Example: None"""
    avatar_url = Column(String)
    """URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience). 
        Example: https://canvas.instructure.com/images/messages/avatar-group-50.png"""
    participants = Column(JsonObject)
"""List[ConversationParticipant]"""
    """Array of users participating in the conversation. Includes current user. 
        Example: None"""
    visible = Column(Boolean)
    """indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call. 
        Example: True"""
    context_name = Column(String)
    """Name of the course or group in which the conversation is occurring. 
        Example: Canvas 101"""


class ConversationParticipant(Base):
    __tablename__ = 'conversation_participant'
    id = Column(Integer)
    """The user ID for the participant. 
        Example: 2"""
    name = Column(String)
    """A short name the user has selected, for use in conversations or other less formal places through the site. 
        Example: Shelly"""
    full_name = Column(String)
    """The full name of the user. 
        Example: Sheldon Cooper"""
    avatar_url = Column(String)
    """If requested, this field will be included and contain a url to retrieve the user's avatar. 
        Example: https://canvas.instructure.com/images/messages/avatar-50.png"""


class CustomColumn(Base):
    __tablename__ = 'custom_column'
    id = Column(Integer)
    """The ID of the custom gradebook column 
        Example: 2"""
    teacher_notes = Column(Boolean)
    """When true, this column's visibility will be toggled in the Gradebook when a user selects to show or hide notes 
        Example: None"""
    title = Column(String)
    """header text 
        Example: Stuff"""
    position = Column(Integer)
    """column order 
        Example: 1"""
    hidden = Column(Boolean)
    """won't be displayed if hidden is true 
        Example: None"""
    read_only = Column(Boolean)
    """won't be editable in the gradebook UI 
        Example: True"""


class CourseEventLink(Base):
    __tablename__ = 'course_event_link'
    course = Column(Integer)
    """ID of the course for the event. 
        Example: 12345"""
    user = Column(Integer)
    """ID of the user for the event (who made the change). 
        Example: 12345"""
    page_view = Column(String)
    """ID of the page view during the event if it exists. 
        Example: e2b76430-27a5-0131-3ca1-48e0eb13f29b"""
    copied_from = Column(Integer)
    """ID of the course that this course was copied from. This is only included if the event_type is copied_from. 
        Example: 12345"""
    copied_to = Column(Integer)
    """ID of the course that this course was copied to. This is only included if the event_type is copied_to. 
        Example: 12345"""
    sis_batch = Column(Integer)
    """ID of the SIS batch that triggered the event. 
        Example: 12345"""


class CourseEvent(Base):
    __tablename__ = 'course_event'
    id = Column(String)
    """ID of the event. 
        Example: e2b76430-27a5-0131-3ca1-48e0eb13f29b"""
    created_at = Column(DateTime)
    """timestamp of the event 
        Example: 2012-07-19T15:00:00-06:00"""
    event_type = Column(String)
    """Course event type The event type defines the type and schema of the event_data object. 
        Example: updated"""
    event_data = Column(String)
    """Course event data depending on the event type.  This will return an object containing the relevant event data.  An updated event type will return an UpdatedEventData object. 
        Example: {}"""
    event_source = Column(String)
    """Course event source depending on the event type.  This will return a string containing the source of the event. 
        Example: manual|sis|api"""
    links = relationship('CourseEventLink')
    """Jsonapi.org links 
        Example: {'course': '12345', 'user': '12345', 'page_view': 'e2b76430-27a5-0131-3ca1-48e0eb13f29b'}"""


class CreatedEventData(Base):
    """The created event data object returns all the fields that were set in the format of the following example.  If a field does not exist it was not set. The value of each field changed is in the format of [:old_value, :new_value].  The created event type also includes a created_source field to specify what triggered the creation of the course."""
    __tablename__ = 'created_event_data'
    name = Column(JsonObject)
"""List[str]"""
    """None 
        Example: [None, 'Course 1']"""
    start_at = Column(JsonObject)
"""List[datetime]"""
    """None 
        Example: [None, '2012-01-19T15:00:00-06:00']"""
    conclude_at = Column(JsonObject)
"""List[datetime]"""
    """None 
        Example: [None, '2012-01-19T15:00:00-08:00']"""
    is_public = Column(JsonObject)
"""List[bool]"""
    """None 
        Example: [None, False]"""
    created_source = Column(String)
    """The type of action that triggered the creation of the course. 
        Example: manual|sis|api"""


class UpdatedEventData(Base):
    """The updated event data object returns all the fields that have changed in the format of the following example.  If a field does not exist it was not changed.  The value is an array that contains the before and after values for the change as in [:old_value, :new_value]."""
    __tablename__ = 'updated_event_data'
    name = Column(JsonObject)
"""List[str]"""
    """None 
        Example: ['Course 1', 'Course 2']"""
    start_at = Column(JsonObject)
"""List[datetime]"""
    """None 
        Example: ['2012-01-19T15:00:00-06:00', '2012-07-19T15:00:00-06:00']"""
    conclude_at = Column(JsonObject)
"""List[datetime]"""
    """None 
        Example: ['2012-01-19T15:00:00-08:00', '2012-07-19T15:00:00-08:00']"""
    is_public = Column(JsonObject)
"""List[bool]"""
    """None 
        Example: [True, False]"""


class Favorite(Base):
    __tablename__ = 'favorite'
    context_id = Column(Integer)
    """The ID of the object the Favorite refers to 
        Example: 1170"""
    contextTypeEnum = enum.Enum('contextTypeEnum', ['Course'])
    """Enum for the allowed values of the context_type field"""
    context_type = Column(Enum(contextTypeEnum))
    """The type of the object the Favorite refers to (currently, only 'Course' is supported) 
        Example: Course"""


class Page(Base):
    __tablename__ = 'page'
    page_id = Column(Integer)
    """the ID of the page 
        Example: 1"""
    url = Column(String)
    """the unique locator for the page 
        Example: my-page-title"""
    title = Column(String)
    """the title of the page 
        Example: My Page Title"""
    created_at = Column(DateTime)
    """the creation date for the page 
        Example: 2012-08-06T16:46:33-06:00"""
    updated_at = Column(DateTime)
    """the date the page was last updated 
        Example: 2012-08-08T14:25:20-06:00"""
    hide_from_students = Column(Boolean)
    """(DEPRECATED) whether this page is hidden from students (note: this is always reflected as the inverse of the published value) 
        Example: None"""
    editing_roles = Column(String)
    """roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used 
        Example: teachers,students"""
    last_edited_by = relationship('User')
    """the User who last edited the page (this may not be present if the page was imported from another system) 
        Example: None"""
    body = Column(String)
    """the page content, in HTML (present when requesting a single page; omitted when listing pages) 
        Example: <p>Page Content</p>"""
    published = Column(Boolean)
    """whether the page is published (true) or draft state (false). 
        Example: True"""
    front_page = Column(Boolean)
    """whether this page is the front page for the wiki 
        Example: None"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: None"""
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: None"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This page is locked until September 1 at 12:00am"""


class PageRevision(Base):
    __tablename__ = 'page_revision'
    revision_id = Column(Integer)
    """an identifier for this revision of the page 
        Example: 7"""
    updated_at = Column(DateTime)
    """the time when this revision was saved 
        Example: 2012-08-07T11:23:58-06:00"""
    latest = Column(Boolean)
    """whether this is the latest revision or not 
        Example: True"""
    edited_by = relationship('User')
    """the User who saved this revision, if applicable (this may not be present if the page was imported from another system) 
        Example: None"""
    url = Column(String)
    """the following fields are not included in the index action and may be omitted from the show action via summary=1 the historic url of the page 
        Example: old-page-title"""
    title = Column(String)
    """the historic page title 
        Example: Old Page Title"""
    body = Column(String)
    """the historic page contents 
        Example: <p>Old Page Content</p>"""


class ExternalFeed(Base):
    __tablename__ = 'external_feed'
    id = Column(Integer)
    """The ID of the feed 
        Example: 5"""
    display_name = Column(String)
    """The title of the feed, pulled from the feed itself. If the feed hasn't yet been pulled, a temporary name will be synthesized based on the URL 
        Example: My Blog"""
    url = Column(String)
    """The HTTP/HTTPS URL to the feed 
        Example: http://example.com/myblog.rss"""
    header_match = Column(String)
    """If not null, only feed entries whose title contains this string will trigger new posts in Canvas 
        Example: pattern"""
    created_at = Column(DateTime)
    """When this external feed was added to Canvas 
        Example: 2012-06-01T00:00:00-06:00"""
    verbosityEnum = enum.Enum('verbosityEnum', ['link_only', 'truncate', 'full'])
    """Enum for the allowed values of the verbosity field"""
    verbosity = Column(Enum(verbosityEnum))
    """The verbosity setting determines how much of the feed's content is imported into Canvas as part of the posting. 'link_only' means that only the title and a link to the item. 'truncate' means that a summary of the first portion of the item body will be used. 'full' means that the full item body will be used. 
        Example: truncate"""


class Module(Base):
    __tablename__ = 'module'
    id = Column(Integer)
    """the unique identifier for the module 
        Example: 123"""
    workflowStateEnum = enum.Enum('workflowStateEnum', ['active', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(workflowStateEnum))
    """the state of the module: 'active', 'deleted' 
        Example: active"""
    position = Column(Integer)
    """the position of this module in the course (1-based) 
        Example: 2"""
    name = Column(String)
    """the name of this module 
        Example: Imaginary Numbers and You"""
    unlock_at = Column(DateTime)
    """(Optional) the date this module will unlock 
        Example: 2012-12-31T06:00:00-06:00"""
    require_sequential_progress = Column(Boolean)
    """Whether module items must be unlocked in order 
        Example: True"""
    prerequisite_module_ids = Column(JsonObject)
"""List[int]"""
    """IDs of Modules that must be completed before this one is unlocked 
        Example: [121, 122]"""
    items_count = Column(Integer)
    """The number of items in the module 
        Example: 10"""
    items_url = Column(String)
    """The API URL to retrive this module's items 
        Example: https://canvas.example.com/api/v1/modules/123/items"""
    items = Column(JsonObject)
"""List[ModuleItem]"""
    """The contents of this module, as an array of Module Items. (Present only if requested via include[]=items AND the module is not deemed too large by Canvas.) 
        Example: None"""
    stateEnum = enum.Enum('stateEnum', ['locked', 'unlocked', 'started', 'completed'])
    """Enum for the allowed values of the state field"""
    state = Column(Enum(stateEnum))
    """The state of this Module for the calling user one of 'locked', 'unlocked', 'started', 'completed' (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) 
        Example: started"""
    completed_at = Column(DateTime)
    """the date the calling user completed the module (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) 
        Example: None"""
    publish_final_grade = Column(Boolean)
    """if the student's final grade for the course should be published to the SIS upon completion of this module 
        Example: None"""
    published = Column(Boolean)
    """(Optional) Whether this module is published. This field is present only if the caller has permission to view unpublished modules. 
        Example: True"""

