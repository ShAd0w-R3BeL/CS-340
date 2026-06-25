🐺 CS-340: Client/Server Development
🌙 Building Database-Driven Foundations
📌 Overview

This repository contains the projects and assignments completed for CS-340: Client/Server Development at SNHU.

This course focuses on applying database systems concepts to develop robust applications that interface client-side Python code with MongoDB 6.x.

🎯 Course Competencies

CS-30433: Apply database systems concepts and principles in the development of a client/server application.  

CS-30434: Create a database that can interface with client-side code.  

CS-30435: Develop client-side code that interfaces with databases.  

🛠 Tech Stack & Tools

Language: Python

Database: MongoDB 6.x

Driver: PyMongo

Environment: Codio

Visualization: Dash, Plotly, Dash-Leaflet (utilizing dl.MarkerClusterGroup for performance)

Key Concepts: CRUD Operations, Data Aggregation Pipelines, Dashboard Data Visualization, and Client/Server Architecture.

📂 Project Highlights

Project One: CRUD Implementation

Objective: Developing core functionality for database interaction and data manipulation.

Key Artifacts: crud.py (modular database interface) and ProjectOneTestScript.ipynb.

Project Two: Dashboard & Visualization

Objective: Implementing a database-driven dashboard to visualize inventory data and streamline backend management.

Key Artifacts: ProjectTwoDashboard.ipynb.

Proof of Execution: Confirmed via server logs showing successful initialization on port 8000 and connection to the aac database.

📖 Reflective Journal (Module Eight)

Maintainability and Adaptability

To write maintainable code, I utilized the Model-View-Controller (MVC) pattern.

By creating the AnimalShelter class in crud.py, I decoupled my database logic from the UI.

This allowed me to test CRUD functionality independently and ensured that the dashboard remained stable even when modifying the underlying data schema.

Computer Scientist’s Approach

My approach centered on deconstruction and iterative development.

I first mapped the client’s requirements to the MongoDB schema, then built the backend logic before tackling the visualization.

When faced with Codio network isolation, I documented the successful server initialization as proof of application readiness, highlighting that the environment's internal firewall was the sole factor preventing remote access.

The Role of Computer Science

Computer scientists act as bridge-builders between raw data and actionable intelligence.

My work for Grazioso Salvare helps the company automate the retrieval and visualization of rescue records, allowing stakeholders to identify breed trends and rescue outcomes instantly.

⚖️ Academic Integrity & AI Disclosure

Academic Purpose: This work was completed for academic purposes at Southern New Hampshire University.

AI Usage: Generative AI tools were used as supplemental aids for brainstorming and formatting, consistent with university policy on critical thinking.

🚀 Getting Started

To explore the code, clone this repository:

git clone https://github.com/ShAd0w-R3BeL/CS-340.git

🌙 Contact

Name: Matthew Wood

Email: matthew.wood16@snhu.edu

LinkedIn: Matthew R. Wood
