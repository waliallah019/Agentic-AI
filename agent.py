# agent.py
# Contains the Agent class which takes a goal and breaks it into subtasks.
# It uses Groq API when available, otherwise falls back to a local mock.

import requests
import json

API_KEY = "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"
USE_API = False   # Change to True if you want real Groq API calls


class Agent:
    def __init__(self):
        self.model = "llama-3.3-70b-versatile"
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def _mock_response(self, goal):
        # Simple offline fallback response
        return [
            f"Define the goal clearly: {goal}",
            "Identify required resources",
            "Create a timeline",
            "Break work into tasks",
            "Review and adjust the plan"
        ]

    def generate_subtasks(self, goal):
        """Generate 3–5 subtasks from a goal."""

        if not USE_API:
            return self._mock_response(goal)

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"Break this goal into 3-5 short actionable subtasks: {goal}"

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }

        response = requests.post(self.api_url, headers=headers, json=payload)

        if response.status_code == 200:
            text = response.json()["choices"][0]["message"]["content"]
            lines = [t.strip("-• ") for t in text.split("\n") if t.strip()]
            return lines[:5]
        else:
            return self._mock_response(goal)
