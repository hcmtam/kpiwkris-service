ANALYZE_ASSISTANT_PROMPT = "You are an analytical assistant who helps to identify keywords in a given text. You can group the found keywords into categories."

ANALYZE_ASSISTANT_FORMAT = {
    "requirementKeywords": {
        "SoftwareDevelopment": [
            "clean code",
            "maintainable code",
            "scalable code",
            "custom features",
            "technical implementation",
            "software architecture",
            "development paradigms",
        ],
        "Collaboration": [
            "project stakeholders",
            "development team",
            "user-friendly systems",
            "knowledge sharing",
        ],
        "ProcessAndLearning": [
            "ownership",
            "learning opportunities",
        ],
    },
    "passageKeywords": {
        "WebDevelopment": [
            "Typescript",
            "React",
            "Angular",
        ],
        "ProgrammingLanguages": ["Python", "Typescript", "JavaScript"],
        "CollaborationTools": ["Git", "Visual Studio", "Figma", "Postman"],
        "BackendDatabases": [
            "microservices",
            "MongoDB",
            "MySQL",
            "RestAPI",
        ],
        "CloudHosting": ["Azure", "AWS"],
        "DesignConcepts": ["data modeling", "system design", "CMS"],
        "OtherTools": ["Docker", "RxJS", "SSO"],
    },
}

ENHANCE_ASSISTANT_PROMPT = "You are an analytical assistant who helps to enhance content by given keywords and passage. You can recommend similar words to the keywords and achieve a higher matched content for given passage. You can group these recommendations into categories."

ENHANCE_ASSISTANT_FORMAT = {
    "enhancement": {
        "SoftwareDevelopment": [
            "Add 'system design' and 'data modeling' to Text 1",
            "Replace 'scalable code' with 'microservices'",
        ],
        "Collaboration": [
            "Add 'collaboration tools' like Git, Figma to Text 1",
            "Use 'stakeholders' or 'mentorship' in Text 2",
        ],
        "ProcessAndLearning": [
            "Include 'testing and monitoring tools' in Text 2",
            "Add Docker and Postman explicitly in Text 1",
        ],
        "CloudHosting": ["Mention AWS and Azure in Text 1"],
        "DesignConcepts": [
            "Replace 'features' with 'CMS' in Text 1",
            "Add 'UI/UX' in Text 1 under design aspects",
        ],
    },
    "passageKeywords": {
        "SoftwareDevelopment": [
            "software architecture ↔ system design",
            "software solutions ↔ microservices",
        ],
        "Collaboration": ["collaboration ↔ Git/Figma", "user-friendly systems ↔ UI/UX"],
        "ProcessAndLearning": ["testing ↔ Docker/Postman", "documentation ↔ RestAPI"],
        "DesignConcepts": ["user-friendly systems ↔ UI/UX", "features ↔ CMS"],
    },
}

ASSISTANT_PROMPT = "You are an analytical assistant who helps to identify keywords in a given text. You can group the found keywords into categories. You are able to calculate matched percentage scores to see keywords in given text 2 compared to given 1. You can recommend similar words to the keywords and achieve a higher matched percentage score for given text 2. "

ASSISTANT_FORMAT = {
    "requirementKeywords": {
        "SoftwareDevelopment": [
            "clean code",
            "maintainable code",
            "scalable code",
            "custom features",
            "technical implementation",
            "software architecture",
            "development paradigms",
        ],
        "Collaboration": [
            "project stakeholders",
            "development team",
            "user-friendly systems",
            "knowledge sharing",
        ],
        "ProcessAndLearning": [
            "ownership",
            "learning opportunities",
        ],
    },
    "passageKeywords": {
        "WebDevelopment": [
            "Typescript",
            "React",
            "Angular",
        ],
        "ProgrammingLanguages": ["Python", "Typescript", "JavaScript"],
        "CollaborationTools": ["Git", "Visual Studio", "Figma", "Postman"],
        "BackendDatabases": [
            "microservices",
            "MongoDB",
            "MySQL",
            "RestAPI",
        ],
        "CloudHosting": ["Azure", "AWS"],
        "DesignConcepts": ["data modeling", "system design", "CMS"],
        "OtherTools": ["Docker", "RxJS", "SSO"],
    },
    "matchedKeywords": {
        "SoftwareDevelopment": [
            "software architecture ↔ system design",
            "software solutions ↔ microservices",
        ],
        "Collaboration": ["collaboration ↔ Git/Figma", "user-friendly systems ↔ UI/UX"],
        "ProcessAndLearning": ["testing ↔ Docker/Postman", "documentation ↔ RestAPI"],
        "DesignConcepts": ["user-friendly systems ↔ UI/UX", "features ↔ CMS"],
    },
    "matchedScore": {"current": "30.77%", "optimized": "57.69%"},
    "similarKeywords": {
        "SoftwareDevelopment": [
            "system design (similar to software architecture)",
            "microservices (similar to software solutions)",
        ],
        "Collaboration": [
            "collaboration tools (similar to stakeholders, development team)",
            "UI/UX (similar to user-friendly systems)",
        ],
        "ProcessAndLearning": [
            "Docker/Postman (similar to testing and monitoring)",
            "RestAPI (similar to documentation)",
        ],
        "CloudHosting": ["Azure and AWS (similar to cloud platforms not in Text 1)"],
        "DesignConcepts": [
            "CMS (similar to features)",
            "data modeling (similar to integrations)",
        ],
    },
    "recommendChanges": {
        "SoftwareDevelopment": [
            "Add 'system design' and 'data modeling' to Text 1",
            "Replace 'scalable code' with 'microservices'",
        ],
        "Collaboration": [
            "Add 'collaboration tools' like Git, Figma to Text 1",
            "Use 'stakeholders' or 'mentorship' in Text 2",
        ],
        "ProcessAndLearning": [
            "Include 'testing and monitoring tools' in Text 2",
            "Add Docker and Postman explicitly in Text 1",
        ],
        "CloudHosting": ["Mention AWS and Azure in Text 1"],
        "DesignConcepts": [
            "Replace 'features' with 'CMS' in Text 1",
            "Add 'UI/UX' in Text 1 under design aspects",
        ],
    },
}
