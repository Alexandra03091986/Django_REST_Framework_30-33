from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from materials.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор для модели Course.
    Преобразует объекты курсов в JSON и обратно для API.
    Включает все поля модели, включая связанные уроки."""

    class Meta:
        """Метаданные сериализатора курса."""
        model = Course
        fields = "__all__"

class CourseDetailSerializer(ModelSerializer):
    """Сериализатор для модели Course.
    Преобразует объекты курсов в JSON и обратно для API.
    Включает все поля модели, включая связанные уроки."""

    count_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        """Возвращает количество уроков в курсе."""
        return course.lesson_set.count()

    class Meta:
        """Метаданные сериализатора курса."""
        model = Course
        fields = ("name", "count_lessons")

class LessonSerializer(ModelSerializer):
    """Сериализатор для модели Lesson.
    Преобразует объекты уроков в JSON и обратно для API.
    Включает все поля модели и информацию о курсе."""
    class Meta:
        """Метаданные сериализатора урока."""
        model = Lesson
        fields = "__all__"
