from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.pagination import PageNumberPagination

from api.models import Student
from api.serializers import StudentSerializer


class StudentsResultsPagination(PageNumberPagination):
    """
    Количество выводимых студентов при запросе.
    """
    page_size = 10


class StudentViewSet(viewsets.ModelViewSet):
    """
    Эндпоинт API позволяющий просматривать, удалять
    или редактировать студентов.
    """
    queryset = Student.objects.all().order_by('surname')
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = StudentsResultsPagination
