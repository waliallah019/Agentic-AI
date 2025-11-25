# evaluate.py
# Contains objective and subjective evaluation functions.

def objective_evaluation(plan):
    """Returns step count and word count."""
    steps = len(plan)
    words = sum(len(p.split()) for p in plan)
    return {
        "steps": steps,
        "word_count": words
    }


def subjective_evaluation(plan):
    """
    Mocked LLM-like subjective evaluation.
    No API calls; returns fixed human-like feedback.
    """
    clarity = "Plan is generally clear but could be more concise."
    actionability = "Tasks are actionable and realistic."
    return {
        "clarity": clarity,
        "actionability": actionability
    }


def reflect_plan(plan):
    """Improve clarity by shortening tasks."""
    improved = []
    for p in plan:
        # Simple reflection: remove unnecessary fluff
        cleaned = p.replace("Make sure to ", "").replace("Ensure to ", "")
        improved.append(cleaned)
    return improved
