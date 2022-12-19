# Linked Lists syntax is similar to a set of nested dictionaries
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next":{
                "value": 7,
                "next": None
            }
        }
    }
}

# prints out the number 23
print(head['next']['next']['value'])
