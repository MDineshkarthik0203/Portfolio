from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.shortcuts import render

def portfolio(request):
    return render(request, 'Portfolio.html')

class ContactView(APIView):

    # POST /api/contact/
    # Receives name, email, message from the portfolio form and saves to database
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'success': True, 'message': 'Message received! I will get back to you soon.'},
                status=status.HTTP_201_CREATED
            )

        return Response(
            {'success': False, 'errors': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    # GET /api/contact/
    # Returns all messages (useful for checking from admin/Postman)
    def get(self, request):
        messages = ContactMessage.objects.all().order_by('-sent_at')
        serializer = ContactMessageSerializer(messages, many=True)
        return Response(serializer.data)
