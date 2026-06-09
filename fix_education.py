import json

education = {
    "title": {
        "locales": {
            "en": {
                "title_short": "Education",
                "title_short_nav": "Education",
                "title_long_prefix": "This is my",
                "title_long": "{{Education}} Background"
            },
            "es": {
                "title_short": "Educación",
                "title_short_nav": "Educación",
                "title_long_prefix": "Esta es mi",
                "title_long": "{{Formación}} Educativa"
            },
            "fr": {
                "title_short": "Éducation",
                "title_short_nav": "Éducation",
                "title_long_prefix": "C'est mon",
                "title_long": "{{Contexte}} Éducatif"
            },
            "ko": {
                "title_short": "교육",
                "title_short_nav": "교육",
                "title_long_prefix": "이것은 내",
                "title_long": "{{교육적}} 배경"
            }
        }
    },
    "articles": [
        {
            "id": 1,
            "component": "ArticleTimeline",
            "locales": {},
            "settings": {
                "order_items_by": "dateStart",
                "order_items_sort": "desc"
            },
            "items": [
                {
                    "id": 1,
                    "img": "images/pictures/niu.svg",
                    "faIcon": "",
                    "faIconColors": {"bg": "", "fill": ""},
                    "dateStart": {"year": 2022, "month": 7},
                    "dateEnd": {"year": 2026, "month": 6},
                    "locales": {
                        "en": {
                            "title": "{{Bachelor}} of Technology",
                            "province": "",
                            "country": "India",
                            "institution": "Noida International University",
                            "text": "Currently pursuing a Bachelor of Technology degree with a specialization in Computer Science and Engineering. Gained foundational knowledge in programming, data structures, algorithms, and software development principles.",
                            "list": [],
                            "tags": []
                        }
                    }
                }
            ]
        }
    ]
}

with open('public/data/sections/education.json', 'w') as f:
    json.dump(education, f, indent=4)

print("Fixed education.json")
