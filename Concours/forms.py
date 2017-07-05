from django import forms
from Concours.models import ConcourForum, ConcourReplyComment, ConcourUserForum, ConcourUserForumReply, User


class ConcourForumForm(forms.ModelForm):
    class Meta:
        model = ConcourForum
        fields = [
            "comment"
        ]


class SubscribeForm(forms.Form):
    contact = forms.IntegerField()
    amount = forms.IntegerField()


class ConcourReplyCommentForm(forms.ModelForm):
    class Meta:
        model = ConcourReplyComment
        fields = [
            "comment_reply"
        ]


class ConcourUserForumForm(forms.ModelForm):
    class Meta:
        model = ConcourUserForum
        fields = [
            "comment", "comment_title"
        ]


class ConcourUserForumReplyForm(forms.ModelForm):
    class Meta:
        model = ConcourUserForumReply
        fields = [
            "usercomment_reply"
        ]
