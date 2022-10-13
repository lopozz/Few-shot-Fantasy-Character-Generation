# base prompt to generate a story given a character and some features
prompt = """
This program generates short stories from the description of fantasy characters.
--
Character: King
Description: I am a king of the whole empire. I give rules and pursuit them. I am brave and fearless.
Story: Once upon a time, there was an Empire. The king ruled that reign demanding obedience from his servants, but he was considered very brave and fearless. Everyone in his kingdom lived a happy and healthy life until a horde of barbarians invaded the territory spreading chaos in the Empire. 
--
Character: Servant
Description: I do what I am told without question. I can not read. I come from the lower class. I have not seen my family in a long time.
Story: One of the servants of the king was leaving in the castle. He was considered by the king almost like a free man due to his loyalty to the Empire. The servant could not read at all but he was always doing what he was told without question. He was originally coming from a lower social class and his family sold him when he was still in swatting clothes.  
--
Character: Elf
Description: I am wise. I never age. I know secrets of the universe.
Story: Elfs, who were once linving among humans in the Empire, were always looking young. They were known to be keepers of nature’s wisdom and understand many secrets of the universe, the material, and the immaterial realms. All the other creatures in the Empire admire them for their characteristics and magic power. One day, however, the elves disappeared without leaving trace. 
--
Character: Assassin
Description: I kill people who deserve to die. I am smart. I am paid to kill. I use poison to kill people.
Story:
"""

response = co.generate(
  model='xlarge',
  prompt=prompt,
  max_tokens=200,
  temperature=0.5,
  stop_sequences=["--"])

output = response.generations[0].text
output = tr.fill(output, width=100)
print(output.strip())
