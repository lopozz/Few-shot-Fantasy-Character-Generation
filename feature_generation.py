# A function that character features given a base prompt and a new character
def features_generator(base_prompt, new_prompt):
  """
  Generate text given a prompt
  Args:
    base_prompt [str]: the base prompt containing the examples
    new_prompt [str]: the new topic to generate
  Returns:
    generation [str]: the newly generated output text
  """
  # generate new features for the characters
  response = co.generate(
    model='xlarge',
    prompt = base_prompt + new_prompt,
    max_tokens=75,
    temperature=0.4,
    stop_sequences=["----"])
  generation = response.generations[0].text

  return generation


# define the base prompt
# The base prompt
base_prompt = """
This program generate the description of fantasy characters.
----
Character: King
Description:
I am a king of the whole empire.
I give rules and pursuit them.
I am brave and fearless.
----
Character: Servant
Description:
I do what I am told without question.
I can not read.
I come from the lower class.
I have not seen my family in a long time.
----
Character: Thieft
Description:
I steal things from those who have more than me.
I am smart and shady.
I use knife to threaten people.
I move only in the darkness.
----
Character: Elf
Description:
I am wise and intelligent. 
I never age. 
I know secrets of the universe.
----
Character:"""

# List of character to which assign features
characters = ["Assassin",
              "Wizard",
              "Orc", 
              "Knight"]


# Append the generations in a list 
features = []

for character in characters:
  current_prompt = " " + character + "\n" + "Description:"
  feat = features_generator(base_prompt, current_prompt)
  feat = feat.strip().replace("----","")
  features.append(feat)
  
# Display the generated features
for character,feat in zip(characters,features):
  print(f"Character: {character}")
  print(f"Description:\n{feat}")
  print("-"*10)
