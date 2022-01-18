import instaloader

L = instaloader.Instaloader()

if __name__ == "__main__":
    USER = input("Enter your username: ")
    L.interactive_login(USER)

    print(f"Successfully logged into {USER}")
    target = input(
        "Enter the username of yourself or someone you're following whose followers you want to compare: "
    )
    profile = instaloader.Profile.from_username(L.context, target)

    print(f"Fetching the users that {target} is following (this might take a while...)")
    followees = set()
    for fwle in profile.get_followees():
        followees.add(fwle)

    print(
        f"Fetching the users that are following {target} (this might take a while...)"
    )
    followers = set()
    for fwler in profile.get_followers():
        followers.add(fwler)

    print("Filtering out the non-followers")
    diff = followees.difference(followers)

    print("Writing output to result.txt")
    with open("result.txt", "w") as output:
        if len(diff) == 0:
            output.write(
                f"{target}'s followees and followers are balanced, as all things should be."
            )
        else:
            for unfwl in diff:
                output.write(unfwl.username + "\n")

    print("Output successfully recorded in result.txt")
