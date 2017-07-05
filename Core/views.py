from django.core.mail import EmailMessage
from Core.forms import ContactForm, UserRegisterForm, UserProfileForm, PictureForm, DonateForm
from Core.models import UserDonateMoMo
from Concours.models import ConcourCourse, StudentSubscribedConcourcourse, ConcourToCourseMap, Concour, ConcourTeacher
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
import urllib.parse
import requests
# Create your views here.


def Homepage(request):
    context = {
        "Title": "Targeted Education For All"
    }
    return render(request, "Core/index.html", context)


def Logout_user(request):
    logout(request)
    return redirect("/")


def SeeAllCourses(request):

    universityconcourcourses = ConcourCourse.objects.all().order_by('-ratings__average')[:8]

    context = {
        "universityconcourcourses": universityconcourcourses,
    }
    return render(request, "Core/AllCourses/index.html", context)


@login_required
def User_Profile(request):

    context = {
        "Title": " Profile"
    }
    return render(request, "Core/UserProfile/index.html", context)


# to put success/error messages
@transaction.atomic
@login_required
def UpdateProfile(request, user_id):

    if request.method == "POST":
        user_form = UserRegisterForm(request.POST or None, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():  # if the data in form is valid
            user = User.objects.get(pk=user_id)  # get user info and compare password

            username = user_form.cleaned_data["username"]
            password = user_form.cleaned_data["password"]

            if check_password(password, user.password):  # this hashes the password:

                user.username = request.POST.get("username")
                user.first_name = request.POST.get("first_name")
                user.last_name = request.POST.get("last_name")
                user.email = request.POST.get("email")
                user.userprofile.nationality = request.POST.get("nationality")
                user.userprofile.dateofbirth = request.POST.get("dateofbirth")
                user.userprofile.gender = request.POST.get("gender")
                user.userprofile.levelofeducation = request.POST.get("levelofeducation")
                user.userprofile.contact = request.POST.get("contact")
                user.save()

                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, "Update successful")
                        return redirect("homepg:userprofile")

            else:
                messages.error(request, "Wrong Password")
                return redirect("homepg:editprofile", user_id)
        else:
            messages.error(request, "Error occured, Try again")
            return redirect("homepg:editprofile", user_id)

    else:
        return render(request, "Core/UserProfile/EditProfile.html", {})


# to put success/error messages
@transaction.atomic
@login_required
def Edit_ProfilePic(request, user_id):

    if request.method == "POST":
        pic_form = PictureForm(request.POST, request.FILES)

        if pic_form.is_valid():
            user = User.objects.get(pk=user_id)  # we get the information corresponding to the user
            user.userprofile.userpic = pic_form.cleaned_data['image']  # changing the pic
            user.save()
            messages.success(request, "Update Successful")
            return redirect("homepg:userprofile")
        else:
            messages.error(request, "Error occured, Try again Later")
            return redirect("homepg:userprofile")
    else:
        return render(request, "Core/UserProfile/editpic.html", {"Title": "TEFA Profile", "Message": "Choose Your New Display Picture"})


@login_required
def User_Courses(request, user_id):

    userconcourcourses = StudentSubscribedConcourcourse.objects.filter(student=user_id)  # courses student has subscribed for with level


    Universityconcourmedicalcourses = []
    Universityconcourengineeringcourses = []
    Universityconcourcommercialcourses = []
    Universityconcourartscourses = []
    Universityconcoursciencecourses = []

    for subcourse in userconcourcourses:  # selecting user university courses
        usercourse = get_object_or_404(ConcourToCourseMap, coursename_id=subcourse.course.id, schoolname_id=subcourse.concour.id)
        if usercourse.coursename.departement.id == 1:  # "Arts"
            if usercourse not in Universityconcourartscourses:
                Universityconcourartscourses.append(usercourse)
        elif usercourse.coursename.departement.id == 2:  # "Science"
            if usercourse not in Universityconcoursciencecourses:
                Universityconcoursciencecourses.append(usercourse)
        elif usercourse.coursename.departement.id == 3:  # "Commercial"
            if usercourse not in Universityconcourcommercialcourses:
                Universityconcourcommercialcourses.append(usercourse)
        elif usercourse.coursename.departement.id == 4:  # "Engineering"
            if usercourse not in Universityconcourengineeringcourses:
                Universityconcourengineeringcourses.append(usercourse)
        elif usercourse.coursename.departement.id == 5:  # "Medicals"
            if usercourse not in Universityconcourmedicalcourses:
                Universityconcourmedicalcourses.append(usercourse)

    context = {
        "Universityconcourmedicalcourses": Universityconcourmedicalcourses,
        "Universityconcourengineeringcourses": Universityconcourengineeringcourses,
        "Universityconcourcommercialcourses": Universityconcourcommercialcourses,
        "Universityconcourartscourses": Universityconcourartscourses,
        "Universityconcoursciencecourses": Universityconcoursciencecourses,
    }
    return render(request, "Core/Usercourses/index.html", context)


def Contact_Us(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            user_email = request.POST["email"]
            contact_subject = request.POST["subject"]
            contact_content = request.POST["content"]

            # sending Tefa email
            email = EmailMessage(contact_subject, contact_content, to=[user_email])
            email.send()

            return redirect("homepg:contactus_confirmation")

        else:
            context = {
                "message": "An error occurred, please try again later"
            }
            return render(request, "Core/Contact_Us/index.html", context)

    return render(request, "Core/Contact_Us/index.html", {})


def Contact_usConfirmation(request):

    return render(request, "confirmation.html", {"message": "Your email was successfully sent, we shall review the contents and contact you as soon as possible through your email address"})


def Privacy_Policies(request):

    return render(request, "Core/Privacy_Policies/index.html", {})


def About_Us(request):

    return render(request, "Core/About_Us/index.html", {})


def Search(request):

    if request.method == "GET":
        searchString = request.GET.get("q").strip()
        if len(searchString) == 0:
            messages.error(request, "Nothing was found relating to your search")
            return render(request, "Search.html", {})
        else:
            counts = {}
            results = {}

            results["Courses"] = ConcourToCourseMap.objects.filter(Q(coursename__coursename__icontains=searchString))
            results["Concours"] = Concour.objects.filter(Q(schoolname__icontains=searchString))
            #results["Teachers"] = ConcourTeacher.objects.filter(Q(teachername__icontains=searchString))

            counts["Courses"] = results["Courses"].count()
            counts["Concours"] = results["Concours"].count()
            #counts["Teachers"] = results["Teachers"].count()


            context = {
                "resultsconcour": results["Concours"],
                "resultscourses": results["Courses"],
                #"resultsteachers": results["Teachers"],
                #"countteachers": counts["Teachers"],
                "countconcour": counts["Concours"],
                "countcourses": counts["Courses"],
                "searchstring": searchString,
            }
            return render(request, "Search.html", context)
    else:
        redirect("/")


def Adverts(request):
    return HttpResponse("Here we will make company adverts")


def Donate(request):
    return render(request, "Core/Donate.html", {})


@login_required  # subscribing for a course
def DonateMoMo(request):  # when you subscribe it enters a table with the course for particular level
    if request.method == "POST":  # if user is in submitted form
        donate_form = DonateForm(request.POST)
        if donate_form.is_valid():  # no error in form
            _amount = request.POST["amount"]
            _tel = request.POST["phonenumber"]
            donnorEmail = request.POST["email"]
            donatereason = request.POST["comment"]
            _email = "blaisefonyuy@gmail.com"  # Merchant email used to register for MoMo Merchant Account
            main_api = "https://developer.mtn.cm/OnlineMomoWeb/faces/transaction/transactionRequest.xhtml?idbouton=2&typebouton=PAIE&"

            contactstring = str(_tel)

            if len(contactstring) >= 9 and len(contactstring) <= 12:  # making sure number is above 9 digits for cameroon
                Donate_transaction = UserDonateMoMo()
                # composining the momo json request
                api_url = main_api + urllib.parse.urlencode({'_amount': 1}) + "&" + urllib.parse.urlencode(
                    {'_tel': _tel}) + "&_clP=&" + urllib.parse.urlencode({'_email': _email})
                jason_data = requests.get(
                    api_url).json()  # carries out transaction request and stores response (jason response from MTN Mobile Money)

                jason_status = str(jason_data["StatusCode"])

                if jason_status == "01":  # means a successful transaction

                    # saving donate transaction info
                    Donate_transaction.comment = donatereason
                    Donate_transaction.email = donnorEmail
                    Donate_transaction.phoneNumber = _tel
                    Donate_transaction.amount = _amount
                    Donate_transaction.statusCode = int(jason_status)
                    Donate_transaction.transactionId = jason_data["TransactionID"]
                    Donate_transaction.save()

                    # send email to alert client of his subscription sending Tefa email
                    email_subject = "TEFA Donation"
                    email_content = "Thank you for your generous donation. IT will go in for Support and maintainance of the platform."
                    email = EmailMessage(email_subject, email_content, to=[donnorEmail])
                    email.send()

                    # success message (transaction success)
                    messages.success(request,
                                     " Successfully donated to TEFA ")

                    # redirect to homepage
                    return redirect("/")  # if user is already subscribed for course direct him to video page

                else:  # transaction failure
                    # saving donate transaction info
                    Donate_transaction.comment = donatereason
                    Donate_transaction.email = donnorEmail
                    Donate_transaction.phoneNumber = _tel
                    Donate_transaction.amount = _amount
                    Donate_transaction.statusCode = int(jason_status)
                    Donate_transaction.transactionId = jason_data["TransactionID"]
                    Donate_transaction.save()

                    # send email to alert client of his subscription sending Tefa email
                    email_subject = "TEFA Donation"
                    email_content = "Donation failed. We are really sorry for the errors, we will get the problems resolved as soon as possible."
                    email = EmailMessage(email_subject, email_content, to=[donnorEmail])
                    email.send()

                    # error message (transaction success)
                    messages.error(request, " Your Donation failed Try again later")

                    # redirect to course Video page
                    return redirect("homepg:donatemomo")  # if user is already subscribed for course direct him to video page

            else:
                messages.error(request, " Phone Number Incorrect, Please try again later")
                return redirect("homepg:donatemomo")  # inputted email was wrong

        else:
            messages.error(request, " Enter a valid information ")
            return redirect("homepg:donatemomo")  # inputted email was wrong

    else:
        return render(request, "Core/Donate.html", {})







