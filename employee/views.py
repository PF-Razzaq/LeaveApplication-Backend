from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate ,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework import status
from .models import Employee,ApplyForLeave,LeaveTable
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
    user = authenticate(request, username=email, password=password)


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
    
@api_view(['GET'])
def leave_table_view(request):
    if request.method == 'GET':
        try:
            leave_table = LeaveTable.objects.first()
            data = {
                'total_leave': leave_table.total_leave,
                'approved_days': leave_table.approved_days,
                'pending_leaves': leave_table.pending_leaves,
            }
            return Response(data)
        except LeaveTable.DoesNotExist:
            return Response({'error: Leave table does not exist'},status=404)
        
@api_view(['POST'])
def leave_table_update(request):
    if request.method == 'POST':
        approved_days = request.data.get('approved_days')
        try:
            leave_table = LeaveTable.objects.first()
            if leave_table:
                leave_table.approved_days = approved_days
                leave_table.save()
                return Response({'message': 'Leave table updated successfully'})
            else:
                return Response({'error': 'No leave table records found'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        

@api_view(['GET'])
def get_employee_leave(request, employee_id):
    try:
        # Retrieve the employee object
        employee = get_object_or_404(Employee, id=employee_id)
        
        # Retrieve the associated LeaveTable instance for the employee
        leave_table = employee.leave_table
        
        # Retrieve the leaves associated with the LeaveTable id
        leaves = ApplyForLeave.objects.filter(leave_table_id=leave_table.id)
        
        # Serialize the leaves data as needed and return
        # This depends on your serializer implementation
        # For simplicity, returning a dictionary representation
        serialized_leaves = [{'leave_type': leave.leave_type, 'days': leave.days} for leave in leaves]
        
        return Response(serialized_leaves)
    
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)
    except LeaveTable.DoesNotExist:
        return Response({'error': 'LeaveTable not found for the employee'}, status=404)
    except Exception as e:
        return Response({'error': str(e)}, status=500)