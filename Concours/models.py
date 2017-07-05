from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.


class ConcourDepartement(models.Model):
    departement = models.CharField(max_length=100)

    def __str__(self):
        return self.departement


class ConcourTeacher(models.Model):
    def teacher_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Image/Teacher/Picture/id_<id>/<filename>
        return 'Image/Teacher/Picture/id_{0}/{1}'.format(instance.id, filename)

    teachername = models.CharField(max_length=100)
    teacheremail = models.CharField(max_length=100)
    teachercontact = models.CharField(max_length=100)
    teacherpic = models.ImageField(upload_to=teacher_directory_path)
    teacherbiography = models.TextField()

    def __str__(self):
        return self.teachername


class Concour(models.Model):
    def concour_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Image/Concour/Logo/id_<id>/<filename>
        return 'Image/Concour/Logo/id_{0}/{1}'.format(instance.id, filename)

    departement = models.ForeignKey(ConcourDepartement)
    schoolname = models.CharField(max_length=100)
    schoollogo = models.ImageField(upload_to=concour_directory_path)
    schooldescription = models.TextField()

    def __str__(self):
        return self.schoolname


class ConcourCourse(models.Model):
    def course_logo_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Image/Course/Logo/id_<id>/<filename>
        return 'Image/Course/Logo/id_{0}/{1}'.format(instance.id, filename)

    def course_videintro_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Video/Course/Intro/id_<id>/<filename>
        return 'Video/Course/Intro/id_{0}/{1}'.format(instance.id, filename)

    def course_videoposter_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Image/Course/Video_Poster/id_<id>/<filename>
        return 'Image/Course/Video_Poster/id_{0}/{1}'.format(instance.id, filename)

    departement = models.ForeignKey(ConcourDepartement)
    coursename = models.CharField(max_length=100)
    courselogo = models.ImageField(upload_to=course_logo_directory_path)
    courseintrovideo = models.FileField(upload_to=course_videintro_directory_path, null=True)
    coursevideoposter = models.FileField(upload_to=course_videoposter_directory_path, null=True, blank=True)
    courseintro = models.TextField()
    coursestart = models.DateField(null=True)
    courseend = models.DateField(null=True)
    ratings = GenericRelation(Rating, related_query_name='Concourcourse')

    def __str__(self):
        return self.coursename


class ConcourToCourseMap(models.Model):
    schoolname = models.ForeignKey(Concour)
    coursename = models.ForeignKey(ConcourCourse)


class MoMoTransactions(models.Model):  # note that this doesnot contain the model StudentSubscribedConcourcourse as a foreign key because it can be a transaction can occur without a successful subscribtion
    username = models.ForeignKey(User, )  # contains user
    coursename = models.ForeignKey(ConcourToCourseMap)  # contains usnique course
    phoneNumber = models.IntegerField()
    amount = models.IntegerField()
    transactionId = models.IntegerField()  # momo transaction id
    statusCode = models.IntegerField()  # status of momo transaction
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.transactionId

    class Meta:
        ordering = ["-timecreated"]


class StudentSubscribedConcourcourse(models.Model):
    course = models.ForeignKey(ConcourCourse)  # contains the id of the course
    student = models.ForeignKey(User)  # contains the id of the student
    level = models.ForeignKey(ConcourDepartement)
    concour = models.ForeignKey(Concour)
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True, null=True, blank=True)

    def __int__(self):
        return self.course

    class Meta:
        ordering = ["-timecreated"]


class ConcourChapter(models.Model):
    course = models.ForeignKey(ConcourCourse)
    teacher = models.ForeignKey(ConcourTeacher, null=True, blank=True)  # contains teachers id
    chapternumber = models.IntegerField()
    chaptertitle = models.CharField(max_length=100)

    def __str__(self):
        return self.chaptertitle


class ConcourTopic(models.Model):
    def topic_video_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Video/Course/Topic/id_<id>/<filename>
        return 'Video/Course/Topic/id_{0}/{1}'.format(instance.id, filename)

    def topic_document_directory_path(instance, filename):  # function to define uploaded file path
        # file will be uploaded to MEDIA_ROOT/Document/Course/Topic/id_<id>/<filename>
        return 'Document/Course/Topic/id_{0}/{1}'.format(instance.id, filename)

    chapter = models.ForeignKey(ConcourChapter)  # change this to chapter
    topicnumber = models.IntegerField()
    topicname = models.CharField(max_length=100)
    topicintro = models.TextField(null=True, blank=True)
    topicvideo = models.FileField(upload_to=topic_video_directory_path, null=True, blank=True)
    topicdocument = models.FileField(upload_to=topic_document_directory_path, null=True, blank=True)
    #ratings = GenericRelation(Rating, related_query_name='ConcourTopic')

    def __str__(self):
        return self.topicname


class ConcourForum(models.Model):
    user = models.ForeignKey(User)  # contains user id
    course = models.ForeignKey(ConcourCourse)  # contains course id
    chapter = models.ForeignKey(ConcourChapter)  # contains chapter id
    topic = models.ForeignKey(ConcourTopic)  # contains topic id
    comment = models.CharField(max_length=500)  # comment on forum
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True)
    ratings = GenericRelation(Rating, related_query_name='Concourforum')

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-timecreated"]


class ConcourReplyComment(models.Model):
    user = models.ForeignKey(User)  # contains user who commented
    comment = models.ForeignKey(ConcourForum)  # contains comment he replied on
    comment_reply = models.TextField()  # reply to comment
    replystate = models.BooleanField(default=False)  # determine if the reply has been seen by user who wrote comment
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.comment_reply

    class Meta:
        ordering = ["-timecreated"]


class ConcourUserForum(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(ConcourCourse)
    comment_title = models.CharField(max_length=100)
    comment = models.TextField()
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    ratings = GenericRelation(Rating, related_query_name='userforum')

    def __str__(self):
        return self.comment_title

    class Meta:
        ordering = ["-timecreated"]


class ConcourUserForumReply(models.Model):
    user = models.ForeignKey(User)  # contains user who commented
    usercomment = models.ForeignKey(ConcourUserForum)  # contains comment he replied on
    usercomment_reply = models.TextField()  # reply to comment
    replystate = models.BooleanField(default=False)  # determine if the reply has been seen by user who wrote comment
    timecreated = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __str__(self):
        return self.usercomment_reply

    class Meta:
        ordering = ["-timecreated"]


class ConcourMCQQuestion(models.Model):
    chapter = models.ForeignKey(ConcourChapter)
    question = models.TextField()
    question_marks = models.IntegerField()

    def __str__(self):
        return self.question


class ConcourMCQAnswer(models.Model):
    question = models.ForeignKey(ConcourMCQQuestion)
    answer = models.CharField(max_length=999)
    correctanswer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class ConcourMCQScore(models.Model):
    chapter = models.ForeignKey(ConcourChapter)
    user = models.ForeignKey(User)
    user_score = models.IntegerField()

    def __str__(self):
        return self.user.username

