from django.conf.urls import url
from Concours.views import All_Courses, Arts_Courses, Commercial_Courses, Science_Courses, Selected_Arts_Course, Selected_Commercial_Course, Selected_Science_Course, ReplyusercreatedComment, UserCreateComment, UserPersonalForum, UserSearch_Forum, EngineerConcour, MedicalConcour, ScienceConcour, ArtsConcour, AllConcours
from Concours.views import Subscribe, CourseVideos, Forum, Forum_CreateComment, Reply_ForumComment, ConfirmationEmail, Quiz, Quiz_Correction, Medical_Courses, Selected_Medical_Course, Engineering_Courses, Selected_Engineering_Course

app_name = "Concours"

urlpatterns = [
    url(r'^All_Concours/$', AllConcours, name="allconcours"),
    url(r'^Arts_Concour/$', ArtsConcour, name="artsconcours"),
    url(r'^Science_Concour/$', ScienceConcour, name="scienceconcours"),
    url(r'^Engineering_Concour/$', EngineerConcour, name="engineeringconcours"),
    url(r'^Medical_Concour/$', MedicalConcour, name="medicalconcours"),
    url(r'^All_Courses/$', All_Courses, name="allcourses"),
    url(r'^Arts_Courses/(?P<school_id>\d+)/$', Arts_Courses, name="artscourses"),
    url(r'^Science_Courses/(?P<school_id>\d+)/$', Science_Courses, name="sciencecourses"),
    url(r'^Commercial_Courses/(?P<school_id>\d+)/$', Commercial_Courses, name="commercialcourses"),
    url(r'^Engineering_Courses/(?P<school_id>\d+)/$', Engineering_Courses, name="engineeringcourses"),
    url(r'^Medical_Courses/(?P<school_id>\d+)/$', Medical_Courses, name="medicalcourses"),
    url(r'^Arts_Course/(?P<user_id>\d+)/(?P<school_id>\d+)/(?P<course_id>\d+)/$', Selected_Arts_Course, name="selectedartscourse"),
    url(r'^Science_Course/(?P<user_id>\d+)/(?P<school_id>\d+)/(?P<course_id>\d+)/$', Selected_Science_Course, name="selectedsciencecourse"),
    url(r'^Commercial_Course/(?P<user_id>\d+)/(?P<school_id>\d+)/(?P<course_id>\d+)/$', Selected_Commercial_Course, name="selectedcommercialcourse"),
    url(r'^Engineering_Course/(?P<user_id>\d+)/(?P<school_id>\d+)/(?P<course_id>\d+)/$', Selected_Engineering_Course, name="selectedengineeringcourse"),
    url(r'^Medical_Course/(?P<user_id>\d+)/(?P<school_id>\d+)/(?P<course_id>\d+)/$', Selected_Medical_Course, name="selectedmedicalcourse"),
    url(r'^Subscribe/Course/(?P<course_id>\d+)/(?P<user_id>\d+)/(?P<school_id>\d+)/$', Subscribe, name="subscribe"),
    url(r'^Course/(?P<course_id>\d+)/(?P<chapter_id>\d+)/(?P<topic_id>\d+)/$', CourseVideos, name="coursevideos"),
    url(r'^Course/Forum/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<chapter_id>\d+)/(?P<topic_id>\d+)/$', Forum, name="forum"),
    url(r'^Course/Forum/Add/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<chapter_id>\d+)/(?P<topic_id>\d+)/$', Forum_CreateComment, name="addcomment"),
    url(r'^Course/Forum/Add/Reply/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<chapter_id>\d+)/(?P<topic_id>\d+)/(?P<comment_id>\d+)/$', Reply_ForumComment, name="replycomment"),
    url(r'^Course/Forum/User/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<Usercomment_id>\d+)/$', UserPersonalForum, name="userforum"),
    url(r'^Course/Forum/User/Add/(?P<user_id>\d+)/(?P<course_id>\d+)/$', UserCreateComment, name="useraddcomment"),
    url(r'^Course/Forum/User/Add/Reply/(?P<user_id>\d+)/(?P<Usercomment_id>\d+)/$', ReplyusercreatedComment, name="userreplycomment"),
    url(r'^Course/Forum/Search/User/(?P<course_id>\d+)/$', UserSearch_Forum, name="usersearchforum"),
    url(r'^Course/Quiz/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<chapter_id>\d+)/$', Quiz, name="quiz"),
    url(r'^Course/Quiz/Results/(?P<user_id>\d+)/(?P<course_id>\d+)/(?P<chapter_id>\d+)/$', Quiz_Correction, name="quizcorrection"),
]
