# M. Overman, 1/16/2025
# whalecum 2 the tutorial

WAR = "never changes"

message_one = "Hello world"
print(message_one)

message_two = "Python Crash Course"
print("Wait a minute. So you're telling me this is some kind of", message_two + "?")

# f-strings my beloved
# NOTICE: MUST USE DOUBLE QUOTES FOR F-STRINGS
first_name = "chinese"
last_name = "mike"
full_name = f"{first_name} {last_name}".title()
print("Got a Mexican homie named", full_name)

# escape characters are like minecraft commands that you can just put anywhere on a string (but not nearly as cool)
print("Pl\t**\tpy")

# stripping strings sounds a lot more suggestive than it actually is
print("     Somebody come get her, she dancing like a...".strip())

# dedicated function for removing prefixes discovered, eggheads currently fuming
print("Dr. House".removeprefix("Dr. "))

# integers and floats up next
# remember how to integer-divide (//) and exponentiate (**)
# never forget PEMDAS. MD and AS are treated as the same step, so read both from left to right

print(9 - 4 / 2 * 5 + 8) # all single-slash division will return a float no matter what.
print(0.2 + 0.1) # me when floating point precision errors (╯°□°）╯︵ ┻━┻

# underscores can be used as commas in large numbers
print(10000000000)
print(10_000_000_000)

# Python lets you change constants. it's just an unspoken rule kinda thing
WAR = "has changed"