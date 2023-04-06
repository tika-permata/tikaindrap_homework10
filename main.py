data = [
    {
        "name": "ilham",
        "sex": "male",
        "age": 21,
        "marital": "single",
        "social": "student"
    },
    {
        "name": "cori",
        "sex": "male",
        "age": 20,
        "marital": "married",
        "social": "employee"
    },
    {
        "name": "yosepin",
        "sex": "female",
        "age": 18,
        "marital": "single",
        "social": "student"
    },
    {
        "name": "cantik",
        "sex": "female",
        "age": 35,
        "marital": "married",
        "social": "employee"
    },
    {
        "name": "iqbal",
        "sex": "male",
        "age": 23,
        "marital": "single",
        "social": "employee"
    }
]

def group_people(data):
    groups = {}
    for item in data:
        sex = item["sex"]
        age = item["age"]
        marital = item["marital"]
        social = item["social"]
        key = (sex, age, marital, social)
        if key in groups:
            groups[key].append(item)
        else:
            groups[key] = [item]
    return groups

result = group_people(data)
print(result)