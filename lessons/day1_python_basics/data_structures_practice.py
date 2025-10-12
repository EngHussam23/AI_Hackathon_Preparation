# Create a list of programming languages you want to learn
# Add two more languages to the list
# Create a dictionary with language names as keys and difficulty levels as values
# Write a function that takes a language name and returns its difficulty level

# Data types:
#   Text Type:	str
#   Numeric Types:	int, float, complex
#   Sequence Types:	list, tuple, range
#   Mapping Type:	dict
#   Set Types:	set, frozenset
#   Boolean Type:	bool
#   Binary Types:	bytes, bytearray, memoryview
#   None Type:	NoneType

# This is a list
languages = ["python", "SQL", "HTML", "CSS", "JavaScript", "Docker", "Git"]

# This is a dictionary (difficulty: levels: 0 lowest, 5 highest)
langs_diff = {
    "python": 1,
    "SQL": 4,
    "HTML": 1,
    "CSS": 1,
    "JavaScript": 2,
    "Docker": 5,
    "Git": 2,
}

def my_langs():
    result = ""
    for key, value in langs_diff.items():
        result += f"{key} : {get_difficulties (key)}, "
    return result
def get_difficulties(lang_name) :
    return langs_diff.get(lang_name)

print(my_langs())