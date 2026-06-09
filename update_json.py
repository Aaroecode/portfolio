import json

# Update portfolio.json
with open('public/data/sections/portfolio.json', 'r') as f:
    portfolio = json.load(f)

portfolio['articles'][0]['items'] = [
    {
        "id": 1,
        "categoryId": "category_utilities",
        "img": "",
        "faIcon": "fa-solid fa-server",
        "faIconColors": {"bg": "#7671AA", "fill": "#EEEEEE"},
        "preview": {
            "links": [],
            "screenshots": [],
            "screenshotsAspectRatio": "",
            "youtubeVideo": ""
        },
        "locales": {
            "en": {
                "title": "Minecraft Server Infrastructure",
                "text": "Architected and managed Dockerized game server infrastructure with 99%+ uptime over 2 years. Optimized performance for 20+ players and led 12 contributors.",
                "tags": ["Python", "Docker", "Linux", "DevOps"]
            }
        }
    },
    {
        "id": 2,
        "categoryId": "category_utilities",
        "img": "",
        "faIcon": "fa-solid fa-qrcode",
        "faIconColors": {"bg": "#007396", "fill": "#EEEEEE"},
        "preview": {
            "links": [],
            "screenshots": [],
            "screenshotsAspectRatio": "",
            "youtubeVideo": ""
        },
        "locales": {
            "en": {
                "title": "QR-Based Ticketing System",
                "text": "Designed an automated QR-based ticketing and bulk email distribution system sending 200+ emails per execution. Managed self-hosted mail server with 0 downtime.",
                "tags": ["Python", "FastAPI", "Docker", "Linux"]
            }
        }
    }
]

with open('public/data/sections/portfolio.json', 'w') as f:
    json.dump(portfolio, f, indent=4)


# Update skills.json
with open('public/data/sections/skills.json', 'r') as f:
    skills = json.load(f)

# Article 1 is general skills
# Article 2 is Backend Stack
# Article 3 is DevOps Stack
# Article 4 is AI & ML Stack
# Article 5 is Languages (ID 4)

# Re-write the items for Article 2, 3, 4 based on resume.

for article in skills.get('articles', []):
    if article.get('id') == 2: # Backend Stack
        article['items'] = [
            {
                "id": 1, "img": "", "faIcon": "fa-brands fa-python", "faIconColors": {"bg": "", "fill": "#ffde57"},
                "date": {"year": 2024, "month": 1}, "percentage": 95,
                "locales": {"en": {"title": "Python", "text": "Building reliable backend systems and automation.", "level": "Core"}}
            },
            {
                "id": 2, "img": "", "faIcon": "fa-solid fa-server", "faIconColors": {"bg": "", "fill": "#009688"},
                "date": {"year": 2024, "month": 1}, "percentage": 90,
                "locales": {"en": {"title": "FastAPI & Flask", "text": "Building scalable REST APIs and webhooks.", "level": "Core"}}
            },
            {
                "id": 3, "img": "", "faIcon": "fa-solid fa-database", "faIconColors": {"bg": "", "fill": "#336791"},
                "date": {"year": 2024, "month": 1}, "percentage": 85,
                "locales": {"en": {"title": "PostgreSQL", "text": "Database management, querying, and optimization.", "level": "Core"}}
            }
        ]
    elif article.get('id') == 3: # DevOps Stack
        article['items'] = [
            {
                "id": 1, "img": "", "faIcon": "fa-brands fa-docker", "faIconColors": {"bg": "", "fill": "#0db7ed"},
                "date": {"year": 2024, "month": 1}, "percentage": 90,
                "locales": {"en": {"title": "Docker", "text": "Containerizing applications for deployment.", "level": "Core"}}
            },
            {
                "id": 2, "img": "", "faIcon": "fa-brands fa-linux", "faIconColors": {"bg": "", "fill": "#000000"},
                "date": {"year": 2024, "month": 1}, "percentage": 85,
                "locales": {"en": {"title": "Linux & Nginx", "text": "Managing servers and configuring reverse proxies.", "level": "Core"}}
            },
            {
                "id": 3, "img": "", "faIcon": "fa-solid fa-code-branch", "faIconColors": {"bg": "", "fill": "#bd2c00"},
                "date": {"year": 2024, "month": 1}, "percentage": 80,
                "locales": {"en": {"title": "CI/CD & Cloud", "text": "GitHub Actions, GCP, and DigitalOcean.", "level": "Core"}}
            }
        ]
    elif article.get('id') == 3: # Wait, in original skills.json, AI & ML Stack was also id 3 (a duplicate id). It was the 3rd article in the array but the id field was 3. Let's just iterate by index or check title.
        pass

for index, article in enumerate(skills.get('articles', [])):
    title_en = article.get('locales', {}).get('en', {}).get('title', '')
    if title_en == "AI & ML Stack":
        article['items'] = [
            {
                "id": 1, "img": "", "faIcon": "fa-solid fa-brain", "faIconColors": {"bg": "", "fill": "#ff9800"},
                "date": {"year": 2024, "month": 1}, "percentage": 85,
                "locales": {"en": {"title": "NLP & Transformers", "text": "Hugging Face, LLM APIs, and LangChain integration.", "level": "Core"}}
            },
            {
                "id": 2, "img": "", "faIcon": "fa-solid fa-magnifying-glass-chart", "faIconColors": {"bg": "", "fill": "#2196f3"},
                "date": {"year": 2024, "month": 1}, "percentage": 80,
                "locales": {"en": {"title": "Elasticsearch", "text": "Designing fast search and analytics pipelines.", "level": "Core"}}
            }
        ]

with open('public/data/sections/skills.json', 'w') as f:
    json.dump(skills, f, indent=4)


# Update contact.json
with open('public/data/sections/contact.json', 'r') as f:
    contact = json.load(f)

# The second article contains the items
for article in contact.get('articles', []):
    if article.get('id') == 2:
        # Find and remove instagram (id 5)
        article['items'] = [item for item in article.get('items', []) if item.get('id') != 5]

with open('public/data/sections/contact.json', 'w') as f:
    json.dump(contact, f, indent=4)

print("Updates completed successfully.")
