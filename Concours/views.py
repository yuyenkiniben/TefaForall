from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from Concours.models import ConcourChapter, ConcourCourse, ConcourTopic, StudentSubscribedConcourcourse, ConcourForum, ConcourReplyComment, ConcourMCQQuestion, ConcourMCQAnswer, ConcourMCQScore, ConcourUserForum, ConcourUserForumReply, ConcourToCourseMap, Concour, MoMoTransactions
from Concours.forms import ConcourForumForm, SubscribeForm, ConcourReplyCommentForm, ConcourUserForumForm, ConcourUserForumReplyForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.db.models import Q
import urllib.parse
import requests

# Create your views here.


def AllConcours(request):
    allarts = Concour.objects.filter(departement=1)  # where department = it id corresponding to arts
    allscience = Concour.objects.filter(departement=2)  # where department = it id corresponding to science
    allcommercial = Concour.objects.filter(departement=3)  # where department = it id corresponding to commercial
    allengineer = Concour.objects.filter(departement=4)  # where department = it id corresponding to Engineering
    allmedical = Concour.objects.filter(departement=5)  # where department = it id corresponding to Medical

    context = {
        "allarts": allarts,
        "allscience": allscience,
        "allcommercial": allcommercial,
        "allengineer": allengineer,
        "allmedical": allmedical,
    }
    return render(request, "Concours/Allcourses/index.html", context)


def EngineerConcour(request):
    allenginering_concours = Concour.objects.filter(departement=4)
    paginator = Paginator(allenginering_concours, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allenginering = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allenginering = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allenginering = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage

    return render(request, "Concours/Engineering/index.html", {"allengineering": allenginering})


def MedicalConcour(request):
    allmedical_concours = Concour.objects.filter(departement=5)
    paginator = Paginator(allmedical_concours, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allmedical = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allmedical = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allmedical = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage

    return render(request, "Concours/Medical/index.html", {"allmedical": allmedical})


def ScienceConcour(request):
    allscience_concours = Concour.objects.filter(departement=2)
    paginator = Paginator(allscience_concours, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allscience = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allscience = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allscience = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage

    return render(request, "Concours/Sciencecourses/index.html", {"allscience": allscience})


def ArtsConcour(request):
    allarts_concours = Concour.objects.filter(departement=1)

    paginator = Paginator(allarts_concours, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allarts = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allarts = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allarts = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage

    return render(request, "Concours/Artscourses/index.html", {"allarts": allarts})


def All_Courses(request):
    '''
    allarts = ConcourToCourseMap.objects.filter(schoolname_id=1).order_by('-ratings__average')[:8]  # where department = it id corresponding to arts
    allscience = ConcourToCourseMap.objects.filter(schoolname_id=2).order_by('-ratings__average')[:8]  # where department = it id corresponding to science
    allcommercial = ConcourToCourseMap.objects.filter(schoolname_id=3).order_by('-ratings__average')[:8]  # where department = it id corresponding to commercial
    allengineer = ConcourToCourseMap.objects.filter(schoolname_id=4).order_by('-ratings__average')[:8]  # where department = it id corresponding to Engineering
    allmedical = ConcourToCourseMap.objects.filter(schoolname_id=5).order_by('-ratings__average')[:8]  # where department = it id corresponding to Medical

    context = {
        "allarts": allarts,
        "allscience": allscience,
        "allcommercial": allcommercial,
        "allengineer": allengineer,
        "allmedical": allmedical,
    }
    '''
    return render(request, "Concours/Allcourses/Courses/index.html")


# pagination of 12 courses per page
def Arts_Courses(request, school_id):
    allarts_courses = ConcourToCourseMap.objects.filter(schoolname=school_id)  # departement is found in two tables
    paginator = Paginator(allarts_courses, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allarts = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allarts = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allarts = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage
    concour = Concour.objects.get(id=school_id)

    return render(request, "Concours/Artscourses/Courses/index.html", {"allarts": allarts, "concour":concour })


# pagination of 12 courses per page
def Science_Courses(request, school_id):
    allscience_courses = ConcourToCourseMap.objects.filter(schoolname=school_id)  # departement is found in two tables
    paginator = Paginator(allscience_courses, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allscience = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allscience = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allscience = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage
    concour = Concour.objects.get(id=school_id)

    return render(request, "Concours/Sciencecourses/Courses/index.html", {"allscience": allscience, "concour":concour })


# pagination of 12 courses per page
def Commercial_Courses(request, school_id):
    allcommercial_courses = ConcourToCourseMap.objects.filter(schoolname=school_id)  # departement is found in two tables
    paginator = Paginator(allcommercial_courses, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allcommercial = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allcommercial = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allcommercial = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage
    concour = Concour.objects.get(id=school_id)

    return render(request, "Concours/Commercialcourses/Courses/index.html", {"allcommercial": allcommercial, "concour":concour })


# pagination of 12 courses per page
def Engineering_Courses(request, school_id):
    allenginering_courses = ConcourToCourseMap.objects.filter(schoolname=school_id)  # departement is found in two tables
    paginator = Paginator(allenginering_courses, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allenginering = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allenginering = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allenginering = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage
    concour = Concour.objects.get(id=school_id)

    return render(request, "Concours/Engineering/Courses/index.html", {"allengineering": allenginering, "concour":concour })


# pagination of 12 courses per page
def Medical_Courses(request, school_id):
    allmedical_courses = ConcourToCourseMap.objects.filter(schoolname=school_id)  # departement is found in two tables
    paginator = Paginator(allmedical_courses, 12)  # 10 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        allmedical = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        allmedical = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        allmedical = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage
    concour = Concour.objects.get(id=school_id)

    return render(request, "Concours/Medical/Courses/index.html", {"allmedical": allmedical, "concour":concour })


def Selected_Arts_Course(request, course_id, user_id, school_id):

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):
        subscribed = False
    else:
        subscribed = True

    concour = Concour.objects.get(id=school_id)
    artscourse = get_object_or_404(ConcourCourse, id=course_id)
    chapters = ConcourChapter.objects.filter(course=course_id)

    teachers = []  # to store the teachers id
    for chapter in chapters:
        if chapter.teacher not in teachers:  # Making sure id does not repeat
            teachers.append(chapter.teacher)  # we are selecting all the teachers id in the chapter table and making sure it doesnt repeat

    context = {
        "concour": concour,
        "course": artscourse,
        "teachers": teachers,
        "subscribed": subscribed,
        "Education_level": "Concour School"
    }
    return render(request, "Concours/courseintro.html", context)


def Selected_Science_Course(request, course_id, user_id, school_id):

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):
        subscribed = False
    else:
        subscribed = True

    concour = Concour.objects.get(id=school_id)
    sciencecourse = get_object_or_404(ConcourCourse, id=course_id)  # departement is found in two tables
    chapters = ConcourChapter.objects.filter(course=course_id)

    teachers = []  # to store the teachers id
    for chapter in chapters:
        if chapter.teacher not in teachers:  # Making sure id does not repeat
            teachers.append(chapter.teacher)  # we are selecting all the teachers id in the chapter table and making sure it doesnt repeat

    context = {
        "concour": concour,
        "course": sciencecourse,
        "teachers": teachers,
        "subscribed": subscribed,
        "Education_level": "Concour School"
    }
    return render(request, "Concours/courseintro.html", context)


def Selected_Commercial_Course(request, course_id, user_id, school_id):

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):
        subscribed = False
    else:
        subscribed = True

    concour = Concour.objects.get(id=school_id)
    commercialcourse = get_object_or_404(ConcourCourse, id=course_id)  # departement is found in two tables
    chapters = ConcourChapter.objects.filter(course=course_id)

    teachers = []  # to store the teachers id
    for chapter in chapters:
        if chapter.teacher not in teachers:  # Making sure id does not repeat
            teachers.append(chapter.teacher)  # we are selecting all the teachers id in the chapter table and making sure it doesnt repeat

    context = {
        "concour": concour,
        "course": commercialcourse,
        "teachers": teachers,
        "subscribed": subscribed,
        "Education_level": "Concour School"
    }
    return render(request, "Concours/courseintro.html", context)


def Selected_Engineering_Course(request, course_id, user_id, school_id):

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):
        subscribed= False
    else:
        subscribed=True

    concour = Concour.objects.get(id=school_id)
    engineeringcourse = get_object_or_404(ConcourCourse, id=course_id)
    chapters = ConcourChapter.objects.filter(course=course_id)
    teachers = []  # to store the teachers id

    for chapter in chapters:
        if chapter.teacher not in teachers:  # Making sure id does not repeat
            teachers.append(chapter.teacher)  # we are selecting all the teachers id in the chapter table and making sure it doesnt repeat

    context = {
        "concour": concour,
        "course": engineeringcourse,
        "teachers": teachers,
        "subscribed": subscribed,
        "Education_level": "Concour School"
    }
    return render(request, "Concours/courseintro.html", context)


def Selected_Medical_Course(request, course_id, user_id, school_id):

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):
        subscribed= False
    else:
        subscribed=True

    concour = Concour.objects.get(id=school_id)
    medicalcourse = get_object_or_404(ConcourCourse, id=course_id)  # departement is found in two tables
    chapters = ConcourChapter.objects.filter(course=course_id)

    teachers = []  # to store the teachers id
    for chapter in chapters:
        if chapter.teacher not in teachers:  # Making sure id does not repeat
            teachers.append(chapter.teacher)  # we are selecting all the teachers id in the chapter table and making sure it doesnt repeat

    context = {
        "concour":concour,
        "course": medicalcourse,
        "teachers": teachers,
        "subscribed": subscribed,
        "Education_level": "Concour School"
    }
    return render(request, "Concours/courseintro.html", context)


@login_required  # subscribing for a course
def Subscribe(request, course_id, user_id, school_id):  # when you subscribe it enters a table with the course for particular level
    chapter_id = 1
    topic_id = 1

    if not StudentSubscribedConcourcourse.objects.filter(course=course_id, student=user_id, concour=school_id):  # if user is not yet subscribed
        if request.method =="POST":  # if user is in submitted form
            subscribe_form = SubscribeForm(request.POST)
            if subscribe_form.is_valid():  # no error in form
                _amount = subscribe_form.cleaned_data["amount"]
                _tel = subscribe_form.cleaned_data["contact"]
                _email = "blaisefonyuy@gmail.com"  # Merchant email used to register for MoMo Merchant Account
                main_api = "https://developer.mtn.cm/OnlineMomoWeb/faces/transaction/transactionRequest.xhtml?idbouton=2&typebouton=PAIE&"
                # composining the momo json request
                api_url = main_api+urllib.parse.urlencode({'_amount':1})+"&"+urllib.parse.urlencode({'_tel':_tel})+"&_clP=&"+urllib.parse.urlencode({'_email':_email})
                jason_data = requests.get(api_url).json() # carries out transaction request and stores response (jason response from MTN Mobile Money)

                contactstring = str(_tel)

                if len(contactstring)>=9 and len(contactstring)<=12:  # making sure number is above 9 digits for cameroon
                    user_transaction = MoMoTransactions()
                    user_subscribtion = StudentSubscribedConcourcourse()
                    jason_status = str(jason_data["StatusCode"])

                    if jason_status == "01":  # means a successful transaction

                        # saving subscription info
                        course = ConcourCourse.objects.get(id=course_id)
                        school = Concour.objects.get(id=school_id)
                        user = User.objects.get(id=user_id)
                        user_subscribtion.course = course
                        user_subscribtion.student = user
                        user_subscribtion.level = course.departement
                        user_subscribtion.concour = school
                        user_subscribtion.save()

                        # saving transaction
                        course = ConcourToCourseMap.objects.get(id=course_id)
                        user_transaction.username = user
                        user_transaction.coursename = course
                        user_transaction.phoneNumber = _tel
                        user_transaction.amount = _amount
                        user_transaction.statusCode = int(jason_status)
                        user_transaction.transactionId = jason_data["TransactionID"]
                        user_transaction.save()

                        # send email to alert client of his subscription sending Tefa email
                        email_subject = "TEFA Course Subscription"
                        email_content = "You are recieving this mail because " + user.username + " subscribed for " + course.coursename.coursename + ". Click on the link below to access your course page directly 127.0.0.1:8000/Concours/Subscribe/Course/Confirmation/" + course_id + "/" + user_id + "/" + school_id + "/"
                        email = EmailMessage(email_subject, email_content, to=[user.email])
                        email.send()

                        # success message (transaction success)
                        messages.success(request, user.username+" Successfully subscribed for "+course.coursename.coursename)

                        # redirect to course Video page
                        return redirect("Concours:coursevideos", course_id, chapter_id,
                                    topic_id)  # if user is already subscribed for course direct him to video page

                    else:   # transaction failure
                        user = User.objects.get(id=user_id)

                        # saving transaction
                        course = ConcourToCourseMap.objects.get(id=course_id)
                        user_transaction.username = user
                        user_transaction.coursename = course
                        user_transaction.phoneNumber = _tel
                        user_transaction.amount = _amount
                        user_transaction.statusCode = jason_status
                        user_transaction.transactionId = jason_data["TransactionID"]
                        user_transaction.save()

                        # send email to alert client of his subscription sending Tefa email
                        email_subject = "TEFA Course Subscription"
                        email_content = "You are recieving this mail because " + user.username + " attempted to subscribe for " + course.coursename.coursename + " but the process failed click here to resubscribe 127.0.0.1:8000/Concours/Subscribe/Course/" + course_id + "/" + user_id + "/" + school_id + "/"
                        email = EmailMessage(email_subject, email_content, to=[user.email])
                        email.send()

                        # error message (transaction success)
                        messages.error(request,
                                         user.username + " your subscribtion for " + course.coursename.coursename +" failed. Try again later")

                        # redirect to course Video page
                        return redirect("Concours:subscribe", course_id, user_id, school_id)  # if user is already subscribed for course direct him to video page

                else:
                    messages.error(request, " Phone Number Incorrect, Please try again later")
                    return redirect("Concours:subscribe", course_id, user_id, school_id)  # inputted email was wrong

            else:
                messages.error(request, " Enter a valid phone number    ")
                return redirect("Concours:subscribe", course_id, user_id, school_id)  # inputted email was wrong

        else:
            return render(request, "Concours/Mobile_Money/index.html", { "course_id": course_id, "user_id": user_id, "school_id":school_id } )  # inputted email was wrong
    else:
        return redirect("Concours:coursevideos", course_id, chapter_id, topic_id)  # if user is already subscribed for course direct him to video page



@login_required  # displaying video course page
def CourseVideos(request, course_id, chapter_id, topic_id):

    course = ConcourCourse.objects.get(id=course_id)
    chapters = ConcourChapter.objects.filter(course=course_id)

    Topics = []  # since they can never be greater than the number of chapters

    for chapter in chapters:
        topics = ConcourTopic.objects.filter(chapter=chapter.id)
        Topics.append(topics)  # dictionary that can have the topic fields (just defining each field)

    if chapter_id == 0 and topic_id == 0:
        chapter = ConcourChapter.objects.get(id=1)
        topic = ConcourTopic.objects.get(id=1)
        context = {
            "Title": "Concour ",
            "chapters": chapters,
            "topics": Topics,
            "Topic": topic,
            "Chapter": chapter,
            "course": course
        }
        return render(request, "Concours/CourseVideopage.html", context)

    else:
        chapter = ConcourChapter.objects.get(id=chapter_id)
        topic = ConcourTopic.objects.get(id=topic_id)
        context = {
            "Title": "Concour School",
            "chapters": chapters,
            "topics": Topics,
            "Topic": topic,
            "Chapter": chapter,
            "course": course
        }
        return render(request, "Concours/CourseVideopage.html", context)


@login_required  # forum for chats, questions on particular topics
def Forum(request, user_id, course_id, chapter_id, topic_id):  # this returns the forum page

    page_comments = ConcourForum.objects.filter(course=course_id, chapter=chapter_id, topic=topic_id).order_by('-ratings__average')[:8]
    paginator = Paginator(page_comments, 8)  # 8 signifies the number of posts per page

    page = request.GET.get('page')
    try:
        comments  = paginator.page(page)  # if true the go to next page
    except PageNotAnInteger:
        comments = paginator.page(1)  # if pagenotinteger go to firstpage
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)  # if Emptypage then deliver lastpage

    replys = []
    for comment in comments:
        reply = ConcourReplyComment.objects.filter(comment=comment.id)  # getting the reply associated to a particular comment
        replys.append(reply)

    course = get_object_or_404(ConcourCourse, id=course_id)
    topic = get_object_or_404(ConcourTopic, id=topic_id)

    chapters = ConcourChapter.objects.filter(course=course_id)

    Topics = []  # since they can never be greater than the number of chapters

    for chapter in chapters:
        topics = ConcourTopic.objects.filter(chapter=chapter.id)
        Topics.append(topics)  # dictionary that can have the topic fields (just defining each field)

    usercreatedcomments = ConcourUserForum.objects.filter(course=course_id).order_by('-ratings__average')[:8]

    context = {
        "chapters": chapters,
        "topics": Topics,
        "topic": topic,
        "course": course,
        "comments": comments,
        "replys": replys,
        "course_id": course_id,
        "topic_id": topic_id,
        "chapter_id": chapter_id,
        "usercreatedcomments": usercreatedcomments
    }
    return render(request, "Concours/Forum/Forum.html", context)


# to put success/error messages
@login_required
def Forum_CreateComment(request,  user_id, course_id, chapter_id, topic_id):  # inside the function we can take the arguments to be the names of our form

    if request.method == "POST":
        comment_form = ConcourForumForm(request.POST or None)

        if comment_form.is_valid():
            comment = ConcourForum()
            user = User.objects.get(id=user_id)
            course = ConcourCourse.objects.get(id=course_id)
            chapter = ConcourChapter.objects.get(id=chapter_id)
            topic = ConcourTopic.objects.get(id=topic_id)

            if request.POST["comment"]:
                comment.user = user
                comment.course = course
                comment.topic = topic
                comment.chapter = chapter
                comment.comment = request.POST["comment"]
                comment.save()

                messages.success(request, "Comment Successfully posted")
                return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)  # List all the comments in forum

            else:
                return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)  # List all the comments in forum

        else:
            messages.error(request, "Error occurred try again later")
            return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)  # List all the comments in forum

    else:
        return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)  # List all the comments in forum


# to put success/error messages
@login_required
def Reply_ForumComment(request, user_id, comment_id, course_id, chapter_id, topic_id):
    reply_form = ConcourReplyCommentForm(request.POST)
    if reply_form.is_valid():  # error no in form
        comment_reply = reply_form.cleaned_data["comment_reply"]
        reply = ConcourReplyComment()
        reply.comment_reply = comment_reply
        reply.user = get_object_or_404(User, id=user_id)
        reply.comment = get_object_or_404(ConcourForum, id=comment_id)
        reply.save()
        messages.success(request, "Reply Successfully posted")
        return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)
    else:
        messages.error(request, "Error occurred please try again later")
        return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)


@login_required  # forum for chats, questions on particular topics
def UserPersonalForum(request, user_id, Usercomment_id, course_id):  # this returns the forum page

    comments = ConcourUserForum.objects.filter(course=course_id).order_by('-ratings__average')[:8]
    usercomment = get_object_or_404(ConcourUserForum, id=Usercomment_id)
    usercommentreplies = ConcourUserForumReply.objects.filter(user=user_id, usercomment=Usercomment_id)

    context = {
        "course_id": course_id,
        "Comments": comments,
        "UserComment": usercomment,
        "Replies": usercommentreplies
    }
    return render(request, "Concours/Forum/UserForum.html", context)


@login_required()
def UserSearch_Forum(request, course_id):
    if request.method == "GET":
        searchString = request.GET.get("q")
        if len(searchString) == 0:
            messages.error(request, "Nothing was found relating to your search")
            return render(request, "Concours/Forum/UserForumSearch.html", {"searchString": searchString, "course_id": course_id})
        else:
            searchtopics= ConcourUserForum.objects.filter(comment__icontains=searchString )

            countsearchtopics = searchtopics.count()

            return render(request, "Concours/Forum/UserForumSearch.html", {"course_id": course_id, "searchtopics": searchtopics, "countsearchtopics": countsearchtopics, "searchString": searchString})


# to put success/error messages
@login_required
def UserCreateComment(request, user_id, course_id):  # inside the function we can take the arguments to be the names of our form

    if request.method == "POST":
        comment_form = ConcourUserForumForm(request.POST or None)

        if comment_form.is_valid():
            user = get_object_or_404(User, id=user_id)
            course = get_object_or_404(ConcourCourse, id=course_id)
            comment = ConcourUserForum()
            comment.user = user
            comment.course = course
            comment.comment_title = request.POST["comment_title"]
            comment.comment = request.POST["comment"]
            comment.save()

            messages.success(request, "Comment Successfully posted")
            Usercomment_id = comment.id
            return redirect("Concours:userforum", user_id, course_id, Usercomment_id)  # List all the comments in forum

        else:
            chapter_id = 1
            topic_id = 1
            messages.error(request, "Error occurred try again later")
            return redirect("Concours:forum", user_id, course_id, chapter_id, topic_id)  # List all the comments in forum

    else:
        return render(request, "Concours/Forum/UsercreateForum.html", {"course_id": course_id})  # Display form to create topic of discussion


# to put success/error messages
@login_required
def ReplyusercreatedComment(request, user_id, Usercomment_id):
    usercomment = get_object_or_404(ConcourUserForum, id=Usercomment_id)  # getting the comment to which a reply is being associated
    course_id = usercomment.course.id
    if request.method == "POST":
        userConcourReplyComment_form = ConcourUserForumReplyForm(request.POST or None)
        if userConcourReplyComment_form.is_valid():
            userConcourReplyComment = ConcourUserForumReply()
            userConcourReplyComment.usercomment_reply = request.POST["usercomment_reply"]
            userConcourReplyComment.user = get_object_or_404(User, id=user_id)
            userConcourReplyComment.usercomment = usercomment
            userConcourReplyComment.save()
            messages.success(request, "Reply Successfully posted")
            return redirect("Concours:userforum", user_id ,course_id, Usercomment_id)
        else:
            messages.success(request, "An error occurred plesae try again later")
            return redirect("Concours:userforum", user_id ,course_id, Usercomment_id)
    else:
        chapter_id=1
        topic_id=1
        return Forum(request, user_id, course_id, chapter_id, topic_id)


@login_required()
def ConfirmationEmail(request):
    return render(request, "confirmation.html", {"message": "Your subscription link has been sent to your email address click on it to complete subscription"})


@login_required()
def Quiz(request, user_id, chapter_id, course_id):
    score=ConcourMCQScore.objects.filter(chapter=chapter_id, user=user_id)

    if score: # if user has already taken the quiz redirect him to videos
        messages.error(request, "You had already taken the quiz")
        context ={
            "Chapter": get_object_or_404(ConcourChapter, id=chapter_id),
            "Course": get_object_or_404(ConcourCourse, id=course_id),
            "User_Score": get_object_or_404(ConcourMCQScore, user=user_id, chapter=chapter_id).user_score
        }
        return render(request, "Concours/Quiz_Results.html", context)

    else:
        course = get_object_or_404(ConcourCourse, id=course_id)  # getting course
        chapter = get_object_or_404(ConcourChapter, id=chapter_id)  # getting chapter
        mcq_questions = ConcourMCQQuestion.objects.filter(chapter=chapter_id)  # getting all the questions corresponding to the chapter

        mcq_answers = []  # to store the answers corresponding to each question

        for question in mcq_questions:  # for each question save its corresponding answers
            answers = ConcourMCQAnswer.objects.filter(question=question.id)
            mcq_answers.append(answers)

        context = {
            "Course": course,
            "Chapter": chapter,
            "mcq_questions": mcq_questions,
            "mcq_answers": mcq_answers
        }
        return render(request, "Concours/Quiz_Display.html", context)


@login_required()
def Quiz_Correction(request, chapter_id, course_id, user_id):
    score=ConcourMCQScore.objects.filter(chapter=chapter_id, user=user_id)

    if score: # if user has already taken the quiz redirect him to videos
        messages.error(request, "You had already taken the quiz")
        context ={
            "Chapter": chapter_id,
            "Course": course_id,
            "User_Score": get_object_or_404(ConcourMCQScore, user=user_id, chapter=chapter_id).user_score
        }
        return render(request, "Concours/Quiz_Results.html", context)


    User_Score = 0  # value to contain userscore
    if request.method=="POST":
        questions = ConcourMCQQuestion.objects.filter(chapter=chapter_id)  # ets all the questions of the course chapter
        for question in questions:  # For each question, get the user inputted answer
            answer_ids = set([int(x) for x in dict(request.POST)[str(question.id)]])  # getting the id of the user's answer to each question
            correct_answers = set([ x.id for x in ConcourMCQAnswer.objects.filter(question=question.id, correctanswer=True)])  # getting correct answers
            # note that for a question we can have multiple answers hence multiple answer_id
            # searching if any of the user answers are incorrect, then stop and give him zero

            if correct_answers & answer_ids == correct_answers:  # if the intersection is the set of correct answers
                User_Score += question.question_marks  # mark his question as correct

        Total_Score = ConcourMCQScore()
        Total_Score.chapter = get_object_or_404(ConcourChapter, id=chapter_id)
        Total_Score.user = get_object_or_404(User, id=user_id)
        Total_Score.user_score = User_Score
        Total_Score.save()

        Chapter = get_object_or_404(ConcourChapter, id=chapter_id)
        Course = Chapter.course

        context = {
            "User_Score": User_Score,
            "Chapter": Chapter,
            "Course": Course
        }
        return render(request, "Concours/Quiz_Results.html", context)

    else:
        return render(request, "Error.html", {})