# py.exe -3
# Creates a CSV file with the input of LootTable.json file
import json
import sys
import csv


def main():
  if len(sys.argv) != 2:
    print("File please")
    return
  filename = sys.argv[1]

  with open(filename, 'r') as f:
    data = json.load(f)
  headers = ["name", "minPlat", "maxPlat", "minGold", "maxGold", "minSkill", "minHealth", "maxHealth", "goldDropRate", "healthDropRate",
             "platDropRate", "itemDropRate", "skillDropRate", "lockedSkillDropRate", "signatureSkillDropRate", "goldCompensation"]
  bad_loot = ["DebugSkills", "DebugItems", "MuseumItem", "MuseumSkill"]
  print(', '.join(headers))

  for e in data['dropTableEntries']:
    a = []
    if e['name'] not in bad_loot:
      for h in headers:
        try:
          a.append("{}".format(str(e[h])))
        except:
          a.append("")
    print(','.join(a))


if __name__ == "__main__":
  sys.exit(main())
