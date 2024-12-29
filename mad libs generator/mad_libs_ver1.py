def mad_libs():
    story_template = """
    Once upon a time, there was a {adjective} {noun}. 
    It loved to {verb} {adverb}. One day, it met a {adjective2} {noun2} and they {verb2} together.
    """

    words = {}

    parts_of_speech =[
        ("adjective","Enter an adjective: "),
        ("noun","Enter a noun: "),
        ("verb","Enter a verb: "),
        ("adverb","Enter an adverb: "),
        ("adjective2","Enter an adjective: "),
        ("noun2","Enter a noun: "),
        ("verb2","Enter a verb: "),
    ]

    for part,prompt in parts_of_speech:
        while True:
            word = input(prompt)
            if word:
                words[part] = word
                break
            else:
                print("input cannot be empty, try again.")
            
    story = story_template.format(**words)
    print(story)

mad_libs()