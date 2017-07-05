from django.conf.urls import url
from Core.views import Homepage, Logout_user, User_Profile, UpdateProfile, Edit_ProfilePic, Contact_usConfirmation, User_Courses, Search #, Social_CreatePassword, CreatePassword
from Core.views import Contact_Us, About_Us, Adverts, Privacy_Policies, Donate, DonateMoMo, SeeAllCourses


app_name = "homepg"

urlpatterns = [
    url(r'^$', Homepage, name="homepage"),
    url(r'^Search/$', Search, name="search"),
    url(r'^Logout/$', Logout_user, name="logout"),
    url(r'^All_Courses/$', SeeAllCourses, name="seeallcourses"),
    url(r'^Profile/$', User_Profile, name="userprofile"),
    # url(r'^Profile/Create_Password/$', CreatePassword, name="displaycreatepassword"),
    # url(r'^Profile/Create_Password/(?P<user_id>\d+)/$', Social_CreatePassword, name="createpassword"),
    url(r'^My_Courses/(?P<user_id>\d+)/$', User_Courses, name="usercourses"),
    url(r'^Edit/ProfilePic/(?P<user_id>\d+)/$', Edit_ProfilePic, name="editprofilepic"),
    url(r'^Update/Profile/(?P<user_id>\d+)/$', UpdateProfile, name="editprofile"),
    url(r'^Contact_Us/$', Contact_Us, name="contactus"),
    url(r'^Contact_Us/Confirmation/$', Contact_usConfirmation, name="contactus_confirmation"),
    url(r'^About_Us/$', About_Us, name="aboutus"),
    url(r'^Adverts/$', Adverts, name="advert"),
    url(r'^Privacy_Policies/$', Privacy_Policies, name="privacy_policies"),
    url(r'^Donate/$', Donate, name="donate"),
    url(r'^Donate/MTN_Mobile_Money/$', DonateMoMo, name="donatemomo"),

]