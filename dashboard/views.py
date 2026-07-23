from students.models import Student
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Max, Min
import pandas as pd


@login_required
def dashboard(request):

    total = Student.objects.count()

    avg_math = Student.objects.aggregate(
    Avg('math_score')
)['math_score__avg']

    avg_science = Student.objects.aggregate(
    Avg('science_score')
)['science_score__avg']

    avg_english = Student.objects.aggregate(
    Avg('english_score')
)['english_score__avg']

    max_score = Student.objects.aggregate(
    Max('math_score')
)['math_score__max']

    min_score = Student.objects.aggregate(
    Min('math_score')
)['math_score__min']

    male = Student.objects.filter(
        gender='Male'
    ).count()

    female = Student.objects.filter(
        gender='Female'
    ).count()

    df = pd.DataFrame(
        list(Student.objects.values())
    )

    avg_subjects = df[
        [
            'math_score',
            'science_score',
            'english_score'
        ]
    ].mean()

    best_subject = avg_subjects.idxmax()
    worst_subject = avg_subjects.idxmin()

    best_gender = df.groupby(
        'gender'
    )['math_score'].mean().idxmax()

    best_lunch = df.groupby(
        'lunch'
    )['math_score'].mean().idxmax()

    best_preparation = df.groupby(
        'test_preparation'
    )['math_score'].mean().idxmax()


    pass_count = Student.objects.filter(
    math_score__gte=50,
    science_score__gte=50,
    english_score__gte=50
    ).count()

    fail_count = total - pass_count
    pass_ratio = (pass_count / total) * 100
    fail_ratio = (fail_count / total) * 100
    
    context = {

        'total': total,
        'avg_math': avg_math,
        'avg_science': avg_science,
        'avg_english': avg_english,
        'max_score': max_score,
        'min_score': min_score,
        'male': male,
        'female': female,
        'best_subject': best_subject,
        'worst_subject': worst_subject,
        'best_gender': best_gender,
        'best_lunch': best_lunch,
        'best_preparation': best_preparation,
        'pass_count': pass_count,
        'fail_count': fail_count,
        'pass_ratio': round(pass_ratio,2),
        'fail_ratio': round(fail_ratio,2),
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context,
    )