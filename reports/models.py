from django.db import models


class AbstractItem(models.Model):

    """Abstract Item"""

    name = models.CharField("선택가능한 옵션", max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CompanyName(AbstractItem):

    """CompanyName Model Definition"""

    class Meta:
        verbose_name = "사업장명"


class Department(AbstractItem):

    """Department Model Definition"""

    class Meta:
        verbose_name = "부서"


class Rater(AbstractItem):

    """Rater Model Definition"""

    class Meta:
        verbose_name_plural = "평가자"


class Process(AbstractItem):

    """Process Model Definition"""

    class Meta:
        verbose_name_plural = "공정명"


class Place(AbstractItem):

    """Place Model Definition"""

    class Meta:
        verbose_name_plural = "장소"


class RiskType(AbstractItem):

    """Place Model Definition"""

    class Meta:
        verbose_name_plural = "위험 분류"


class Factor(AbstractItem):

    """Place Model Definition"""

    class Meta:
        verbose_name_plural = "유해위험요인"


class AfterPlan(AbstractItem):

    """AfterPlan Model Definition"""

    class Meta:
        verbose_name_plural = "위험성 감소 대책 및 관리 방안"


class ReportContent(models.Model):

    """ReportContent Model Definition"""

    class Meta:
        verbose_name_plural = "리포트 리스트"

    risk_type = models.ForeignKey(
        "RiskType",
        related_name="risk_type",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="위험분류",
    )
    factor = models.ForeignKey(
        "Factor",
        related_name="factor",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="유해위험요인",
    )
    factor_source = models.TextField("유해위험요인 원인")
    row_basis = models.TextField("관련 근거")

    present_measures = models.TextField("현재의 안전보건 조치")
    present_frequency = models.IntegerField("현재 위험성 가능성")
    present_importance = models.IntegerField("현재 위험성 중대성")

    after_plan = models.ManyToManyField(
        "AfterPlan",
        related_name="after_plan",
        blank=True,
        verbose_name="위험성 감소 대책 및 관리 방안",
    )
    after_frequency = models.IntegerField("개선 후 위험성 가능성")
    after_importance = models.IntegerField("개선 후 위험성 중대성")

    improvement_date = models.DateField(("개선 예정일"))
    improvement_officer = models.CharField(
        "개선 책임자",
        max_length=20,
    )
    present_img = models.ImageField(
        upload_to="report_photos",
        verbose_name="개선 전 사진",
        blank=True,
    )
    after_img = models.ImageField(
        upload_to="report_photos",
        verbose_name="개선 후 사진",
        blank=True,
    )

    report = models.ForeignKey(
        "Report",
        related_name="report_content",
        on_delete=models.CASCADE,
        verbose_name="리포트",
    )

    def __str__(self):
        return str(self.risk_type)

    def rating_average(self):
        avg = self.after_frequency * self.after_importance
        return avg


class Report(models.Model):

    """Report Model Definition"""

    class Meta:
        verbose_name_plural = "리포트"

    last_update = models.DateTimeField(auto_now=True)
    company_name = models.ForeignKey(
        "CompanyName",
        related_name="company_name",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="사업장명",
    )
    department = models.ForeignKey(
        "Department",
        related_name="department",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="부서명",
    )
    rater = models.ManyToManyField(
        "Rater",
        related_name="rater",
        blank=True,
        verbose_name="평가자",
    )
    effective_date = models.DateField(("평가 일시"))
    process = models.ForeignKey(
        "Process",
        related_name="process",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="공정명",
    )
    place = models.ForeignKey(
        "Place",
        related_name="place",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="작업명 또는 장소",
    )

    def __str__(self):
        return str(self.company_name)

    def total_rating(self):
        all_report = self.report_content.all()
        all_ratings = 0

        for report in all_report:
            all_ratings += report.rating_average()
        return round(all_ratings / len(all_report), 1)

    total_rating.short_description = "위험성 평균점수"
