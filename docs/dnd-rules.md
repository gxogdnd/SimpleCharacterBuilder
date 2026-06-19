# A quick D&D primer (for contributors)

You do **not** need to know Dungeons & Dragons to contribute here. This page
explains just enough of the rules to understand the code and the data files.

## Ability scores

Every character has six **ability scores**, usually ranging from 3 to 20 for
player characters (the rules allow 1–30):

| Ability        | Short | Governs, roughly… |
| -------------- | ----- | ----------------- |
| Strength       | STR   | lifting, melee power |
| Dexterity      | DEX   | agility, stealth, aim |
| Constitution   | CON   | health, stamina |
| Intelligence   | INT   | reasoning, recall |
| Wisdom         | WIS   | awareness, intuition |
| Charisma       | CHA   | force of personality |

### Modifiers

What actually gets added to dice rolls is the **modifier**, derived from the
score: subtract 10 and round *down* after halving.

```
modifier = (score - 10) // 2
```

So 10–11 → +0, 12–13 → +1, 8–9 → −1, 20 → +5. This single rule lives in
[`rules.ability_modifier`](../src/charsheet/rules.py) and powers most of the
sheet.

## Race

A character's **race** (Human, Elf, Dwarf, …) grants small **ability score
increases** and details like size and walking speed. We store these in
[`data/races.json`](../src/charsheet/data/races.json).

## Class

A character's **class** (Fighter, Wizard, …) defines how they fight or cast
spells. The two pieces we model so far are the **hit die** (how tough they are)
and their two **saving-throw proficiencies**. See
[`data/classes.json`](../src/charsheet/data/classes.json).

## Skills

There are 18 **skills** (Stealth, Perception, …), and each is tied to one
ability. A character's bonus with a skill is built from that ability's
modifier. The skill→ability mapping is in
[`data/skills.json`](../src/charsheet/data/skills.json).

## Things not modelled yet

Proficiency bonus, hit points, spell slots, equipment, feats, and leveling are
all still to come — many of them as contributor issues. If a rule isn't in the
code yet, that's an opportunity, not a bug.

---

## Attribution

This project includes material from the **System Reference Document 5.1**
("SRD 5.1") by Wizards of the Coast LLC, available under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).
The SRD content is owned by Wizards of the Coast and used here under that
licence; it is not covered by this project's MIT licence.
