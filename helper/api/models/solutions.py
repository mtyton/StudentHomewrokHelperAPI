from django.db import models


class WorksheetGroup(models.Model):
    """
    This model describes groups in database, every group means college, department, major, degree and semester
    because for each semester of every degree of every major there will be different worksheets.
    It is used to filter Worksheets.
    """
    department_major = models.ForeignKey("DepartmentMajor", on_delete=models.CASCADE)
    degree = models.ForeignKey("Degree", on_delete=models.CASCADE)
    semester = models.ForeignKey("Semester", on_delete=models.CASCADE)


class WorksheetAuthor(models.Model):
    """
    Author of a worksheet.
    Probably a professor or a doctor on exact college.
    """
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    academic_title = models.CharField(max_length=255)
    college = models.ForeignKey("College", on_delete=models.CASCADE)


class Worksheet(models.Model):
    """
    Simply model to keep worksheet with multiple tasks
    """
    title = models.CharField(max_length=255)
    author = models.ForeignKey("WorksheetAuthor", on_delete=models.CASCADE)


class Task(models.Model):
    """
    Task description assigned to a worksheet
    """
    description = models.CharField(max_length=255)
    worksheet = models.ForeignKey("Worksheet", on_delete=models.CASCADE)


class Solution(models.Model):
    """
    This keeps the solution for given problem
    """
    task = models.ForeignKey("Task", on_delete=models.CASCADE)
    solution_file = models.FileField(upload_to="")
    solution_text = models.CharField(max_length=750)
    solution_rate = models.FloatField()
