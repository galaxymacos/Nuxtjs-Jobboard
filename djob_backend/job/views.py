from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


# Create your views here.
class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[:5]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        categories = request.GET.get('categories', '')
        print(categories)
        if categories:
            categories = categories.split(',')
            jobs = jobs.filter(category_id__in=categories)
        query = request.GET.get('query', '')
        if query:
            jobs = jobs.filter(title__icontains=query)
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)


class JobsDetailView(APIView):
    def get(self, request, pk, format=None):
        jobs = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(jobs)

        return Response(serializer.data)
