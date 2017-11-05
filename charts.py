from __future__ import division
import os
import pandas as pd
from collections import OrderedDict
from werkzeug.contrib.fixers import ProxyFix
from flask import Flask, render_template

app = Flask(__name__)

onboarding_stage = [0, 20, 40, 50, 70, 90, 95, 99, 100]


def import_data(file_path):
    with open(file_path, "rb") as csvfile:
        df = pd.read_csv(csvfile)
        percentage = df['onboarding_percentage']
        return percentage


def analyze_data(cohort):
    user_count = OrderedDict()
    user_count[0], user_count[20], user_count[40], user_count[50], user_count[
        70], user_count[90], user_count[95], user_count[99], user_count[100] = 0, 0, 0, 0, 0, 0, 0, 0, 0
    total_users = 0

    for num in cohort:
        if int(num) not in onboarding_stage:
            pass
        total_users += 1
        key = int(num)
        user_count[key] += 1
        for stage in onboarding_stage:
            if stage < key:
                user_count[stage] = user_count[stage] + 1
    stage_percentages = [int(kwargs / total_users * 100)
                         for args, kwargs in user_count.items()]
    print(user_count)

    return stage_percentages


def get_cohorts():
    file_path = os.path.join(app.root_path, 'export.csv')
    cohorts = import_data(file_path)
    return cohorts


@app.route('/')
def chart():
    cohort = get_cohorts()
    cohort1 = cohort[1:112]
    cohort2 = cohort[112:246]
    cohort3 = cohort[246:307]
    cohort4 = cohort[307:338]
    d1 = analyze_data(cohort1)
    d2 = analyze_data(cohort2)
    d3 = analyze_data(cohort3)
    d4 = analyze_data(cohort4)
    return render_template('index.html', d1=d1, d2=d2, d3=d3, d4=d4, levels=onboarding_stage)


@app.route('/cohort1')
def cohort_one():
    cohort_data = get_cohorts()
    cohort = cohort_data[1:112]
    data = analyze_data(cohort)
    return render_template('cohort1.html', data=data, name='Cohort I', levels=onboarding_stage)


@app.route('/cohort2')
def cohort_two():
    cohort_data = get_cohorts()
    cohort = cohort_data[112:246]
    data = analyze_data(cohort)
    return render_template('cohort2.html', data=data, name='Cohort II', levels=onboarding_stage)


@app.route('/cohort3')
def cohort_three():
    cohort_data = get_cohorts()
    cohort = cohort_data[246:307]
    data = analyze_data(cohort)
    return render_template('cohort3.html', data=data, name='Cohort III', levels=onboarding_stage)


@app.route('/cohort4')
def cohort_four():
    cohort_data = get_cohorts()
    cohort = cohort_data[307:338]
    data = analyze_data(cohort)
    return render_template('cohort4.html', data=data, name='Cohort IV', levels=onboarding_stage)


@app.route('/404')
def error_404():
    return render_template('404.html')


app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
