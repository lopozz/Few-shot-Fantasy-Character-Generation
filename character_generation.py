charaters = ["King", "Servant", "Assassin", "Wizad"]
base_prompt = """
This program generates fantasy characters.
--
Character: King
--
Character: Servant
--
Character: Elf
--
Character: Assassin
--
Character: Wizard
--
Character:
"""
paragraphs = []

for i in range(10):
  response = co.generate(
    model='xlarge',
    prompt=base_prompt,
    max_tokens=20,
    temperature=0.4,
    stop_sequences=["----"])
  output = response.generations[0].text
  output = tr.fill(output, width=100)
  if output.replace("----","").strip() not in charaters:
    charaters.append(output.replace("----","").strip())
    base_prompt = base_prompt.rstrip() + ' ' + output.replace("----","").strip() + "\n" + "----" + "\n" + "Character:"
  print(output.replace("----","").strip())
