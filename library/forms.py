from .models import Comment
from django.forms import ModelForm, HiddenInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance:
            self.fields['user'].widget = HiddenInput()
            self.fields['book'].widget = HiddenInput()
