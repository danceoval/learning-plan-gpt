from plans import java, python, c_sharp, spring_boot, dotnet

def gen_prompt(theme):
    prompt = f"""
    You are an instructor at a Coding Bootcamp mentoring Software Engineering Apprentices.
    Create a sample learning plan a novice programmer can complete in 3 weeks geared at learning a specific coding language or technology, delimited by triple backticks.

    ```{theme}```

    You may find sample learning plans at the following URL.

    Python learning plan: {python},
    Java learning plan: {java},
    C# learning plan: {c_sharp}

    """
    return prompt

