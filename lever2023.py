#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/5/11 15:30
# @Author  : Allan Wei
# @File    : lever2023.py
import requests
from faker import Faker


url = 'https://api.sandbox.lever.co/v1/postings?perform_as=562f92f1-7191-41fc-b144-1897b95b2ee7'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic Q04rT3IvU2dWb21haHk3dU43Zm9BMnVqdWR6cnFnek1QL2ZvMFV1MlcrWW9jazE4'
}
fake = Faker()
text_value = fake.word()
data = {
    "text": text_value,
    "owner": "562f92f1-7191-41fc-b144-1897b95b2ee7",
    "categories": {
        "commitment": "Full-time",
        "department": "R&D",
        "location": "Mountain View",
        "team": "Machine Learning"
    },
    "content": {
        "descriptionHtml": "<div>The <u><b>Infrastructure Engineer</b></u> will act as...</div><div>Superman.</div>",
        "lists": [
            {
                "text": "Job requirements",
                "content": "<li>Quick learner</li><li>Ambitious</li>"
            }
        ],
        "closingPostingHtml": "<div>Our <a href=\"\">company</a> is <span>proud</span> to be an equal opportunity workplace.</div>"
    },
    "tags": [
        "engineering",
        "high-priority"
    ],
    "state": "published",
    "distributionChannels": [
        "internal",
        "public"
    ],
    "workplaceType": "onsite",
    "salaryDescriptionHtml": "<p>This is a salary description.</p>",
    "salaryRange": {
        "max": 60000,
        "min": 40000,
        "currency": "USD",
        "interval": "per-year-salary"
    }
}
for i in range(5):
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)