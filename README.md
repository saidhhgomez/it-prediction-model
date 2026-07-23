# AI Career Prediction Platform

This project was developed to help students analyze their professional profile and obtain an estimated prediction about their future career in the AI and Data field. The system combines Machine Learning, FastAPI, PostgreSQL, OpenAI API and a layered architecture to provide predictions and personalized feedback.

### Prerequisites

To run this project it is necessary:

- **Python** : Programming language, version **3.10.0**
- **Visual Studio Code** : IDE for development.
- **virtualenv** : Tool to create isolated Python environments.
- **Git** : To clone the repository.
- **Supabase PostgreSQL** : Database service.
- **OpenAI API Key** : Required for AI-generated feedback.

### Installing

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   ```

2. **Open the project in Visual Studio Code**

3. **Download the trained models**
   - Download the **models** folder from:
     - [IT Machine Learning Trained Model](https://drive.google.com/drive/folders/1WImBRbZoCla8kQixFMWOflLK3TtdXUf3?usp=sharing)
   - Copy the **models** folder into the root of the project.

4. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

5. **Activate the virtual environment**

   Windows:
   ```bash
   .venv\Scripts\activate
   ```

6. **Install all dependencies**
   ```bash
   pip install -r requirements.txt
   ```

7. **Create the environment variables**

   Create a **.env** file in the root of the project.

   Example:

   ```text
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_HOST=your_database_host
   DB_PORT=6543
   DB_NAME=your_database_name

   OPENAI_API_KEY=your_openai_api_key
   ```

8. **Run the FastAPI server**
   ```bash
   uvicorn backend.main:app --reload
   ```

9. **Run the Frontend**

   Open a new terminal and navigate to the frontend folder:

   ```bash
   cd frontend
   ```

   Install all Node.js dependencies:

   ```bash
   npm ci
   ```

   Start the development server:

   ```bash
   npm run dev
   ```

   The frontend will be available at:

   ```
   http://localhost:3000
   ```

## Technologies

This project was developed using:

- Python
- FastAPI
- Scikit-Learn
- Pandas
- PostgreSQL (Supabase)
- OpenAI API
- Uvicorn
- Joblib

## Project Architecture

The project follows a layered architecture to make the code easier to maintain and integrate with other applications through REST APIs.

Main layers:

- Routers
- Services
- Schemas
- Database
- Machine Learning Models

The prediction models are independent from the business logic, allowing each component to be maintained separately.

## Usage

This project can be used as a learning resource for students or developers interested in Machine Learning, FastAPI, REST APIs and AI integration.

The system predicts:

- Future Demand
- Automation Risk
- Career Growth
- Salary Projection

It also generates personalized professional feedback using the OpenAI API.

Please do not use this project for commercial purposes.

## Acknowledgments

This project was completely developed by me as a personal learning project to improve my knowledge in Artificial Intelligence, Machine Learning, Backend Development and API integration.