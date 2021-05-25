from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import UUIDStamp
from uuid import uuid4

# Create your views here.
@api_view(['GET',])
def getuuids(request):

    # creates new uuidstamp
    UUIDStamp.objects.create(uuid_obj=uuid4())
    
    # gets all uuidstamp object from model
    uuidstamps = UUIDStamp.objects.all()

    # Pagination wasn't included because of the requirements given

    # gets an array of custom dictionary where key is datetime and value is uuid
    data = [ uuidstamp.get_uuid_stamp_dic() for uuidstamp in uuidstamps] 
    return Response(data)
