class Volunteer:

    def __init__(self, name, skills):

        self.name = name

        self.skills = skills


def assign_task(task, volunteers):

    for volunteer in volunteers:

        if task in volunteer.skills:

            return volunteer.name

    return "No Suitable Volunteer"


if __name__ == "__main__":

    volunteers = [

        Volunteer(
            "Rahul",
            ["medical", "rescue"]
        ),

        Volunteer(
            "Priya",
            ["food", "logistics"]
        )
    ]

    result = assign_task(
        "medical",
        volunteers
    )

    print(result)