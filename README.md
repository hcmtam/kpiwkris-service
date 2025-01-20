# KPI with Kris - Backend

This project is a web application backend built using Django. It leverages OpenAI's API for AI analysis of input content, provides suggestions based on the analysis, and calculates a KPI achieved score. The application also utilizes Redis for session management, allowing users to return to their sessions and bookmark them for future access.

## Features

- **AI Analysis** : Integrates with OpenAI to analyze user input and provide actionable suggestions.

- **KPI Scoring**: Computes a KPI achieved score based on user input and AI analysis.

- **Session Management**: Uses Redis to store session data, enabling users to resume their sessions easily.

- **Bookmarking**: Allows users to bookmark their sessions, which are then stored in the database for easy retrieval.

- **Retrieving Bookmarks**: Users can view and revisit their bookmarked sessions at any time.

## Getting Started

### Prerequisites

Make sure you have the following prepared:

- Python 3.8+
- Django 3.2+
- Redis (personally suggested use upstash https://upstash.com/ to host redis )

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or feedback, feel free to open an issue.
