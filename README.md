A small educational project demonstrating core Agentic AI concepts:

- Goal → subtasks (Agent)
- Tool use (time estimator)
- Reflection (clarity improvement)
- Objective & subjective evaluation
- Log saving

This project uses:
- Python only
- Mocked LLM responses for offline use
- Optional Groq API integration (set `USE_API = True` in agent.py)

---

## Folder Structure

goal_planner/
│
├── agent.py
├── tools.py
├── evaluate.py
├── main.py
└── README.md

yaml
Copy code

---

## Running the project

1. Ensure Python 3.8+ is installed.
2. Open terminal in `goal_planner/`.
3. Run:

python main.py

cpp
Copy code

4. Enter any goal, e.g.:

I want to start a YouTube channel

yaml
Copy code

Evaluations will be saved in **evaluation_log.txt**.

---

## Enabling Groq API (optional)

In `agent.py`, set:

USE_API = True

diff
Copy code

The project already includes:
- Groq API key (as provided)
- llama-3.3-70b-versatile model
