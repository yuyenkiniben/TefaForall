from django.contrib import admin
from Concours.models import ConcourDepartement, ConcourChapter, ConcourCourse, ConcourTeacher, ConcourTopic, StudentSubscribedConcourcourse, Concour, ConcourToCourseMap
from Concours.models import ConcourForum, ConcourReplyComment, ConcourMCQQuestion, ConcourMCQAnswer, ConcourMCQScore, ConcourUserForum, ConcourUserForumReply, MoMoTransactions

# Register your models here.


class StudentSubscribedcourseAdmin(admin.ModelAdmin):
    list_display = ["id", "student", "course", "concour"]
    list_filter = ["id", "student", "course"]
    list_display_links = ["student"]
    search_fields = ["student"]  # this will make the title and content searchable

    class Meta:
        model = StudentSubscribedConcourcourse


class MoMoTransactionsAdmin(admin.ModelAdmin):
    list_display = ["id", "coursename", "transactionId", "phoneNumber", "statusCode", "timecreated", "amount"]
    list_filter = ["id", "transactionId", "coursename"]
    list_display_links = ["transactionId"]
    search_fields = ["transactionId", "coursename"]  # this will make the title and content searchable

    class Meta:
        model = MoMoTransactions


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "departement"]
    list_filter = ["id"]
    list_display_links = ["departement"]
    search_fields = ["departement"]  # this will make the title and content searchable

    class Meta:
        model = ConcourDepartement


class ConcourAdmin(admin.ModelAdmin):
    list_display = ["id", "schoolname", "departement", "schoollogo", "schooldescription"]
    list_filter = ["schoolname"]
    list_display_links = ["schoolname"]
    search_fields = ["schoolname", "departement"]  # this will make the title and content searchable

    class Meta:
        model = Concour


class ConcourToCourseAdmin(admin.ModelAdmin):
    list_display = ["id", "schoolname", "coursename"]
    list_filter = ["schoolname"]
    list_display_links = ["schoolname"]
    search_fields = ["schoolname", "coursename"]  # this will make the title and content searchable

    class Meta:
        model = ConcourToCourseMap


class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "coursename", "courselogo", "departement", "courseintrovideo", "coursevideoposter", "courseintro"]
    list_filter = ["coursename"]
    list_display_links = ["coursename"]
    search_fields = ["coursename", "departement"]  # this will make the title and content searchable
    ordering = ["-ratings"]

    class Meta:
        model = ConcourCourse


class ChapterAdmin(admin.ModelAdmin):
    list_display = ["id", "course", "teacher", "chapternumber", "chaptertitle"]
    list_filter = ["course", "chapternumber"]
    list_display_links = ["course"]
    search_fields = ["course", "chaptertitle"]  # this will make the title and content searchable

    class Meta:
        model = ConcourChapter


class TopicAdmin(admin.ModelAdmin):
    list_display = ["id", "chapter", "topicnumber", "topicname", "topicvideo", "topicdocument", "topicintro"]
    list_filter = ["chapter", "topicname"]
    list_display_links = ["topicname"]
    search_fields = ["topicname", "chapter"]  # this will make the title and content searchable

    class Meta:
        model = ConcourTopic


class TeacherAdmin(admin.ModelAdmin):
    list_display = ["id", "teachername", "teacheremail", "teacherpic", "teachercontact", "teacherbiography"]
    list_filter = ["teachername", "teacheremail"]
    list_display_links = ["teachername"]
    search_fields = ["teacheremail", "teachername"]  # this will make the title and content searchable

    class Meta:
        model = ConcourTeacher


class ForumAdmin(admin.ModelAdmin):
    list_display = ["id", "comment", "timecreated"]  # how the table in database will be displayed
    search_fields = ["comment"]  # items through which we will search the database
    list_display_links = ["comment"]
    list_filter = ["id"]
    ordering = ["-ratings"]

    class Meta:
        model = ConcourForum


class ReplycommentAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "comment", "comment_reply", "replystate", "timecreated"]
    list_filter = ["id", "comment_reply", "replystate"]
    list_display_links = ["user"]
    search_fields = ["user"]  # this will make the title and content searchable

    class Meta:
        model = ConcourReplyComment


class MCQuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "chapter", "question", "question_marks"]
    list_filter = ["id", "chapter", ]
    list_display_links = ["question"]
    search_fields = ["chapter", "question"]  # this will make the title and content searchable

    class Meta:
        model = ConcourMCQQuestion


class MCQ_AnswersAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "answer", "correctanswer"]
    list_filter = ["id", "question"]
    list_display_links = ["question"]
    search_fields = ["question", "correctanswer"]  # this will make the title and content searchable

    class Meta:
        model = ConcourMCQAnswer


class MCQ_ScoreAdmin(admin.ModelAdmin):
    list_display = ["id", "chapter", "user", "user_score"]
    list_filter = ["id", "chapter", "user_score"]
    list_display_links = ["user"]
    search_fields = ["user", "user_score"]  # this will make the title and content searchable

    class Meta:
        model = ConcourMCQScore


class UserForumAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "comment_title", "comment", "timecreated", "course"]
    list_filter = ["id", "user", "timecreated"]
    list_display_links = ["comment_title"]
    search_fields = ["comment_title", "user"]  # this will make the title and content searchable
    ordering = ["-ratings"]

    class Meta:
        model = ConcourUserForum


class UserForumReplyAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "usercomment", "usercomment_reply", "timecreated", "replystate"]
    list_filter = ["id", "user", "timecreated"]
    list_display_links = ["usercomment"]
    search_fields = ["usercomment", "user"]  # this will make the title and content searchable

    class Meta:
        model = ConcourUserForumReply


admin.site.register(Concour, ConcourAdmin)
admin.site.register(ConcourToCourseMap, ConcourToCourseAdmin)
admin.site.register(ConcourForum, ForumAdmin)
admin.site.register(ConcourUserForum, UserForumAdmin)
admin.site.register(ConcourUserForumReply, UserForumReplyAdmin)
admin.site.register(ConcourReplyComment, ReplycommentAdmin)
admin.site.register(ConcourTeacher, TeacherAdmin)
admin.site.register(ConcourTopic, TopicAdmin)
admin.site.register(ConcourChapter, ChapterAdmin)
admin.site.register(ConcourDepartement, DepartmentAdmin)
admin.site.register(ConcourCourse, CourseAdmin)
admin.site.register(StudentSubscribedConcourcourse, StudentSubscribedcourseAdmin)
admin.site.register(ConcourMCQScore, MCQ_ScoreAdmin)
admin.site.register(ConcourMCQQuestion, MCQuestionAdmin)
admin.site.register(ConcourMCQAnswer, MCQ_AnswersAdmin)
admin.site.register(MoMoTransactions, MoMoTransactionsAdmin)
