# EXPERIMENT 3
# Healthcare Knowledge Repository

import json
import os


# Function to load knowledge from JSON
def load_knowledge_base():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "../data/diseases.json"
    )

    with open(file_path, "r") as file:
        knowledge_base = json.load(file)

    return knowledge_base


# Display all diseases
def display_diseases(knowledge_base):

    print("=" * 60)
    print("HEALTHCARE KNOWLEDGE REPOSITORY")
    print("=" * 60)

    for disease in knowledge_base:

        category = knowledge_base[disease]["category"]

        print(f"{disease:<20} | {category}")


# Display complete information
def display_disease(knowledge_base, disease_name):

    if disease_name not in knowledge_base:

        print("Disease not found.")

        return

    data = knowledge_base[disease_name]

    print("\n" + "=" * 60)
    print("DISEASE:", disease_name)
    print("=" * 60)

    for key, value in data.items():

        if isinstance(value, list):

            print(
                key.replace("_", " ").title(),
                ":",
                ", ".join(value)
            )

        else:

            print(
                key.replace("_", " ").title(),
                ":",
                value
            )


# Search disease by symptom
def search_by_symptom(knowledge_base, symptom):

    print("\nDiseases associated with:", symptom)

    found = False

    for disease, data in knowledge_base.items():

        if symptom in data["symptoms"]:

            print("-", disease)
            found = True

    if not found:

        print("No matching disease found.")


# Search by body system
def search_by_body_system(knowledge_base, system):

    print("\nDiseases affecting:", system)

    found = False

    for disease, data in knowledge_base.items():

        if data["body_system"] == system:

            print("-", disease)
            found = True

    if not found:

        print("No matching disease found.")


# Search by category
def search_by_category(knowledge_base, category):

    print("\nDiseases in category:", category)

    found = False

    for disease, data in knowledge_base.items():

        if data["category"] == category:

            print("-", disease)
            found = True

    if not found:

        print("No matching disease found.")


# Search by risk factor
def search_by_risk_factor(knowledge_base, factor):

    print("\nDiseases associated with:", factor)

    found = False

    for disease, data in knowledge_base.items():

        if factor in data["risk_factors"]:

            print("-", disease)
            found = True

    if not found:

        print("No matching disease found.")


# Main program
if __name__ == "__main__":

    knowledge_base = load_knowledge_base()

    print("\nKnowledge repository accessed successfully.")

    # Display all diseases
    display_diseases(knowledge_base)

    # Display individual disease
    display_disease(
        knowledge_base,
        "Diabetes"
    )

    # Search operations
    search_by_symptom(
        knowledge_base,
        "Headache"
    )

    search_by_body_system(
        knowledge_base,
        "Respiratory System"
    )

    search_by_category(
        knowledge_base,
        "Infectious Disease"
    )

    search_by_risk_factor(
        knowledge_base,
        "Family History"
    )
