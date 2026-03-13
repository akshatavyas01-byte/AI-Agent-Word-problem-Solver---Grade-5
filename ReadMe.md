# Word problem Solver - Grade 5
## 1. Overview
``This project implements an AI agent that solves Grade 5 mathematical word problems.``

 When a user submits a word problem, the agent analyzes the text, selects the required arithmetic operation, and solves it step-by-step using tools such as Addition, Subtraction, Multiplication, and Division.


## 2. Problem Statement

#### Grade 5 students often struggle to identify which arithmetic operation to use in word problems.

This project introduces an AI agent that analyzes the problem, selects the correct operation, and provides a clear step-by-step solution.

## 3. Solution Approach

#### This project uses an LLM-powered agent with predefined tools such as Addition, Subtraction, Multiplication, and Division.
#### Given a word problem, the agent:
    1. Interprets the question
    2. Chooses the correct arithmetic operation
    3. Uses predefined tools:
        - Addition
        - Subtraction
        - Multiplication
        - Division
    4. Produces a step-by-step solution
    The focus of this project is to build a working AI agent capable of reasoning through problems and streaming responses to the user interface.

## 4. Key Features
    - Submit Grade 5 word problems through the interface.
    - Receive step-by-step solutions streamed in real time.
    - View the last five previously solved problems stored in the database.

## 5. System Architecture

    - Frontend - Streamlit
    - LLM - Hugging Face (zai-org/GLM-5)
    - LLM-Orchestration - LangChain
    - Storage - SQLite Database

## 6. Tech Stack

    - **Language:** Python  
    - **Frontend:** Streamlit  
    - **LLM Orchestration:** LangChain  
    - **Model Provider:** Hugging Face (zai-org/GLM-5)
    - **Environment Management:** python-dotenv  

## 7. How It Works (Execution Flow)
    1. User Submission
    - The user enters a word problem in the interface and clicks Solve.

    2. Agent Reasoning
    - The word problem is sent to the AI agent along with the set of available arithmetic tools.
    - The agent analyzes the problem and determines which operation may be required.
    - It then selects a tool, sends the input to the tool, receives the output, and analyzes the result.
    - This step-by-step reasoning process continues until the agent reaches a final solution.
    - During this process, the reasoning steps are streamed to the user in real time.

    3. Solution Display
    - Once the agent finishes reasoning, the final solution is displayed to the user.

    4. Database Storage
    - The word problem and its final solution are stored in the messages table as Human and AI entries.
    - The application retrieves and displays the last five entries from the table as Question and Answer.

## 8. Example Input & Output
### 1. Docker Run
![Docker Run](images\docker_run.png)

### 2. Streamlit UI:
![Streamlit UI](images\streaming.png)

### 3. Upload Word Problem:
![Word Problem Uploaded system thinking](images\Thinking.png)

### 4. Streamed Answer
![Answer Streamed](images\Answer.png)

### 5. History
![History 1](images\histoy.png)
![History 2](images\history2.png)

### 6.Video Demo
[![Watch Demo](images\streaming.png)](https://www.youtube.com/watch?v=7o6yV1BGRDo)


## 9. Installation & Setup
### 1. Clone the Repository:
```python
git clone https://github.com/your-username/risk-analyser.git
cd risk-analyser
```
### 2. Create Virtual Environment
```python
python -m venv .venv
```
### Activate it:
Windows vscode terminal:
```python
.venv\Scripts\Activate.ps1
```
### 3. Install Dependencies
```python
pip install -r requirements.txt
```
### 4. Add Environment Variables
Create a .env file and add:
```python
api_key=your_api_key_here
```

## 10. Usage 
### 1. Run the streamlit frontend:
```python
streamlit run main/UI.py
```
### 3. Open the browser and:
    - Enter a word problem
    - Click Solve
    - View streamed step-by-step solution of the word problem.

### 4. The last 5 generated solution with its word problem remain visible.

### With DOCKER
### 1. Build the docker image:
```python
docker build -t problem_solver .
``` 
### 2. Run the container:
```python
docker run -p 8051:8051 --env-file .env problem_solver 
```
### 3. Open the application in your browser and enter a word problem.

## 11. Project Structure

     project/
            |── main/
            |   |── agent.py
            |   |── UI.py
            |   |── database.db
            |
            |── images/
            |
            |
            |── .env
            |
            |── dockerfile
            |── start.sh
            |
            |── requirements.txt
            |
            └── ReadMe.md

## 12. Limitations   
    - Limited to basic arithmetic operations only(Addition, Subtraction, Multiplication & Division)
    - No user authentication system
    - No per-user session data storage
    - No caching for repeated questions
    - No request rate limiting or API usage control

## 13. Future Improvements
    - Add support for more complex arithmetic operations
    - Implement a user authentication system
    - Add per-user session data storage
    - Implement caching for repeated questions
    - Add request rate limiting or API usage control


## 14. License
This project is licensed under the MIT License.

## 15. Author
**Akshata Vyas**  
GitHub: [akshatavyas01-byte](https://github.com/akshatavyas01-byte)