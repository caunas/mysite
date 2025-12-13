import pytest

from blog.factories import ProjectFactory

@pytest.fixture
def project_published():
    return ProjectFactory(name_repo="PROJECT FACTORIED")

@pytest.mark.django_db
def test_create_published_project(project_published):
    assert project_published.name_repo == "PROJECT FACTORIED"