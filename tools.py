# tools.py
# Contains simple tool functions used by the subtasks.

def estimate_time_for_task(task):
    """Very basic fake time estimator."""
    words = len(task.split())
    minutes = max(1, words // 2)
    return f"~{minutes} min"
