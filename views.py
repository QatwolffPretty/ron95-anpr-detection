from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PlateLog
from .serializers import PlateLogSerializer

@api_view(['GET'])
def health_check(request):
    return Response({ "status": "OK", "message": "API is running." })

@api_view(['GET', 'POST'])
def plate_logs(request):
    if request.method == 'GET':
        logs = PlateLog.objects.all().order_by('-timestamp')[:10]
        serializer = PlateLogSerializer(logs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlateLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response(serializer.errors, status=400)
