from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ApplyForLeave
from .serializers import ApplyForLeaveSerializer

class ApplyForLeaveListCreateView(generics.ListCreateAPIView):
    queryset = ApplyForLeave.objects.all()
    serializer_class = ApplyForLeaveSerializer

class ApplyForLeaveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplyForLeave.objects.all()
    serializer_class = ApplyForLeaveSerializer


@api_view(['GET', 'POST'])
def apply_leave_list(request):
    if request.method == 'GET':
        queryset = ApplyForLeave.objects.all()
        serializer = ApplyForLeaveSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ApplyForLeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def apply_leave_detail(request, pk):
    try:
        applyleave = ApplyForLeave.objects.get(pk=pk)
    except ApplyForLeave.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ApplyForLeaveSerializer(applyleave, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        applyleave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    