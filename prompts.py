from plans import java, python, c_sharp, spring_boot, dotnet

def gen_prompt(theme):
    prompt = f"""
    You are a Career Coach mentoring Software Engineering Apprentices.
    Create a sample learning plan a novice software engineering apprentice can complete in 3 weeks geared at learning a specific coding language, technology, or soft skill delimited by triple backticks.
    Include actionable steps, as well as learning resources that Apprentices may reference will completing the learning plan.
    
    ```{theme}```

    Please base the generated plan on sample learning plans at the following URLs.

    Python learning plan: {python},
    Java learning plan: {java},
    C# learning plan: {c_sharp}
    """
    return prompt


