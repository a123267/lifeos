# LifeOS — Personal Productivity & Analytics Platform

## 1. Project Overview

LifeOS is a full-stack personal productivity application that combines daily
planning, weekly goal management, habit tracking, and productivity analytics.

The project is designed to demonstrate how application development and data
engineering can work together in a single system.

LifeOS will capture productivity activity, process historical data through
an ETL pipeline, and transform it into meaningful insights through an
analytics dashboard.

AI-powered planning and productivity recommendations are planned as future
enhancements.

## 2. Key Features

### Productivity Management
- Create, update, complete, delete, and reschedule daily tasks.
- Organise tasks by category and priority.
- Create weekly goals and track progress.
- Track recurring habits and completion history.

### Data Engineering
- Store application data in a relational database.
- Capture meaningful activity events.
- Extract activity records incrementally.
- Validate data and handle duplicate or invalid records.
- Transform activity data into analytical datasets.
- Load results into analytics tables.
- Monitor pipeline execution and data quality.

### Analytics and Visualisation
- Analyse task completion rates.
- Compare planned and actual time.
- Monitor habit consistency and weekly goal achievement.
- Explore productivity trends over time.
- Visualise analytical results through an interactive dashboard.

### Software Engineering
- Develop REST APIs using Python and FastAPI.
- Validate requests and handle errors.
- Write automated tests.
- Use Git and GitHub for version control.
- Containerise the application using Docker.
- Document setup and deployment procedures.

### Planned AI Enhancements
- AI-assisted weekly planning.
- Data-informed productivity recommendations.
- Natural-language task management.
- AI-based task prioritisation.

AI features will be introduced after the core application and analytics
pipeline are established.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, FastAPI |
| Database | MySQL |
| ORM | SQLAlchemy |
| Request Validation | Pydantic |
| Data Processing | Pandas |
| Analytics | SQL, Python |
| Visualisation | Chart.js |
| Testing | Pytest |
| Version Control | Git, GitHub |
| Containerisation | Docker |
| AI (Future Phase) | LLM API or local model |

## 4. Planned Implementation Stages

The project will be developed incrementally.

1. **Project Foundation**
   - Set up the development environment.
   - Configure FastAPI and MySQL.
   - Establish the initial database schema.

2. **Core Backend**
   - Implement task, habit, and weekly goal APIs.
   - Add request validation, error handling, and activity logging.

3. **Frontend Development**
   - Build the planner, dashboard, and habit-tracking interface.
   - Connect the frontend to the backend APIs.

4. **ETL Pipeline**
   - Extract activity data.
   - Validate and transform records.
   - Load analytical tables.
   - Monitor pipeline execution and data quality.

5. **Analytics Dashboard**
   - Calculate productivity metrics.
   - Visualise trends and goal progress.
   - Validate analytical results.

6. **Testing and Reliability**
   - Test APIs, business rules, database operations, and ETL transformations.
   - Verify duplicate handling and pipeline reruns.

7. **Containerisation and Deployment**
   - Configure Docker.
   - Document setup and execution.
   - Deploy the application if suitable hosting is available.

8. **AI Integration**
   - Introduce AI-assisted planning and productivity recommendations.
   - Evaluate recommendations using user feedback.

## 5. Project Status

**Current stage:** Project setup

The implementation will progress through the stages described above.
Features will be marked as complete as they are implemented and tested.

## 6. Security

- Never commit passwords, API keys, or database credentials.
- Keep local environment variables in an untracked `.env` file.
- Provide a `.env.example` file containing placeholder values only.
- Do not publish real personal activity data.

## 7. Project Goals

The primary goals of LifeOS are to:

- Build a practical personal productivity tool.
- Demonstrate backend development and relational database design.
- Implement a reliable, testable ETL pipeline.
- Generate useful analytics from historical activity.
- Explore responsible AI integration using actual application data.
