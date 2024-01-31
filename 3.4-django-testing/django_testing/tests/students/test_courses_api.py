import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student 
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory
    
@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db(transaction=True)
def test_retrieve_course(client, course_factory):
    course = course_factory(_quantity=2)
    for number in range(len(course)):
        response = client.get(f'/api/v1/courses/{number+1}/')
        data = response.json()
        assert response.status_code == 200, 'Статус должен 200'
        assert data['name'] == course[number].name, 'Отсутствуют данные'

@pytest.mark.django_db(transaction=True)
def test_list_course(client, course_factory):
    course = course_factory(_quantity=2)
    response = client.get('/api/v1/courses/')
    data = response.json()
    assert response.status_code == 200, 'Статус должен 200'
    assert len(course) == len(data), 'Количество созданны и запрошенных не соответствует'
    for i, n in enumerate(data):
        assert n['name'] == course[i].name, 'Отсутствуют данные'

@pytest.mark.django_db(transaction=True)
def test_id_filter_course(client, course_factory):
    course = course_factory(_quantity=2)
    for number in range(len(course)):
        response = client.get(f'/api/v1/courses/?id={course[number].id}')
        data = response.json()
        assert response.status_code == 200, 'Статус должен 200'
        assert data[0]['name'] == course[number].name, 'Отсутствуют данные'

@pytest.mark.django_db(transaction=True)
def test_name_filter_course(client, course_factory):
    course = course_factory(_quantity=2)
    for number in range(len(course)):
        response = client.get(f'/api/v1/courses/?name={course[number].name}')
        data = response.json()
        assert response.status_code == 200, 'Статус должен 200'
        assert data[0]['name'] == course[number].name, 'Отсутствуют данные'

@pytest.mark.django_db(transaction=True)
def test_post_course(client, student_factory):
    student = student_factory(_quantity=2)
    response = client.post("/api/v1/courses/", data={"name": "Django", "students": [student[0].id, student[1].id]}, format='json')
    assert response.status_code == 201, 'Статус должен 201'
    assert response.data['name'] == 'Django', 'Название не соответствует созданному объекту'
    assert len(response.data['students']) == 2, 'Количество студентов не соответствует добавленному'

@pytest.mark.django_db(transaction=True)
def test_put_course(client, student_factory):
    student = student_factory(_quantity=2)
    response_post = client.post("/api/v1/courses/", data={"name": "Django", "students": [student[0].id, student[1].id]}, format='json')
    response_put = client.put("/api/v1/courses/1/", data={'name': 'FastAPI'}, format='json')
    response_get = client.get("/api/v1/courses/1/")
    assert response_put.status_code == 200
    assert response_post.data['name'] != response_put.data['name']
    assert response_get.data['name'] == response_put.data['name']
    assert len(response_post.data['students']) == len(response_get.data['students'])

@pytest.mark.django_db(transaction=True)
def test_delete_course(client, course_factory):
    course = course_factory(_quantity=2)
    response = client.delete('/api/v1/courses/1/')
    response_get = client.get('/api/v1/courses/1/')
    assert response.status_code == 204
    assert response_get.status_code == 404

@pytest.mark.django_db(transaction=True)
def test_accepted_valid_course(client, course_factory, student_factory):
    course = course_factory(_quantity=2)
    student = student_factory(_quantity=21)
    list_ = []
    for i in range(20):
        list_.append(student[i].id)
    response_put = client.patch('/api/v1/courses/1/', data={'students': list_}, format='json')
    assert len(response_put.data.get('students', 0)) == 20
    list_.append(20)
    response_put = client.patch('/api/v1/courses/1/', data={'students': list_}, format='json')
    assert response_put.data.get('students') == None