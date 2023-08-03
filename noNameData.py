#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/2/21 14:38
# @Author  : Allan Wei
# @File    : testData2023.py
from faker import Faker
import pandas as pd

fake = Faker()

data = []
for i in range(50000):
    # name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    school = fake.company()
    company = fake.company()
    skills = fake.random_elements(elements=('Python', 'Java', 'C++', 'JavaScript', 'HTML', 'CSS'), length=3, unique=True)
    major = fake.job()
    title = fake.random_element(elements=('Software Engineer', 'Data Analyst', 'Web Developer', 'Product Manager', 'Marketing Specialist'))
    tag = fake.random_element(elements=('Beginner', 'Intermediate', 'Advanced', 'Expert'))
    data.append([email, phone, school, company, skills, major, title, tag])

df = pd.DataFrame(data, columns=['Email', 'Phone', 'School', 'Company', 'Skills', 'Major', 'Title', 'Tag'])
df.to_excel('data005.xlsx', index=False)