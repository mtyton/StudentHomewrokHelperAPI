from django.db import models


class BaseContactModel(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class College(BaseContactModel):
    """
    Model for keeping all available colleges, downloaded
    from Ministry of Education website.
    """
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=300, unique=True)
    is_national = models.BooleanField()
    created = models.BooleanField()

    def __str__(self):
        return str(self.name)


class CollegeDepartment(models.Model):
    """
    Department of given college, it is created by users
    """
    name = models.CharField(max_length=255)
    college = models.ForeignKey("College", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.college) + " " + str(self.name)


class DepartmentMajor(models.Model):
    """
    Model keeps data about exact departments majors
    """
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        "CollegeDepartment", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.department) + " " + str(self.name)


class Degree(models.Model):
    """
    The degree that student tries to get on department major
    """
    degree_name = models.CharField(max_length=255)

    def __str__(self):
        return self.degree_name


class Semester(models.Model):
    """
    Semester number of degree
    """
    degree = models.ForeignKey("Degree", on_delete=models.CASCADE)
    number = models.IntegerField()

    def __str__(self):
        return str(self.degree) + " " + str(self.number)
