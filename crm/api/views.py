from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from leads.models import Lead
from .serializers import LeadSerializer


class LeadView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        leads = Lead.objects.all()
        serializer = LeadSerializer(leads, many=True)

        context = {"leads": serializer.data}

        return Response(context)

    def post(self, request):
        lead = request.data.get('lead')
        serializer = LeadSerializer(data=lead)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        context = {"success": "Lead  created successfully."}

        return Response(context)
