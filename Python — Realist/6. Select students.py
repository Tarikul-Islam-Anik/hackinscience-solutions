def select_student(students, threshold):
    accepted = []
    refused = []

    for i in students:
        if i[-1] >= threshold:
            accepted.append(i)
        else:
            refused.append(i)
    status = {
        "Accepted": sorted(accepted, key=lambda x: x[-1], reverse=True),
        "Refused": sorted(refused, key=lambda x: x[-1]),
    }

    return status
