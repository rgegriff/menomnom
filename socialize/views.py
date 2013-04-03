from django.views.generic import ListView
from models import Message
from management.models import BizPost
# Create your views here.



class MessageList(ListView):
    queryset = Message.objects.recent_posts()
    template_name = "socialize.html"

    def get_context_data(self, **kwargs):
        '''attach the biz messages to the objects list'''

        qset = super(MessageList, self).get_context_data(**kwargs)
        print qset
        qset['biz_posts'] = BizPost.objects.all().order_by('-post_time')[:20]
        return qset