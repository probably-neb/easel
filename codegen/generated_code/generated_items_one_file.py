class AccountCalendar(Base):
    __tablename__ = 'account_calendar'
    id = Column(Integer, primary_key=True)
    """the ID of the account associated with this calendar 
        Example: 204"""
    name = Column(String)
    """the name of the account associated with this calendar 
        Example: Department of Chemistry"""
    root_account_id = Column(Integer)
    """the ID of the root account, or null if this is the root account 
        Example: 1"""
    visible = Column(Boolean)
    """whether this calendar is visible to users 
        Example: True"""
    sub_account_count = Column(Integer)
    """number of this account's direct sub-accounts 
        Example: 0"""
    asset_string = Column(String)
    """Asset string of the account 
        Example: account_4"""
    type = Column(String)
    """Object type 
        Example: account"""
    calendar_event_url = Column(String)
    """url to get full detailed events 
        Example: /accounts/2/calendar_events/%7B%7B%20id%20%7D%7D"""
    can_create_calendar_events = Column(Boolean)
    """whether the user can create calendar events 
        Example: True"""
    create_calendar_event_url = Column(String)
    """API path to create events for the account 
        Example: /accounts/2/calendar_events"""
    new_calendar_event_url = Column(String)
    """url to open the more options event editor 
        Example: /accounts/6/calendar_events/new"""
    parent_account_id = Column(Integer)
    """the account's parent ID, or null if this is the root account 
        Example: 1"""
class AccountNotification(Base):
    __tablename__ = 'account_notification'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the AccountNotification 
        Example: 123456"""
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
    AccountNotificationAllowedValues = enum.Enum('AccountNotificationAllowedValues', ['warning', 'information', 'question', 'error', 'calendar'])
    """Enum for the allowed values of the icon field"""
    icon = Column(Enum(AccountNotificationAllowedValues))
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
class Report(Base):
    __tablename__ = 'report'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the report. 
        Example: 1"""
    report = Column(String)
    """The type of report. 
        Example: sis_export_csv"""
    file_url = Column(String)
    """The url to the report download. 
        Example: https://example.com/some/path"""
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
    progress = Column(Integer)
    """The progress of the report 
        Example: 100"""
    current_line = Column(Integer)
    """This is the current line count being written to the report. It updates every 1000 records. 
        Example: 12000"""
    parameters = relationship('ReportParameters')
    """The report parameters 
        Example: {'course_id': 2, 'start_at': '2012-07-13T10:55:20-06:00', 'end_at': '2012-07-13T10:55:20-06:00'}"""
    attachment = relationship('File')
    """The attachment api object of the report. Only available after the report has completed. 
        Example: """
class ReportParameters(Base):
    """The parameters returned will vary for each report."""
    __tablename__ = 'report_parameters'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ReportParameters 
        Example: 123456"""
    include_deleted = Column(Boolean)
    """If true, deleted objects will be included. If false, deleted objects will be omitted. 
        Example: False"""
    ReportParametersAllowedValues = enum.Enum('ReportParametersAllowedValues', ['users', 'courses', 'outcomes'])
    """Enum for the allowed values of the order field"""
    order = Column(Enum(ReportParametersAllowedValues))
    """The sort order for the csv, Options: 'users', 'courses', 'outcomes'. 
        Example: users"""
    users = Column(Boolean)
    """If true, user data will be included. If false, user data will be omitted. 
        Example: False"""
    accounts = Column(Boolean)
    """If true, account data will be included. If false, account data will be omitted. 
        Example: False"""
    terms = Column(Boolean)
    """If true, term data will be included. If false, term data will be omitted. 
        Example: False"""
    courses = Column(Boolean)
    """If true, course data will be included. If false, course data will be omitted. 
        Example: False"""
    sections = Column(Boolean)
    """If true, section data will be included. If false, section data will be omitted. 
        Example: False"""
    enrollments = Column(Boolean)
    """If true, enrollment data will be included. If false, enrollment data will be omitted. 
        Example: False"""
    groups = Column(Boolean)
    """If true, group data will be included. If false, group data will be omitted. 
        Example: False"""
    xlist = Column(Boolean)
    """If true, data for crosslisted courses will be included. If false, data for crosslisted courses will be omitted. 
        Example: False"""
    sis_terms_csv = Column(Integer)
    """No Description Provided 
        Example: 1"""
    sis_accounts_csv = Column(Integer)
    """No Description Provided 
        Example: 1"""
    include_enrollment_state = Column(Boolean)
    """If true, enrollment state will be included. If false, enrollment state will be omitted. Defaults to false. 
        Example: False"""
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
    course_id = Column(Integer)
    """The id of the course to report on 
        Example: 2"""
    enrollment_term_id = Column(Integer)
    """The canvas id of the term to get grades from 
        Example: 2"""
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    """the ID of the Account object 
        Example: 2"""
    name = Column(String)
    """The display name of the account 
        Example: Canvas Account"""
    uuid = Column(String)
    """The UUID of the account 
        Example: WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5"""
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
    integration_id = Column(String)
    """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. 
        Example: 123xyz"""
    lti_guid = Column(String)
    """The account's identifier that is sent as context_id in LTI launches. 
        Example: 123xyz"""
    workflow_state = Column(String)
    """The state of the account. Can be 'active' or 'deleted'. 
        Example: active"""
    sis_account_id = Column(String)
    """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information. 
        Example: 123xyz"""
    parent_account_id = Column(Integer)
    """The account's parent ID, or null if this is the root account 
        Example: 1"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 12"""
class HelpLink(Base):
    __tablename__ = 'help_link'
    id = Column(String, primary_key=True)
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
    HelpLinkAllowedValues = enum.Enum('HelpLinkAllowedValues', ['default', 'custom'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(HelpLinkAllowedValues))
    """The type of the help link 
        Example: default"""
    available_to = Column(JsonObject)
"""List[str]"""
    """The roles that have access to this help link 
        Example: ['user', 'student', 'teacher', 'admin', 'observer', 'unenrolled']"""
class HelpLinks(Base):
    __tablename__ = 'help_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the HelpLinks 
        Example: 123456"""
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
class TermsOfService(Base):
    __tablename__ = 'terms_of_service'
    id = Column(Integer, primary_key=True)
    """Terms Of Service id 
        Example: 1"""
    TermsOfServiceAllowedValues = enum.Enum('TermsOfServiceAllowedValues', ['default', 'custom', 'no_terms'])
    """Enum for the allowed values of the terms_type field"""
    terms_type = Column(Enum(TermsOfServiceAllowedValues))
    """The given type for the Terms of Service 
        Example: default"""
    passive = Column(Boolean)
    """Boolean dictating if the user must accept Terms of Service 
        Example: False"""
    content = Column(String)
    """Content of the Terms of Service 
        Example: To be or not to be that is the question"""
    self_registration_type = Column(String)
    """The type of self registration allowed 
        Example: ['none', 'observer', 'all']"""
    account_id = Column(Integer)
    """The id of the root account that owns the Terms of Service 
        Example: 1"""
class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    """the ID of the Account object 
        Example: 2"""
    name = Column(String)
    """The display name of the account 
        Example: Canvas Account"""
    uuid = Column(String)
    """The UUID of the account 
        Example: WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5"""
    root_account_id = Column(Integer)
    """The ID of the root account, or null if this is the root account 
        Example: 1"""
    workflow_state = Column(String)
    """The state of the account. Can be 'active' or 'deleted'. 
        Example: active"""
    parent_account_id = Column(Integer)
    """The account's parent ID, or null if this is the root account 
        Example: 1"""
class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the account role/user assignment. 
        Example: 1023"""
    role = Column(String)
    """The account role assigned. This can be 'AccountAdmin' or a user-defined role created by the Roles API. 
        Example: AccountAdmin"""
    workflow_state = Column(String)
    """The status of the account role/user assignment. 
        Example: deleted"""
    user = relationship('User')
    """The user the role is assigned to. See the Users API for details. 
        Example: """
class ExternalFeed(Base):
    __tablename__ = 'external_feed'
    id = Column(Integer, primary_key=True)
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
    ExternalFeedAllowedValues = enum.Enum('ExternalFeedAllowedValues', ['link_only', 'truncate', 'full'])
    """Enum for the allowed values of the verbosity field"""
    verbosity = Column(Enum(ExternalFeedAllowedValues))
    """The verbosity setting determines how much of the feed's content is imported into Canvas as part of the posting. 'link_only' means that only the title and a link to the item. 'truncate' means that a summary of the first portion of the item body will be used. 'full' means that the full item body will be used. 
        Example: truncate"""
class Scope(Base):
    __tablename__ = 'scope'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Scope 
        Example: 123456"""
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
class Appointment(Base):
    """Date and time for an appointment"""
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True)
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
    id = Column(Integer, primary_key=True)
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
    AppointmentGroupAllowedValues = enum.Enum('AppointmentGroupAllowedValues', ['pending', 'active', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(AppointmentGroupAllowedValues))
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
        Example: []"""
    new_appointments = Column(JsonObject)
"""List[CalendarEvent]"""
    """Newly created time slots (same format as appointments above). Only returned in Create/Update responses where new time slots have been added 
        Example: []"""
    max_appointments_per_participant = Column(Integer)
    """Maximum number of time slots a user may register for, or null if no limit 
        Example: 1"""
    min_appointments_per_participant = Column(Integer)
    """Minimum number of time slots a user must register for. If not set, users do not need to sign up for any time slots 
        Example: 1"""
    participants_per_appointment = Column(Integer)
    """Maximum number of participants that may register for each time slot, or null if no limit 
        Example: 1"""
    AppointmentGroupAllowedValues = enum.Enum('AppointmentGroupAllowedValues', ['private', 'protected'])
    """Enum for the allowed values of the participant_visibility field"""
    participant_visibility = Column(Enum(AppointmentGroupAllowedValues))
    """'private' means participants cannot see who has signed up for a particular time slot, 'protected' means that they can 
        Example: private"""
    AppointmentGroupAllowedValues = enum.Enum('AppointmentGroupAllowedValues', ['User', 'Group'])
    """Enum for the allowed values of the participant_type field"""
    participant_type = Column(Enum(AppointmentGroupAllowedValues))
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
class AssignmentExtension(Base):
    __tablename__ = 'assignment_extension'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the AssignmentExtension 
        Example: 123456"""
    user_id = Column(Integer)
    """The ID of the Student that needs the assignment extension. 
        Example: 3"""
    extra_attempts = Column(Integer)
    """Number of times the student is allowed to re-submit the assignment 
        Example: 2"""
    assignment_id = Column(Integer)
    """The ID of the Assignment the extension belongs to. 
        Example: 2"""
class AssignmentGroup(Base):
    __tablename__ = 'assignment_group'
    id = Column(Integer, primary_key=True)
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
    assignments = Column(JsonObject)
"""List[int]"""
    """the assignments in this Assignment Group (see the Assignment API for a detailed list of fields) 
        Example: []"""
    sis_source_id = Column(String)
    """the sis source id of the Assignment Group 
        Example: 1234"""
    rules = relationship('GradingRules')
    """the grading rules that this Assignment Group has 
        Example: """
    integration_data = relationship('Unknown')
    """the integration data of the Assignment Group 
        Example: {'5678': '0954'}"""
class GradingRules(Base):
    __tablename__ = 'grading_rules'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the GradingRules 
        Example: 123456"""
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
class Assignment(Base):
    __tablename__ = 'assignment'
    id = Column(Integer, primary_key=True)
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
        Example: """
    html_url = Column(String)
    """the URL to the assignment's web page 
        Example: https://..."""
    submissions_download_url = Column(String)
    """the URL to download all submissions as a zip 
        Example: https://example.com/courses/:course_id/assignments/:id/submissions?zip=1"""
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
    grade_group_students_individually = Column(Boolean)
    """If this is a group assignment, boolean flag indicating whether or not students will be graded individually. 
        Example: False"""
    peer_reviews = Column(Boolean)
    """Boolean indicating if peer reviews are required for this assignment 
        Example: False"""
    automatic_peer_reviews = Column(Boolean)
    """Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews. 
        Example: False"""
    peer_review_count = Column(Integer)
    """Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. 
        Example: 0"""
    peer_reviews_assign_at = Column(DateTime)
    """String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment's due date, the assignment's due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true. 
        Example: 2012-07-01T23:59:00-06:00"""
    intra_group_peer_reviews = Column(Boolean)
    """Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work 
        Example: false"""
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
    points_possible = Column(Integer)
    """the maximum points possible for the assignment 
        Example: 12.0"""
    AssignmentAllowedValues = enum.Enum('AssignmentAllowedValues', ['discussion_topic', 'online_quiz', 'on_paper', 'not_graded', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_types field"""
    submission_types = Column(Enum(AssignmentAllowedValues))
    """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' 
        Example: ['online_text_entry']"""
    has_submitted_submissions = Column(Boolean)
    """If true, the assignment has been submitted to by at least one student 
        Example: True"""
    AssignmentAllowedValues = enum.Enum('AssignmentAllowedValues', ['pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'])
    """Enum for the allowed values of the grading_type field"""
    grading_type = Column(Enum(AssignmentAllowedValues))
    """The type of grading the assignment receives; one of 'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points' 
        Example: points"""
    published = Column(Boolean)
    """Whether the assignment is published 
        Example: True"""
    unpublishable = Column(Boolean)
    """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the assignment. 
        Example: False"""
    only_visible_to_overrides = Column(Boolean)
    """Whether the assignment is only visible to overrides. 
        Example: False"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: False"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This assignment is locked until September 1 at 12:00am"""
    anonymous_submissions = Column(Boolean)
    """(Optional) whether anonymous submissions are accepted (applies only to quiz assignments) 
        Example: False"""
    freeze_on_copy = Column(Boolean)
    """(Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: False"""
    frozen = Column(Boolean)
    """(Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: False"""
    frozen_attributes = Column(JsonObject)
"""List[str]"""
    """(Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account. 
        Example: ['title']"""
    use_rubric_for_grading = Column(Boolean)
    """(Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric. 
        Example: True"""
    rubric_settings = Column(String)
    """(Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric. 
        Example: {"points_possible"=>12}"""
    rubric = Column(JsonObject)
"""List[RubricCriteria]"""
    """(Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric. 
        Example: """
    assignment_visibility = Column(JsonObject)
"""List[int]"""
    """(Optional) If 'assignment_visibility' is included in the 'include' parameter, includes an array of student IDs who can see this assignment. 
        Example: [137, 381, 572]"""
    overrides = Column(JsonObject)
"""List[AssignmentOverride]"""
    """(Optional) If 'overrides' is included in the 'include' parameter, includes an array of assignment override objects. 
        Example: """
    omit_from_final_grade = Column(Boolean)
    """(Optional) If true, the assignment will be omitted from the student's final grade 
        Example: True"""
    moderated_grading = Column(Boolean)
    """Boolean indicating if the assignment is moderated. 
        Example: True"""
    grader_count = Column(Integer)
    """The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors. 
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
    can_submit = Column(Boolean)
    """(Optional) If retrieving a single assignment and 'can_submit' is included in the 'include' parameter, flags whether user has the right to submit the assignment (i.e. checks enrollment dates, submission types, locked status, attempts remaining, etc...). Including 'can submit' automatically includes 'submission' in the include parameter. Not available when observed_users are included. 
        Example: True"""
    anonymize_students = Column(Boolean)
    """(Optional) Boolean indicating whether student names are anonymized 
        Example: False"""
    require_lockdown_browser = Column(Boolean)
    """(Optional) Boolean indicating whether the Respondus LockDown Browser® is required for this assignment. 
        Example: False"""
    important_dates = Column(Boolean)
    """(Optional) Boolean indicating whether this assignment has important dates. 
        Example: False"""
    muted = Column(Boolean)
    """(Optional, Deprecated) Boolean indicating whether notifications are muted for this assignment. 
        Example: False"""
    assignment_group_id = Column(Integer)
    """the ID of the assignment's group 
        Example: 2"""
    integration_id = Column(String)
    """(optional, Third Party unique identifier for Assignment) 
        Example: 12341234"""
    quiz_id = Column(Integer)
    """(Optional) id of the associated quiz (applies only when submission_types is ['online_quiz']) 
        Example: 620"""
    annotatable_attachment_id = Column(Integer)
    """The id of the attachment to be annotated by students. Relevant only if submission_types includes 'student_annotation'. 
        Example: """
    group_category_id = Column(Integer)
    """The ID of the assignment’s group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment. 
        Example: 1"""
    final_grader_id = Column(Integer)
    """The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments. 
        Example: 3"""
    grading_standard_id = Column(Integer)
    """The id of the grading standard being applied to this assignment. Valid if grading_type is 'letter_grade' or 'gpa_scale'. 
        Example: """
    course_id = Column(Integer)
    """the ID of the course the assignment belongs to 
        Example: 123"""
    external_tool_tag_attributes = relationship('ExternalToolTagAttributes')
    """(Optional) assignment's settings for external tools if submission_types include 'external_tool'. Only url and new_tab are included (new_tab defaults to false).  Use the 'External Tools' API if you need more information about an external tool. 
        Example: """
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: """
    submission = relationship('Submission')
    """(Optional) If 'submission' is included in the 'include' parameter, includes a Submission object that represents the current user's (user who is requesting information from the api) current submission for the assignment. See the Submissions API for an example response. If the user does not have a submission, this key will be absent. 
        Example: """
    turnitin_settings = relationship('TurnitinSettings')
    """Settings to pass along to turnitin to control what kinds of matches should be considered. originality_report_visibility can be 'immediate', 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can be null, 'percent', 'words' exclude_small_matches_value: - if type is null, this will be null also - if type is 'percent', this will be a number between 0 and 100 representing match size to exclude as a percentage of the document size. - if type is 'words', this will be number > 0 representing how many words a match must contain for it to be considered NOTE: This flag will not appear unless your account has the Turnitin plugin available 
        Example: """
    discussion_topic = relationship('DiscussionTopic')
    """(Optional) the DiscussionTopic associated with the assignment, if applicable 
        Example: """
    integration_data = relationship('Unknown')
    """(optional, Third Party integration data for assignment) 
        Example: {'5678': '0954'}"""
    score_statistics = relationship('ScoreStatistic')
    """(Optional) If 'score_statistics' and 'submission' are included in the 'include' parameter and statistics are available, includes the min, max, and mode for this assignment 
        Example: """
class AssignmentDate(Base):
    """Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field."""
    __tablename__ = 'assignment_date'
    id = Column(Integer, primary_key=True)
    """(Optional, missing if 'base' is present) id of the assignment override this date represents 
        Example: 1"""
    base = Column(Boolean)
    """(Optional, present if 'id' is missing) whether this date represents the assignment's or quiz's default due date 
        Example: True"""
    title = Column(String)
    """No Description Provided 
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
class AssignmentOverride(Base):
    __tablename__ = 'assignment_override'
    id = Column(Integer, primary_key=True)
    """the ID of the assignment override 
        Example: 4"""
    student_ids = Column(JsonObject)
"""List[int]"""
    """the IDs of the override's target students (present if the override targets an ad-hoc set of students) 
        Example: [1, 2, 3]"""
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
    group_id = Column(Integer)
    """the ID of the override's target group (present if the override targets a group and the assignment is a group assignment) 
        Example: 2"""
    assignment_id = Column(Integer)
    """the ID of the assignment the override applies to 
        Example: 123"""
class ExternalToolTagAttributes(Base):
    __tablename__ = 'external_tool_tag_attributes'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ExternalToolTagAttributes 
        Example: 123456"""
    url = Column(String)
    """URL to the external tool 
        Example: http://instructure.com"""
    new_tab = Column(Boolean)
    """Whether or not there is a new tab for the external tool 
        Example: False"""
    resource_link_id = Column(String)
    """the identifier for this tool_tag 
        Example: ab81173af98b8c33e66a"""
class LockInfo(Base):
    __tablename__ = 'lock_info'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the LockInfo 
        Example: 123456"""
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
    """No Description Provided 
        Example: True"""
class NeedsGradingCount(Base):
    """Used by Assignment model"""
    __tablename__ = 'needs_grading_count'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the NeedsGradingCount 
        Example: 123456"""
    needs_grading_count = Column(Integer)
    """Number of submissions that need grading 
        Example: 5"""
    section_id = Column(String)
    """The section ID 
        Example: 123456"""
class RubricCriteria(Base):
    __tablename__ = 'rubric_criteria'
    id = Column(String, primary_key=True)
    """The id of rubric criteria. 
        Example: crit1"""
    points = Column(Integer)
    """No Description Provided 
        Example: 10"""
    vendor_guid = Column(String)
    """(Optional) The 3rd party vendor's GUID for the outcome this criteria references, if any. 
        Example: abdsfjasdfne3jsdfn2"""
    description = Column(String)
    """No Description Provided 
        Example: Criterion 1"""
    long_description = Column(String)
    """No Description Provided 
        Example: Criterion 1 more details"""
    criterion_use_range = Column(Boolean)
    """No Description Provided 
        Example: True"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """No Description Provided 
        Example: """
    ignore_for_scoring = Column(Boolean)
    """No Description Provided 
        Example: True"""
    learning_outcome_id = Column(String)
    """(Optional) The id of the learning outcome this criteria uses, if any. 
        Example: 1234"""
class RubricRating(Base):
    __tablename__ = 'rubric_rating'
    id = Column(String, primary_key=True)
    """No Description Provided 
        Example: rat1"""
    points = Column(Integer)
    """No Description Provided 
        Example: 10"""
    description = Column(String)
    """No Description Provided 
        Example: Full marks"""
    long_description = Column(String)
    """No Description Provided 
        Example: Student completed the assignment flawlessly."""
class ScoreStatistic(Base):
    """Used by Assignment model"""
    __tablename__ = 'score_statistic'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ScoreStatistic 
        Example: 123456"""
    min = Column(Integer)
    """Min score 
        Example: 1"""
    max = Column(Integer)
    """Max score 
        Example: 10"""
    mean = Column(Integer)
    """Mean score 
        Example: 6"""
    upper_q = Column(Integer)
    """Upper quartile score 
        Example: 10"""
    median = Column(Integer)
    """Median score 
        Example: 6"""
    lower_q = Column(Integer)
    """Lower quartile score 
        Example: 1"""
class TurnitinSettings(Base):
    __tablename__ = 'turnitin_settings'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the TurnitinSettings 
        Example: 123456"""
    originality_report_visibility = Column(String)
    """No Description Provided 
        Example: after_grading"""
    s_paper_check = Column(Boolean)
    """No Description Provided 
        Example: False"""
    internet_check = Column(Boolean)
    """No Description Provided 
        Example: False"""
    journal_check = Column(Boolean)
    """No Description Provided 
        Example: False"""
    exclude_biblio = Column(Boolean)
    """No Description Provided 
        Example: False"""
    exclude_quoted = Column(Boolean)
    """No Description Provided 
        Example: False"""
    exclude_small_matches_type = Column(String)
    """No Description Provided 
        Example: percent"""
    exclude_small_matches_value = Column(Integer)
    """No Description Provided 
        Example: 50"""
class AuthenticationProvider(Base):
    __tablename__ = 'authentication_provider'
    id = Column(Integer, primary_key=True)
    """Valid for all providers. 
        Example: 1649"""
    identifier_format = Column(String)
    """Valid for SAML providers. 
        Example: urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"""
    auth_type = Column(String)
    """Valid for all providers. 
        Example: saml"""
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
        Example: """
    auth_host = Column(String)
    """Valid for LDAP providers. 
        Example: 127.0.0.1"""
    auth_filter = Column(String)
    """Valid for LDAP providers. 
        Example: filter1"""
    auth_over_tls = Column(Integer)
    """Valid for LDAP providers. 
        Example: """
    auth_base = Column(String)
    """Valid for LDAP and CAS providers. 
        Example: """
    auth_username = Column(String)
    """Valid for LDAP providers. 
        Example: username1"""
    auth_port = Column(Integer)
    """Valid for LDAP providers. 
        Example: """
    position = Column(Integer)
    """Valid for all providers. 
        Example: 1"""
    login_attribute = Column(String)
    """Valid for SAML providers. 
        Example: nameid"""
    sig_alg = Column(String)
    """Valid for SAML providers. 
        Example: http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"""
    jit_provisioning = Column(Boolean)
    """Just In Time provisioning. Valid for all providers except Canvas (which has the similar in concept self_registration setting). 
        Example: """
    mfa_required = Column(Boolean)
    """If multi-factor authentication is required when logging in with this authentication provider. The account must not have MFA disabled. 
        Example: """
    idp_entity_id = Column(String)
    """Valid for SAML providers. 
        Example: http://example.com/saml1"""
    federated_attributes = relationship('FederatedAttributesConfig')
    """No Description Provided 
        Example: """
class FederatedAttributeConfig(Base):
    """A single attribute name to be federated when a user logs in"""
    __tablename__ = 'federated_attribute_config'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the FederatedAttributeConfig 
        Example: 123456"""
    attribute = Column(String)
    """The name of the attribute as it will be sent from the authentication provider 
        Example: mail"""
    provisioning_only = Column(Boolean)
    """If the attribute should be applied only when provisioning a new user, rather than all logins 
        Example: False"""
class FederatedAttributesConfig(Base):
    """A mapping of Canvas attribute names to attribute names that a provider may send, in order to update the value of these attributes when a user logs in. The values can be a FederatedAttributeConfig, or a raw string corresponding to the "attribute" property of a FederatedAttributeConfig. In responses, full FederatedAttributeConfig objects are returned if JIT provisioning is enabled, otherwise just the attribute names are returned."""
    __tablename__ = 'federated_attributes_config'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the FederatedAttributesConfig 
        Example: 123456"""
    admin_roles = Column(String)
    """A comma separated list of role names to grant to the user. Note that these only apply at the root account level, and not sub-accounts. If the attribute is not marked for provisioning only, the user will also be removed from any other roles they currently hold that are not still specified by the IdP. 
        Example: """
    display_name = Column(String)
    """The full display name of the user 
        Example: """
    email = Column(String)
    """The user's e-mail address 
        Example: """
    given_name = Column(String)
    """The first, or given, name of the user 
        Example: """
    locale = Column(String)
    """The user's preferred locale/language 
        Example: """
    name = Column(String)
    """The full name of the user 
        Example: """
    sortable_name = Column(String)
    """The full name of the user for sorting purposes 
        Example: """
    surname = Column(String)
    """The surname, or last name, of the user 
        Example: """
    timezone = Column(String)
    """The user's preferred time zone 
        Example: """
    sis_user_id = Column(String)
    """The unique SIS identifier 
        Example: """
    integration_id = Column(String)
    """The secondary unique identifier for SIS purposes 
        Example: """
class SSOSettings(Base):
    """Settings that are applicable across an account's authentication configuration, even if there are multiple individual providers"""
    __tablename__ = 'sso_settings'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SSOSettings 
        Example: 123456"""
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
class AuthenticationEvent(Base):
    __tablename__ = 'authentication_event'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the AuthenticationEvent 
        Example: 123456"""
    created_at = Column(DateTime)
    """timestamp of the event 
        Example: 2012-07-19T15:00:00-06:00"""
    AuthenticationEventAllowedValues = enum.Enum('AuthenticationEventAllowedValues', ['login', 'logout'])
    """Enum for the allowed values of the event_type field"""
    event_type = Column(Enum(AuthenticationEventAllowedValues))
    """authentication event type ('login' or 'logout') 
        Example: login"""
    account_id = Column(Integer)
    """ID of the account associated with the event. will match the account_id in the associated pseudonym. 
        Example: 2319"""
    pseudonym_id = Column(Integer)
    """ID of the pseudonym (login) associated with the event 
        Example: 9478"""
    user_id = Column(Integer)
    """ID of the user associated with the event will match the user_id in the associated pseudonym. 
        Example: 362"""
class BlackoutDate(Base):
    """Blackout dates are used to prevent scheduling assignments on a given date in course pacing."""
    __tablename__ = 'blackout_date'
    id = Column(Integer, primary_key=True)
    """the ID of the blackout date 
        Example: 1"""
    context_type = Column(String)
    """No Description Provided 
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
    context_id = Column(Integer)
    """the context owning the blackout date 
        Example: 1"""
class BlueprintMigration(Base):
    __tablename__ = 'blueprint_migration'
    id = Column(Integer, primary_key=True)
    """The ID of the migration. 
        Example: 1"""
    subscription_id = Column(Integer)
    """The ID of the associated course's blueprint subscription. Only present when querying a course associated with a blueprint. 
        Example: 101"""
    workflow_state = Column(String)
    """Current state of the content migration: queued, exporting, imports_queued, completed, exports_failed, imports_failed 
        Example: running"""
    created_at = Column(DateTime)
    """Time when the migration was queued 
        Example: 2013-08-28T23:59:00-06:00"""
    exports_started_at = Column(DateTime)
    """Time when the exports begun 
        Example: 2013-08-28T23:59:00-06:00"""
    imports_queued_at = Column(DateTime)
    """Time when the exports were completed and imports were queued 
        Example: 2013-08-28T23:59:00-06:00"""
    imports_completed_at = Column(DateTime)
    """Time when the imports were completed 
        Example: 2013-08-28T23:59:00-06:00"""
    comment = Column(String)
    """User-specified comment describing changes made in this operation 
        Example: Fixed spelling in question 3 of midterm exam"""
    user_id = Column(Integer)
    """The ID of the user who queued the migration. 
        Example: 3"""
    template_id = Column(Integer)
    """The ID of the template the migration belongs to. Only present when querying a blueprint course. 
        Example: 2"""
class BlueprintRestriction(Base):
    """A set of restrictions on editing for copied objects in associated courses"""
    __tablename__ = 'blueprint_restriction'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the BlueprintRestriction 
        Example: 123456"""
    content = Column(Boolean)
    """Restriction on main content (e.g. title, description). 
        Example: True"""
    points = Column(Boolean)
    """Restriction on points possible for assignments and graded learning objects 
        Example: True"""
    due_dates = Column(Boolean)
    """Restriction on due dates for assignments and graded learning objects 
        Example: False"""
    availability_dates = Column(Boolean)
    """Restriction on availability dates for an object 
        Example: True"""
class BlueprintSubscription(Base):
    """Associates a course with a blueprint"""
    __tablename__ = 'blueprint_subscription'
    id = Column(Integer, primary_key=True)
    """The ID of the blueprint course subscription 
        Example: 101"""
    template_id = Column(Integer)
    """The ID of the blueprint template the associated course is subscribed to 
        Example: 1"""
    blueprint_course = relationship('Unknown')
    """The blueprint course subscribed to 
        Example: {'id': 2, 'name': 'Biology 100 Blueprint', 'course_code': 'BIOL 100 BP', 'term_name': 'Default term'}"""
class BlueprintTemplate(Base):
    __tablename__ = 'blueprint_template'
    id = Column(Integer, primary_key=True)
    """The ID of the template. 
        Example: 1"""
    last_export_completed_at = Column(DateTime)
    """Time when the last export was completed 
        Example: 2013-08-28T23:59:00-06:00"""
    associated_course_count = Column(Integer)
    """Number of associated courses for the template 
        Example: 3"""
    course_id = Column(Integer)
    """The ID of the Course the template belongs to. 
        Example: 2"""
    latest_migration = relationship('BlueprintMigration')
    """Details of the latest migration 
        Example: """
class ChangeRecord(Base):
    """Describes a learning object change propagated to associated courses from a blueprint course"""
    __tablename__ = 'change_record'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ChangeRecord 
        Example: 123456"""
    asset_type = Column(String)
    """The type of the learning object that was changed in the blueprint course.  One of 'assignment', 'attachment', 'discussion_topic', 'external_tool', 'quiz', 'wiki_page', 'syllabus', or 'settings'.  For 'syllabus' or 'settings', the asset_id is the course id. 
        Example: assignment"""
    asset_name = Column(String)
    """The name of the learning object that was changed in the blueprint course. 
        Example: Some Assignment"""
    change_type = Column(String)
    """The type of change; one of 'created', 'updated', 'deleted' 
        Example: created"""
    html_url = Column(String)
    """The URL of the changed object 
        Example: https://canvas.example.com/courses/101/assignments/2"""
    locked = Column(Boolean)
    """Whether the object is locked in the blueprint 
        Example: False"""
    exceptions = Column(JsonObject)
"""List[Unknown]"""
    """A list of ExceptionRecords for linked courses that did not receive this update. 
        Example: [{'course_id': 101, 'conflicting_changes': ['points']}]"""
    asset_id = Column(Integer)
    """The ID of the learning object that was changed in the blueprint course. 
        Example: 2"""
class ExceptionRecord(Base):
    """Lists associated courses that did not receive a change propagated from a blueprint"""
    __tablename__ = 'exception_record'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ExceptionRecord 
        Example: 123456"""
    conflicting_changes = Column(JsonObject)
"""List[Unknown]"""
    """A list of change classes in the associated course's copy of the item that prevented a blueprint change from being applied. One or more of ['content', 'points', 'due_dates', 'availability_dates']. 
        Example: ['points']"""
    course_id = Column(Integer)
    """The ID of the associated course 
        Example: 101"""
class Bookmark(Base):
    __tablename__ = 'bookmark'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 1"""
    name = Column(String)
    """No Description Provided 
        Example: Biology 101"""
    url = Column(String)
    """No Description Provided 
        Example: /courses/1"""
    position = Column(Integer)
    """No Description Provided 
        Example: 1"""
    data = relationship('Unknown')
    """No Description Provided 
        Example: {'active_tab': 1}"""
class AssignmentEvent(Base):
    __tablename__ = 'assignment_event'
    id = Column(String, primary_key=True)
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
    AssignmentEventAllowedValues = enum.Enum('AssignmentEventAllowedValues', ['published', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(AssignmentEventAllowedValues))
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
    assignment_overrides = relationship('AssignmentOverride')
    """The list of AssignmentOverrides that apply to this event (See the Assignments API). This information is useful for determining which students or sections this assignment-due event applies to. 
        Example: """
    important_dates = Column(Boolean)
    """Boolean indicating whether this has important dates. 
        Example: True"""
    assignment = relationship('Assignment')
    """The full assignment JSON data (See the Assignments API) 
        Example: """
class CalendarEvent(Base):
    __tablename__ = 'calendar_event'
    id = Column(Integer, primary_key=True)
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
        Example: """
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
        Example: False"""
    child_events_count = Column(Integer)
    """The number of child_events. See child_events (and parent_event_id) 
        Example: 0"""
    child_events = Column(JsonObject)
"""List[int]"""
    """Included by default, but may be excluded (see include[] option). If this is a time slot (see the Appointment Groups API) this will be a list of any reservations. If this is a course-level event, this will be a list of section-level events (if any) 
        Example: """
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
        Example: False"""
    created_at = Column(DateTime)
    """When the calendar event was created 
        Example: 2012-07-12T10:55:20-06:00"""
    updated_at = Column(DateTime)
    """When the calendar event was last updated 
        Example: 2012-07-12T10:55:20-06:00"""
    appointment_group_url = Column(String)
    """The API URL of the appointment group 
        Example: """
    own_reservation = Column(Boolean)
    """If the event is a reservation, this a boolean indicating whether it is the current user's reservation, or someone else's 
        Example: False"""
    reserve_url = Column(String)
    """If the event is a time slot, the API URL for reserving it 
        Example: """
    reserved = Column(Boolean)
    """If the event is a time slot, a boolean indicating whether the user has already made a reservation for it 
        Example: False"""
    participant_type = Column(String)
    """The type of participant to sign up for a slot: 'User' or 'Group' 
        Example: User"""
    participants_per_appointment = Column(Integer)
    """If the event is a time slot, this is the participant limit 
        Example: """
    available_slots = Column(Integer)
    """If the event is a time slot and it has a participant limit, an integer indicating how many slots are available 
        Example: """
    user = Column(String)
    """If the event is a user-level reservation, this will contain the user participant JSON (refer to the Users API). 
        Example: """
    group = Column(String)
    """If the event is a group-level reservation, this will contain the group participant JSON (refer to the Groups API). 
        Example: """
    important_dates = Column(Boolean)
    """Boolean indicating whether this has important dates. 
        Example: True"""
    series_uuid = Column(uuid)
    """Identifies the recurring event series this event may belong to 
        Example: """
    rrule = Column(String)
    """An iCalendar RRULE for defining how events in a recurring event series repeat. 
        Example: """
    series_natural_language = Column(String)
    """A natural language expression of how events occur in the series. (e.g. Daily, 2 times) 
        Example: """
    blackout_date = Column(Boolean)
    """Boolean indicating whether this has blackout date. 
        Example: True"""
    appointment_group_id = Column(Integer)
    """Various Appointment-Group-related fields.These fields are only pertinent to time slots (appointments) and reservations of those time slots. See the Appointment Groups API. The id of the appointment group 
        Example: """
    parent_event_id = Column(Integer)
    """Normally null. If this is a reservation (see the Appointment Groups API), the id will indicate the time slot it is for. If this is a section-level event, this will be the course-level parent event. 
        Example: """
class Collaboration(Base):
    __tablename__ = 'collaboration'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the collaboration 
        Example: 43"""
    collaboration_type = Column(String)
    """A name for the type of collaboration 
        Example: Microsoft Office"""
    user_id = Column(Integer)
    """The canvas id of the user who created the collaboration 
        Example: 92"""
    context_type = Column(String)
    """The canvas type of the course or group to which the collaboration belongs 
        Example: Course"""
    url = Column(String)
    """The LTI launch url to view collaboration. 
        Example: """
    created_at = Column(DateTime)
    """The timestamp when the collaboration was created 
        Example: 2012-06-01T00:00:00-06:00"""
    updated_at = Column(DateTime)
    """The timestamp when the collaboration was last modified 
        Example: 2012-06-01T00:00:00-06:00"""
    description = Column(String)
    """No Description Provided 
        Example: """
    title = Column(String)
    """No Description Provided 
        Example: """
    type = Column(String)
    """Another representation of the collaboration type 
        Example: ExternalToolCollaboration"""
    update_url = Column(String)
    """The LTI launch url to edit the collaboration 
        Example: """
    user_name = Column(String)
    """The name of the user who owns the collaboration 
        Example: John Danger"""
    context_id = Column(Integer)
    """The canvas id of the course or group to which the collaboration belongs 
        Example: 77"""
    document_id = Column(String)
    """The collaboration document identifier for the collaboration provider 
        Example: oinwoenfe8w8ef_onweufe89fef"""
class Collaborator(Base):
    __tablename__ = 'collaborator'
    id = Column(Integer, primary_key=True)
    """The unique user or group identifier for the collaborator. 
        Example: 12345"""
    CollaboratorAllowedValues = enum.Enum('CollaboratorAllowedValues', ['user', 'group'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(CollaboratorAllowedValues))
    """The type of collaborator (e.g. 'user' or 'group'). 
        Example: user"""
    name = Column(String)
    """The name of the collaborator. 
        Example: Don Draper"""
class CommMessage(Base):
    __tablename__ = 'comm_message'
    id = Column(Integer, primary_key=True)
    """The ID of the CommMessage. 
        Example: 42"""
    created_at = Column(DateTime)
    """The date and time this message was created 
        Example: 2013-03-19T21:00:00Z"""
    sent_at = Column(DateTime)
    """The date and time this message was sent 
        Example: 2013-03-20T22:42:00Z"""
    CommMessageAllowedValues = enum.Enum('CommMessageAllowedValues', ['created', 'staged', 'sending', 'sent', 'bounced', 'dashboard', 'cancelled', 'closed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(CommMessageAllowedValues))
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
class CommunicationChannel(Base):
    __tablename__ = 'communication_channel'
    id = Column(Integer, primary_key=True)
    """The ID of the communication channel. 
        Example: 16"""
    address = Column(String)
    """The address, or path, of the communication channel. 
        Example: sheldon@caltech.example.com"""
    CommunicationChannelAllowedValues = enum.Enum('CommunicationChannelAllowedValues', ['email', 'push', 'sms', 'twitter'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(CommunicationChannelAllowedValues))
    """The type of communcation channel being described. Possible values are: 'email', 'push', 'sms', or 'twitter'. This field determines the type of value seen in 'address'. 
        Example: email"""
    position = Column(Integer)
    """The position of this communication channel relative to the user's other channels when they are ordered. 
        Example: 1"""
    CommunicationChannelAllowedValues = enum.Enum('CommunicationChannelAllowedValues', ['unconfirmed', 'active'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(CommunicationChannelAllowedValues))
    """The current state of the communication channel. Possible values are: 'unconfirmed' or 'active'. 
        Example: active"""
    user_id = Column(Integer)
    """The ID of the user that owns this communication channel. 
        Example: 1"""
class Conference(Base):
    __tablename__ = 'conference'
    id = Column(Integer, primary_key=True)
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
        Example: False"""
    long_running = Column(Boolean)
    """If true the conference is long running and has no expected end time 
        Example: False"""
    recordings = Column(JsonObject)
"""List[ConferenceRecording]"""
    """A List of recordings for the conference 
        Example: """
    url = Column(String)
    """URL for the conference, may be null if the conference type doesn't set it 
        Example: """
    join_url = Column(String)
    """URL to join the conference, may be null if the conference type doesn't set it 
        Example: """
    context_type = Column(String)
    """The type of this conference's context, typically 'Course' or 'Group'. 
        Example: """
    context_id = Column(Integer)
    """The ID of this conference's context. 
        Example: """
    user_settings = relationship('Unknown')
    """A collection of settings specific to the conference type 
        Example: {'record': True}"""
class ConferenceRecording(Base):
    __tablename__ = 'conference_recording'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ConferenceRecording 
        Example: 123456"""
    duration_minutes = Column(Integer)
    """No Description Provided 
        Example: 0"""
    title = Column(String)
    """No Description Provided 
        Example: course2: Test conference 3 [170]_0"""
    updated_at = Column(DateTime)
    """No Description Provided 
        Example: 2013-12-12T16:09:33.903-07:00"""
    created_at = Column(DateTime)
    """No Description Provided 
        Example: 2013-12-12T16:09:09.960-07:00"""
    playback_url = Column(String)
    """No Description Provided 
        Example: http://example.com/recording_url"""
class ContentExport(Base):
    __tablename__ = 'content_export'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the export 
        Example: 101"""
    created_at = Column(DateTime)
    """the date and time this export was requested 
        Example: 2014-01-01T00:00:00Z"""
    ContentExportAllowedValues = enum.Enum('ContentExportAllowedValues', ['common_cartridge', 'qti'])
    """Enum for the allowed values of the export_type field"""
    export_type = Column(Enum(ContentExportAllowedValues))
    """the type of content migration: 'common_cartridge' or 'qti' 
        Example: common_cartridge"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    ContentExportAllowedValues = enum.Enum('ContentExportAllowedValues', ['created', 'exporting', 'exported', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(ContentExportAllowedValues))
    """Current state of the content migration: created exporting exported failed 
        Example: exported"""
    user_id = Column(Integer)
    """The ID of the user who started the export 
        Example: 4"""
    attachment = relationship('File')
    """attachment api object for the export package (not present before the export completes or after it becomes unavailable for download.) 
        Example: {'url': 'https://example.com/api/v1/attachments/789?download_frd=1&verifier=bG9sY2F0cyEh'}"""
class ContentMigration(Base):
    __tablename__ = 'content_migration'
    id = Column(Integer, primary_key=True)
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
    ContentMigrationAllowedValues = enum.Enum('ContentMigrationAllowedValues', ['pre_processing', 'pre_processed', 'running', 'waiting_for_select', 'completed', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(ContentMigrationAllowedValues))
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
    user_id = Column(Integer)
    """The user who started the migration 
        Example: 4"""
class MigrationIssue(Base):
    __tablename__ = 'migration_issue'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the issue 
        Example: 370663"""
    content_migration_url = Column(String)
    """API url to the content migration 
        Example: https://example.com/api/v1/courses/1/content_migrations/1"""
    description = Column(String)
    """Description of the issue for the end-user 
        Example: Questions in this quiz couldn't be converted"""
    MigrationIssueAllowedValues = enum.Enum('MigrationIssueAllowedValues', ['active', 'resolved'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(MigrationIssueAllowedValues))
    """Current state of the issue: active, resolved 
        Example: active"""
    fix_issue_html_url = Column(String)
    """HTML Url to the Canvas page to investigate the issue 
        Example: https://example.com/courses/1/quizzes/2"""
    MigrationIssueAllowedValues = enum.Enum('MigrationIssueAllowedValues', ['todo', 'warning', 'error'])
    """Enum for the allowed values of the issue_type field"""
    issue_type = Column(Enum(MigrationIssueAllowedValues))
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
class Migrator(Base):
    __tablename__ = 'migrator'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Migrator 
        Example: 123456"""
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
class ContentShare(Base):
    """Content shared between users"""
    __tablename__ = 'content_share'
    id = Column(Integer, primary_key=True)
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
    receivers = Column(JsonObject)
"""List[Unknown]"""
    """An Array of users the content is shared with.  This field is provided only to senders; an empty array will be returned for the receiving users. 
        Example: [{'id': 1, 'display_name': 'Jon Snow', 'avatar_image_url': 'http://localhost:3000/image_url2', 'html_url': 'http://localhost:3000/users/2'}]"""
    read_state = Column(String)
    """Whether the recipient has viewed the content share. 
        Example: read"""
    user_id = Column(Integer)
    """The id of the user who sent or received the content share. 
        Example: 1578941"""
    source_course = relationship('Unknown')
    """The course the content was originally shared from. 
        Example: {'id': 787, 'name': 'History 105'}"""
    sender = relationship('Unknown')
    """The user who shared the content. This field is provided only to receivers; it is not populated in the sender's list of sent content shares. 
        Example: {'id': 1, 'display_name': 'Matilda Vargas', 'avatar_image_url': 'http://localhost:3000/image_url', 'html_url': 'http://localhost:3000/users/1'}"""
    content_export = relationship('ContentExport')
    """The content export record associated with this content share 
        Example: {'id': 42}"""
class Conversation(Base):
    __tablename__ = 'conversation'
    id = Column(Integer, primary_key=True)
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
        Example: """
    audience = Column(JsonObject)
"""List[int]"""
    """Array of user ids who are involved in the conversation, ordered by participation level, then alphabetical. Excludes current user, unless this is a monologue. 
        Example: """
    audience_contexts = Column(JsonObject)
"""List[str]"""
    """Most relevant shared contexts (courses and groups) between current user and other participants. If there is only one participant, it will also include that user's enrollment(s)/ membership type(s) in each course/group. 
        Example: """
    avatar_url = Column(String)
    """URL to appropriate icon for this conversation (custom, individual or group avatar, depending on audience). 
        Example: https://canvas.instructure.com/images/messages/avatar-group-50.png"""
    participants = Column(JsonObject)
"""List[ConversationParticipant]"""
    """Array of users participating in the conversation. Includes current user. 
        Example: """
    visible = Column(Boolean)
    """indicates whether the conversation is visible under the current scope and filter. This attribute is always true in the index API response, and is primarily useful in create/update responses so that you can know if the record should be displayed in the UI. The default scope is assumed, unless a scope or filter is passed to the create/update API call. 
        Example: True"""
    context_name = Column(String)
    """Name of the course or group in which the conversation is occurring. 
        Example: Canvas 101"""
class ConversationParticipant(Base):
    __tablename__ = 'conversation_participant'
    id = Column(Integer, primary_key=True)
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
class CourseEvent(Base):
    __tablename__ = 'course_event'
    id = Column(String, primary_key=True)
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
class CourseEventLink(Base):
    __tablename__ = 'course_event_link'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CourseEventLink 
        Example: 123456"""
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
class CreatedEventData(Base):
    """The created event data object returns all the fields that were set in the format of the following example.  If a field does not exist it was not set. The value of each field changed is in the format of [:old_value, :new_value].  The created event type also includes a created_source field to specify what triggered the creation of the course."""
    __tablename__ = 'created_event_data'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CreatedEventData 
        Example: 123456"""
    name = Column(JsonObject)
"""List[str]"""
    """No Description Provided 
        Example: [None, 'Course 1']"""
    start_at = Column(JsonObject)
"""List[datetime]"""
    """No Description Provided 
        Example: [None, '2012-01-19T15:00:00-06:00']"""
    conclude_at = Column(JsonObject)
"""List[datetime]"""
    """No Description Provided 
        Example: [None, '2012-01-19T15:00:00-08:00']"""
    is_public = Column(JsonObject)
"""List[bool]"""
    """No Description Provided 
        Example: [None, False]"""
    created_source = Column(String)
    """The type of action that triggered the creation of the course. 
        Example: manual|sis|api"""
class UpdatedEventData(Base):
    """The updated event data object returns all the fields that have changed in the format of the following example.  If a field does not exist it was not changed.  The value is an array that contains the before and after values for the change as in [:old_value, :new_value]."""
    __tablename__ = 'updated_event_data'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the UpdatedEventData 
        Example: 123456"""
    name = Column(JsonObject)
"""List[str]"""
    """No Description Provided 
        Example: ['Course 1', 'Course 2']"""
    start_at = Column(JsonObject)
"""List[datetime]"""
    """No Description Provided 
        Example: ['2012-01-19T15:00:00-06:00', '2012-07-19T15:00:00-06:00']"""
    conclude_at = Column(JsonObject)
"""List[datetime]"""
    """No Description Provided 
        Example: ['2012-01-19T15:00:00-08:00', '2012-07-19T15:00:00-08:00']"""
    is_public = Column(JsonObject)
"""List[bool]"""
    """No Description Provided 
        Example: [True, False]"""
class CourseQuizExtension(Base):
    __tablename__ = 'course_quiz_extension'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CourseQuizExtension 
        Example: 123456"""
    extra_attempts = Column(Integer)
    """Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. 
        Example: 1"""
    extra_time = Column(Integer)
    """Amount of extra time allowed for the quiz submission, in minutes. 
        Example: 60"""
    manually_unlocked = Column(Boolean)
    """The student can take the quiz even if it's locked for everyone else 
        Example: True"""
    end_at = Column(String)
    """The time at which the quiz submission will be overdue, and be flagged as a late submission. 
        Example: 2013-11-07T13:16:18Z"""
    user_id = Column(Integer)
    """The ID of the Student that needs the quiz extension. 
        Example: 3"""
class CalendarLink(Base):
    __tablename__ = 'calendar_link'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CalendarLink 
        Example: 123456"""
    ics = Column(String)
    """The URL of the calendar in ICS format 
        Example: https://canvas.instructure.com/feeds/calendars/course_abcdef.ics"""
class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the course 
        Example: 370663"""
    uuid = Column(String)
    """the UUID of the course 
        Example: WvAHhY5FINzq5IyRIJybGeiXyFkG3SqHUPb7jZY5"""
    sis_import_id = Column(Integer)
    """the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: 34"""
    name = Column(String)
    """the full name of the course. If the requesting user has set a nickname for the course, the nickname will be shown here. 
        Example: InstructureCon 2012"""
    course_code = Column(String)
    """the course code 
        Example: INSTCON12"""
    original_name = Column(String)
    """the actual course name. This field is returned only if the requesting user has set a nickname for the course. 
        Example: InstructureCon-2012-01"""
    CourseAllowedValues = enum.Enum('CourseAllowedValues', ['unpublished', 'available', 'completed', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(CourseAllowedValues))
    """the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted' 
        Example: available"""
    root_account_id = Column(Integer)
    """the root account associated with the course 
        Example: 81259"""
    grading_periods = Column(JsonObject)
"""List[GradingPeriod]"""
    """A list of grading periods associated with the course 
        Example: """
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
        Example: """
    total_students = Column(Integer)
    """optional: the total number of active and invited students in the course 
        Example: 32"""
    CourseAllowedValues = enum.Enum('CourseAllowedValues', ['feed', 'wiki', 'modules', 'syllabus', 'assignments'])
    """Enum for the allowed values of the default_view field"""
    default_view = Column(Enum(CourseAllowedValues))
    """the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future 
        Example: feed"""
    syllabus_body = Column(String)
    """optional: user-generated HTML for the course syllabus 
        Example: <p>syllabus html goes here</p>"""
    needs_grading_count = Column(Integer)
    """optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count 
        Example: 17"""
    course_progress = relationship('CourseProgress')
    """optional: information on progress through the course returned only if include[]=course_progress 
        Example: """
    apply_assignment_group_weights = Column(Boolean)
    """weight final grade based on assignment group percentages 
        Example: True"""
    permissions = Column(JsonObject)
"""Dict[str, bool]"""
    """optional: the permissions the user has for the course. returned only for a single course and include[]=permissions 
        Example: {'create_discussion_topic': True, 'create_announcement': True}"""
    is_public = Column(Boolean)
    """No Description Provided 
        Example: True"""
    is_public_to_auth_users = Column(Boolean)
    """No Description Provided 
        Example: True"""
    public_syllabus = Column(Boolean)
    """No Description Provided 
        Example: True"""
    public_syllabus_to_auth = Column(Boolean)
    """No Description Provided 
        Example: True"""
    public_description = Column(String)
    """optional: the public description of the course 
        Example: Come one, come all to InstructureCon 2012!"""
    storage_quota_mb = Column(Integer)
    """No Description Provided 
        Example: 5"""
    storage_quota_used_mb = Column(Integer)
    """No Description Provided 
        Example: 5"""
    hide_final_grades = Column(Boolean)
    """No Description Provided 
        Example: False"""
    license = Column(String)
    """No Description Provided 
        Example: Creative Commons"""
    allow_student_assignment_edits = Column(Boolean)
    """No Description Provided 
        Example: False"""
    allow_wiki_comments = Column(Boolean)
    """No Description Provided 
        Example: False"""
    allow_student_forum_attachments = Column(Boolean)
    """No Description Provided 
        Example: False"""
    open_enrollment = Column(Boolean)
    """No Description Provided 
        Example: True"""
    self_enrollment = Column(Boolean)
    """No Description Provided 
        Example: False"""
    restrict_enrollments_to_course_dates = Column(Boolean)
    """No Description Provided 
        Example: False"""
    course_format = Column(String)
    """No Description Provided 
        Example: online"""
    access_restricted_by_date = Column(Boolean)
    """optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings 
        Example: False"""
    time_zone = Column(String)
    """The course's IANA time zone name. 
        Example: America/Denver"""
    blueprint = Column(Boolean)
    """optional: whether the course is set as a Blueprint Course (blueprint fields require the Blueprint Courses feature) 
        Example: True"""
    blueprint_restrictions_by_object_type = relationship('Unknown')
    """optional: Sets of restrictions differentiated by object type applied to locked course objects 
        Example: {'assignment': {'content': True, 'points': True}, 'wiki_page': {'content': True}}"""
    template = Column(Boolean)
    """optional: whether the course is set as a template (requires the Course Templates feature) 
        Example: True"""
    integration_id = Column(String)
    """the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information. 
        Example: """
    enrollment_term_id = Column(Integer)
    """the enrollment term associated with the course 
        Example: 34"""
    sis_course_id = Column(String)
    """the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information. 
        Example: """
    grading_standard_id = Column(Integer)
    """the grading standard associated with the course 
        Example: 25"""
    account_id = Column(Integer)
    """the account associated with the course 
        Example: 81259"""
    term = relationship('Term')
    """optional: the enrollment term object for the course returned only if include[]=term 
        Example: """
    calendar = relationship('CalendarLink')
    """course calendar 
        Example: """
    blueprint_restrictions = relationship('Unknown')
    """optional: Set of restrictions applied to all locked course objects 
        Example: {'content': True, 'points': True, 'due_dates': False, 'availability_dates': False}"""
class CourseProgress(Base):
    __tablename__ = 'course_progress'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CourseProgress 
        Example: 123456"""
    requirement_count = Column(Integer)
    """total number of requirements from all modules 
        Example: 10"""
    requirement_completed_count = Column(Integer)
    """total number of requirements the user has completed from all modules 
        Example: 1"""
    next_requirement_url = Column(String)
    """url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress 
        Example: http://localhost/courses/1/modules/items/2"""
    completed_at = Column(DateTime)
    """date the course was completed. null if the course has not been completed by this user 
        Example: 2013-06-01T00:00:00-06:00"""
class Term(Base):
    __tablename__ = 'term'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 1"""
    name = Column(String)
    """No Description Provided 
        Example: Default Term"""
    start_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-06-01T00:00:00-06:00"""
    end_at = Column(DateTime)
    """No Description Provided 
        Example: """
class ColumnDatum(Base):
    """ColumnDatum objects contain the entry for a column for each user."""
    __tablename__ = 'column_datum'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ColumnDatum 
        Example: 123456"""
    content = Column(String)
    """No Description Provided 
        Example: Nut allergy"""
    user_id = Column(Integer)
    """No Description Provided 
        Example: 2"""
class CustomColumn(Base):
    __tablename__ = 'custom_column'
    id = Column(Integer, primary_key=True)
    """The ID of the custom gradebook column 
        Example: 2"""
    teacher_notes = Column(Boolean)
    """When true, this column's visibility will be toggled in the Gradebook when a user selects to show or hide notes 
        Example: False"""
    title = Column(String)
    """header text 
        Example: Stuff"""
    position = Column(Integer)
    """column order 
        Example: 1"""
    hidden = Column(Boolean)
    """won't be displayed if hidden is true 
        Example: False"""
    read_only = Column(Boolean)
    """won't be editable in the gradebook UI 
        Example: True"""
class DiscussionTopic(Base):
    """A discussion topic"""
    __tablename__ = 'discussion_topic'
    id = Column(Integer, primary_key=True)
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
        Example: False"""
    user_can_see_posts = Column(Boolean)
    """Whether or not posts in this topic are visible to the user. 
        Example: True"""
    discussion_subentry_count = Column(Integer)
    """The count of entries in the topic. 
        Example: 0"""
    DiscussionTopicAllowedValues = enum.Enum('DiscussionTopicAllowedValues', ['read', 'unread'])
    """Enum for the allowed values of the read_state field"""
    read_state = Column(Enum(DiscussionTopicAllowedValues))
    """The read_state of the topic for the current user, 'read' or 'unread'. 
        Example: read"""
    unread_count = Column(Integer)
    """The count of unread entries of this topic for the current user. 
        Example: 0"""
    subscribed = Column(Boolean)
    """Whether or not the current user is subscribed to this topic. 
        Example: True"""
    DiscussionTopicAllowedValues = enum.Enum('DiscussionTopicAllowedValues', ['initial_post_required', 'not_in_group_set', 'not_in_group', 'topic_is_announcement'])
    """Enum for the allowed values of the subscription_hold field"""
    subscription_hold = Column(Enum(DiscussionTopicAllowedValues))
    """(Optional) Why the user cannot subscribe to this topic. Only one reason will be returned even if multiple apply. Can be one of: 'initial_post_required': The user must post a reply first; 'not_in_group_set': The user is not in the group set for this graded group discussion; 'not_in_group': The user is not in this topic's group; 'topic_is_announcement': This topic is an announcement 
        Example: not_in_group_set"""
    delayed_post_at = Column(DateTime)
    """The datetime to publish the topic (if not right away). 
        Example: """
    published = Column(Boolean)
    """Whether this discussion topic is published (true) or draft state (false) 
        Example: True"""
    lock_at = Column(DateTime)
    """The datetime to lock the topic (if ever). 
        Example: """
    locked = Column(Boolean)
    """Whether or not the discussion is 'closed for comments'. 
        Example: False"""
    pinned = Column(Boolean)
    """Whether or not the discussion has been 'pinned' by an instructor 
        Example: False"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: True"""
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
    podcast_url = Column(String)
    """If the topic is a podcast topic this is the feed url for the current user. 
        Example: /feeds/topics/1/enrollment_1XAcepje4u228rt4mi7Z1oFbRpn3RAkTzuXIGOPe.rss"""
    DiscussionTopicAllowedValues = enum.Enum('DiscussionTopicAllowedValues', ['side_comment', 'threaded'])
    """Enum for the allowed values of the discussion_type field"""
    discussion_type = Column(Enum(DiscussionTopicAllowedValues))
    """The type of discussion. Values are 'side_comment', for discussions that only allow one level of nested comments, and 'threaded' for fully threaded discussions. 
        Example: side_comment"""
    attachments = Column(JsonObject)
"""List[FileAttachment]"""
    """Array of file attachments. 
        Example: """
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
    root_topic_id = Column(Integer)
    """If the topic is for grading and a group assignment this will point to the original topic in the course. 
        Example: """
    assignment_id = Column(Integer)
    """The unique identifier of the assignment if the topic is for grading, otherwise null. 
        Example: """
    group_category_id = Column(Integer)
    """The unique identifier of the group category if the topic is a group discussion, otherwise null. 
        Example: """
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: """
class FileAttachment(Base):
    """A file attachment"""
    __tablename__ = 'file_attachment'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the FileAttachment 
        Example: 123456"""
    content-type = Column(String)
    """No Description Provided 
        Example: unknown/unknown"""
    url = Column(String)
    """No Description Provided 
        Example: http://www.example.com/courses/1/files/1/download"""
    filename = Column(String)
    """No Description Provided 
        Example: content.txt"""
    display_name = Column(String)
    """No Description Provided 
        Example: content.txt"""
class ePortfolio(Base):
    __tablename__ = 'e_portfolio'
    id = Column(Integer, primary_key=True)
    """The database ID of the ePortfolio 
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
    """A flag indicating whether the ePortfolio has been
      flagged or moderated as spam. One of 'flagged_as_possible_spam',
      'marked_as_safe', 'marked_as_spam', or null 
        Example: """
    user_id = Column(Integer)
    """The user ID to which the ePortfolio belongs 
        Example: 1"""
class ePortfolioPage(Base):
    __tablename__ = 'e_portfolio_page'
    id = Column(Integer, primary_key=True)
    """The database ID of the ePortfolio 
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
    eportfolio_id = Column(Integer)
    """The ePortfolio ID to which the entry belongs 
        Example: 1"""
class CourseEpubExport(Base):
    """Combination of a Course & EpubExport."""
    __tablename__ = 'course_epub_export'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the course 
        Example: 101"""
    name = Column(String)
    """the name for the course 
        Example: Maths 101"""
    epub_export = relationship('EpubExport')
    """ePub export API object 
        Example: """
class EpubExport(Base):
    __tablename__ = 'epub_export'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the export 
        Example: 101"""
    created_at = Column(DateTime)
    """the date and time this export was requested 
        Example: 2014-01-01T00:00:00Z"""
    progress_url = Column(String)
    """The api endpoint for polling the current progress 
        Example: https://example.com/api/v1/progress/4"""
    EpubExportAllowedValues = enum.Enum('EpubExportAllowedValues', ['created', 'exporting', 'exported', 'generating', 'generated', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(EpubExportAllowedValues))
    """Current state of the ePub export: created exporting exported generating generated failed 
        Example: exported"""
    user_id = Column(Integer)
    """The ID of the user who started the export 
        Example: 4"""
    attachment = relationship('File')
    """attachment api object for the export ePub (not present until the export completes) 
        Example: {'url': 'https://example.com/api/v1/attachments/789?download_frd=1&verifier=bG9sY2F0cyEh'}"""
class EnrollmentTerm(Base):
    __tablename__ = 'enrollment_term'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the enrollment term. 
        Example: 1"""
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
    course_count = Column(Integer)
    """The number of courses in the term (available via include) 
        Example: 80"""
    sis_term_id = Column(String)
    """The SIS id of the term. Only included if the user has permission to view SIS information. 
        Example: Sp2014"""
    overrides = relationship('Unknown')
    """Term date overrides for specific enrollment types 
        Example: {'StudentEnrollment': {'start_at': '2014-01-07T08:00:00-05:00', 'end_at': '2014-05-14T05:00:00-04:0'}}"""
class EnrollmentTermsList(Base):
    __tablename__ = 'enrollment_terms_list'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the EnrollmentTermsList 
        Example: 123456"""
    enrollment_terms = Column(JsonObject)
"""List[EnrollmentTerm]"""
    """a paginated list of all terms in the account 
        Example: []"""
class Enrollment(Base):
    __tablename__ = 'enrollment'
    id = Column(Integer, primary_key=True)
    """The ID of the enrollment. 
        Example: 1"""
    sis_course_id = Column(String)
    """The SIS Course ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    course_section_id = Column(Integer)
    """The unique id of the user's section. 
        Example: 1"""
    sis_account_id = Column(String)
    """The SIS Account ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
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
    root_account_id = Column(Integer)
    """The unique id of the user's account. 
        Example: 1"""
    type = Column(String)
    """The enrollment type. One of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'DesignerEnrollment', 'ObserverEnrollment'. 
        Example: StudentEnrollment"""
    associated_user_id = Column(Integer)
    """The unique id of the associated user. Will be null unless type is ObserverEnrollment. 
        Example: """
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
    override_grade = Column(String)
    """The user's override grade for the course. 
        Example: A"""
    override_score = Column(Integer)
    """The user's override score for the course. 
        Example: 99.99"""
    unposted_current_grade = Column(String)
    """The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. 
        Example: """
    unposted_final_grade = Column(String)
    """The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. 
        Example: """
    unposted_current_score = Column(String)
    """The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: """
    unposted_final_score = Column(String)
    """The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: """
    has_grading_periods = Column(Boolean)
    """optional: Indicates whether the course the enrollment belongs to has grading periods set up. (applies only to student enrollments, and only available in course endpoints) 
        Example: True"""
    totals_for_all_grading_periods_option = Column(Boolean)
    """optional: Indicates whether the course the enrollment belongs to has the Display Totals for 'All Grading Periods' feature enabled. (applies only to student enrollments, and only available in course endpoints) 
        Example: True"""
    current_grading_period_title = Column(String)
    """optional: The name of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: Fall Grading Period"""
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
    course_integration_id = Column(String)
    """The Course Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    sis_section_id = Column(String)
    """The SIS Section ID in which the enrollment is associated. Only displayed if present. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    user_id = Column(Integer)
    """The unique id of the user. 
        Example: 1"""
    current_grading_period_id = Column(Integer)
    """optional: The id of the currently active grading period, if one exists. If the course the enrollment belongs to does not have grading periods, or if no currently active grading period exists, the value will be null. (applies only to student enrollments, and only available in course endpoints) 
        Example: 5"""
    section_integration_id = Column(String)
    """The Section Integration ID in which the enrollment is associated. This field is only included if the user has permission to view SIS information. 
        Example: SHEL93921"""
    role_id = Column(Integer)
    """The id of the enrollment role. 
        Example: 1"""
    role = Column(String)
    """The enrollment role, for course-level permissions. This field will match `type` if the enrollment role has not been customized. 
        Example: StudentEnrollment"""
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: 83"""
    course_id = Column(Integer)
    """The unique id of the course. 
        Example: 1"""
    user = relationship('User')
    """A description of the user. 
        Example: {'id': 3, 'name': 'Student 1', 'sortable_name': '1, Student', 'short_name': 'Stud 1'}"""
    grades = relationship('Grade')
    """The URL to the Canvas web UI page containing the grades associated with this enrollment. 
        Example: {'html_url': 'https://...', 'current_score': 35, 'current_grade': None, 'final_score': 6.67, 'final_grade': None}"""
class Grade(Base):
    __tablename__ = 'grade'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Grade 
        Example: 123456"""
    html_url = Column(String)
    """The URL to the Canvas web UI page for the user's grades, if this is a student enrollment. 
        Example: """
    current_grade = Column(String)
    """The user's current grade in the class. Only included if user has permissions to view this grade. 
        Example: """
    final_grade = Column(String)
    """The user's final grade for the class. Only included if user has permissions to view this grade. 
        Example: """
    current_score = Column(String)
    """The user's current score in the class. Only included if user has permissions to view this score. 
        Example: """
    final_score = Column(String)
    """The user's final score for the class. Only included if user has permissions to view this score. 
        Example: """
    current_points = Column(Integer)
    """The total points the user has earned in the class. Only included if user has permissions to view this score and 'current_points' is passed in the request's 'include' parameter. 
        Example: 150"""
    unposted_current_grade = Column(String)
    """The user's current grade in the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins. 
        Example: """
    unposted_final_grade = Column(String)
    """The user's final grade for the class including muted/unposted assignments. Only included if user has permissions to view this grade, typically teachers, TAs, and admins.. 
        Example: """
    unposted_current_score = Column(String)
    """The user's current score in the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: """
    unposted_final_score = Column(String)
    """The user's final score for the class including muted/unposted assignments. Only included if user has permissions to view this score, typically teachers, TAs, and admins.. 
        Example: """
    unposted_current_points = Column(Integer)
    """The total points the user has earned in the class, including muted/unposted assignments. Only included if user has permissions to view this score (typically teachers, TAs, and admins) and 'current_points' is passed in the request's 'include' parameter. 
        Example: 150"""
class ErrorReport(Base):
    """A collection of information around a specific notification of a problem"""
    __tablename__ = 'error_report'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ErrorReport 
        Example: 123456"""
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
class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Favorite 
        Example: 123456"""
    FavoriteAllowedValues = enum.Enum('FavoriteAllowedValues', ['Course'])
    """Enum for the allowed values of the context_type field"""
    context_type = Column(Enum(FavoriteAllowedValues))
    """The type of the object the Favorite refers to (currently, only 'Course' is supported) 
        Example: Course"""
    context_id = Column(Integer)
    """The ID of the object the Favorite refers to 
        Example: 1170"""
class Feature(Base):
    __tablename__ = 'feature'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Feature 
        Example: 123456"""
    feature = Column(String)
    """The symbolic name of the feature, used in FeatureFlags 
        Example: fancy_wickets"""
    display_name = Column(String)
    """The user-visible name of the feature 
        Example: Fancy Wickets"""
    FeatureAllowedValues = enum.Enum('FeatureAllowedValues', ['Course', 'RootAccount', 'Account', 'User'])
    """Enum for the allowed values of the applies_to field"""
    applies_to = Column(Enum(FeatureAllowedValues))
    """The type of object the feature applies to (RootAccount, Account, Course, or User):
 * RootAccount features may only be controlled by flags on root accounts.
 * Account features may be controlled by flags on accounts and their parent accounts.
 * Course features may be controlled by flags on courses and their parent accounts.
 * User features may be controlled by flags on users and site admin only. 
        Example: Course"""
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
    feature_flag = relationship('FeatureFlag')
    """The FeatureFlag that applies to the caller 
        Example: {'feature': 'fancy_wickets', 'state': 'allowed'}"""
class FeatureFlag(Base):
    __tablename__ = 'feature_flag'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the FeatureFlag 
        Example: 123456"""
    FeatureFlagAllowedValues = enum.Enum('FeatureFlagAllowedValues', ['Course', 'Account', 'User'])
    """Enum for the allowed values of the context_type field"""
    context_type = Column(Enum(FeatureFlagAllowedValues))
    """The type of object to which this flag applies (Account, Course, or User). (This field is not present if this FeatureFlag represents the global Canvas default) 
        Example: Account"""
    feature = Column(String)
    """The feature this flag controls 
        Example: fancy_wickets"""
    FeatureFlagAllowedValues = enum.Enum('FeatureFlagAllowedValues', ['off', 'allowed', 'allowed_on', 'on'])
    """Enum for the allowed values of the state field"""
    state = Column(Enum(FeatureFlagAllowedValues))
    """The policy for the feature at this context.  can be 'off', 'allowed', 'allowed_on', or 'on'. 
        Example: allowed"""
    locked = Column(Boolean)
    """If set, this feature flag cannot be changed in the caller's context because the flag is set 'off' or 'on' in a higher context 
        Example: False"""
    context_id = Column(Integer)
    """The id of the object to which this flag applies (This field is not present if this FeatureFlag represents the global Canvas default) 
        Example: 1038"""
class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 569"""
    uuid = Column(String)
    """No Description Provided 
        Example: SUj23659sdfASF35h265kf352YTdnC4"""
    display_name = Column(String)
    """No Description Provided 
        Example: file.txt"""
    filename = Column(String)
    """No Description Provided 
        Example: file.txt"""
    content-type = Column(String)
    """No Description Provided 
        Example: text/plain"""
    url = Column(String)
    """No Description Provided 
        Example: http://www.example.com/files/569/download?download_frd=1&verifier=c6HdZmxOZa0Fiin2cbvZeI8I5ry7yqD7RChQzb6P"""
    size = Column(Integer)
    """file size in bytes 
        Example: 43451"""
    created_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    updated_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    unlock_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-07T14:58:50Z"""
    locked = Column(Boolean)
    """No Description Provided 
        Example: False"""
    hidden = Column(Boolean)
    """No Description Provided 
        Example: False"""
    lock_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-20T14:58:50Z"""
    hidden_for_user = Column(Boolean)
    """No Description Provided 
        Example: False"""
    thumbnail_url = Column(String)
    """No Description Provided 
        Example: """
    modified_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    mime_class = Column(String)
    """simplified content-type mapping 
        Example: html"""
    locked_for_user = Column(Boolean)
    """No Description Provided 
        Example: False"""
    lock_explanation = Column(String)
    """No Description Provided 
        Example: This assignment is locked until September 1 at 12:00am"""
    preview_url = Column(String)
    """optional: url to the document preview. This url is specific to the user making the api call. Only included in submission endpoints. 
        Example: """
    media_entry_id = Column(String)
    """identifier for file in third-party transcoding service 
        Example: m-3z31gfpPf129dD3sSDF85SwSDFnwe"""
    folder_id = Column(Integer)
    """No Description Provided 
        Example: 4207"""
    lock_info = relationship('LockInfo')
    """No Description Provided 
        Example: """
class Folder(Base):
    __tablename__ = 'folder'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 2937"""
    context_type = Column(String)
    """No Description Provided 
        Example: Course"""
    files_count = Column(Integer)
    """No Description Provided 
        Example: 0"""
    position = Column(Integer)
    """No Description Provided 
        Example: 3"""
    updated_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    folders_url = Column(String)
    """No Description Provided 
        Example: https://www.example.com/api/v1/folders/2937/folders"""
    files_url = Column(String)
    """No Description Provided 
        Example: https://www.example.com/api/v1/folders/2937/files"""
    full_name = Column(String)
    """No Description Provided 
        Example: course files/11folder"""
    lock_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    folders_count = Column(Integer)
    """No Description Provided 
        Example: 0"""
    name = Column(String)
    """No Description Provided 
        Example: 11folder"""
    created_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    unlock_at = Column(DateTime)
    """No Description Provided 
        Example: """
    hidden = Column(Boolean)
    """No Description Provided 
        Example: False"""
    hidden_for_user = Column(Boolean)
    """No Description Provided 
        Example: False"""
    locked = Column(Boolean)
    """No Description Provided 
        Example: True"""
    locked_for_user = Column(Boolean)
    """No Description Provided 
        Example: False"""
    for_submissions = Column(Boolean)
    """If true, indicates this is a read-only folder containing files submitted to assignments 
        Example: False"""
    parent_folder_id = Column(Integer)
    """No Description Provided 
        Example: 2934"""
    context_id = Column(Integer)
    """No Description Provided 
        Example: 1401"""
class License(Base):
    __tablename__ = 'license'
    id = Column(String, primary_key=True)
    """a short string identifying the license 
        Example: cc_by_sa"""
    name = Column(String)
    """the name of the license 
        Example: CC Attribution ShareAlike"""
    url = Column(String)
    """a link to the license text 
        Example: http://creativecommons.org/licenses/by-sa/4.0"""
class UsageRights(Base):
    """Describes the copyright and license information for a File"""
    __tablename__ = 'usage_rights'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the UsageRights 
        Example: 123456"""
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
class GradeChangeEvent(Base):
    __tablename__ = 'grade_change_event'
    id = Column(String, primary_key=True)
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
        Example: False"""
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
    """No Description Provided 
        Example: """
class GradeChangeEventLinks(Base):
    __tablename__ = 'grade_change_event_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the GradeChangeEventLinks 
        Example: 123456"""
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
class Day(Base):
    __tablename__ = 'day'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Day 
        Example: 123456"""
    date = Column(DateTime)
    """the date represented by this entry 
        Example: 1986-08-09"""
    graders = Column(Integer)
    """an array of the graders who were responsible for the submissions in this response. the submissions are grouped according to the person who graded them and the assignment they were submitted for. 
        Example: []"""
class Grader(Base):
    __tablename__ = 'grader'
    id = Column(Integer, primary_key=True)
    """the user_id of the user who graded the contained submissions 
        Example: 27"""
    name = Column(String)
    """the name of the user who graded the contained submissions 
        Example: Some User"""
    assignments = Column(JsonObject)
"""List[int]"""
    """the assignment groups for all submissions in this response that were graded by this user.  The details are not nested inside here, but the fact that an assignment is present here means that the grader did grade submissions for this assignment on the contextual date. You can use the id of a grader and of an assignment to make another API call to find all submissions for a grader/assignment combination on a given date. 
        Example: [1, 2, 3]"""
class SubmissionHistory(Base):
    __tablename__ = 'submission_history'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SubmissionHistory 
        Example: 123456"""
    versions = Column(JsonObject)
"""List[SubmissionVersion]"""
    """an array of all the versions of this submission 
        Example: """
    submission_id = Column(Integer)
    """the id of the submission 
        Example: 4"""
class SubmissionVersion(Base):
    """A SubmissionVersion object contains all the fields that a Submission object does, plus additional fields prefixed with current_* new_* and previous_* described below."""
    __tablename__ = 'submission_version'
    id = Column(Integer, primary_key=True)
    """the id of the submission of which this is a version 
        Example: 11607"""
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
        Example: """
    workflow_state = Column(String)
    """the state of the submission at this version 
        Example: unsubmitted"""
    grader_id = Column(Integer)
    """the user id of the user who graded this version of the submission 
        Example: 67379"""
    grader = Column(String)
    """the name of the user who graded this version of the submission 
        Example: Grader Name"""
    assignment_id = Column(Integer)
    """the id of the assignment this submissions is for 
        Example: 22604"""
    user_id = Column(Integer)
    """the user ID of the student who created this submission 
        Example: 67376"""
class GradingPeriod(Base):
    __tablename__ = 'grading_period'
    id = Column(Integer, primary_key=True)
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
class GradingSchemeEntry(Base):
    __tablename__ = 'grading_scheme_entry'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the GradingSchemeEntry 
        Example: 123456"""
    name = Column(String)
    """The name for an entry value within a GradingStandard that describes the range of the value 
        Example: A"""
    value = Column(Integer)
    """The value for the name of the entry within a GradingStandard.  The entry represents the lower bound of the range for the entry. This range includes the value up to the next entry in the GradingStandard, or 100 if there is no upper bound. The lowest value will have a lower bound range of 0. 
        Example: 0.9"""
class GradingStandard(Base):
    __tablename__ = 'grading_standard'
    id = Column(Integer, primary_key=True)
    """the id of the grading standard 
        Example: 1"""
    title = Column(String)
    """the title of the grading standard 
        Example: Account Standard"""
    context_type = Column(String)
    """the context this standard is associated with, either 'Account' or 'Course' 
        Example: Account"""
    grading_scheme = Column(JsonObject)
"""List[GradingSchemeEntry]"""
    """A list of GradingSchemeEntry that make up the Grading Standard as an array of values with the scheme name and value 
        Example: [{'name': 'A', 'value': 0.9}, {'name': 'B', 'value': 0.8}, {'name': 'C', 'value': 0.7}, {'name': 'D', 'value': 0.6}]"""
    context_id = Column(Integer)
    """the id for the context either the Account or Course id 
        Example: 1"""
class GroupCategory(Base):
    __tablename__ = 'group_category'
    id = Column(Integer, primary_key=True)
    """The ID of the group category. 
        Example: 17"""
    name = Column(String)
    """The display name of the group category. 
        Example: Math Groups"""
    role = Column(String)
    """Certain types of group categories have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account group categories have a role of null. 
        Example: communities"""
    GroupCategoryAllowedValues = enum.Enum('GroupCategoryAllowedValues', ['restricted', 'enabled'])
    """Enum for the allowed values of the self_signup field"""
    self_signup = Column(Enum(GroupCategoryAllowedValues))
    """If the group category allows users to join a group themselves, thought they may only be a member of one group per group category at a time. Values include 'restricted', 'enabled', and null 'enabled' allows students to assign themselves to a group 'restricted' restricts them to only joining a group in their section null disallows students from joining groups 
        Example: """
    GroupCategoryAllowedValues = enum.Enum('GroupCategoryAllowedValues', ['first', 'random'])
    """Enum for the allowed values of the auto_leader field"""
    auto_leader = Column(Enum(GroupCategoryAllowedValues))
    """Gives instructors the ability to automatically have group leaders assigned.  Values include 'random', 'first', and null; 'random' picks a student from the group at random as the leader, 'first' sets the first student to be assigned to the group as the leader 
        Example: """
    context_type = Column(String)
    """The course or account that the category group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'Course', the course_id field would be replaced by an course_id field. 
        Example: Account"""
    group_limit = Column(Integer)
    """If self-signup is enabled, group_limit can be set to cap the number of users in each group. If null, there is no limit. 
        Example: """
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information. 
        Example: """
    sis_group_category_id = Column(String)
    """The SIS identifier for the group category. This field is only included if the user has permission to manage or view SIS information. 
        Example: """
    account_id = Column(Integer)
    """No Description Provided 
        Example: 3"""
    progress = relationship('Progress')
    """If the group category has not yet finished a randomly student assignment request, a progress object will be attached, which will contain information related to the progress of the assignment request. Refer to the Progress API for more information 
        Example: """
class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    """The ID of the group. 
        Example: 17"""
    name = Column(String)
    """The display name of the group. 
        Example: Math Group 1"""
    description = Column(String)
    """A description of the group. This is plain text. 
        Example: """
    is_public = Column(Boolean)
    """Whether or not the group is public.  Currently only community groups can be made public.  Also, once a group has been set to public, it cannot be changed back to private. 
        Example: False"""
    followed_by_user = Column(Boolean)
    """Whether or not the current user is following this group. 
        Example: False"""
    GroupAllowedValues = enum.Enum('GroupAllowedValues', ['parent_context_auto_join', 'parent_context_request', 'invitation_only'])
    """Enum for the allowed values of the join_level field"""
    join_level = Column(Enum(GroupAllowedValues))
    """How people are allowed to join the group.  For all groups except for community groups, the user must share the group's parent course or account.  For student organized or community groups, where a user can be a member of as many or few as they want, the applicable levels are 'parent_context_auto_join', 'parent_context_request', and 'invitation_only'.  For class groups, where students are divided up and should only be part of one group of the category, this value will always be 'invitation_only', and is not relevant. * If 'parent_context_auto_join', anyone can join and will be automatically accepted. * If 'parent_context_request', anyone  can request to join, which must be approved by a group moderator. * If 'invitation_only', only those how have received an invitation my join the group, by accepting that invitation. 
        Example: invitation_only"""
    members_count = Column(Integer)
    """The number of members currently in the group 
        Example: 0"""
    avatar_url = Column(String)
    """The url of the group's avatar 
        Example: https://<canvas>/files/avatar_image.png"""
    context_type = Column(String)
    """The course or account that the group belongs to. The pattern here is that whatever the context_type is, there will be an _id field named after that type. So if instead context_type was 'account', the course_id field would be replaced by an account_id field. 
        Example: Course"""
    GroupAllowedValues = enum.Enum('GroupAllowedValues', ['communities', 'student_organized', 'imported'])
    """Enum for the allowed values of the role field"""
    role = Column(Enum(GroupAllowedValues))
    """Certain types of groups have special role designations. Currently, these include: 'communities', 'student_organized', and 'imported'. Regular course/account groups have a role of null. 
        Example: """
    sis_group_id = Column(String)
    """The SIS ID of the group. Only included if the user has permission to view SIS information. 
        Example: group4a"""
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
        Example: """
    group_category_id = Column(Integer)
    """The ID of the group's category. 
        Example: 4"""
    course_id = Column(Integer)
    """No Description Provided 
        Example: 3"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 14"""
class GroupMembership(Base):
    __tablename__ = 'group_membership'
    id = Column(Integer, primary_key=True)
    """The id of the membership object 
        Example: 92"""
    user_id = Column(Integer)
    """The id of the user object to which the membership belongs 
        Example: 3"""
    GroupMembershipAllowedValues = enum.Enum('GroupMembershipAllowedValues', ['accepted', 'invited', 'requested'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(GroupMembershipAllowedValues))
    """The current state of the membership. Current possible values are 'accepted', 'invited', and 'requested' 
        Example: accepted"""
    moderator = Column(Boolean)
    """Whether or not the user is a moderator of the group (the must also be an active member of the group to moderate) 
        Example: True"""
    just_created = Column(Boolean)
    """optional: whether or not the record was just created on a create call (POST), i.e. was the user just added to the group, or was the user already a member 
        Example: True"""
    group_id = Column(Integer)
    """The id of the group object to which the membership belongs 
        Example: 17"""
    sis_import_id = Column(Integer)
    """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information. 
        Example: 4"""
class HistoryEntry(Base):
    """Information about a recently visited item or page in Canvas"""
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the HistoryEntry 
        Example: 123456"""
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
    context_id = Column(Integer)
    """The id of the context, if applicable 
        Example: 123"""
class InstAccessToken(Base):
    __tablename__ = 'inst_access_token'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the InstAccessToken 
        Example: 123456"""
    token = Column(String)
    """The InstAccess token itself -- a signed, encrypted JWT 
        Example: eyJhbGciOiJSU0ExXzUiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0.EstatUwzltksvZn4wbjHYiwleM986vzryrv4R9jqvYDGEY4rt6KPG4Q6lJ3oI0piYbH7h17i8vIWv35cqrgRbb7fzmGQ0Ptj74OEjx-1gGBMZCbZTE4W206XxPHRm9TS4qOAvIq0hsvJroE4xZsVWJFiUIKl_Wd2udbvqwF8bvnMKPAx_ooa-9mWaG1N9kd4EWC3Oxu9wi7j8ZG_TbkLSXAg1KxLaO2zXBcU5_HWrKFRxOjHmWpaOMKWkjUInt-DA6fLRszBZp9BFGoop8S9KDs6f1JebLgyM5gGrP-Gz7kSEAPO9eVXtjpd6N29wMClNI0X-Ppp_40Fp4Z3vocTKQ.c_tcevWI68RuZ0s04fDSEQ.wV8KIPHGfYwxm19MWt3K7VVGm4qqZJruPwAZ8rdUANTzJoqwafqOnYZLCyky8lV7J-m64SMVUmR-BOha_CmJEKVVw7T5x70MTP6-nv4RMVPpcViHsNgE2f1GE9HUauVePw7CrnV0PyVaNq2EZasDgdHdye4iG_-hXXQZRnGYzxl8UceTLBVkpEYHlXKdD7DyQ0IT2BYOcZSpXyW7kEIvAHpNaNbvTPCR2t0SeGbuNf8PpYVjohKDpXhNgQ-Pyl9pxs05TrdjTq1fIctzTLqIN58nfqzoqQld6rSkjcAZZXgr8bOsg8EDFMov5gTv2_Uf-YOm52yD1SbL0lJ-VdpKgXu7XtQ4UmEOj40W4uXF-KmLTjEwQmdbmtKrruhakIeth7EZa3w0Xg6RRyHLqKUheAdTgxAIer8MST8tamZlqW1b9wjMw371zSSjeksF_UjTS9p9i7eTtRPuAbf9geDhKb5e-y29MJaL1eKkhTMiEOPY3O4XGGuqRdRMrbjkNmla_RxiQhFJ3T8Dem-yDRan8gqaJLfRRrvGViz-lty96bQT-Z0hVer1uJhAtkM6RT_DgrnAUP_66LfaupZr6bLCKwnYocF1ICcAzkcYw7l5jHa4DTc2ZLgLi-yfbv2wGXpybAvLfZcO424TxHOuQykCSvbfPPuf06kkjPbYmMg6_GdM3JcQ_50VUXQFZkjH45BH5zX7y-2u0ReM8zxt65RpJAvlivrc8j2_E-u0LhlzCwEgsnd61lG4baaI86IVl4wNXkMDui4CgGvAUAf4AXW7Imw_cF0zI69z0SLfahjaYkdREGIYKStBtPAR04sfsR7o.LHBODYub4W4Vq-SXfdbk1Q"""
class JWT(Base):
    __tablename__ = 'jwt'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the JWT 
        Example: 123456"""
    token = Column(String)
    """The signed, encrypted, base64 encoded JWT 
        Example: ZXlKaGJHY2lPaUprYVhJaUxDSmxibU1pT2lKQk1qVTJSME5OSW4wLi5QbnAzS1QzLUJkZ3lQZHgtLm5JT0pOV01iZmdtQ0g3WWtybjhLeHlMbW13cl9yZExXTXF3Y0IwbXkzZDd3V1NDd0JYQkV0UTRtTVNJSVRrX0FJcG0zSU1DeThMcW5NdzA0ckdHVTkweDB3MmNJbjdHeWxOUXdveU5ZZ3UwOEN4TkZteUpCeW5FVktrdU05QlRyZXZ3Y1ZTN2hvaC1WZHRqM19PR3duRm5yUVgwSFhFVFc4R28tUGxoQVUtUnhKT0pNakx1OUxYd2NDUzZsaW9ZMno5NVU3T0hLSGNpaDBmSGVjN2FzekVJT3g4NExUeHlReGxYU3BtbFZ5LVNuYWdfbVJUeU5yNHNsMmlDWFcwSzZCNDhpWHJ1clJVVm1LUkVlVTl4ZVVJcTJPaWNpSHpfemJ0X3FrMjhkdzRyajZXRnBHSlZPNWcwTlUzVHlSWk5qdHg1S2NrTjVSQjZ1X2FzWTBScjhTY2VhNFk3Y2JFX01wcm54cFZTNDFIekVVSVRNdzVMTk1GLVpQZy52LVVDTkVJYk8zQ09EVEhPRnFXLUFR"""
class LatePolicy(Base):
    __tablename__ = 'late_policy'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the late policy 
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
    LatePolicyAllowedValues = enum.Enum('LatePolicyAllowedValues', ['hour', 'day'])
    """Enum for the allowed values of the late_submission_interval field"""
    late_submission_interval = Column(Enum(LatePolicyAllowedValues))
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
    course_id = Column(Integer)
    """the unique identifier for the course 
        Example: 123"""
class LineItem(Base):
    __tablename__ = 'line_item'
    id = Column(String, primary_key=True)
    """The fully qualified URL for showing, updating, and deleting the Line Item 
        Example: http://institution.canvas.com/api/lti/courses/5/line_items/2"""
    scoreMaximum = Column(Integer)
    """The maximum score of the Line Item 
        Example: 50"""
    label = Column(String)
    """The label of the Line Item. 
        Example: 50"""
    tag = Column(String)
    """Tag used to qualify a line Item beyond its ids 
        Example: 50"""
    resourceId = Column(String)
    """A Tool Provider specified id for the Line Item. Multiple line items can share the same resourceId within a given context 
        Example: 50"""
    resourceLinkId = Column(String)
    """The resource link id the Line Item is attached to 
        Example: 50"""
    https://canvas.instructure.com/lti/submission_type = Column(String)
    """The extension that defines the submission_type of the line_item. Only returns if set through the line_item create endpoint. 
        Example: {
	"type":"external_tool",
	"external_tool_url":"https://my.launch.url",
}"""
    https://canvas.instructure.com/lti/launch_url = Column(String)
    """The launch url of the Line Item. Only returned if `include=launch_url` query parameter is passed, and only for Show and List actions. 
        Example: https://my.tool.url/launch"""
class Assessment(Base):
    """A simple assessment that collects pass/fail results for a student"""
    __tablename__ = 'assessment'
    id = Column(String, primary_key=True)
    """A unique identifier for this live assessment 
        Example: 42"""
    key = Column(String)
    """A client specified unique identifier for the assessment 
        Example: 2014-05-27,outcome_52"""
    title = Column(String)
    """A human readable title for the assessment 
        Example: May 27th Reading Assessment"""
class Result(Base):
    """A pass/fail results for a student"""
    __tablename__ = 'result'
    id = Column(String, primary_key=True)
    """A unique identifier for this result 
        Example: 42"""
    passed = Column(Boolean)
    """Whether the user passed or not 
        Example: True"""
    assessed_at = Column(DateTime)
    """When this result was recorded 
        Example: 2014-05-13T00:01:57-06:00"""
    links = relationship('ResultLinks')
    """Unique identifiers of objects associated with this result 
        Example: {'user': '42', 'assessor': '23', 'assessment': '5'}"""
class ResultLinks(Base):
    """Unique identifiers of objects associated with a result"""
    __tablename__ = 'result_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ResultLinks 
        Example: 123456"""
    user = Column(String)
    """A unique identifier for the user to whom this result applies 
        Example: 42"""
    assessor = Column(String)
    """A unique identifier for the user who created this result 
        Example: 23"""
    assessment = Column(String)
    """A unique identifier for the assessment that this result is for 
        Example: 5"""
class MediaObject(Base):
    __tablename__ = 'media_object'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the MediaObject 
        Example: 123456"""
    can_add_captions = Column(Boolean)
    """No Description Provided 
        Example: """
    user_entered_title = Column(String)
    """No Description Provided 
        Example: """
    title = Column(String)
    """No Description Provided 
        Example: """
    media_type = Column(String)
    """No Description Provided 
        Example: """
    media_tracks = Column(String)
    """No Description Provided 
        Example: """
    media_sources = Column(String)
    """No Description Provided 
        Example: """
    media_id = Column(String)
    """No Description Provided 
        Example: """
class MediaTrack(Base):
    __tablename__ = 'media_track'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: """
    media_object_id = Column(Integer)
    """No Description Provided 
        Example: """
    kind = Column(String)
    """No Description Provided 
        Example: """
    locale = Column(String)
    """No Description Provided 
        Example: """
    content = Column(String)
    """No Description Provided 
        Example: """
    created_at = Column(String)
    """No Description Provided 
        Example: """
    updated_at = Column(String)
    """No Description Provided 
        Example: """
    webvtt_content = Column(String)
    """No Description Provided 
        Example: """
    user_id = Column(Integer)
    """No Description Provided 
        Example: """
class ProvisionalGrade(Base):
    __tablename__ = 'provisional_grade'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ProvisionalGrade 
        Example: 123456"""
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
        Example: False"""
    speedgrader_url = Column(String)
    """A link to view this provisional grade in SpeedGrader™ 
        Example: http://www.example.com/courses/123/gradebook/speed_grader?..."""
    provisional_grade_id = Column(Integer)
    """The identifier for the provisional grade 
        Example: 23"""
class CompletionRequirement(Base):
    __tablename__ = 'completion_requirement'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CompletionRequirement 
        Example: 123456"""
    CompletionRequirementAllowedValues = enum.Enum('CompletionRequirementAllowedValues', ['must_view', 'must_submit', 'must_contribute', 'min_score', 'must_mark_done'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(CompletionRequirementAllowedValues))
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
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ContentDetails 
        Example: 123456"""
    points_possible = Column(Integer)
    """No Description Provided 
        Example: 20"""
    due_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-12-31T06:00:00-06:00"""
    unlock_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-12-31T06:00:00-06:00"""
    lock_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-12-31T06:00:00-06:00"""
    locked_for_user = Column(Boolean)
    """No Description Provided 
        Example: True"""
    lock_explanation = Column(String)
    """No Description Provided 
        Example: This quiz is part of an unpublished module and is not available yet."""
    lock_info = relationship('LockInfo')
    """No Description Provided 
        Example: {'asset_string': 'assignment_4', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00', 'context_module': {}}"""
class Module(Base):
    __tablename__ = 'module'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the module 
        Example: 123"""
    ModuleAllowedValues = enum.Enum('ModuleAllowedValues', ['active', 'deleted'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(ModuleAllowedValues))
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
        Example: """
    ModuleAllowedValues = enum.Enum('ModuleAllowedValues', ['locked', 'unlocked', 'started', 'completed'])
    """Enum for the allowed values of the state field"""
    state = Column(Enum(ModuleAllowedValues))
    """The state of this Module for the calling user one of 'locked', 'unlocked', 'started', 'completed' (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) 
        Example: started"""
    completed_at = Column(DateTime)
    """the date the calling user completed the module (Optional; present only if the caller is a student or if the optional parameter 'student_id' is included) 
        Example: """
    publish_final_grade = Column(Boolean)
    """if the student's final grade for the course should be published to the SIS upon completion of this module 
        Example: """
    published = Column(Boolean)
    """(Optional) Whether this module is published. This field is present only if the caller has permission to view unpublished modules. 
        Example: True"""
class ModuleItem(Base):
    __tablename__ = 'module_item'
    id = Column(Integer, primary_key=True)
    """the unique identifier for the module item 
        Example: 768"""
    position = Column(Integer)
    """the position of this item in the module (1-based) 
        Example: 1"""
    title = Column(String)
    """the title of this item 
        Example: Square Roots: Irrational numbers or boxy vegetables?"""
    indent = Column(Integer)
    """0-based indent level; module items may be indented to show a hierarchy 
        Example: 0"""
    ModuleItemAllowedValues = enum.Enum('ModuleItemAllowedValues', ['File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool'])
    """Enum for the allowed values of the type field"""
    type = Column(Enum(ModuleItemAllowedValues))
    """the type of object referred to one of 'File', 'Page', 'Discussion', 'Assignment', 'Quiz', 'SubHeader', 'ExternalUrl', 'ExternalTool' 
        Example: Assignment"""
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
        Example: False"""
    content_details = relationship('ContentDetails')
    """(Present only if requested through include[]=content_details) If applicable, returns additional details specific to the associated object 
        Example: {'points_possible': 20, 'due_at': '2012-12-31T06:00:00-06:00', 'unlock_at': '2012-12-31T06:00:00-06:00', 'lock_at': '2012-12-31T06:00:00-06:00'}"""
    published = Column(Boolean)
    """(Optional) Whether this module item is published. This field is present only if the caller has permission to view unpublished items. 
        Example: True"""
    content_id = Column(Integer)
    """the id of the object referred to applies to 'File', 'Discussion', 'Assignment', 'Quiz', 'ExternalTool' types 
        Example: 1337"""
    module_id = Column(Integer)
    """the id of the Module this item appears in 
        Example: 123"""
    completion_requirement = relationship('CompletionRequirement')
    """Completion requirement for this module item 
        Example: {'type': 'min_score', 'min_score': 10, 'completed': True}"""
class ModuleItemSequence(Base):
    __tablename__ = 'module_item_sequence'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ModuleItemSequence 
        Example: 123456"""
    items = Column(JsonObject)
"""List[ModuleItemSequenceNode]"""
    """an array containing one ModuleItemSequenceNode for each appearence of the asset in the module sequence (up to 10 total) 
        Example: [{'prev': None, 'current': {'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}, 'next': {'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}, 'mastery_path': {'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}}]"""
    modules = Column(JsonObject)
"""List[Module]"""
    """an array containing each Module referenced above 
        Example: [{'id': 123, 'name': 'Overview'}, {'id': 127, 'name': 'Imaginary Numbers'}]"""
class ModuleItemSequenceNode(Base):
    __tablename__ = 'module_item_sequence_node'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ModuleItemSequenceNode 
        Example: 123456"""
    current = relationship('ModuleItem')
    """The ModuleItem being queried 
        Example: {'id': 768, 'module_id': 123, 'title': 'A lonely page', 'type': 'Page'}"""
    mastery_path = relationship('Unknown')
    """The conditional release rule for the module item, if applicable 
        Example: {'locked': True, 'assignment_sets': [], 'selected_set_id': None, 'awaiting_choice': False, 'still_processing': False, 'modules_url': '/courses/11/modules', 'choose_url': '/courses/11/modules/items/9/choose', 'modules_tab_disabled': False}"""
    next = relationship('ModuleItem')
    """The next ModuleItem in the sequence 
        Example: {'id': 769, 'module_id': 127, 'title': 'Project 1', 'type': 'Assignment'}"""
    prev = relationship('ModuleItem')
    """The previous ModuleItem in the sequence 
        Example: """
class NamesAndRoleContext(Base):
    """An abbreviated representation of an LTI Context"""
    __tablename__ = 'names_and_role_context'
    id = Column(String, primary_key=True)
    """LTI Context unique identifier 
        Example: 4dde05e8ca1973bcca9bffc13e1548820eee93a3"""
    label = Column(String)
    """LTI Context short name or code 
        Example: CS-101"""
    title = Column(String)
    """LTI Context full name 
        Example: Computer Science 101"""
class NamesAndRoleMembership(Base):
    """A member of a LTI Context in one or more roles"""
    __tablename__ = 'names_and_role_membership'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the NamesAndRoleMembership 
        Example: 123456"""
    NamesAndRoleMembershipAllowedValues = enum.Enum('NamesAndRoleMembershipAllowedValues', ['Active'])
    """Enum for the allowed values of the status field"""
    status = Column(Enum(NamesAndRoleMembershipAllowedValues))
    """Membership state 
        Example: Active"""
    name = Column(String)
    """Member's full name. Only included if tool privacy level is `public` or `name_only`. 
        Example: Sienna Howell"""
    picture = Column(String)
    """URL to the member's avatar. Only included if tool privacy level is `public`. 
        Example: https://example.instructure.com/images/messages/avatar-50.png"""
    given_name = Column(String)
    """Member's 'first' name. Only included if tool privacy level is `public` or `name_only`. 
        Example: Sienna"""
    family_name = Column(String)
    """Member's 'last' name. Only included if tool privacy level is `public` or `name_only`. 
        Example: Howell"""
    email = Column(String)
    """Member's email address. Only included if tool privacy level is `public` or `email_only`. 
        Example: showell@school.edu"""
    lis_person_sourcedid = Column(String)
    """Member's primary SIS identifier. Only included if tool privacy level is `public` or `name_only`. 
        Example: 1238.8763.00"""
    roles = Column(JsonObject)
"""List[NamesAndRoleMembershipAllowedValues]"""
    """Member's roles in the current Context, expressed as LTI/LIS URNs. 
        Example: ['http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor', 'http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper']"""
    message = Column(JsonObject)
"""List[NamesAndRoleMessage]"""
    """Only present when the request specifies a `rlid` query parameter. Contains additional attributes which would appear in the LTI launch message were this member to click the link referenced by the `rlid` query parameter 
        Example: [{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'en', 'https://www.instructure.com/canvas_user_id': 1, 'https://www.instructure.com/canvas_user_login_id': 'showell@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'America/Denver'}}]"""
    user_id = Column(String)
    """Member's unique LTI identifier. 
        Example: 535fa085f22b4655f48cd5a36a9215f64c062838"""
class NamesAndRoleMemberships(Base):
    __tablename__ = 'names_and_role_memberships'
    id = Column(String, primary_key=True)
    """Invocation URL 
        Example: https://example.instructure.com/api/lti/courses/1/names_and_roles?tlid=f91ca4d8-fa84-4a9b-b08e-47d5527416b0"""
    members = Column(JsonObject)
"""List[NamesAndRoleMembership]"""
    """A list of NamesAndRoleMembership 
        Example: [{'status': 'Active', 'name': 'Sienna Howell', 'picture': 'https://example.instructure.com/images/messages/avatar-50.png', 'given_name': 'Sienna', 'family_name': 'Howell', 'email': 'showell@school.edu', 'lis_person_sourcedid': '1238.8763.00', 'user_id': '535fa085f22b4655f48cd5a36a9215f64c062838', 'roles': ['http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor', 'http://purl.imsglobal.org/vocab/lis/v2/membership#ContentDeveloper'], 'message': [{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'en', 'https://www.instructure.com/canvas_user_id': 1, 'https://www.instructure.com/canvas_user_login_id': 'showell@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'America/Denver'}}]}, {'status': 'Active', 'name': 'Terrence Walls', 'picture': 'https://example.instructure.com/images/messages/avatar-51.png', 'given_name': 'Terrence', 'family_name': 'Walls', 'email': 'twalls@school.edu', 'lis_person_sourcedid': '5790.3390.11', 'user_id': '86157096483e6b3a50bfedc6bac902c0b20a824f', 'roles': ['http://purl.imsglobal.org/vocab/lis/v2/membership#Learner'], 'message': [{'https://purl.imsglobal.org/spec/lti/claim/message_type': 'LtiResourceLinkRequest', 'locale': 'de', 'https://www.instructure.com/canvas_user_id': 2, 'https://www.instructure.com/canvas_user_login_id': 'twalls@school.edu', 'https://purl.imsglobal.org/spec/lti/claim/custom': {'message_locale': 'en', 'person_address_timezone': 'Europe/Berlin'}}]}]"""
    context = relationship('NamesAndRoleContext')
    """The LTI Context containing the memberships 
        Example: {'id': '4dde05e8ca1973bcca9bffc13e1548820eee93a3', 'label': 'CS-101', 'title': 'Computer Science 101'}"""
class NamesAndRoleMessage(Base):
    """Additional attributes which would appear in the LTI launch message were this member to click the specified resource link (`rlid` query parameter)"""
    __tablename__ = 'names_and_role_message'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the NamesAndRoleMessage 
        Example: 123456"""
    NamesAndRoleMessageAllowedValues = enum.Enum('NamesAndRoleMessageAllowedValues', ['LtiResourceLinkRequest'])
    """Enum for the allowed values of the https://purl.imsglobal.org/spec/lti/claim/message_type field"""
    https://purl.imsglobal.org/spec/lti/claim/message_type = Column(Enum(NamesAndRoleMessageAllowedValues))
    """The type of LTI message being described. Always set to 'LtiResourceLinkRequest' 
        Example: LtiResourceLinkRequest"""
    locale = Column(String)
    """The member's preferred locale 
        Example: en"""
    https://www.instructure.com/canvas_user_login_id = Column(String)
    """The member's primary login username 
        Example: showell@school.edu"""
    https://www.instructure.com/canvas_user_id = Column(Integer)
    """The member's API ID 
        Example: 1"""
    https://purl.imsglobal.org/spec/lti/claim/custom = relationship('Unknown')
    """Expanded LTI custom parameters that pertain to the member (as opposed to the Context) 
        Example: {'message_locale': 'en', 'person_address_timezone': 'America/Denver'}"""
class NotificationPreference(Base):
    __tablename__ = 'notification_preference'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the NotificationPreference 
        Example: 123456"""
    href = Column(String)
    """No Description Provided 
        Example: https://canvas.instructure.com/users/1/communication_channels/email/student@example.edu/notification_preferences/new_announcement"""
    notification = Column(String)
    """The notification this preference belongs to 
        Example: new_announcement"""
    category = Column(String)
    """The category of that notification 
        Example: announcement"""
    NotificationPreferenceAllowedValues = enum.Enum('NotificationPreferenceAllowedValues', ['immediately', 'daily', 'weekly', 'never'])
    """Enum for the allowed values of the frequency field"""
    frequency = Column(Enum(NotificationPreferenceAllowedValues))
    """How often to send notifications to this communication channel for the given notification. Possible values are 'immediately', 'daily', 'weekly', and 'never' 
        Example: daily"""
class OriginalityReport(Base):
    __tablename__ = 'originality_report'
    id = Column(Integer, primary_key=True)
    """The id of the OriginalityReport 
        Example: 4"""
    originality_score = Column(Integer)
    """A number between 0 and 100 representing the originality score 
        Example: 0.16"""
    originality_report_url = Column(String)
    """A non-LTI launch URL where the originality score of the file may be found. 
        Example: http://www.example.com/report"""
    error_report = Column(String)
    """A message describing the error. If set, the workflow_state will become 'error.' 
        Example: """
    submission_time = Column(DateTime)
    """The submitted_at date time of the submission. 
        Example: """
    file_id = Column(Integer)
    """The id of the file receiving the originality score 
        Example: 8"""
    root_account_id = Column(Integer)
    """The id of the root Account associated with the OriginalityReport 
        Example: 1"""
    originality_report_file_id = Column(Integer)
    """The ID of the file within Canvas containing the originality report document (if provided) 
        Example: 23"""
    tool_setting = relationship('ToolSetting')
    """A ToolSetting object containing optional 'resource_type_code' and 'resource_url' 
        Example: """
class ToolSetting(Base):
    __tablename__ = 'tool_setting'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ToolSetting 
        Example: 123456"""
    resource_type_code = Column(String)
    """the resource type code of the resource handler to use to display originality reports 
        Example: originality_reports"""
    resource_url = Column(String)
    """a URL that may be used to override the launch URL inferred by the specified resource_type_code. If used a 'resource_type_code' must also be specified. 
        Example: http://www.test.com/originality_report"""
class OutcomeGroup(Base):
    __tablename__ = 'outcome_group'
    id = Column(Integer, primary_key=True)
    """the ID of the outcome group 
        Example: 1"""
    url = Column(String)
    """the URL for fetching/updating the outcome group. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1"""
    context_type = Column(String)
    """No Description Provided 
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
    context_id = Column(Integer)
    """the context owning the outcome group. may be null for global outcome groups. omitted in the abbreviated form. 
        Example: 1"""
    parent_outcome_group = relationship('OutcomeGroup')
    """an abbreviated OutcomeGroup object representing the parent group of this outcome group, if any. omitted in the abbreviated form. 
        Example: """
class OutcomeLink(Base):
    __tablename__ = 'outcome_link'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeLink 
        Example: 123456"""
    url = Column(String)
    """the URL for fetching/updating the outcome link. should be treated as opaque 
        Example: /api/v1/accounts/1/outcome_groups/1/outcomes/1"""
    context_type = Column(String)
    """No Description Provided 
        Example: Account"""
    outcome = relationship('Outcome')
    """an abbreviated Outcome object representing the outcome linked into the containing outcome group. 
        Example: """
    assessed = Column(Boolean)
    """whether this outcome has been used to assess a student in the context of this outcome link.  In other words, this will be set to true if the context is a course, and a student has been assessed with this outcome in that course. 
        Example: True"""
    can_unlink = Column(Boolean)
    """whether this outcome link is manageable and is not the last link to an aligned outcome 
        Example: """
    context_id = Column(Integer)
    """the context owning the outcome link. will match the context owning the outcome group containing the outcome link; included for convenience. may be null for links in global outcome groups. 
        Example: 1"""
    outcome_group = relationship('OutcomeGroup')
    """an abbreviated OutcomeGroup object representing the group containing the outcome link. 
        Example: """
class OutcomeImport(Base):
    __tablename__ = 'outcome_import'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the outcome import. 
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
    OutcomeImportAllowedValues = enum.Enum('OutcomeImportAllowedValues', ['created', 'importing', 'succeeded', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(OutcomeImportAllowedValues))
    """The current state of the outcome import.
 - 'created': The outcome import has been created.
 - 'importing': The outcome import is currently processing.
 - 'succeeded': The outcome import has completed successfully.
 - 'failed': The outcome import failed. 
        Example: imported"""
    progress = Column(String)
    """The progress of the outcome import. 
        Example: 100"""
    processing_errors = Column(JsonObject)
"""List[List[Unknown]]"""
    """An array of row number / error message pairs. Returns the first 25 errors. 
        Example: [[1, 'Missing required fields: title']]"""
    learning_outcome_group_id = Column(Integer)
    """The unique identifier for the group into which the outcomes will be imported to, or NULL. 
        Example: 1"""
    user = relationship('User')
    """The user that initiated the outcome_import. See the Users API for details. 
        Example: """
    data = relationship('OutcomeImportData')
    """See the OutcomeImportData specification above. 
        Example: """
class OutcomeImportData(Base):
    __tablename__ = 'outcome_import_data'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeImportData 
        Example: 123456"""
    import_type = Column(String)
    """The type of outcome import 
        Example: instructure_csv"""
class OutcomeAlignment(Base):
    """An asset aligned with this outcome"""
    __tablename__ = 'outcome_alignment'
    id = Column(String, primary_key=True)
    """A unique identifier for this alignment 
        Example: quiz_3"""
    name = Column(String)
    """The name of this alignment 
        Example: Big mid-term test"""
    html_url = Column(String)
    """(Optional) A URL for details about this alignment 
        Example: """
class OutcomePath(Base):
    """The full path to an outcome"""
    __tablename__ = 'outcome_path'
    id = Column(Integer, primary_key=True)
    """A unique identifier for this outcome 
        Example: 42"""
    parts = relationship('OutcomePathPart')
    """an array of OutcomePathPart objects 
        Example: """
class OutcomePathPart(Base):
    """An outcome or outcome group"""
    __tablename__ = 'outcome_path_part'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomePathPart 
        Example: 123456"""
    name = Column(String)
    """The title of the outcome or outcome group 
        Example: Spelling out numbers"""
class OutcomeResult(Base):
    """A student's result for an outcome"""
    __tablename__ = 'outcome_result'
    id = Column(Integer, primary_key=True)
    """A unique identifier for this result 
        Example: 42"""
    score = Column(Integer)
    """The student's score 
        Example: 6"""
    submitted_or_assessed_at = Column(DateTime)
    """The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed. 
        Example: 2013-02-01T00:00:00-06:00"""
    percent = Column(Integer)
    """score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome 
        Example: 0.65"""
    links = relationship('Unknown')
    """Unique identifiers of objects associated with this result 
        Example: {'user': '3', 'learning_outcome': '97', 'alignment': '53'}"""
class OutcomeRollup(Base):
    __tablename__ = 'outcome_rollup'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeRollup 
        Example: 123456"""
    name = Column(String)
    """The name of the resource for this rollup. For example, the user name. 
        Example: John Doe"""
    scores = relationship('OutcomeRollupScore')
    """an array of OutcomeRollupScore objects 
        Example: """
    links = relationship('OutcomeRollupLinks')
    """No Description Provided 
        Example: {'course': 42, 'user': 42, 'section': 57}"""
class OutcomeRollupLinks(Base):
    __tablename__ = 'outcome_rollup_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeRollupLinks 
        Example: 123456"""
    course = Column(Integer)
    """If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to 
        Example: 42"""
    user = Column(Integer)
    """(Optional) The id of the user that this rollup applies to 
        Example: 42"""
    section = Column(Integer)
    """(Optional) The id of the section the user is in 
        Example: 57"""
class OutcomeRollupScore(Base):
    __tablename__ = 'outcome_rollup_score'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeRollupScore 
        Example: 123456"""
    score = Column(Integer)
    """The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores. 
        Example: 3"""
    count = Column(Integer)
    """The number of alignment scores included in this rollup. 
        Example: 6"""
    links = relationship('OutcomeRollupScoreLinks')
    """No Description Provided 
        Example: {'outcome': '42'}"""
class OutcomeRollupScoreLinks(Base):
    __tablename__ = 'outcome_rollup_score_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the OutcomeRollupScoreLinks 
        Example: 123456"""
    outcome = Column(Integer)
    """The id of the related outcome 
        Example: 42"""
class Outcome(Base):
    __tablename__ = 'outcome'
    id = Column(Integer, primary_key=True)
    """the ID of the outcome 
        Example: 1"""
    url = Column(String)
    """the URL for fetching/updating the outcome. should be treated as opaque 
        Example: /api/v1/outcomes/1"""
    context_type = Column(String)
    """No Description Provided 
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
    OutcomeAllowedValues = enum.Enum('OutcomeAllowedValues', ['decaying_average', 'n_mastery', 'latest', 'highest', 'average'])
    """Enum for the allowed values of the calculation_method field"""
    calculation_method = Column(Enum(OutcomeAllowedValues))
    """the method used to calculate a students score 
        Example: decaying_average"""
    calculation_int = Column(Integer)
    """this defines the variable value used by the calculation_method. included only if calculation_method uses it 
        Example: 65"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """possible ratings for this outcome. included only if the outcome embeds a rubric criterion. omitted in the abbreviated form. 
        Example: """
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
    context_id = Column(Integer)
    """the context owning the outcome. may be null for global outcomes 
        Example: 1"""
class OutcomeAlignment(Base):
    __tablename__ = 'outcome_alignment'
    id = Column(Integer, primary_key=True)
    """the id of the aligned learning outcome. 
        Example: 1"""
    assessment_id = Column(Integer)
    """the id of the aligned live assessment (null for assignments). 
        Example: 3"""
    submission_types = Column(String)
    """a string representing the different submission types of an aligned assignment. 
        Example: online_text_entry,online_url"""
    url = Column(String)
    """the URL for the aligned assignment. 
        Example: /courses/1/assignments/5"""
    title = Column(String)
    """the title of the aligned assignment. 
        Example: Unit 1 test"""
    assignment_id = Column(Integer)
    """the id of the aligned assignment (null for live assessments). 
        Example: 2"""
class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Page 
        Example: 123456"""
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
        Example: False"""
    editing_roles = Column(String)
    """roles allowed to edit the page; comma-separated list comprising a combination of 'teachers', 'students', 'members', and/or 'public' if not supplied, course defaults are used 
        Example: teachers,students"""
    body = Column(String)
    """the page content, in HTML (present when requesting a single page; omitted when listing pages) 
        Example: <p>Page Content</p>"""
    published = Column(Boolean)
    """whether the page is published (true) or draft state (false). 
        Example: True"""
    front_page = Column(Boolean)
    """whether this page is the front page for the wiki 
        Example: False"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: False"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This page is locked until September 1 at 12:00am"""
    page_id = Column(Integer)
    """the ID of the page 
        Example: 1"""
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: """
    last_edited_by = relationship('User')
    """the User who last edited the page (this may not be present if the page was imported from another system) 
        Example: """
class PageRevision(Base):
    __tablename__ = 'page_revision'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the PageRevision 
        Example: 123456"""
    updated_at = Column(DateTime)
    """the time when this revision was saved 
        Example: 2012-08-07T11:23:58-06:00"""
    latest = Column(Boolean)
    """whether this is the latest revision or not 
        Example: True"""
    url = Column(String)
    """the following fields are not included in the index action and may be omitted from the show action via summary=1 the historic url of the page 
        Example: old-page-title"""
    title = Column(String)
    """the historic page title 
        Example: Old Page Title"""
    body = Column(String)
    """the historic page contents 
        Example: <p>Old Page Content</p>"""
    revision_id = Column(Integer)
    """an identifier for this revision of the page 
        Example: 7"""
    edited_by = relationship('User')
    """the User who saved this revision, if applicable (this may not be present if the page was imported from another system) 
        Example: """
class PeerReview(Base):
    __tablename__ = 'peer_review'
    id = Column(Integer, primary_key=True)
    """The id of the Peer Review 
        Example: 1"""
    asset_id = Column(Integer)
    """The id for the asset associated with this Peer Review 
        Example: 13"""
    asset_type = Column(String)
    """The type of the asset 
        Example: Submission"""
    workflow_state = Column(String)
    """The state of the Peer Review, either 'assigned' or 'completed' 
        Example: assigned"""
    submission_comments = Column(String)
    """The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional) 
        Example: SubmissionComment"""
    user_id = Column(Integer)
    """The user id for the owner of the asset 
        Example: 7"""
    user = Column(String)
    """the User object for the owner of the asset if the user include parameter is provided (see user API) (optional) 
        Example: User"""
    assessor_id = Column(Integer)
    """The assessors user id 
        Example: 23"""
    assessor = Column(String)
    """The User object for the assessor if the user include parameter is provided (see user API) (optional) 
        Example: User"""
class LtiAssignment(Base):
    """A Canvas assignment"""
    __tablename__ = 'lti_assignment'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 4"""
    name = Column(String)
    """No Description Provided 
        Example: Midterm Review"""
    description = Column(String)
    """No Description Provided 
        Example: <p>Do the following:</p>..."""
    points_possible = Column(Integer)
    """No Description Provided 
        Example: 10"""
    due_at = Column(DateTime)
    """The due date for the assignment. If a user id is supplied and an assignment override is in place this field will reflect the due date as it applies to the user. 
        Example: 2012-07-01T23:59:00-06:00"""
    course_id = Column(Integer)
    """No Description Provided 
        Example: 10000000000060"""
    lti_id = Column(String)
    """No Description Provided 
        Example: 86157096483e6b3a50bfedc6bac902c0b20a824f"""
    lti_course_id = Column(String)
    """No Description Provided 
        Example: 66157096483e6b3a50bfedc6bac902c0b20a8241"""
class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 569"""
    size = Column(Integer)
    """No Description Provided 
        Example: 4"""
    content-type = Column(String)
    """No Description Provided 
        Example: text/plain"""
    url = Column(String)
    """No Description Provided 
        Example: http://www.example.com/files/569/download?download_frd=1&verifier=c6HdZmxOZa0Fiin2cbvZeI8I5ry7yqD7RChQzb6P"""
    display_name = Column(String)
    """No Description Provided 
        Example: file.txt"""
    created_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
    updated_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-07-06T14:58:50Z"""
class Submission(Base):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Submission 
        Example: 123456"""
    course_id = Column(Integer)
    """No Description Provided 
        Example: 10000000000060"""
    attempt = Column(Integer)
    """This is the submission attempt number. 
        Example: 1"""
    body = Column(String)
    """The content of the submission, if it was submitted directly in a text field. 
        Example: There are three factors too..."""
    SubmissionAllowedValues = enum.Enum('SubmissionAllowedValues', ['online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_type field"""
    submission_type = Column(Enum(SubmissionAllowedValues))
    """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation') 
        Example: online_text_entry"""
    submitted_at = Column(DateTime)
    """The timestamp when the assignment was submitted 
        Example: 2012-01-01T01:00:00Z"""
    url = Column(String)
    """The URL of the submission (for 'online_url' submissions). 
        Example: """
    eula_agreement_timestamp = Column(String)
    """UTC timestamp showing when the user agreed to the EULA (if given by the tool provider) 
        Example: 1508250487578"""
    SubmissionAllowedValues = enum.Enum('SubmissionAllowedValues', ['graded', 'submitted', 'unsubmitted', 'pending_review'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(SubmissionAllowedValues))
    """The current state of the submission 
        Example: submitted"""
    assignment_id = Column(Integer)
    """The submission's assignment id 
        Example: 23"""
    lti_course_id = Column(String)
    """No Description Provided 
        Example: 66157096483e6b3a50bfedc6bac902c0b20a8241"""
    user_id = Column(Integer)
    """The id of the user who created the submission 
        Example: 134"""
    attachments = relationship('File')
    """Files that are attached to the submission 
        Example: """
class PlannerNote(Base):
    """A planner note"""
    __tablename__ = 'planner_note'
    id = Column(Integer, primary_key=True)
    """The ID of the planner note 
        Example: 234"""
    title = Column(String)
    """The title for a planner note 
        Example: Bring books tomorrow"""
    description = Column(String)
    """The description of the planner note 
        Example: I need to bring books tomorrow for my course on biology"""
    workflow_state = Column(String)
    """The current published state of the planner note 
        Example: active"""
    todo_date = Column(DateTime)
    """The datetime of when the planner note should show up on their planner 
        Example: 2017-05-09T10:12:00Z"""
    linked_object_type = Column(String)
    """the type of the linked learning object 
        Example: assignment"""
    linked_object_html_url = Column(String)
    """the Canvas web URL of the linked learning object 
        Example: https://canvas.example.com/courses/1578941/assignments/131072"""
    linked_object_url = Column(String)
    """the API URL of the linked learning object 
        Example: https://canvas.example.com/api/v1/courses/1578941/assignments/131072"""
    course_id = Column(Integer)
    """The course that the note is in relation too, if applicable 
        Example: 1578941"""
    user_id = Column(Integer)
    """The id of the associated user creating the planner note 
        Example: 1578941"""
    linked_object_id = Column(Integer)
    """the id of the linked learning object 
        Example: 131072"""
class PlannerOverride(Base):
    """User-controlled setting for whether an item should be displayed on the planner or not"""
    __tablename__ = 'planner_override'
    id = Column(Integer, primary_key=True)
    """The ID of the planner override 
        Example: 234"""
    plannable_type = Column(String)
    """The type of the associated object for the planner override 
        Example: Assignment"""
    user_id = Column(Integer)
    """The id of the associated user for the planner override 
        Example: 1578941"""
    workflow_state = Column(String)
    """The current published state of the item, synced with the associated object 
        Example: published"""
    marked_complete = Column(Boolean)
    """Controls whether or not the associated plannable item is marked complete on the planner 
        Example: False"""
    dismissed = Column(Boolean)
    """Controls whether or not the associated plannable item shows up in the opportunities list 
        Example: False"""
    created_at = Column(DateTime)
    """The datetime of when the planner override was created 
        Example: 2017-05-09T10:12:00Z"""
    updated_at = Column(DateTime)
    """The datetime of when the planner override was updated 
        Example: 2017-05-09T10:12:00Z"""
    deleted_at = Column(DateTime)
    """The datetime of when the planner override was deleted, if applicable 
        Example: 2017-05-15T12:12:00Z"""
    assignment_id = Column(Integer)
    """The id of the plannable's associated assignment, if it has one 
        Example: 1578941"""
    plannable_id = Column(Integer)
    """The id of the associated object for the planner override 
        Example: 1578941"""
class PollChoice(Base):
    __tablename__ = 'poll_choice'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the poll choice. 
        Example: 1023"""
    is_correct = Column(Boolean)
    """Specifies whether or not this poll choice is a 'correct' choice. 
        Example: true"""
    text = Column(String)
    """The text of the poll choice. 
        Example: Choice A"""
    position = Column(Integer)
    """The order of the poll choice in relation to it's sibling poll choices. 
        Example: 1"""
    poll_id = Column(Integer)
    """The id of the poll this poll choice belongs to. 
        Example: 1779"""
class PollSession(Base):
    __tablename__ = 'poll_session'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the poll session. 
        Example: 1023"""
    course_id = Column(Integer)
    """The id of the Course this poll session is associated with 
        Example: 1111"""
    is_published = Column(Boolean)
    """Specifies whether or not this poll session has been published for students to participate in. 
        Example: true"""
    has_public_results = Column(Boolean)
    """Specifies whether the results are viewable by students. 
        Example: true"""
    created_at = Column(String)
    """The time at which the poll session was created. 
        Example: 2014-01-07T15:16:18Z"""
    poll_submissions = relationship('PollSubmission')
    """If the poll session has public results, this will return an array of all submissions, viewable by both students and teachers. If the results are not public, for students it will return their submission only. 
        Example: """
    course_section_id = Column(Integer)
    """The id of the Course Section this poll session is associated with 
        Example: 444"""
    poll_id = Column(Integer)
    """The id of the Poll this poll session is associated with 
        Example: 55"""
    results = relationship('Unknown')
    """The results of the submissions of the poll. Each key is the poll choice id, and the value is the count of submissions. 
        Example: {'144': 10, '145': 3, '146': 27, '147': 8}"""
class PollSubmission(Base):
    __tablename__ = 'poll_submission'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the poll submission. 
        Example: 1023"""
    user_id = Column(Integer)
    """the unique identifier of the user who submitted this poll submission. 
        Example: 4555"""
    created_at = Column(String)
    """The date and time the poll submission was submitted. 
        Example: 2013-11-07T13:16:18Z"""
    poll_choice_id = Column(Integer)
    """The unique identifier of the poll choice chosen for this submission. 
        Example: 155"""
class Poll(Base):
    __tablename__ = 'poll'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the poll. 
        Example: 1023"""
    question = Column(String)
    """The question/title of the poll. 
        Example: What do you consider most important to your learning in this course?"""
    description = Column(String)
    """A short description of the poll. 
        Example: This poll is to determine what priorities the students in the course have."""
    created_at = Column(String)
    """The time at which the poll was created. 
        Example: 2014-01-07T15:16:18Z"""
    user_id = Column(Integer)
    """The unique identifier for the user that created the poll. 
        Example: 105"""
    total_results = relationship('Unknown')
    """An aggregate of the results of all associated poll sessions, with the poll choice id as the key, and the aggregated submission count as the value. 
        Example: {'543': 20, '544': 5, '545': 17}"""
class Proficiency(Base):
    __tablename__ = 'proficiency'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Proficiency 
        Example: 123456"""
    ratings = Column(JsonObject(List))
    """An array of proficiency ratings. See the ProficiencyRating specification above. 
        Example: []"""
class ProficiencyRating(Base):
    __tablename__ = 'proficiency_rating'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the ProficiencyRating 
        Example: 123456"""
    description = Column(String)
    """The description of the rating 
        Example: Exceeds Mastery"""
    points = Column(Integer)
    """A non-negative number of points for the rating 
        Example: 4"""
    mastery = Column(Boolean)
    """Indicates the rating where mastery is first achieved 
        Example: False"""
    color = Column(String)
    """The hex color code of the rating 
        Example: 127A1B"""
class Progress(Base):
    __tablename__ = 'progress'
    id = Column(Integer, primary_key=True)
    """the ID of the Progress object 
        Example: 1"""
    context_type = Column(String)
    """No Description Provided 
        Example: Account"""
    tag = Column(String)
    """the type of operation 
        Example: course_batch_update"""
    completion = Column(Integer)
    """percent completed 
        Example: 100"""
    ProgressAllowedValues = enum.Enum('ProgressAllowedValues', ['queued', 'running', 'completed', 'failed'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(ProgressAllowedValues))
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
    url = Column(String)
    """url where a progress update can be retrieved with an LTI access token 
        Example: https://canvas.example.edu/api/lti/courses/1/progress/1"""
    user_id = Column(Integer)
    """the id of the user who started the job 
        Example: 123"""
    context_id = Column(Integer)
    """the context owning the job. 
        Example: 1"""
    results = relationship('Unknown')
    """optional results of the job. omitted when job is still pending 
        Example: {'id': '123'}"""
class DeveloperKey(Base):
    __tablename__ = 'developer_key'
    id = Column(Integer, primary_key=True)
    """The ID should match the Developer Key ID in canvas 
        Example: 1000000000040"""
    is_lti_key = Column(Boolean)
    """true the tool is a lti key, null is not a lti key 
        Example: true"""
    visible = Column(Boolean)
    """Controls if the tool is visable 
        Example: true"""
    account_name = Column(String)
    """The name of the account associated with the tool 
        Example: The Academy"""
    public_jwk = Column(String)
    """The public key in jwk format 
        Example: {
	"kty":"RSA",
	"e":"AQAB",
	"n":"ufmgt156hs168mgdhy168jrsydt168ju816rtahesuvdbmnrtd87t7h8ser",
	"alg":"RS256",
	"use":"sig",
	"kid":"Se68gr16s6tj_87sdr98g489dsfjy-547a6eht1",
}"""
    vendor_code = Column(String)
    """The code of the vendor managing the tool 
        Example: fi5689s9avewr68"""
    last_used_at = Column(DateTime)
    """The date and time the tool was last used 
        Example: 2019-06-07T20:34:33Z"""
    access_token_count = Column(Integer)
    """The number of active access tokens associated with the tool 
        Example: 0"""
    redirect_uris = Column(String)
    """redirect uris description 
        Example: https://redirect.to.here.com"""
    redirect_uri = Column(String)
    """redirect uri description 
        Example: https://redirect.to.here.com"""
    api_key = Column(String)
    """Api key for api access for the tool 
        Example: sd45fg648sr546tgh15S15df5se56r4xdf45asef456"""
    notes = Column(String)
    """Notes for use specifications for the tool 
        Example: Used for sorting graded assignments"""
    name = Column(String)
    """Display name of the tool 
        Example: Tool 1"""
    created_at = Column(DateTime)
    """The time the jwk was created 
        Example: 2019-06-07T20:34:33Z"""
    user_name = Column(String)
    """The user name of the tool creator 
        Example: johnsmith"""
    email = Column(String)
    """Email associated with the tool owner 
        Example: johnsmith@instructure.com"""
    require_scopes = Column(Boolean)
    """True if the tool has required permissions, null if there are no needed permissions 
        Example: true"""
    icon_url = Column(String)
    """Icon to be displayed with the name of the tool 
        Example: null"""
    scopes = Column(String)
    """Specified permissions for the tool 
        Example: https://canvas.instructure.com/lti/public_jwk/scope/update"""
    workflow_state = Column(String)
    """The current state of the tool 
        Example: active"""
    user_id = Column(String)
    """ID of the user associated with the tool 
        Example: tu816dnrs6zdsg148918dmu"""
class QuizAssignmentOverride(Base):
    """Set of assignment-overridden dates for a quiz."""
    __tablename__ = 'quiz_assignment_override'
    id = Column(Integer, primary_key=True)
    """ID of the assignment override, unless this is the base construct, in which case the 'id' field is omitted. 
        Example: 1"""
    due_at = Column(DateTime)
    """The date after which any quiz submission is considered late. 
        Example: 2014-02-21T06:59:59Z"""
    unlock_at = Column(DateTime)
    """Date when the quiz becomes available for taking. 
        Example: """
    lock_at = Column(DateTime)
    """When the quiz will stop being available for taking. A value of null means it can always be taken. 
        Example: 2014-02-21T06:59:59Z"""
    title = Column(String)
    """Title of the section this assignment override is for, if any. 
        Example: Project X"""
    base = Column(Boolean)
    """If this property is present, it means that dates in this structure are not based on an assignment override, but are instead for all students. 
        Example: True"""
class QuizAssignmentOverrideSet(Base):
    """Set of assignment-overridden dates for a quiz."""
    __tablename__ = 'quiz_assignment_override_set'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizAssignmentOverrideSet 
        Example: 123456"""
    all_dates = relationship('QuizAssignmentOverride')
    """An array of all assignment overrides active for the quiz. This is visible only to teachers and staff. 
        Example: """
    quiz_id = Column(String)
    """ID of the quiz those dates are for. 
        Example: 1"""
    due_dates = relationship('QuizAssignmentOverride')
    """An array of quiz assignment overrides. For students, this array will always contain a single item which is the set of dates that apply to that student. For teachers and staff, it may contain more. 
        Example: """
class QuizAssignmentOverrideSetContainer(Base):
    """Container for set of assignment-overridden dates for a quiz."""
    __tablename__ = 'quiz_assignment_override_set_container'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizAssignmentOverrideSetContainer 
        Example: 123456"""
    quiz_assignment_overrides = Column(JsonObject)
"""List[QuizAssignmentOverrideSet]"""
    """The QuizAssignmentOverrideSet 
        Example: """
class QuizExtension(Base):
    __tablename__ = 'quiz_extension'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizExtension 
        Example: 123456"""
    user_id = Column(Integer)
    """The ID of the Student that needs the quiz extension. 
        Example: 3"""
    extra_attempts = Column(Integer)
    """Number of times the student is allowed to re-take the quiz over the multiple-attempt limit. 
        Example: 1"""
    extra_time = Column(Integer)
    """Amount of extra time allowed for the quiz submission, in minutes. 
        Example: 60"""
    manually_unlocked = Column(Boolean)
    """The student can take the quiz even if it's locked for everyone else 
        Example: True"""
    end_at = Column(String)
    """The time at which the quiz submission will be overdue, and be flagged as a late submission. 
        Example: 2013-11-07T13:16:18Z"""
    quiz_id = Column(Integer)
    """The ID of the Quiz the quiz extension belongs to. 
        Example: 2"""
class QuizIPFilter(Base):
    __tablename__ = 'quiz_ip_filter'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizIPFilter 
        Example: 123456"""
    name = Column(String)
    """A unique name for the filter. 
        Example: Current Filter"""
    account = Column(String)
    """Name of the Account (or Quiz) the IP filter is defined in. 
        Example: Some Quiz"""
    filter = Column(String)
    """An IP address (or range mask) this filter embodies. 
        Example: 192.168.1.1/24"""
class QuizGroup(Base):
    __tablename__ = 'quiz_group'
    id = Column(Integer, primary_key=True)
    """The ID of the question group. 
        Example: 1"""
    name = Column(String)
    """The name of the question group. 
        Example: Fraction questions"""
    pick_count = Column(Integer)
    """The number of questions to pick from the group to display to the student. 
        Example: 3"""
    question_points = Column(Integer)
    """The amount of points allotted to each question in the group. 
        Example: 10"""
    position = Column(Integer)
    """The order in which the question group will be retrieved and displayed. 
        Example: 1"""
    assessment_question_bank_id = Column(Integer)
    """The ID of the Assessment question bank to pull questions from. 
        Example: 2"""
    quiz_id = Column(Integer)
    """The ID of the Quiz the question group belongs to. 
        Example: 2"""
class Answer(Base):
    __tablename__ = 'answer'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the answer.  Do not supply if this answer is part of a new question 
        Example: 6656"""
    answer_text = Column(String)
    """The text of the answer. 
        Example: Constantinople"""
    answer_weight = Column(Integer)
    """An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should be 100. 
        Example: 100"""
    answer_comments = Column(String)
    """Specific contextual comments for a particular answer. 
        Example: Remember to check your spelling prior to submitting this answer."""
    text_after_answers = Column(String)
    """Used in missing word questions.  The text to follow the missing word 
        Example:  is the capital of Utah."""
    answer_match_left = Column(String)
    """Used in matching questions.  The static value of the answer that will be displayed on the left for students to match for. 
        Example: Salt Lake City"""
    answer_match_right = Column(String)
    """Used in matching questions. The correct match for the value given in answer_match_left.  Will be displayed in a dropdown with the other answer_match_right values.. 
        Example: Utah"""
    matching_answer_incorrect_matches = Column(String)
    """Used in matching questions. A list of distractors, delimited by new lines (
) that will be seeded with all the answer_match_right values. 
        Example: Nevada
California
Washington"""
    numerical_answer_type = Column(String)
    """Used in numerical questions.  Values can be 'exact_answer', 'range_answer', or 'precision_answer'. 
        Example: exact_answer"""
    exact = Column(Integer)
    """Used in numerical questions of type 'exact_answer'.  The value the answer should equal. 
        Example: 42"""
    margin = Column(Integer)
    """Used in numerical questions of type 'exact_answer'. The margin of error allowed for the student's answer. 
        Example: 4"""
    approximate = Column(Integer)
    """Used in numerical questions of type 'precision_answer'.  The value the answer should equal. 
        Example: 1234600000.0"""
    precision = Column(Integer)
    """Used in numerical questions of type 'precision_answer'. The numerical precision that will be used when comparing the student's answer. 
        Example: 4"""
    start = Column(Integer)
    """Used in numerical questions of type 'range_answer'. The start of the allowed range (inclusive). 
        Example: 1"""
    end = Column(Integer)
    """Used in numerical questions of type 'range_answer'. The end of the allowed range (inclusive). 
        Example: 10"""
    blank_id = Column(Integer)
    """Used in fill in multiple blank and multiple dropdowns questions. 
        Example: 1170"""
class QuizQuestion(Base):
    __tablename__ = 'quiz_question'
    id = Column(Integer, primary_key=True)
    """The ID of the quiz question. 
        Example: 1"""
    position = Column(Integer)
    """The order in which the question will be retrieved and displayed. 
        Example: 1"""
    question_name = Column(String)
    """The name of the question. 
        Example: Prime Number Identification"""
    question_type = Column(String)
    """The type of the question. 
        Example: multiple_choice_question"""
    question_text = Column(String)
    """The text of the question. 
        Example: Which of the following is NOT a prime number?"""
    points_possible = Column(Integer)
    """The maximum amount of points possible received for getting this question correct. 
        Example: 5"""
    correct_comments = Column(String)
    """The comments to display if the student answers the question correctly. 
        Example: That's correct!"""
    incorrect_comments = Column(String)
    """The comments to display if the student answers incorrectly. 
        Example: Unfortunately, that IS a prime number."""
    neutral_comments = Column(String)
    """The comments to display regardless of how the student answered. 
        Example: Goldbach's conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers."""
    answers = Column(JsonObject)
"""List[Answer]"""
    """An array of available answers to display to the student. 
        Example: """
    quiz_id = Column(Integer)
    """The ID of the Quiz the question belongs to. 
        Example: 2"""
class QuizReport(Base):
    __tablename__ = 'quiz_report'
    id = Column(Integer, primary_key=True)
    """the ID of the quiz report 
        Example: 5"""
    QuizReportAllowedValues = enum.Enum('QuizReportAllowedValues', ['student_analysis', 'item_analysis'])
    """Enum for the allowed values of the report_type field"""
    report_type = Column(Enum(QuizReportAllowedValues))
    """which type of report this is possible values: 'student_analysis', 'item_analysis' 
        Example: student_analysis"""
    readable_type = Column(String)
    """a human-readable (and localized) version of the report_type 
        Example: Student Analysis"""
    includes_all_versions = Column(Boolean)
    """boolean indicating whether the report represents all submissions or only the most recent ones for each student 
        Example: True"""
    anonymous = Column(Boolean)
    """boolean indicating whether the report is for an anonymous survey. if true, no student names will be included in the csv 
        Example: False"""
    generatable = Column(Boolean)
    """boolean indicating whether the report can be generated, which is true unless the quiz is a survey one 
        Example: True"""
    created_at = Column(DateTime)
    """when the report was created 
        Example: 2013-05-01T12:34:56-07:00"""
    updated_at = Column(DateTime)
    """when the report was last updated 
        Example: 2013-05-01T12:34:56-07:00"""
    url = Column(String)
    """the API endpoint for this report 
        Example: http://canvas.example.com/api/v1/courses/1/quizzes/1/reports/1"""
    progress_url = Column(String)
    """if the report has not yet finished generating, a URL where information about its progress can be retrieved. refer to the Progress API for more information (Note: not available in JSON-API format) 
        Example: """
    quiz_id = Column(Integer)
    """the ID of the quiz 
        Example: 4"""
    progress = relationship('Progress')
    """if the report is being generated, a Progress object that represents the operation. Refer to the Progress API for more information about the format. (Note: available only in JSON-API format) 
        Example: """
    file = relationship('File')
    """if the report has finished generating, a File object that represents it. refer to the Files API for more information about the format 
        Example: """
class QuizStatistics(Base):
    __tablename__ = 'quiz_statistics'
    id = Column(Integer, primary_key=True)
    """The ID of the quiz statistics report. 
        Example: 1"""
    multiple_attempts_exist = Column(Boolean)
    """Whether there are any students that have made mutliple submissions for this quiz. 
        Example: True"""
    includes_all_versions = Column(Boolean)
    """In the presence of multiple attempts, this field describes whether the statistics describe all the submission attempts and not only the latest ones. 
        Example: True"""
    generated_at = Column(DateTime)
    """The time at which the statistics were generated, which is usually after the occurrence of a quiz event, like a student submitting it. 
        Example: 2013-01-23T23:59:00-07:00"""
    url = Column(String)
    """The API HTTP/HTTPS URL to this quiz statistics. 
        Example: http://canvas.example.edu/api/v1/courses/1/quizzes/2/statistics"""
    html_url = Column(String)
    """The HTTP/HTTPS URL to the page where the statistics can be seen visually. 
        Example: http://canvas.example.edu/courses/1/quizzes/2/statistics"""
    submission_statistics = relationship('QuizStatisticsSubmissionStatistics')
    """Question-specific statistics for each question and its answers. 
        Example: """
    quiz_id = Column(Integer)
    """The ID of the Quiz the statistics report is for. 
NOTE: AVAILABLE ONLY IN NON-JSON-API REQUESTS. 
        Example: 2"""
    links = relationship('QuizStatisticsLinks')
    """JSON-API construct that contains links to media related to this quiz statistics object. 
NOTE: AVAILABLE ONLY IN JSON-API REQUESTS. 
        Example: """
    question_statistics = relationship('QuizStatisticsQuestionStatistics')
    """Question-specific statistics for each question and its answers. 
        Example: """
class QuizStatisticsAnswerPointBiserial(Base):
    """A point-biserial construct for a single pre-defined answer in a Multiple-Choice or True/False question."""
    __tablename__ = 'quiz_statistics_answer_point_biserial'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizStatisticsAnswerPointBiserial 
        Example: 123456"""
    point_biserial = Column(Integer)
    """The point biserial value for this answer. Value ranges between -1 and 1. 
        Example: -0.802955068546966"""
    correct = Column(Boolean)
    """Convenience attribute that denotes whether this is the correct answer as opposed to being a distractor. This is mutually exclusive with the `distractor` value 
        Example: True"""
    distractor = Column(Boolean)
    """Convenience attribute that denotes whether this is a distractor answer and not the correct one. This is mutually exclusive with the `correct` value 
        Example: False"""
    answer_id = Column(Integer)
    """ID of the answer the point biserial is for. 
        Example: 3866"""
class QuizStatisticsAnswerStatistics(Base):
    """Statistics for a specific pre-defined answer in a Multiple-Choice or True/False quiz question."""
    __tablename__ = 'quiz_statistics_answer_statistics'
    id = Column(Integer, primary_key=True)
    """ID of the answer. 
        Example: 3866"""
    text = Column(String)
    """The text attached to the answer. 
        Example: Blue."""
    weight = Column(Integer)
    """An integer to determine correctness of the answer. Incorrect answers should be 0, correct answers should 100 
        Example: 100"""
    responses = Column(Integer)
    """Number of students who have chosen this answer. 
        Example: 2"""
class QuizStatisticsLinks(Base):
    """Links to media related to QuizStatistics."""
    __tablename__ = 'quiz_statistics_links'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizStatisticsLinks 
        Example: 123456"""
    quiz = Column(String)
    """HTTP/HTTPS API URL to the quiz this statistics describe. 
        Example: http://canvas.example.edu/api/v1/courses/1/quizzes/2"""
class QuizStatisticsQuestionStatistics(Base):
    """Statistics for submissions made to a specific quiz question."""
    __tablename__ = 'quiz_statistics_question_statistics'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizStatisticsQuestionStatistics 
        Example: 123456"""
    responses = Column(Integer)
    """Number of students who have provided an answer to this question. Blank or empty responses are not counted. 
        Example: 3"""
    answers = relationship('QuizStatisticsAnswerStatistics')
    """Statistics related to each individual pre-defined answer. 
        Example: """
class QuizStatisticsSubmissionStatistics(Base):
    """Generic statistics for all submissions for a quiz."""
    __tablename__ = 'quiz_statistics_submission_statistics'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizStatisticsSubmissionStatistics 
        Example: 123456"""
    unique_count = Column(Integer)
    """The number of students who have taken the quiz. 
        Example: 3"""
    score_average = Column(Integer)
    """The mean of the student submission scores. 
        Example: 4.33333333333333"""
    score_high = Column(Integer)
    """The highest submission score. 
        Example: 6"""
    score_low = Column(Integer)
    """The lowest submission score. 
        Example: 3"""
    score_stdev = Column(Integer)
    """Standard deviation of the submission scores. 
        Example: 1.24721912892465"""
    correct_count_average = Column(Integer)
    """The mean of the number of questions answered correctly by each student. 
        Example: 3.66666666666667"""
    incorrect_count_average = Column(Integer)
    """The mean of the number of questions answered incorrectly by each student. 
        Example: 5"""
    duration_average = Column(Integer)
    """The average time spent by students while taking the quiz. 
        Example: 42.333333333"""
    scores = relationship('Unknown')
    """A percentile distribution of the student scores, each key is the percentile (ranges between 0 and 100%) while the value is the number of students who received that score. 
        Example: {'50': 1, '34': 5, '100': 1}"""
class QuizSubmissionEvent(Base):
    """An event passed from the Quiz Submission take page"""
    __tablename__ = 'quiz_submission_event'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizSubmissionEvent 
        Example: 123456"""
    created_at = Column(DateTime)
    """a timestamp record of creation time 
        Example: 2014-10-08T19:29:58Z"""
    event_type = Column(String)
    """the type of event being sent 
        Example: question_answered"""
    event_data = relationship('Unknown')
    """custom contextual data for the specific event type 
        Example: {'answer': '42'}"""
class QuizSubmissionQuestion(Base):
    __tablename__ = 'quiz_submission_question'
    id = Column(Integer, primary_key=True)
    """The ID of the QuizQuestion this answer is for. 
        Example: 1"""
    flagged = Column(Boolean)
    """Whether this question is flagged. 
        Example: True"""
    answer = Column(String)
    """The provided answer (if any) for this question. The format of this parameter depends on the type of the question, see the Appendix for more information. 
        Example: """
    answers = Column(JsonObject)
"""List[str]"""
    """The possible answers for this question when those possible answers are necessary.  The presence of this parameter is dependent on permissions. 
        Example: """
class JSONAPIPagination(Base):
    __tablename__ = 'jsonapi_pagination'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the JSONAPIPagination 
        Example: 123456"""
class QuizSubmissionUserList(Base):
    __tablename__ = 'quiz_submission_user_list'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizSubmissionUserList 
        Example: 123456"""
class QuizSubmissionUserListMeta(Base):
    __tablename__ = 'quiz_submission_user_list_meta'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizSubmissionUserListMeta 
        Example: 123456"""
class QuizSubmission(Base):
    __tablename__ = 'quiz_submission'
    id = Column(Integer, primary_key=True)
    """The ID of the quiz submission. 
        Example: 1"""
    user_id = Column(Integer)
    """The ID of the Student that made the quiz submission. 
        Example: 3"""
    started_at = Column(String)
    """The time at which the student started the quiz submission. 
        Example: 2013-11-07T13:16:18Z"""
    finished_at = Column(String)
    """The time at which the student submitted the quiz submission. 
        Example: 2013-11-07T13:16:18Z"""
    end_at = Column(String)
    """The time at which the quiz submission will be overdue, and be flagged as a late submission. 
        Example: 2013-11-07T13:16:18Z"""
    attempt = Column(Integer)
    """For quizzes that allow multiple attempts, this field specifies the quiz submission attempt number. 
        Example: 3"""
    extra_attempts = Column(Integer)
    """Number of times the student was allowed to re-take the quiz over the multiple-attempt limit. 
        Example: 1"""
    extra_time = Column(Integer)
    """Amount of extra time allowed for the quiz submission, in minutes. 
        Example: 60"""
    manually_unlocked = Column(Boolean)
    """The student can take the quiz even if it's locked for everyone else 
        Example: True"""
    time_spent = Column(Integer)
    """Amount of time spent, in seconds. 
        Example: 300"""
    score = Column(Integer)
    """The score of the quiz submission, if graded. 
        Example: 3"""
    score_before_regrade = Column(Integer)
    """The original score of the quiz submission prior to any re-grading. 
        Example: 2"""
    kept_score = Column(Integer)
    """For quizzes that allow multiple attempts, this is the score that will be used, which might be the score of the latest, or the highest, quiz submission. 
        Example: 5"""
    fudge_points = Column(Integer)
    """Number of points the quiz submission's score was fudged by. 
        Example: 1"""
    has_seen_results = Column(Boolean)
    """Whether the student has viewed their results to the quiz. 
        Example: True"""
    workflow_state = Column(String)
    """The current state of the quiz submission. Possible values: ['untaken'|'pending_review'|'complete'|'settings_only'|'preview']. 
        Example: untaken"""
    overdue_and_needs_submission = Column(Boolean)
    """Indicates whether the quiz submission is overdue and needs submission 
        Example: false"""
    submission_id = Column(Integer)
    """The ID of the Submission the quiz submission represents. 
        Example: 1"""
    quiz_id = Column(Integer)
    """The ID of the Quiz the quiz submission belongs to. 
        Example: 2"""
class Quiz(Base):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True)
    """the ID of the quiz 
        Example: 5"""
    title = Column(String)
    """the title of the quiz 
        Example: Hamlet Act 3 Quiz"""
    html_url = Column(String)
    """the HTTP/HTTPS URL to the quiz 
        Example: http://canvas.example.edu/courses/1/quizzes/2"""
    mobile_url = Column(String)
    """a url suitable for loading the quiz in a mobile webview.  it will persiste the headless session and, for quizzes in public courses, will force the user to login 
        Example: http://canvas.example.edu/courses/1/quizzes/2?persist_healdess=1&force_user=1"""
    preview_url = Column(String)
    """A url that can be visited in the browser with a POST request to preview a quiz as the teacher. Only present when the user may grade 
        Example: http://canvas.example.edu/courses/1/quizzes/2/take?preview=1"""
    description = Column(String)
    """the description of the quiz 
        Example: This is a quiz on Act 3 of Hamlet"""
    QuizAllowedValues = enum.Enum('QuizAllowedValues', ['practice_quiz', 'assignment', 'graded_survey', 'survey'])
    """Enum for the allowed values of the quiz_type field"""
    quiz_type = Column(Enum(QuizAllowedValues))
    """type of quiz possible values: 'practice_quiz', 'assignment', 'graded_survey', 'survey' 
        Example: assignment"""
    time_limit = Column(Integer)
    """quiz time limit in minutes 
        Example: 5"""
    shuffle_answers = Column(Boolean)
    """shuffle answers for students? 
        Example: False"""
    QuizAllowedValues = enum.Enum('QuizAllowedValues', ['always', 'until_after_last_attempt'])
    """Enum for the allowed values of the hide_results field"""
    hide_results = Column(Enum(QuizAllowedValues))
    """let students see their quiz responses? possible values: null, 'always', 'until_after_last_attempt' 
        Example: always"""
    show_correct_answers = Column(Boolean)
    """show which answers were correct when results are shown? only valid if hide_results=null 
        Example: True"""
    show_correct_answers_last_attempt = Column(Boolean)
    """restrict the show_correct_answers option above to apply only to the last submitted attempt of a quiz that allows multiple attempts. only valid if show_correct_answers=true and allowed_attempts > 1 
        Example: True"""
    show_correct_answers_at = Column(DateTime)
    """when should the correct answers be visible by students? only valid if show_correct_answers=true 
        Example: 2013-01-23T23:59:00-07:00"""
    hide_correct_answers_at = Column(DateTime)
    """prevent the students from seeing correct answers after the specified date has passed. only valid if show_correct_answers=true 
        Example: 2013-01-23T23:59:00-07:00"""
    one_time_results = Column(Boolean)
    """prevent the students from seeing their results more than once (right after they submit the quiz) 
        Example: True"""
    QuizAllowedValues = enum.Enum('QuizAllowedValues', ['keep_highest', 'keep_latest'])
    """Enum for the allowed values of the scoring_policy field"""
    scoring_policy = Column(Enum(QuizAllowedValues))
    """which quiz score to keep (only if allowed_attempts != 1) possible values: 'keep_highest', 'keep_latest' 
        Example: keep_highest"""
    allowed_attempts = Column(Integer)
    """how many times a student can take the quiz -1 = unlimited attempts 
        Example: 3"""
    one_question_at_a_time = Column(Boolean)
    """show one question at a time? 
        Example: False"""
    question_count = Column(Integer)
    """the number of questions in the quiz 
        Example: 12"""
    points_possible = Column(Integer)
    """The total point value given to the quiz 
        Example: 20"""
    cant_go_back = Column(Boolean)
    """lock questions after answering? only valid if one_question_at_a_time=true 
        Example: False"""
    access_code = Column(String)
    """access code to restrict quiz access 
        Example: 2beornot2be"""
    ip_filter = Column(String)
    """IP address or range that quiz access is limited to 
        Example: 123.123.123.123"""
    due_at = Column(DateTime)
    """when the quiz is due 
        Example: 2013-01-23T23:59:00-07:00"""
    lock_at = Column(DateTime)
    """when to lock the quiz 
        Example: """
    unlock_at = Column(DateTime)
    """when to unlock the quiz 
        Example: 2013-01-21T23:59:00-07:00"""
    published = Column(Boolean)
    """whether the quiz has a published or unpublished draft state. 
        Example: True"""
    unpublishable = Column(Boolean)
    """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the quiz. 
        Example: True"""
    locked_for_user = Column(Boolean)
    """Whether or not this is locked for the user. 
        Example: False"""
    lock_explanation = Column(String)
    """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true. 
        Example: This quiz is locked until September 1 at 12:00am"""
    speedgrader_url = Column(String)
    """Link to Speed Grader for this quiz. Will not be present if quiz is unpublished 
        Example: http://canvas.instructure.com/courses/1/speed_grader?assignment_id=1"""
    quiz_extensions_url = Column(String)
    """Link to endpoint to send extensions for this quiz. 
        Example: http://canvas.instructure.com/courses/1/quizzes/2/quiz_extensions"""
    all_dates = Column(JsonObject)
"""List[AssignmentDate]"""
    """list of due dates for the quiz 
        Example: """
    version_number = Column(Integer)
    """Current version number of the quiz 
        Example: 3"""
    question_types = Column(JsonObject)
"""List[str]"""
    """List of question types in the quiz 
        Example: ['multiple_choice', 'essay']"""
    anonymous_submissions = Column(Boolean)
    """Whether survey submissions will be kept anonymous (only applicable to 'graded_survey', 'survey' quiz types) 
        Example: False"""
    assignment_group_id = Column(Integer)
    """the ID of the quiz's assignment group: 
        Example: 3"""
    permissions = relationship('QuizPermissions')
    """Permissions the user has for the quiz 
        Example: """
    lock_info = relationship('LockInfo')
    """(Optional) Information for the user about the lock. Present when locked_for_user is true. 
        Example: """
class QuizPermissions(Base):
    """Permissions the user has for the quiz"""
    __tablename__ = 'quiz_permissions'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the QuizPermissions 
        Example: 123456"""
    read = Column(Boolean)
    """whether the user can view the quiz 
        Example: True"""
    submit = Column(Boolean)
    """whether the user may submit a submission for the quiz 
        Example: True"""
    create = Column(Boolean)
    """whether the user may create a new quiz 
        Example: True"""
    manage = Column(Boolean)
    """whether the user may edit, update, or delete the quiz 
        Example: True"""
    read_statistics = Column(Boolean)
    """whether the user may view quiz statistics for this quiz 
        Example: True"""
    review_grades = Column(Boolean)
    """whether the user may review grades for all quiz submissions for this quiz 
        Example: True"""
    update = Column(Boolean)
    """whether the user may update the quiz 
        Example: True"""
class Result(Base):
    __tablename__ = 'result'
    id = Column(String, primary_key=True)
    """The fully qualified URL for showing the Result 
        Example: http://institution.canvas.com/api/lti/courses/5/line_items/2/results/1"""
    userId = Column(String)
    """The lti_user_id or the Canvas user_id 
        Example: 50 | 'abcasdf'"""
    resultScore = Column(Integer)
    """The score of the result as defined by Canvas, scaled to the resultMaximum 
        Example: 50"""
    resultMaximum = Column(Integer)
    """Maximum possible score for this result; 1 is the default value and will be assumed if not specified otherwise. Minimum value of 0 required. 
        Example: 50"""
    comment = Column(String)
    """Comment visible to the student about the result. 
        Example: """
    scoreOf = Column(String)
    """URL of the line item this belongs to 
        Example: http://institution.canvas.com/api/lti/courses/5/line_items/2"""
class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Role 
        Example: 123456"""
    label = Column(String)
    """The label of the role. 
        Example: New Role"""
    role = Column(String)
    """The label of the role. (Deprecated alias for 'label') 
        Example: New Role"""
    base_role_type = Column(String)
    """The role type that is being used as a base for this role. For account-level roles, this is 'AccountMembership'. For course-level roles, it is an enrollment type. 
        Example: AccountMembership"""
    workflow_state = Column(String)
    """The state of the role: 'active', 'inactive', or 'built_in' 
        Example: active"""
    permissions = Column(JsonObject)
"""Dict[str, RolePermissions]"""
    """A dictionary of permissions keyed by name (see permissions input parameter in the 'Create a role' API). 
        Example: {'read_course_content': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_course_list': {'enabled': True, 'locked': True, 'readonly': True, 'explicit': False}, 'read_question_banks': {'enabled': False, 'locked': True, 'readonly': False, 'explicit': True, 'prior_default': False}, 'read_reports': {'enabled': True, 'locked': False, 'readonly': False, 'explicit': False}}"""
    account = relationship('Account')
    """JSON representation of the account the role is in. 
        Example: {'id': 1019, 'name': 'CGNU', 'parent_account_id': 73, 'root_account_id': 1, 'sis_account_id': 'cgnu'}"""
class RolePermissions(Base):
    __tablename__ = 'role_permissions'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the RolePermissions 
        Example: 123456"""
    enabled = Column(Boolean)
    """Whether the role has the permission 
        Example: True"""
    locked = Column(Boolean)
    """Whether the permission is locked by this role 
        Example: False"""
    applies_to_self = Column(Boolean)
    """Whether the permission applies to the account this role is in. Only present if enabled is true 
        Example: True"""
    applies_to_descendants = Column(Boolean)
    """Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true 
        Example: False"""
    readonly = Column(Boolean)
    """Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role). 
        Example: False"""
    explicit = Column(Boolean)
    """Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role. 
        Example: True"""
    prior_default = Column(Boolean)
    """The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true. 
        Example: False"""
class Rubric(Base):
    __tablename__ = 'rubric'
    id = Column(Integer, primary_key=True)
    """the ID of the rubric 
        Example: 1"""
    title = Column(String)
    """title of the rubric 
        Example: some title"""
    context_type = Column(String)
    """No Description Provided 
        Example: Course"""
    points_possible = Column(Integer)
    """No Description Provided 
        Example: 10.0"""
    reusable = Column(Boolean)
    """No Description Provided 
        Example: false"""
    read_only = Column(Boolean)
    """No Description Provided 
        Example: true"""
    free_form_criterion_comments = Column(Boolean)
    """whether or not free-form comments are used 
        Example: true"""
    hide_score_total = Column(Boolean)
    """No Description Provided 
        Example: true"""
    data = Column(JsonObject)
"""List[RubricCriterion]"""
    """An array with all of this Rubric's grading Criteria 
        Example: """
    assessments = Column(JsonObject)
"""List[RubricAssessment]"""
    """If an assessment type is included in the 'include' parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent. 
        Example: """
    associations = Column(JsonObject)
"""List[RubricAssociation]"""
    """If an association type is included in the 'include' parameter, includes an array of rubric association objects for a given rubric, based on the association type requested. If the user does not request an association type this key will be absent. 
        Example: """
    context_id = Column(Integer)
    """the context owning the rubric 
        Example: 1"""
class RubricAssessment(Base):
    __tablename__ = 'rubric_assessment'
    id = Column(Integer, primary_key=True)
    """the ID of the rubric 
        Example: 1"""
    rubric_association_id = Column(Integer)
    """No Description Provided 
        Example: 2"""
    score = Column(Integer)
    """No Description Provided 
        Example: 5.0"""
    artifact_type = Column(String)
    """the object of the assessment 
        Example: Submission"""
    artifact_attempt = Column(Integer)
    """the current number of attempts made on the object of the assessment 
        Example: 2"""
    assessment_type = Column(String)
    """the type of assessment. values will be either 'grading', 'peer_review', or 'provisional_grade' 
        Example: grading"""
    data = Column(JsonObject)
"""List[Unknown]"""
    """(Optional) If 'full' is included in the 'style' parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent. 
        Example: """
    comments = Column(JsonObject)
"""List[str]"""
    """(Optional) If 'comments_only' is included in the 'style' parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent. 
        Example: """
    artifact_id = Column(Integer)
    """the id of the object of the assessment 
        Example: 3"""
    rubric_id = Column(Integer)
    """the rubric the assessment belongs to 
        Example: 1"""
    assessor_id = Column(Integer)
    """user id of the person who made the assessment 
        Example: 6"""
class RubricAssociation(Base):
    __tablename__ = 'rubric_association'
    id = Column(Integer, primary_key=True)
    """the ID of the association 
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
    """No Description Provided 
        Example: """
    purpose = Column(String)
    """Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context. Values will be grading or bookmark. 
        Example: grading"""
    hide_score_total = Column(Boolean)
    """Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading. 
        Example: true"""
    hide_points = Column(Boolean)
    """No Description Provided 
        Example: true"""
    hide_outcome_results = Column(Boolean)
    """No Description Provided 
        Example: true"""
    rubric_id = Column(Integer)
    """the ID of the rubric 
        Example: 1"""
class RubricCriterion(Base):
    __tablename__ = 'rubric_criterion'
    id = Column(String, primary_key=True)
    """the ID of the criterion 
        Example: _10"""
    description = Column(String)
    """No Description Provided 
        Example: """
    long_description = Column(String)
    """No Description Provided 
        Example: """
    points = Column(Integer)
    """No Description Provided 
        Example: 5"""
    criterion_use_range = Column(Boolean)
    """No Description Provided 
        Example: false"""
    ratings = Column(JsonObject)
"""List[RubricRating]"""
    """the possible ratings for this Criterion 
        Example: """
class RubricRating(Base):
    __tablename__ = 'rubric_rating'
    id = Column(String, primary_key=True)
    """No Description Provided 
        Example: name_2"""
    description = Column(String)
    """No Description Provided 
        Example: """
    long_description = Column(String)
    """No Description Provided 
        Example: """
    points = Column(Integer)
    """No Description Provided 
        Example: 5"""
    criterion_id = Column(String)
    """No Description Provided 
        Example: _10"""
class Score(Base):
    __tablename__ = 'score'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Score 
        Example: 123456"""
    userId = Column(String)
    """The lti_user_id or the Canvas user_id 
        Example: 50 | 'abcasdf'"""
    scoreGiven = Column(Integer)
    """The Current score received in the tool for this line item and user, scaled to the scoreMaximum 
        Example: 50"""
    scoreMaximum = Column(Integer)
    """Maximum possible score for this result; it must be present if scoreGiven is present. 
        Example: 50"""
    comment = Column(String)
    """Comment visible to the student about this score. 
        Example: """
    timestamp = Column(String)
    """Date and time when the score was modified in the tool. Should use subsecond precision. 
        Example: 2017-04-16T18:54:36.736+00:00"""
    activityProgress = Column(String)
    """Indicate to Canvas the status of the user towards the activity's completion. Must be one of Initialized, Started, InProgress, Submitted, Completed 
        Example: Completed"""
    gradingProgress = Column(String)
    """Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded 
        Example: FullyGraded"""
class Section(Base):
    __tablename__ = 'section'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the section. 
        Example: 1"""
    name = Column(String)
    """The name of the section. 
        Example: Section A"""
    integration_id = Column(String)
    """Optional: The integration ID of the section. This field is only included if the user has permission to view SIS information. 
        Example: 3452342345"""
    course_id = Column(Integer)
    """The unique Canvas identifier for the course in which the section belongs 
        Example: 7"""
    start_at = Column(DateTime)
    """the start date for the section, if applicable 
        Example: 2012-06-01T00:00:00-06:00"""
    end_at = Column(DateTime)
    """the end date for the section, if applicable 
        Example: """
    restrict_enrollments_to_section_dates = Column(Boolean)
    """Restrict user enrollments to the start and end dates of the section 
        Example: """
    total_students = Column(Integer)
    """optional: the total number of active and invited students in the section 
        Example: 13"""
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import if created through SIS. This field is only included if the user has permission to manage SIS information. 
        Example: 47"""
    nonxlist_course_id = Column(Integer)
    """The unique identifier of the original course of a cross-listed section 
        Example: """
    sis_course_id = Column(String)
    """The unique SIS identifier for the course in which the section belongs. This field is only included if the user has permission to view SIS information. 
        Example: 7"""
    sis_section_id = Column(String)
    """The sis id of the section. This field is only included if the user has permission to view SIS information. 
        Example: s34643"""
class SharedBrandConfig(Base):
    __tablename__ = 'shared_brand_config'
    id = Column(Integer, primary_key=True)
    """The shared_brand_config identifier. 
        Example: 987"""
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
    account_id = Column(String)
    """The id of the account it should be shared within. 
        Example: """
class SisImportError(Base):
    __tablename__ = 'sis_import_error'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SisImportError 
        Example: 123456"""
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
    sis_import_id = Column(Integer)
    """The unique identifier for the SIS import. 
        Example: 1"""
class SisImport(Base):
    __tablename__ = 'sis_import'
    id = Column(Integer, primary_key=True)
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
    SisImportAllowedValues = enum.Enum('SisImportAllowedValues', ['initializing', 'created', 'importing', 'cleanup_batch', 'imported', 'imported_with_messages', 'aborted', 'failed', 'failed_with_messages', 'restoring', 'partially_restored', 'restored'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(SisImportAllowedValues))
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
    statistics = relationship('SisImportStatistics')
    """statistics 
        Example: """
    progress = Column(String)
    """The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage 
        Example: 100"""
    user = relationship('User')
    """The user that initiated the sis_batch. See the Users API for details. 
        Example: """
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
    csv_attachments = Column(JsonObject)
"""List[List[File]]"""
    """An array of CSV files for processing 
        Example: []"""
    diffed_against_import_id = Column(Integer)
    """The ID of the SIS Import that this import was diffed against 
        Example: 1"""
    batch_mode_term_id = Column(String)
    """The term the batch was limited to. 
        Example: 1234"""
    errors_attachment = relationship('File')
    """The errors_attachment api object of the SIS import. Only available if there are errors or warning and import has completed. 
        Example: """
    data = relationship('SisImportData')
    """data 
        Example: """
class SisImportCounts(Base):
    __tablename__ = 'sis_import_counts'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SisImportCounts 
        Example: 123456"""
    accounts = Column(Integer)
    """No Description Provided 
        Example: 0"""
    terms = Column(Integer)
    """No Description Provided 
        Example: 3"""
    abstract_courses = Column(Integer)
    """No Description Provided 
        Example: 0"""
    courses = Column(Integer)
    """No Description Provided 
        Example: 121"""
    sections = Column(Integer)
    """No Description Provided 
        Example: 278"""
    xlists = Column(Integer)
    """No Description Provided 
        Example: 0"""
    users = Column(Integer)
    """No Description Provided 
        Example: 346"""
    enrollments = Column(Integer)
    """No Description Provided 
        Example: 1542"""
    groups = Column(Integer)
    """No Description Provided 
        Example: 0"""
    group_memberships = Column(Integer)
    """No Description Provided 
        Example: 0"""
    grade_publishing_results = Column(Integer)
    """No Description Provided 
        Example: 0"""
    batch_courses_deleted = Column(Integer)
    """the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted 
        Example: 11"""
    batch_sections_deleted = Column(Integer)
    """the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted 
        Example: 0"""
    batch_enrollments_deleted = Column(Integer)
    """the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted 
        Example: 150"""
    error_count = Column(Integer)
    """No Description Provided 
        Example: 0"""
    warning_count = Column(Integer)
    """No Description Provided 
        Example: 0"""
class SisImportData(Base):
    __tablename__ = 'sis_import_data'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SisImportData 
        Example: 123456"""
    import_type = Column(String)
    """The type of SIS import 
        Example: instructure_csv"""
    supplied_batches = Column(JsonObject)
"""List[str]"""
    """Which files were included in the SIS import 
        Example: ['term', 'course', 'section', 'user', 'enrollment']"""
    counts = relationship('SisImportCounts')
    """The number of rows processed for each type of import 
        Example: """
class SisImportStatistic(Base):
    __tablename__ = 'sis_import_statistic'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SisImportStatistic 
        Example: 123456"""
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
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SisImportStatistics 
        Example: 123456"""
    total_state_changes = Column(Integer)
    """This is the total number of items that were changed in the sis import. There are a few caveats that can cause this number to not add up to the individual counts. There are some state changes that happen that have no impact to the object. An example would be changing a course from 'created' to 'claimed'. Both of these would be considered an active course, but would increment this counter. In this example the course would not increment the created or restored counters for course statistic. 
        Example: 382"""
    EnrollmentTerm = relationship('SisImportStatistic')
    """This contains that statistics for terms. 
        Example: """
    AbstractCourse = relationship('SisImportStatistic')
    """This contains that statistics for abstract courses. 
        Example: """
    CourseSection = relationship('SisImportStatistic')
    """This contains that statistics for course sections. 
        Example: """
    GroupCategory = relationship('SisImportStatistic')
    """This contains that statistics for group categories. 
        Example: """
    GroupMembership = relationship('SisImportStatistic')
    """This contains that statistics for group memberships. This can be a direct impact from the import or indirect from an enrollment being deleted. 
        Example: """
    UserObserver = relationship('SisImportStatistic')
    """This contains that statistics for user observers. 
        Example: """
    Account = relationship('SisImportStatistic')
    """This contains that statistics for accounts. 
        Example: """
    Course = relationship('SisImportStatistic')
    """This contains that statistics for courses. 
        Example: """
    Group = relationship('SisImportStatistic')
    """This contains that statistics for groups. 
        Example: """
    AccountUser = relationship('SisImportStatistic')
    """This contains that statistics for account users. 
        Example: """
    Enrollment = relationship('SisImportStatistic')
    """This contains that statistics for enrollments. 
        Example: """
    CommunicationChannel = relationship('SisImportStatistic')
    """This contains that statistics for communication channels. This is an indirect effect from creating or deleting a user. 
        Example: """
    Pseudonym = relationship('SisImportStatistic')
    """This contains that statistics for pseudonyms. Pseudonyms are logins for users, and are the object that ties an enrollment to a user. This would be impacted from the user importer.  
        Example: """
class AssignmentGroupAttributes(Base):
    """Some of the attributes of an Assignment Group. See Assignments API for more details"""
    __tablename__ = 'assignment_group_attributes'
    id = Column(Integer, primary_key=True)
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
class CourseAttributes(Base):
    """Attributes of a course object.  See Courses API for more details"""
    __tablename__ = 'course_attributes'
    id = Column(Integer, primary_key=True)
    """The unique Canvas identifier for the origin course 
        Example: 7"""
    name = Column(String)
    """The name of the origin course. 
        Example: Section A"""
    integration_id = Column(String)
    """The integration ID of the origin_course. 
        Example: I-2"""
    sis_id = Column(String)
    """The sis id of the origin_course. 
        Example: c34643"""
class SectionAssignmentOverrideAttributes(Base):
    """Attributes of an assignment override that apply to the section object.  See Assignments API for more details"""
    __tablename__ = 'section_assignment_override_attributes'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the SectionAssignmentOverrideAttributes 
        Example: 123456"""
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
class SectionAttributes(Base):
    """Some of the attributes of a section. For more details see Sections API."""
    __tablename__ = 'section_attributes'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the section. 
        Example: 1"""
    name = Column(String)
    """The name of the section. 
        Example: Section A"""
    integration_id = Column(String)
    """Optional: The integration ID of the section. 
        Example: 3452342345"""
    xlist_course = relationship('CourseAttributes')
    """Optional: Attributes of the xlist course. Only present when the section has been cross-listed. See Courses API for more details 
        Example: """
    sis_id = Column(String)
    """The sis id of the section. 
        Example: s34643"""
    override = relationship('SectionAssignmentOverrideAttributes')
    """Optional: Attributes of the assignment override that apply to the section. See Assignment API for more details 
        Example: """
    origin_course = relationship('CourseAttributes')
    """The course to which the section belongs or the course from which the section was cross-listed 
        Example: """
class SisAssignment(Base):
    """Assignments that have post_to_sis enabled with other objects for convenience"""
    __tablename__ = 'sis_assignment'
    id = Column(Integer, primary_key=True)
    """The unique identifier for the assignment. 
        Example: 4"""
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
    SisAssignmentAllowedValues = enum.Enum('SisAssignmentAllowedValues', ['discussion_topic', 'online_quiz', 'on_paper', 'not_graded', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_types field"""
    submission_types = Column(Enum(SisAssignmentAllowedValues))
    """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation' 
        Example: ['online_text_entry']"""
    integration_data = Column(String)
    """(optional, Third Party integration data for assignment) 
        Example: other_data"""
    include_in_final_grade = Column(Boolean)
    """If false, the assignment will be omitted from the student's final grade 
        Example: True"""
    assignment_group = Column(JsonObject)
"""List[AssignmentGroupAttributes]"""
    """Includes attributes of a assignment_group for convenience. For more details see Assignments API. 
        Example: """
    sections = Column(JsonObject)
"""List[SectionAttributes]"""
    """Includes attributes of a section for convenience. For more details see Sections API. 
        Example: """
    user_overrides = Column(JsonObject)
"""List[UserAssignmentOverrideAttributes]"""
    """Includes attributes of a user assignment overrides. For more details see Assignments API. 
        Example: """
    integration_id = Column(String)
    """Third Party integration id for assignment 
        Example: 12341234"""
    course_id = Column(Integer)
    """The unique identifier for the course. 
        Example: 6"""
class StudentAttributes(Base):
    """Attributes of student.  See Users API for more details"""
    __tablename__ = 'student_attributes'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the StudentAttributes 
        Example: 123456"""
    sis_user_id = Column(String)
    """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: SHEL93921"""
    user_id = Column(Integer)
    """The unique Canvas identifier for the user 
        Example: 511"""
class UserAssignmentOverrideAttributes(Base):
    """Attributes of assignment overrides that apply to users.  See Assignments API for more details"""
    __tablename__ = 'user_assignment_override_attributes'
    id = Column(Integer, primary_key=True)
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
        Example: """
class MediaComment(Base):
    __tablename__ = 'media_comment'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the MediaComment 
        Example: 123456"""
    content-type = Column(String)
    """No Description Provided 
        Example: audio/mp4"""
    display_name = Column(String)
    """No Description Provided 
        Example: something"""
    media_type = Column(String)
    """No Description Provided 
        Example: audio"""
    url = Column(String)
    """No Description Provided 
        Example: http://example.com/media_url"""
    media_id = Column(String)
    """No Description Provided 
        Example: 3232"""
class Submission(Base):
    __tablename__ = 'submission'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the Submission 
        Example: 123456"""
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
        Example: """
    SubmissionAllowedValues = enum.Enum('SubmissionAllowedValues', ['online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'])
    """Enum for the allowed values of the submission_type field"""
    submission_type = Column(Enum(SubmissionAllowedValues))
    """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation') 
        Example: online_text_entry"""
    submitted_at = Column(DateTime)
    """The timestamp when the assignment was submitted 
        Example: 2012-01-01T01:00:00Z"""
    url = Column(String)
    """The URL of the submission (for 'online_url' submissions). 
        Example: """
    grader_id = Column(Integer)
    """The id of the user who graded the submission. This will be null for submissions that haven't been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools).  Specifically autograded quizzes set grader_id to the negative of the quiz id.  Submissions autograded by LTI tools set grader_id to the negative of the tool id. 
        Example: 86"""
    graded_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-01-02T03:05:34Z"""
    late = Column(Boolean)
    """Whether the submission was made after the applicable due date 
        Example: False"""
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
    SubmissionAllowedValues = enum.Enum('SubmissionAllowedValues', ['graded', 'submitted', 'unsubmitted', 'pending_review'])
    """Enum for the allowed values of the workflow_state field"""
    workflow_state = Column(Enum(SubmissionAllowedValues))
    """The current state of the submission 
        Example: submitted"""
    extra_attempts = Column(Integer)
    """Extra submission attempts allowed for the given user and assignment. 
        Example: 10"""
    posted_at = Column(DateTime)
    """The date this submission was posted to the student, or nil if it has not been posted. 
        Example: 2020-01-02T11:10:30Z"""
    SubmissionAllowedValues = enum.Enum('SubmissionAllowedValues', ['read', 'unread'])
    """Enum for the allowed values of the read_status field"""
    read_status = Column(Enum(SubmissionAllowedValues))
    """The read status of this submission for the given user (optional). Including read_status will mark submission(s) as read. 
        Example: read"""
    redo_request = Column(Boolean)
    """This indicates whether the submission has been reassigned by the instructor. 
        Example: true"""
    user_id = Column(Integer)
    """The id of the user who created the submission 
        Example: 134"""
    assignment_id = Column(Integer)
    """The submission's assignment id 
        Example: 23"""
    anonymous_id = Column(String)
    """A unique short ID identifying this submission without reference to the owning user. Only included if the caller has administrator access for the current account. 
        Example: acJ4Q"""
    user = relationship('User')
    """The submissions user (see user API) (optional) 
        Example: """
    course = relationship('Course')
    """The submission's course (see the course API) (optional) 
        Example: """
    assignment = relationship('Assignment')
    """The submission's assignment (see the assignments API) (optional) 
        Example: """
class SubmissionComment(Base):
    __tablename__ = 'submission_comment'
    id = Column(Integer, primary_key=True)
    """No Description Provided 
        Example: 37"""
    author_name = Column(String)
    """No Description Provided 
        Example: Toph Beifong"""
    comment = Column(String)
    """No Description Provided 
        Example: Well here's the thing..."""
    created_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-01-01T01:00:00Z"""
    edited_at = Column(DateTime)
    """No Description Provided 
        Example: 2012-01-02T01:00:00Z"""
    author_id = Column(Integer)
    """No Description Provided 
        Example: 134"""
    author = Column(String)
    """Abbreviated user object UserDisplay (see users API). 
        Example: {}"""
    media_comment = relationship('MediaComment')
    """No Description Provided 
        Example: """
class Tab(Base):
    __tablename__ = 'tab'
    id = Column(String, primary_key=True)
    """No Description Provided 
        Example: context_external_tool_4"""
    html_url = Column(String)
    """No Description Provided 
        Example: /courses/1/external_tools/4"""
    label = Column(String)
    """No Description Provided 
        Example: WordPress"""
    type = Column(String)
    """No Description Provided 
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
class PairingCode(Base):
    """A code used for linking a user to a student to observe them."""
    __tablename__ = 'pairing_code'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the PairingCode 
        Example: 123456"""
    code = Column(String)
    """The actual code to be sent to other APIs 
        Example: abc123"""
    expires_at = Column(String)
    """When the code expires 
        Example: 2012-05-30T17:45:25Z"""
    workflow_state = Column(String)
    """The current status of the code 
        Example: active"""
    user_id = Column(Integer)
    """The ID of the user. 
        Example: 2"""
class AnonymousUserDisplay(Base):
    """This mini-object is returned in place of UserDisplay when returning student data for anonymous assignments, and includes an anonymous ID to identify a user within the scope of a single assignment."""
    __tablename__ = 'anonymous_user_display'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the AnonymousUserDisplay 
        Example: 123456"""
    avatar_image_url = Column(String)
    """A URL to retrieve a generic avatar. 
        Example: https://en.gravatar.com/avatar/d8cb8c8cd40ddf0cd05241443a591868?s=80&r=g"""
    display_name = Column(String)
    """The anonymized display name for the student. 
        Example: Student 2"""
    anonymous_id = Column(String)
    """A unique short ID identifying this user within the scope of a particular assignment. 
        Example: xn29Q"""
class Avatar(Base):
    """Possible avatar for a user."""
    __tablename__ = 'avatar'
    id = Column(Integer, primary_key=True)
    """['attachment' type only] the internal id of the attachment 
        Example: 12"""
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
    content-type = Column(String)
    """['attachment' type only] the content-type of the attachment. 
        Example: image/jpeg"""
    filename = Column(String)
    """['attachment' type only] the filename of the attachment 
        Example: profile.jpg"""
    size = Column(Integer)
    """['attachment' type only] the size of the attachment 
        Example: 32649"""
class CourseNickname(Base):
    __tablename__ = 'course_nickname'
    id = Column(Integer, primary_key=True)
    """The unique identifier of the CourseNickname 
        Example: 123456"""
    name = Column(String)
    """the actual name of the course 
        Example: S1048576 DPMS1200 Intro to Newtonian Mechanics"""
    nickname = Column(String)
    """the calling user's nickname for the course 
        Example: Physics"""
    course_id = Column(Integer)
    """the ID of the course 
        Example: 88"""
class PageView(Base):
    """The record of a user page view access in Canvas"""
    __tablename__ = 'page_view'
    id = Column(String, primary_key=True)
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
    id = Column(Integer, primary_key=True)
    """The unique identifier of the PageViewLinks 
        Example: 123456"""
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
class Profile(Base):
    """Profile details for a Canvas user."""
    __tablename__ = 'profile'
    id = Column(Integer, primary_key=True)
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
    """No Description Provided 
        Example: """
    bio = Column(String)
    """No Description Provided 
        Example: """
    primary_email = Column(String)
    """sample_user@example.com 
        Example: sample_user@example.com"""
    sis_user_id = Column(String)
    """sis1 
        Example: sis1"""
    avatar_url = Column(String)
    """The avatar_url can change over time, so we recommend not caching it for more than a few hours 
        Example: ..url.."""
    time_zone = Column(String)
    """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone. 
        Example: America/Denver"""
    locale = Column(String)
    """The users locale. 
        Example: """
    k5_user = Column(Boolean)
    """Optional: Whether or not the user is a K5 user. This field is nil if the user settings are not for the user making the request. 
        Example: True"""
    lti_user_id = Column(String)
    """No Description Provided 
        Example: """
    login_id = Column(String)
    """sample_user@example.com 
        Example: sample_user@example.com"""
    calendar = relationship('CalendarLink')
    """No Description Provided 
        Example: """
class User(Base):
    """A Canvas user, e.g. a student, teacher, administrator, observer, etc."""
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
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
    sis_import_id = Column(Integer)
    """The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information. 
        Example: 18"""
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
        Example: """
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
    integration_id = Column(String)
    """The integration_id associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: ABC59802"""
    sis_user_id = Column(String)
    """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information. 
        Example: SHEL93921"""
class UserDisplay(Base):
    """This mini-object is used for secondary user responses, when we just want to provide enough information to display a user."""
    __tablename__ = 'user_display'
    id = Column(Integer, primary_key=True)
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
