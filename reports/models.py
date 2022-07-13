from django.db import models


class AbstractItem(models.Model):
    """Abstract Item"""

    name = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.name


class DepartmentType(AbstractItem):
    pass


class ProcessType(AbstractItem):
    pass


class Company(AbstractItem):
    pass


class Report(models.Model):

    """Report Model"""

    # 공통
    updated = models.DateTimeField("업데이트 날짜", null=True, blank=True)
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        null=True,
    )
    department = models.ForeignKey(
        DepartmentType,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="부서명",
        related_name="department",
    )
    process = models.ForeignKey(
        ProcessType, on_delete=models.CASCADE, null=True, verbose_name="공정명"
    )

    operation = models.CharField("작업내용", max_length=70)
    effective_date = models.DateField(("실시 일자"))
    # 개선 전 위험성
    prev_image = models.FileField("개선 전 이미지", upload_to="notice", null=True, blank=True)
    prev_risk = models.TextField("개선 전 유해인자", null=True)
    prev_frequency = models.IntegerField("개선 전 빈도", blank=True, null=True)
    prev_importance = models.IntegerField("개선 전 중요도", blank=True, null=True)

    # 개선 후 위험성
    after_image = models.FileField(
        "개선 후 이미지", upload_to="notice", null=True, blank=True
    )
    after_risk = models.TextField("개선 대책", null=True)
    after_frequency = models.IntegerField("개선 후 빈도", blank=True, null=True)
    after_importance = models.IntegerField("개선 후 중요도", blank=True, null=True)

    improvement_date = models.DateField(("개선 예정일"), blank=True, null=True)
    improvement_officer = models.CharField(
        "개선 책임자", max_length=20, blank=True, null=True
    )
    is_completion = models.BooleanField("완료여부", default=False, blank=True, null=True)

    def __str__(self):
        return str(self.company)
