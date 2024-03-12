from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate ,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import status
from .models import Employee,ApplyForLeave
from .serializers import *

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employees_list(request, employee_id=None):
    if request.method == 'GET':
        if employee_id:
            try:
                employee = Employee.objects.get(id=employee_id)
                serializer = EmployeeSerializer(employee, context={'request': request})
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            data = Employee.objects.all()
            serializer = EmployeeSerializer(data, context={'request': request}, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def employees_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



class ApplyForLeaveListCreateView(generics.ListCreateAPIView):
    queryset = ApplyForLeave.objects.all()
    serializer_class = ApplyForLeaveSerializer

class ApplyForLeaveDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApplyForLeave.objects.all()
    serializer_class = ApplyForLeaveSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
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

@api_view(['GET','PUT', 'DELETE'])
def apply_leave_detail(request, pk):
    try:
        applyleave = ApplyForLeave.objects.get(pk=pk)
    except ApplyForLeave.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = ApplyForLeaveSerializer(applyleave)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ApplyForLeaveSerializer(applyleave, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        applyleave.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    print('login1')
    user = authenticate(request, username=email, password=password)

    print('login2')
    print(user)
    if user is not None:
        token = Token.objects.get_or_create(user=user)
        return Response({'access_token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid Credential or role'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    
    return Response({'message','Logged out Successfully'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def apply_leave_status(request, pk):
    if request.method == 'GET':
        leave_instance = ApplyForLeave.objects.get(pk=pk)
        serializer = ApplyForLeaveSerializer(leave_instance, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        leave_instance = ApplyForLeave.objects.get(pk=pk)
        leave_instance.status = 1
        leave_instance.save()
        return Response({'message': 'Leave status updated successfully.'})