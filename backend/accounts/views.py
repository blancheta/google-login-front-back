import pprint

from django.conf import settings
from django.http import JsonResponse
from django.views.generic import TemplateView

from google_auth_oauthlib.flow import InstalledAppFlow
from rest_framework.views import APIView


class CustomLoginView(TemplateView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["client_id"] = settings.GOOGLE_CLIENT_ID
        return context


class GoogleExchangeView(APIView):

    def get(self, request, *args, **kwargs):
        print(self.request.GET)
        code = self.request.GET["code"]
        print(code)

        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=["https://www.googleapis.com/auth/userinfo.email", 'openid', "https://www.googleapis.com/auth/userinfo.profile"])
        flow.redirect_uri = "http://localhost:3000"

        credentials = flow.fetch_token(code=code)
        pprint.pprint(credentials)

        return JsonResponse({})
