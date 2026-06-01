from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Students
import json

@csrf_exempt
def StudentData(request, id=None):
    
    if request.method == "GET":
        query = request.GET.get('q','')
        students = Students.objects.filter(name__icontains=query)
        data = []
        for i in students:
            data.append({
                'id': i.id,
                'name': i.name,
                'age': i.age,
                'mobile': i.mobile,
                'city': i.city,
                'active': i.active,
            })
        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        try:
            body = json.loads(request.body)
            student = Students.objects.create(
                name=body.get('name'),
                age=body.get('age'),
                mobile=body.get('mobile'),
                city=body.get('city'),
                active=body.get('active'),
            )
            return JsonResponse({"message": "Student added", "id": student.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "DELETE":
        try:
            if id is None:
                return JsonResponse({"error": "ID required"}, status=400)
            stud = Students.objects.get(id=id)
            stud.delete()
            return JsonResponse({"message": "Student deleted"})
        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    elif request.method == "PUT":
        try:
            if id is None:
                return JsonResponse({"error": "Id required"}, status=400)
            data = json.loads(request.body)
            stud = Students.objects.get(id=id)
            stud.name   = data.get("name")
            stud.age    = data.get("age")
            stud.mobile = data.get("mobile")
            stud.city   = data.get("city")
            stud.active = data.get("active", False)
            stud.save()
            return JsonResponse({"message": "Student Updated"})
        except Students.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Invalid Method"}, status=400)