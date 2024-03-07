from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from app_critics.models import FeedBack as FeedBackModel


class RetrieveMyFeedBackView(LoginRequiredMixin, generic.ListView):
    template_name = "detail-my-feedbacks.html"

    def get_queryset(self):
        return FeedBackModel.objects.all()
        # return FeedBackModel.objects.filter(user=self.request.user)
