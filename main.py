# main.py
# Runs the agent, generates subtasks, applies tools, evaluates, and saves log.

from agent import Agent
from tools import estimate_time_for_task
from evaluate import objective_evaluation, subjective_evaluation, reflect_plan
from datetime import datetime


def save_log(evaluation):
    """Save evaluation in evaluation_log.txt."""
    with open("evaluation_log.txt", "a") as f:
        f.write("\n--- Evaluation (" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ") ---\n")
        for key, value in evaluation.items():
            f.write(f"{key}: {value}\n")
        f.write("\n")


def main():
    print("\n=== Goal Planner (Groq Agentic AI Demo) ===\n")

    goal = input("Enter your goal: ").strip()
    agent = Agent()

    print("\nGenerating subtasks...\n")
    subtasks = agent.generate_subtasks(goal)

    # Apply tool
    final_plan = []
    for t in subtasks:
        est = estimate_time_for_task(t)
        final_plan.append(f"{t} (Estimated time: {est})")

    print("Initial Plan:")
    for step in final_plan:
        print("- " + step)

    # Reflection
    improved_plan = reflect_plan(final_plan)

    print("\nRefined Plan:")
    for step in improved_plan:
        print("- " + step)

    # Evaluations
    obj_eval = objective_evaluation(improved_plan)
    sub_eval = subjective_evaluation(improved_plan)

    evaluation = {
        "objective": obj_eval,
        "subjective": sub_eval
    }

    save_log(evaluation)

    print("\nEvaluation saved to evaluation_log.txt")
    print("\n=== Done ===")


if __name__ == "__main__":
    main()
