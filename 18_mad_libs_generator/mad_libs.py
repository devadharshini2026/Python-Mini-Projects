def mad_libs():
    print("🎭 Welcome to the Mad Libs Story Generator!")
    print("Fill in the blanks to create your own funny story.\n")

    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    verb = input("Enter a verb ending with -ing: ")
    adjective = input("Enter an adjective: ")

    # Story template
    story = f"""
    One day, {name} went to {place}.
    There, they saw a {adjective} {animal} {verb} around.
    Feeling hungry, {name} ate some {food} and laughed out loud.
    What a funny day at {place}!
    """

    print("\n🎉 Here's your Mad Libs story:\n")
    print(story)

    # Save story to file
    with open("mad_libs_story.txt", "a", encoding="utf-8") as f:
        f.write(story + "\n" + "-"*40 + "\n")

    print("📂 Your story has been saved to mad_libs_story.txt")

if __name__ == "__main__":
    mad_libs()
