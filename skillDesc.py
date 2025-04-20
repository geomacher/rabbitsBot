# skillDesc.py

skillsblade = {
    "Hard Hit": {
        "title": "Hard Hit",
        "description": (
            "**Lv 1 Skill**\n"
            "One-Handed Sword/Two-Handed Sword only\n"
            "**MP Cost**: 100\n"
            "**Damage Type**: Physical\n\n"
            "**Base Skill Multiplier**: 1 + 0.05 * Skill Level\n"
            "**Base Skill Constant**: 50 + 5 * Skill Level\n"
            "**Hit Count**: 1 hit\n"
            "**Max Cast Range**: Weapon’s auto attack range\n"
            "**Ailment**: Flinch (Chance up to 50%)\n"
            "**Duration**: 2s\n"
            "**Game Description**: Brutally hit target. Chance to flinch.\n"
            "**OHS Bonus**: Flinch chance +50%\n"
            "**2HS Bonus**: Skill Multiplier +0.5"
        ),
        "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867537650368774144/IMG_7643.PNG?ex=68042765&is=6802d5e5&hm=310d72d27f391aab85786030ce22decdc5bb66327aa4481e47a071897e302797&"
    },
    "Rampage": {
        "title": "Rampage",
        "description": (
            "**Lv 3 Skill**\n"
            "One-Handed Sword/Two-Handed Sword only\n"
            "**MP Cost**: 500\n"
            "**Damage Type**: None\n\n"
            "Boosts next 10 auto attacks and deals a final blow.\n"
            "**Final Blow Multiplier**: Up to 2.5 + 0.05 * SLv\n"
            "**Buff**: Sets DEF/MDEF/Dodge to 0, +MP Recovery\n"
            "**Duration**: 10 attacks or ailment/10 min\n"
            "**OHS Bonus**: First 10 Mult + (0.05 * SLv)\n"
            "**2HS Bonus**: Final Mult +4"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867549181484859402/IMG_7647.PNG?ex=68043223&is=6802e0a3&hm=ec948169716de6c45d9d1f1d2b356c8da44c0804f6601d90cb48722b5e0c99db&"
    },
    "Meteor Breaker": {
        "title": "Meteor Breaker",
        "description": (
            "**Lv 4 Skill**\n"
            "One-Handed Sword/Two-Handed Sword only\n"
            "**MP Cost**: 600\n"
            "**Damage Type**: Physical\n\n"
            "**Hit Count**: 2 hits (Main target); 1 AOE\n"
            "**Invincible while casting**\n"
            "**Ailment**: Dizzy (up to 25%)\n"
            "**Game Description**: Leap and smash the ground like a meteor.\n"
            "**OHS Bonus**: Dizzy Chance +75%\n"
            "**2HS Bonus**: +Skill Mult (First Hit)"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867550215959085076/IMG_7648.PNG?ex=68043319&is=6802e199&hm=feb921b83976bc186ad9a7308508fbb5e97c05d2e67c7dc788d4b134f7d0f437&"
    },
    "Sonic Blade": {
        "title": "Sonic Blade",
        "description": (
            "**Lv 1 Skill**\n"
            "One-Handed Sword/Two-Handed Sword only\n"
            "**MP Cost**: 200\n"
            "**Damage Type**: Physical\n\n"
            "**Dash toward target, hits enemies in path**\n"
            "**Crit Rate**: +(10 * SLv)\n"
            "**Super Mode**: Double Mult, +1m Hit Range\n"
            "**OHS Bonus**: +4m Range\n"
            "**2HS Bonus**: +2m Hit Range, +0.5 Mult"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867647723192844318/IMG_7649.PNG?ex=6803e529&is=680293a9&hm=a7be66ae4853b1362689f98adc071360651ac0de464f6a031532f13eb5412b97&"
    },
    "Spiral Air": {
        "title": "Spiral Air",
        "description": (
            "**Lv 2 Skill**\n"
            "**MP Cost**: 300\n"
            "**Damage Type**: Physical\n"
            "**Hit Count**: 10 hits\n"
            "**No Crits**\n"
            "**Buff**: Crit Damage +(0.5 + 0.5 * SLv + total DEX/(60 - SLv))\n"
            "**2HS Penalty**: Crit Damage buff halved"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867788106748919808/IMG_7650.PNG?ex=680467e7&is=68031667&hm=c72b4f75c0388f9e543ca497c1d5fa8a6d24c61308fe606e8ec9a119f1293ca5&"
    },
    "Sword Tempest": {
        "title": "Sword Tempest",
        "description": (
            "**Lv 3 Skill**\n"
            "**MP Cost**: 400\n"
            "**Damage Type**: Physical\n"
            "**Wave + Tornado effect**\n"
            "**Wave Ailment**: Suction\n"
            "**Game Description**: Slash that causes storm; pulls enemies in.\n"
            "**OHS Bonus**: +Tornado Mult (baseDEX/500)\n"
            "**2HS Bonus**: +Wave Mult (1 + baseSTR/500)"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867843150147223562/IMG_7652.PNG?ex=6803f26a&is=6802a0ea&hm=3cd9eaf56c8f6c5174c17bb8e6ac7ebc57af486deb361a17710e3f7c7d2364ea&"
    },
    "Buster Blade": {
        "title": "Buster Blade",
        "description": (
            "**Lv 4 Skill**\n"
            "**MP Cost**: 300\n"
            "**Damage Type**: Physical\n"
            "**Always Crits**\n"
            "**HP Heal**: 1000 + (OHS: +2 * baseVIT)\n"
            "**Buff**: Weapon ATK + (1 * SLv)% for 10s\n"
            "**OHS Bonus**: Skill Mult + (baseDEX/200)\n"
            "**2HS Bonus**: Skill Mult + (baseSTR/100)\n"
            "**Shield Bonus**: Weapon ATK +(10 + Shield Refine)%"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867879644896428032/BusterBlade.PNG?ex=68041467&is=6802c2e7&hm=fd77452dbd6f8e0919a0f21ec54ee7952c6bbd7d85495473efd8c1139b248d87&"
    },
    "Sword Mastery": {
        "title": "Sword Mastery (Passive)",
        "description": (
            "**Lv 1 Skill**\n"
            "**Weapon ATK**: +(3 * SLv)%\n"
            "**ATK**: +1~3% based on level\n"
            "**Game Description**: Boost sword damage.\n"
            "**Dual Sword Bonus**: Affects subhand too"
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867882113150746644/SwordMastery.PNG?ex=680416b4&is=6802c534&hm=f2e527679092b15634d2edb1487e9b6d8df49fa0bcfdbf84f79389ccdb0d2f37&"
    },
    "Quick Slash": {
        "title": "Quick Slash (Passive)",
        "description": (
            "**Lv 1 Skill**\n"
            "**Attack Speed**: +(SLv)% and +(10 * SLv)\n"
            "**Game Description**: Shortens attack interval for swords."
        ),"image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867883179803934740/QuickSlash.PNG?ex=680417b2&is=6802c632&hm=1b9e20b9fe30156a3d6bade06ab737a2531d869427b2a75961a531c2a43175dc&"
    },
    "War Cry": {
        "title": "War Cry",
        "description": (
            "**Lv 3 Skill**\n"
            "**Weapon**: No Limit\n"
            "**MP Cost**: 300\n"
            "**Damage Type**: None\n\n"
            "**Skill Effect**: Removes [Fear] status from any party member affected.\n"
            "**Buff Effect**: ATK + (Skill Level)% to the entire party\n"
            "**Buff Duration**: (15 + Skill Level) seconds\n"
            "**Game Description**: Perform a rallying cry. Increases ATK for a while. Removes status ailment: [Fear].\n\n"
            "**One-Handed Sword Bonus**: Buff Duration +50 seconds\n"
            "**Two-Handed Sword Bonus**: ATK% of buff +5%\n\n"
            "**Override Rule**:\n"
            "- Higher skill level overrides lower skill level.\n"
            "- If same level, longer duration overrides shorter."
        ),  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867535165566902282/IMG_7644.PNG"  # Ganti URL ini jika ada gambar War Cry spesifik
    },
    "Astute": {
        "title": "Astute",
        "description": (
            "**Lv 1 Skill**\n"
            "**One-Handed Sword/Two-Handed Sword only**\n"
            "**MP Cost: 200**\n"
            "**Damage Type**: Physical\n"
            "**Base Skill Multiplier**: Base Skill Multiplier: 1.5 + 0.1 * Skill Level\n"
            "**Base Skill Constant**: Base Skill Constant: 150 + 5 * Skill Level\n"
            "**Hit Count**: 1 hit\n"
            "**Max Cast Range*Defaults to the weapon's Auto Attack Max Range*:\n\n"
            "**Skill Effect**: The skill has a Motion Speed boost of (5 * Skill Level)%\n"
            "**Buff Effect**: Critical Rate +25\n"
            "**Buff Duration**: 5 seconds (levels 1 to 5); 10 seconds\n\n"
            "**Game Description**: Strongly hit the target in rapid motion. Critical Rate +25 when this skill is activated.\n\n"
            "*One-Handed Sword bonus: MP Cost -100*\n"
            "*Two-Handed Sword bonus: Skill Multiplier +0.5*\n\n"
            "*Two-Handed Sword bonus: Critical Rate of buff is doubled*:\n"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867533441142095872/IMG_7645.PNG?ex=6804237a&is=6802d1fa&hm=06e3e439415b7035554114d66a93ff5fb5649f20e379c07959aab414cb9255f4&https://cdn.discordapp.com/attachments/614452674137686022/867533441142095872/IMG_7645.PNG?ex=6804237a&is=6802d1fa&hm=06e3e439415b7035554114d66a93ff5fb5649f20e379c07959aab414cb9255f4&https://cdn.discordapp.com/attachments/614452674137686022/867533441142095872/IMG_7645.PNG?ex=6804237a&is=6802d1fa&hm=06e3e439415b7035554114d66a93ff5fb5649f20e379c07959aab414cb9255f4&https://cdn.discordapp.com/attachments/614452674137686022/867533441142095872/IMG_7645.PNG?ex=6804237a&is=6802d1fa&hm=06e3e439415b7035554114d66a93ff5fb5649f20e379c07959aab414cb9255f4&"
    },
    "Trigger Slash": {
    "title": "Trigger Slash",
    "description": (
        "**Lv 2 Skill**\n"
        "One-Handed Sword/Two-Handed Sword only\n"
        "**MP Cost**: 300 (Lv 1–5); 200 (Lv 6–10)\n"
        "**Damage Type**: Physical\n"
        "**Element**: Fire\n\n"
        "**Base Skill Multiplier**: 1.5 + 0.05 * Skill Level\n"
        "**Base Skill Constant**: 200 + 10 * Skill Level\n"
        "**Hit Count**: 1 hit\n"
        "**Max Cast Range**: Weapon’s auto attack range\n\n"
        "**Buff Effect**:\n"
        "- Attack MP Recovery +(2 * Skill Level)\n"
        "- Sets next skill’s Animation Time Modifier to 50%\n"
        "**Buff Duration**: Until a skill is used\n\n"
        "**Game Description**: Put power while slashing the target. Enhance Attack MP Heal until the next skill. The motion speeds up one time by this skill.\n\n"
        "**OHS Bonus**: Gains the Perfect Aim attribute\n"
        "**2HS Bonus**: Skill Multiplier +1\n\n"
        "**Note**: This skill’s Animation Time Modifier overrides all other Motion Speed modifiers."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/867542858143367178/IMG_7646.PNG?ex=68042c3f&is=6802dabf&hm=b6e6cb4731e4b0cb1f530beff7797086508811300f1a02a1ff67edc7e83d77f5&"  # Ganti ke link gambar Trigger Slash jika ada
},
"Berserk": {
    "title": "Berserk",
    "description": (
        "**Lv 4 Skill**\n"
        "No Limit\n"
        "**MP Cost**: 500\n"
        "**Damage Type**: None\n\n"
        "**Buff Effect**:\n"
        "- Attack Speed +(10 * Skill Level)% and +(100 * Skill Level)\n"
        "- Critical Rate +(2.5 * Skill Level)\n"
        "- Auto attacks' Skill Multiplier +(0.1 * Skill Level)\n"
        "- Rampage is not removed by ailments while the buff is active\n"
        "- DEF -(100 - Skill Level)%\n"
        "- MDEF -(100 - Skill Level)%\n"
        "- Stability -(100 - 5 * Skill Level)%\n\n"
        "**Buff Duration**: 10 seconds\n\n"
        "**Game Description**: Stop thinking and wield a weapon like a berserker. Increase Normal Attack Power/Attack Speed/Critical Rate for a few seconds and greatly decrease Stability/DEF/MDEF. Rampage is not removed by status ailments while it is in effect.\n\n"
        "**One-Handed Sword Bonus**:\n"
        "- Buff Duration +20 seconds\n"
        "- Stability reduction is halved\n"
        "- DEF% and MDEF% reduction are halved (non Dual Swords)\n\n"
        "**Two-Handed Sword Bonus**:\n"
        "- Buff Duration +20 seconds\n"
        "- Stability reduction is halved\n"
        "- Critical Rate of buff is doubled\n\n"
        "**Notes**:\n"
        "- If Rampage is active, first 10 auto attacks get additive Skill Multiplier bonus (not Final Blow).\n"
        "- Multiplier boost only applies to main hand of Dual Swords.\n"
        "- Stability reduction does **not** affect Dual Swords’ subhand."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869098081340231750/berserk.png?ex=6803e5e9&is=68029469&hm=d43546dd5b44eef1e66e8bb760212fa359931f98ca14a801852397768f00709a&"  # Ganti ini ke gambar Berserk jika ada
},
"Swift Attack": {
    "title": "Swift Attack",
    "description": (
      "**Lv 3 Skill**\n"
      "One-Handed Sword/Two-Handed Sword only\n"
      "**MP Cost**: 300\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 0.3 + 0.05 * Skill Level (Max at 0.75)\n"
      "**Base Skill Constant**: (Skill Level+1)^2 * 3 (Max at 300)\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n\n"
      "**Skill Effect**:\n"
      "- If this skill is at level 10, then the next skill has its MP Cost divided by half and rounded up to the nearest multiple of 100 (e.g. 300/2 = 150 -> 200 MP; 600/2 = 300 -> 300 MP)\n\n"
      "**Game Description**: Kick while pretending to attack with a sword. This skill has \"normal attack proration\". MP Cost for the next skill used will be reduced when the skill reaches its maximum level.\n\n"
      "**Dual Swords Bonus**:\n"
      "- MP Cost reduced by 100\n"
      "- Chance to Tumble 100% at lv 10\n\n"
      "**Notes**: This skill inflicts Normal/Auto Attack Proration. But Damage depends on Physical Proration."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869098092216066058/swiftattack.png?ex=6803e5ec&is=6802946c&hm=4163418af4f07b431544d9882f6c6be39f3f13cfbd8af959ea75ef7609ff8806&"
  },
  "Shutout": {
    "title": "Shutout",
    "description": (
      "**Lv 5 Skill**\n"
      "One-Handed Sword/Two-Handed Sword only\n"
      "**MP Cost**: 100\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 5\n"
      "**Base Skill Constant**: 100\n"
      "**Enhanced Base Skill Multiplier**: 10 + Skill Level\n"
      "**Enhanced Base Skill Constant**: 100\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n\n"
      "**Skill Effect**:\n"
      "- If used on target with Flinch/Tumble/Stun and target doesn’t have Bleed, this skill is enhanced: deals more damage and inflicts Bleed 100% for 10 seconds (no resistance).\n\n"
      "**Game Description**: A merciless blow. If the target is not afflicted by Flinch/Tumble/Stun or Bleed, the damage will increase and the target will be inflicted with [Bleed]. [Don’t trust this misleading description by Asobimo :/] You’re supposed to inflict interrupt for dealing more damage and inflict bleed.\n\n"
      "**One-Handed Sword Bonus**:\n"
      "- Base Skill Multiplier +(BaseDex/200)\n"
      "- Enhanced Base Skill Multiplier +(0.5 * Skill Level + BaseDex/100)\n"
      "- Enhanced Skill's Total Physical Pierce quadrupled\n\n"
      "**Dual Swords Bonus**:\n"
      "- Base Skill Multiplier +(BaseAGI/400)\n"
      "- Enhanced Base Skill Multiplier +(0.5 * Skill Level + BaseAgi/200)\n"
      "- Enhanced Skill's Total Physical Pierce doubled\n\n"
      "**Two-Handed Sword Bonus**:\n"
      "- Base Skill Multiplier +(Skill Level)\n"
      "- This skill is unaffected by Motion Speed% (unlike OHS)"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967811188119465984/shutout.png?ex=68046ba8&is=68031a28&hm=e6536aea81adf9da9f27f3f76e38ae4f5771c0c3970bf60c7e5a2db2b529d656&"
  },
  "Lunar Slash": {
    "title": "Lunar Slash",
    "description": (
      "**Lv 5 Skill**\n"
      "One-Handed Sword/Two-Handed Sword only\n"
      "**MP Cost**: 400\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier (First Hit)**: 10\n"
      "**Base Skill Constant (First Hit)**: 400\n"
      "**Base Skill Multiplier (Second Hit)**: (Total STR * Skill Level * 0.1)/100\n"
      "**Base Skill Constant (Second Hit)**: Base INT/2\n"
      "**Base Skill Multiplier (Stack Hit)**: (Total STR * Skill Level * 0.1)/100\n"
      "**Base Skill Constant (Stack Hit)**: Base INT\n"
      "**Hit Count**: 2 hits on main target (each hit calculated separately)\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n\n"
      "**Second Hit Ailment**: Fatigue\n"
      "**Ailment Chance**: 4 * Skill Level %\n"
      "**Ailment Duration**: 10 seconds\n"
      "**Ailment Resistance**: None\n\n"
      "**Skill Effect**:\n"
      "- For THS only: Using this skill grants +(CC) Lunar Slash stacks.\n"
      "- Lunar Slash stacks are consumed by using other attack skills (excluding Lunar Slash) to trigger Stack Damage.\n"
      "- Max stack: 9\n"
      "- Stack/Additional Hits have fixed Critical Rate +(10 * Skill Level + CRT) (CRT = Personal Stat).\n"
      "- All hits are affected by srd% and Sword Techniques (stack is unaffected by combo tags).\n\n"
      "**Game Description**: Slashes target and magic blade will deal additional damage after a slight delay. The magic blade may inflict [Fatigue].\n\n"
      "**Two-Handed Sword Bonus**:\n"
      "- Additional attack when another skill is used\n"
      "- Extra attack can't inflict Fatigue\n"
      "- Additional attack has increased Critical Rate\n\n"
      "**Notes**:\n"
      "- Lunar Slash grants stacks even if the initial attack misses or is evaded.\n"
      "- When using AoE skills, each target consumes 1 stack.\n"
      "- CC = Combo Count: Opener(1CC) > 2CC > 3CC and so on."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967812558016876654/moonslash.png?ex=68046cee&is=68031b6e&hm=dd008260305a8b37917e4e81c89352154afa9cd0e7d0e1c47bdbd76b796e851f&"
  },
  "Aura Blade": {
    "title": "Aura Blade",
    "description": (
      "**Lv 5 Skill**\n"
      "One-Handed Sword/Two-Handed Sword only\n"
      "**MP Cost**: 200\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 5 + Skill Level\n"
      "**Base Skill Constant**: 200\n"
      "**Hit Count**: 2 hits (for OHS) or 1 hit (for THS); damage calculation is done once then spread evenly between the hits\n"
      "**Maximum Cast Range**: 100m (theoretically infinite, but requires a target to cast)\n"
      "**Hit Range**: 3.5m radius\n\n"
      "**Buff Effect**:\n"
      "- Increase next skill damage by 1.2x (+20%; applied multiplicatively at the end of damage calculation after added along with Brave Aura bonus and Mana Recharge reduction)\n"
      "- Gain Additional Melee% by (10 * Skill Level)%\n"
      "**Buff Duration**: 40 seconds OR until you use skills\n\n"
      "**Passive Effect**:\n"
      "- Passively grant extra skill multiplier to :busterblade:Buster Blade by +(0.2 * Skill Level) + baseDEX/200 multiplier additively.\n\n"
      "**Game Description**: “Slashes and clears your surroundings with a blade surrounded by an aura. The power of the next skill used is 1.2x stronger. Grants Additional Melee to weapon while active.”\n\n"
      "**One-Handed Sword Bonus**:\n"
      "- Buffs will not be consumed when using skill\n"
      "- Extends Aura Blade buffs by 10 seconds whenever you get Buster Blade buff\n\n"
      "**Dual Swords Bonus**:\n"
      "- Power/Damage of the next skill becomes 1.1x stronger\n\n"
      "**Two-Handed Sword Penalty**:\n"
      "- Additional Melee granted gets reduced to 50%\n\n"
      "**Two-Handed Sword Bonus**:\n"
      "- Power/Damage of the next skill becomes 1.3x stronger\n\n"
      "**Notes**:\n"
      "- The Damage buff of this skill can affect any skill, except its own skill Aura Blade."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967813297841782784/aurablade.png?ex=68046d9f&is=68031c1f&hm=c992e29f48b60dd5ed9b8e87906efc3d1ec24618208ea8167f800fbece79e786&"
    },
    "Gladiate": {
    "title": "Gladiate",
    "description": (
      "**Lv 5 Skill**\n"
      "One-Handed Sword/Two-Handed Sword only\n"
      "**MP Cost**: 0\n\n"
      "**Skill Effect**:\n"
      "- Using this skill will give (Skill Level) Gladiate stacks buff.\n"
      "- Every time you receive damage during this buff, you will lose 1 stack and recover MP depending on the weapon you’re using and also depend on Total AMPR you have.\n\n"
      "**Buff Effect**:\n"
      "- Reduce any damage received by (Skill Level) %\n"
      "- When this buff ends, recover your MP by (10 per current Gladiate stack). Note: if you recast this buff again, then it will not end this buff, but instead, its buff duration will be refreshed to 10 seconds.\n"
      "- **Buff Duration**: 10 seconds\n\n"
      "**Game Description**: “Reduce the damage received for a certain number of times in 10 seconds. Slightly restores MP when damage is reduced. Recover 10 MP per number of damage reduction effects remaining when the time is up.”\n\n"
      "**One-Handed Sword Bonus**:\n"
      "- Amount of MP recovered when losing a stack is based on (Total AMPR * Skill Level / 10)\n\n"
      "**Dual Swords Penalty (Bonus)**:\n"
      "- Amount of MP recovered when losing a stack is based on (Total AMPR / 4 * Skill Level / 10)\n"
      "- Total damage reduction will be doubled\n\n"
      "**Two-Handed Sword Penalty (Bonus)**:\n"
      "- Amount of MP recovered when losing a stack is based on (Total AMPR * 75% * Skill Level / 10)\n"
      "- Total damage reduction will be doubled\n\n"
      "**Notes**:\n"
      "- This skill cannot be used as the first skill of a combo."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967813298068271155/gladiate.png?ex=68046d9f&is=68031c1f&hm=1c3a037b3154fec7e5fcced6e8ea93da4f874ef1881701738ebf2a1da5ef0303&"
  },
  "Hammer Slam": {
    "title": "Hammer Slam",
    "description": (
      "**T1 Skill**\n"
      "Two-Handed Sword only\n"
      "**MP Cost**: 100\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Constant**: 100\n"
      "**Base Skill Multiplier**: 1 + Skill Level * 0.05 + Total Vit / 100 + baseSTR / 500\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
      "**Hit Range**: [Defaults to the weapon's Auto Attack Max Range or 2.5m?] around the target\n\n"
      "**Skill Effect**:\n"
      "- If used consecutively (i.e. your last skill action is this skill), then the MP Cost becomes 0 MP and inflicts normal proration (damage is always 100% proration, unaffected by Normal/Physical Proration).\n"
      "- This consecutively used skill's 0 MP cost won't work as an opener, as it requires 1 MP cost to start.\n"
      "- This skill has Absolute Critical against interrupted targets.\n\n"
      "**Game Description**: “Performs a narrow-range attack around the targets as if you are slamming them down. Guarantees a critical hit on targets immobilized by Flinch or other status ailments. MP Cost becomes 0 if used consecutively.”\n"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234851230530932786/hammerslam.png?ex=68044693&is=6802f513&hm=e4bd9395a58a8c29abfbc09c4c8d0fea837a209f7ed1e101a6b8d5bc19aec8f6&"
    },
    "Cleaving Attack": {
    "title": "Cleaving Attack",
    "description": (
      "**T2 Skill**\n"
      "Two-Handed Sword only\n"
      "**MP Cost**: 300\n\n"
      "**Base Skill Constant**: 150 + Skill Level * 15 + Total Vit\n"
      "**Base Skill Multiplier**: 1.5 + Skill Level * 0.1 + Total STR / 200 * (Number of Enemy Hit - 1)\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
      "**Hit Range**: Defaults to the weapon's Auto Attack Max Range around the caster\n\n"
      "**Skill Effect**:\n"
      "- Upon use, recover MP by (each target hit - 1) MP Bar. Note: cannot exceed the skill's MP consumption. E.g., using this skill with 0 MP cost due to combo will result in no MP gain, since it is 0 MP cost. If it costs 6 MP, you'll gain 6 MP bar if you can hit 7 targets.\n\n"
      "**Game Description**: “Swings the sword horizontally to deal with multiple opponents. If 2 or more targets are involved, the power will increase proportionally and consumed MP will be restored.”\n"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234851230044520498/cleavingattack.png?ex=68044693&is=6802f513&hm=154aeabc820deea3456b778c60fbd056b4378cb257c1b682fc087567e1f7f9cb&"
    },
    "Storm Blaze": {
    "title": "Storm Blaze",
    "description": (
      "**T3 Skill**\n"
      "Two-Handed Sword only\n"
      "**MP Cost**: 200\n\n"
      "**Base Skill Constant**: 100 + Skill Level * 10 + Total Vit\n"
      "**Base Skill Multiplier**: (0.5 + Skill Level * 0.05) * Blaze Stack consumed\n"
      "**Hit Count**: 1\n"
      "**Maximum Cast Range**: 16m\n"
      "**Hit Range**: Length of 16m and radius of (2 + 0.4 * Blaze Stack) m, from the caster towards the main target\n\n"
      "**Skill Effect**:\n"
      "- Passively gain 1 Blaze Stack for every auto attack, or 2 stacks if using Rampage auto attack. Use Hammer Slam (only if used consecutively) to gain +1 Blaze Stack.\n"
      "- Can store up to (10 + Base Dex / 25) stacks. Upon use, up to 10 stacks can be consumed for damage and MP gain formula.\n"
      "- Upon use, gain MP by (Blaze Stack consumed^2 * 3).\n\n"
      "**Game Description**: “Attacks enemies in a straight line with an aerial slash. Wind Power will accumulate when a normal attack hits. Wind Power is consumed upon skill activation. Power, attack range, and MP recovery increase according to the amount consumed.”\n"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234851231034245200/stormblaze.png?ex=68044693&is=6802f513&hm=10ef4d906da1e73cef4740c85ffa37befd08ca8e6cd82040707d7696037c7c8c&https://cdn.discordapp.com/attachments/614452674137686022/1234851231034245200/stormblaze.png?ex=68044693&is=6802f513&hm=10ef4d906da1e73cef4740c85ffa37befd08ca8e6cd82040707d7696037c7c8c&"
  },
  "Garde Blade": {
    "title": "Garde Blade",
    "description": (
      "**T4 Skill**\n"
      "Two-Handed Sword only\n"
      "**MP Cost**: 300\n\n"
      "**Buff Effect**:\n"
      "- Your weapon refinement now works like a shield's refinement value.\n"
      "- Increase your Physical Resistance & Magic Resistance by +(Skill Level)%\n"
      "- If you don’t have this skill buff yet, using this skill will recover Guard gauge by (2.5 * Skill Level + VIT/100). Can only recover until you reach 100 Guard Gauge.\n"
      "- You will be immune to interrupted (Flinch/Tumble/Stun/Knockback) if you Perfect Guard.\n\n"
      "**Buff Duration**: 70 seconds or UNTIL you got “Guard Power Break”\n\n"
      "**Game Description**: “A defense technique using a two-handed sword. Boosts Physical/Magic Resistance and improves Guard ability for 70 seconds. Recovers Guard Power a bit when the buff is applied. Overwriting won't trigger this recovery.”\n\n"
      "- You cannot use this skill if you got “Guard Power Break.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234851230308892672/gardeblade.png?ex=68044693&is=6802f513&hm=2016a6b195daf6815db6d107019a07f2e8622ef1ee2a60b42075e7d3e2fff1c8&"
  },
  "Ogre Slash": {
    "title": "Ogre Slash",
    "description": (
      "**T5 Skill**\n"
      "Two-Handed Sword only\n"
      "**MP Cost**: 500\n\n"
      "**Base Skill Constant (First Hit)**: Total Dex\n"
      "**Base Skill Multiplier (First Hit)**: (Base STR + Base VIT)/100\n"
      "**Base Skill Constant (Second AOE Hit)**: 500\n"
      "**Base Skill Multiplier (Second AOE Hit)**: 2 * Ogre Stack Consumed\n"
      "**Hit Count**: 2 hits\n"
      "**Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
      "**Second Hit Range**: 2m around the target\n\n"
      "**Skill Effect**:\n"
      "- You will passively gain Ogre Stack by:\n"
      "   - +Floor(Skill Level / 2) from being the first to engage battle\n"
      "   - +1 from getting warning red/blue AOE\n"
      "   - +1 from receiving damage taken\n"
      "   - +1 from perfect timed guard\n"
      "- You can store up to 20 Ogre stacks, but can only consume up to 10 stacks.\n"
      "- This skill has Physical Pierce by (10 * Ogre Stack Consumed)%; if this effect makes this skill’s total Physical Pierce exceed 100%, every 1% excessive Physical Pierce is converted to 0.01 bonus multiplier to the First Hit instead.\n"
      "- The second AOE hit of this skill can be affected by SRD%. The second AOE’s proration is the same as the first hit’s proration.\n"
      "- During this skill animation, you’re immune to interrupt ailments (Flinch/Tumble/Stun/Knockback).\n\n"
      "**Buff Effect**:\n"
      "- Double Rampage Auto Attack and Final Blow damage.\n"
      "- Mitigate Berserk Stability Penalty by 50%. So, Berserk at Level 10 with -25% stability will become -12% stability.\n"
      "- Mitigate DEF/MDEF% Berserk Penalty by 50%.\n"
      "- You will recover HP based on MP Bar consumption by (MP Bar Consumed ^ 2) * 100 HP.\n\n"
      "**Buff Duration**: (3 + 2 * Skill Level) seconds\n\n"
      "**Game Description**: “Deals damage to the target and after a short while, causes an explosion at the target's feet, dealing additional damage. If the conditions are met, Ogre Power will be accumulated and consumed upon skill activation to increase the power and buff.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234851230778523708/orgeslash.png?ex=68044693&is=6802f513&hm=7a85f490d272fdd70dc873bbd7b5ad6fb6127ce9f39f993d53c878d2d8a928b8&https://cdn.discordapp.com/attachments/614452674137686022/1234851230778523708/orgeslash.png?ex=68044693&is=6802f513&hm=7a85f490d272fdd70dc873bbd7b5ad6fb6127ce9f39f993d53c878d2d8a928b8&https://cdn.discordapp.com/attachments/614452674137686022/1234851230778523708/orgeslash.png?ex=68044693&is=6802f513&hm=7a85f490d272fdd70dc873bbd7b5ad6fb6127ce9f39f993d53c878d2d8a928b8&"
  }



}


######################################## BOW #################################################################################################################################################################


skillsshot = {
    "Power Shot": {
    "title": "Power Shot",
    "description": (
      "**Lv 1 Skill**\n"
      "Bow/Bowgun/Arrow only\n"
      "**MP Cost**: 100\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 1.25 + 0.05 * Skill Level\n"
      "**Base Skill Constant**: 50 + 8 * Skill Level\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: 16m\n\n"
      "**Skill Effect**:\n"
      "- This skill has an innate Motion Speed penalty of (155 - 10.5 * Skill Level)%; the penalty is applied as follows:\n"
      "   Power Shot Animation Time Modifier = Animation Time Modifier * (1 + Motion Speed penalty/100)\n"
      "- This skill gains Critical Rate +(5 * Skill Level) if your target has Slow Ailments\n\n"
      "**Ailment: Tumble**\n"
      "Base Ailment Chance: 20% + (3 * Skill Level)%\n"
      "Ailment Duration: 3 seconds\n"
      "Ailment Resistance: 3 seconds (Easy and Normal); 6 seconds (Hard); 12 seconds (Nightmare); 18 seconds (Ultimate)\n\n"
      "**Game Description**: “Shoot the target with stronger power. The charge time reduces as the skill levels up. Chance to inflict [Tumble] on the target. Critical rate increases on Slowed targets.”\n\n"
      "**Bow bonus**:\n"
      "- Tumble chance +40%\n\n"
      "**Bowgun bonus**:\n"
      "- Motion Speed penalty -50%\n\n"
      "**Bowgun penalty**:\n"
      "- Tumble chance -40%"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869081218224906291/powershot.png?ex=68047ef5&is=68032d75&hm=ba5347352b316cdf277e8c723c9dd329807742d8bfc3726140564b39c3a96088&"
  },
  "Bullseye": {
    "title": "Bullseye",
    "description": (
      "**Lv 1 Skill**\n"
      "Bow/Bowgun/Arrow only\n"
      "**MP Cost**: 200\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 0.25 + 0.05 * Skill Level; multiplier for each hit\n"
      "**Base Skill Constant**: 30 + 4 * Skill Level; constant for each hit\n"
      "**Hit Count**: 3 hits; dodge, Evasion, Guard, Anticipate, Guard Break and critical calculations are done for the first hit, then copied for the other hits; the rest of damage calculation is done for each hit\n"
      "**Maximum Cast Range**: 12m\n\n"
      "**Skill Effect**:\n"
      "- This skill has Physical Pierce +(4 * Skill Level)% on the second hit\n"
      "- Physical Pierce +(8 * Skill Level)% on the third hit\n\n"
      "**Game Description**: “Consecutively shoot at a point. The damage dealt increases attack by attack.”\n\n"
      "**Bow bonus**:\n"
      "- Skill Multiplier +0.25\n\n"
      "**Bowgun bonus**:\n"
      "- Second hit's Physical Pierce +10%; third hit's Physical Pierce +20%"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084769382703164/bullseye.png?ex=68048243&is=680330c3&hm=366485df0f3a5d544ffe2e057c161a1886bd74b15a3e56bdc611674f9edbf79b&"
  },
  "Arrow Rain": {
    "title": "Arrow Rain",
    "description": (
      "**Lv 2 Skill**\n"
      "Bow/Bowgun/Arrow only\n"
      "**MP Cost**: 300\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 1 + Floor(Skill Level / 2) * 0.06; multiplier for each hit\n"
      "**Base Skill Constant**: 50 + Floor((Skill Level + 1)/2) * 10; constant for each hit\n"
      "**Hit Count**:\n"
      "- 1 hit (levels 1 and 2)\n"
      "- 2 hits (levels 3 to 5)\n"
      "- 3 hits (levels 6 to 8)\n"
      "- 4 hits (levels 9 and 10)\n"
      "(Damage calculation is done for each hit)\n\n"
      "**Maximum Cast Range**: 12m\n"
      "**Hit Range (Radius)** around the target when the skill is cast:\n"
      "- 1.5m (levels 1 to 3)\n"
      "- 2m (levels 4 to 6)\n"
      "- 2.5m (levels 7 to 9)\n"
      "- 3m (level 10)\n\n"
      "**Game Description**: “Shoot a lot of arrows to the sky. The arrows fall down at intervals and deal damage.”\n\n"
      "**Bow bonus**:\n"
      "- Hit Range +2m\n"
      "- Hit Count is doubled\n\n"
      "**Bowgun bonus**:\n"
      "- Skill Multiplier +0.7\n\n"
      "**Additional Notes**:\n"
      "- This skill is unaffected by Whack, Long Range and Short Range Damage/Long Range Damage stats\n"
      "- Triple Thrust's Skill Constant buff is divided by the Hit Count"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084800684797982/arrowrain.png?ex=6804824b&is=680330cb&hm=881a779c7161f1298dddaa313adc913cc107f29ea75742aa2c86b63960e67e0d&"
  },
  "Snipe": {
    "title": "Snipe",
    "description": (
      "**Lv 3 Skill**\n"
      "Bow/Bowgun/Arrow only\n"
      "**MP Cost**: 400\n"
      "**Damage Type**: Physical\n\n"
      "**Base Skill Multiplier**: 7 + 0.1 * Skill Level\n"
      "**Base Skill Constant**: 300 + 10 * Skill Level\n"
      "**Hit Count**: 1 hit\n"
      "**Maximum Cast Range**: 16m\n"
      "**Charge Time**:\n"
      "- 5 seconds (levels 1 and 2)\n"
      "- 4 seconds (levels 3 and 4)\n"
      "- 3 seconds (levels 5 to 7)\n"
      "- 2 seconds (levels 8 and 9)\n"
      "- 1 second (level 10)\n\n"
      "**Skill Effect**:\n"
      "- Gains **Perfect Aim** if the target has **Blind** ailment\n"
      "- Critical Rate penalty: (25 - floor(Skill Level/2))%\n"
      "  > Snipe Critical Rate = Total Critical Rate * (1 - Penalty/100)\n\n"
      "**Ailment: Armor Break**\n"
      "- Base Chance: 50% + (2 * Skill Level)%\n"
      "- Duration: 5 seconds\n"
      "- Resistance: None\n\n"
      "**Game Description**: “Snipe a weak point. The charge time decreases as the skill levels up. Chance to inflict [Armor Break]. 100% chance to hit Blind targets.”\n\n"
      "**Bow bonus**:\n"
      "- Skill Multiplier +2\n"
      "- Armor Break chance +30%\n"
      "- Total Critical Rate penalty becomes (10 - Skill Level)%\n\n"
      "**Bowgun bonus**:\n"
      "- Skill Multiplier +3\n"
      "- Charge Time -0.5 seconds\n"
      "- Stability of this skill increased by +20%\n\n"
      "**Bowgun penalty**:\n"
      "- Armor Break chance -60%"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084817751441489/snipe.png?ex=6804824f&is=680330cf&hm=ba3211c0abbfd247185264e11e31cf96633c6d21a27a96a41fa3ea684b1f44fb&"
  },
  "Cross Fire": {
    "title": "Cross Fire",
    "description": (
      "**Lv 4 Skill**\n"
      "Bow/Bowgun only\n"
      "**MP Cost**: 400 (buff cast) / 0 (attack cast)\n"
      "**Damage Type**: Physical\n\n"
      "**Main Hit Skill Multiplier**: (4 + 0.5 * Skill Level) * number of charges\n"
      "**Additional Hits Skill Multiplier**: 2 (each hit)\n"
      "**Decoy Hit Skill Multiplier**: (0.8 + 0.1 * Skill Level) * number of charges\n"
      "**Main Hit Skill Constant**: 300 + 10 * Skill Level\n"
      "**Additional Hits Skill Constant**: 300 + 10 * Skill Level (each hit)\n"
      "**Decoy Hit Skill Constant**: 60 + 2 * Skill Level\n"
      "**Hit Count**:\n"
      "- 1 hit (Main Hit and Decoy Hit)\n"
      "- (number of charges - 1) hits for Additional Hits\n\n"
      "**Cast Range**:\n"
      "- Buff Cast: Unlimited\n"
      "- Attack Cast: 12m\n"
      "**Hit Range**:\n"
      "- Main Hit: 100m length, 1m radius from caster\n"
      "- Additional Hits: Around main target\n"
      "- Decoy Hit: 100m length, 1m radius from decoy position\n\n"
      "**Skill Effect**:\n"
      "- Attack cast will fizzle if no charges available\n"
      "- Additional hit from Decoy Shot if active\n"
      "- Attack cast ignores Combo Tag if same as Buff cast\n"
      "- Combo Multiplier carries over and is calculated as:\n"
      "  `Total = Attack Combo Multiplier + Buff Combo Multiplier - 100`\n"
      "- Only *Bloodsucker* and *Mind’s Eye* tags cannot apply on buff cast\n"
      "- Buff cast can still apply tags like *Smite*, *Save*, *Tenacity*, etc.\n\n"
      "**Buff Effect**:\n"
      "- Makes next Cross Fire cast 0 MP\n"
      "- Gains charges over time, starting from 0\n"
      "- Max Charges:\n"
      "  - 2 (Lv 1–3), 3 (Lv 4–6), 4 (Lv 7–9), 5 (Lv 10)\n"
      "- Charge Time:\n"
      "  - 1s (1st), 2s (2nd), 5s (3rd), 10s (4th), 17s (5th)\n"
      "- Getting hit:\n"
      "  - Stops charging\n"
      "  - Cancels buff if no charges\n"
      "- Buff Duration: Until you use the attack cast OR get hit with 0 charges\n"
      "- Charge animation not affected by status Motion Speed, but is by *Swift* tag\n\n"
      "**Game Description**:\n"
      "“Charge Skill (5 Levels). Attack toward a target and deal damage in a straight line. Power increases as the charge level increases and adds an attack. Add another attack by meeting certain conditions.”\n\n"
      "**Bow bonus**:\n"
      "- Main Hit Multiplier bonus: ((baseDex/500 + 0.5) * number of charges)\n"
      "- Main Hit radius +1m\n\n"
      "**Bowgun bonus**:\n"
      "- Additional Hits Multiplier +1\n"
      "- Additional Hits Physical Pierce +(baseDex / 10)%\n\n"
      "**Damage Modifier Notes**:\n"
      "- *Whack*, *Long Range*, and *Short Range Damage* affect Main & Decoy Hits\n"
      "- *Whack* only affects Additional Hits"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084836323790858/crossfire.png?ex=68048253&is=680330d3&hm=b083cc7470c2cb7a699ed95823d3cd8bf141237cc0277908e6f344b549a070cf&"
  },
  "Moeba Shot": {
    "title": "Moeba Shot",
    "description": (
      "**Lv 1 Skill**\n"
      "Bow/Bowgun/Arrow only\n"
      "**MP Cost**: 100\n"
      "**Damage Type**: Physical\n"
      "**Element**: Water (Dual Element – gains extra element from equipped Arrow)\n\n"
      "**Base Skill Multiplier**: 1 + 0.05 * Skill Level\n"
      "**Base Skill Constant**: 50 + 5 * Skill Level\n"
      "**Hit Count**: 1 hit\n"
      "**Max Cast Range**: 14m\n\n"
      "**Bonus Effect**:\n"
      "- If this skill causes *Slow* ailment, then **for that hit only**, bonus:\n"
      "  - Base Skill Multiplier += (0.5 + baseDex / 100)\n\n"
      "**Ailment: Slow**\n"
      "- Base Chance: 50% + (2 * Skill Level)%\n"
      "- Duration: 10 seconds\n"
      "- Resistance: None\n\n"
      "**Game Description**:\n"
      "“Shoot with sticky liquid. Water element attack. Dual Element with Arrow. Chance to inflict [Slow Down] on the target.”\n\n"
      "**Bow bonus**:\n"
      "- Slow Chance +30%\n\n"
      "**Bowgun bonus**:\n"
      "- Skill Multiplier +0.5\n"
      "- Slow Chance -30%"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084859266662450/moebashot.png?ex=68048259&is=680330d9&hm=4686549a4115579b3eef397f7e5cb20d80c289e52558444c1abdb4535fac0ef7&"
  },
  "Paralysis Shot": {
  "title": "Paralysis Shot",
  "description": (
    "**Lv 2 Skill**\n"
    "Bow/Bowgun/Arrow only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n"
    "**Element**: Wind (Dual Element – gains extra element from equipped Arrow)\n\n"
    "**Base Skill Multiplier**: 1.1 + 0.05 * Skill Level\n"
    "**Base Skill Constant**: 100 + 20 * Skill Level\n"
    "**Hit Count**: 1 hit\n"
    "**Max Cast Range**: 14m\n\n"
    "**Bonus Effect**:\n"
    "- If this skill causes *Paralysis* ailment, then **for that hit only**, bonus:\n"
    "  - Base Skill Multiplier += (1 + baseDex / 100)\n\n"
    "**Buff Effect**:\n"
    "- Increases Stability by +(Skill Level)%\n"
    "- Duration: 10 seconds\n\n"
    "**Ailment: Paralysis**\n"
    "- Base Chance: 50% + (2 * Skill Level)%\n"
    "- Duration: 10 seconds\n"
    "- Resistance: None\n\n"
    "**Game Description**:\n"
    "“Shoot the target with a paralysis poison. Wind element attack. Dual Element with Arrow. Chance to inflict [Paralysis] on the target. Increase your Stability for a while.”\n\n"
    "**Bow bonus**:\n"
    "- Skill Multiplier +1\n"
    "- Paralysis Chance +20%\n\n"
    "**Bowgun bonus**:\n"
    "- Skill Multiplier +1.5\n"
    "- Paralysis Chance -20%"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084871035858964/paralysisshot.png?ex=6804825c&is=680330dc&hm=eb6d7939fb9100157b50a4977e2d8263f17fd9ebc7d31d789e4d6b82f7bf3d6b&"
},
"Smoke Dust": {
  "title": "Smoke Dust",
  "description": (
    "**Lv 3 Skill**\n"
    "Bow/Bowgun/Arrow only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n"
    "**Element**: Dark (Dual Element – gains extra element from equipped Arrow)\n\n"
    "**Base Skill Multiplier**: 1.2 + 0.05 * Skill Level\n"
    "**Base Skill Constant**: 200 + 30 * Skill Level\n"
    "**Hit Count**: 1 hit\n"
    "**Max Cast Range**: 14m\n\n"
    "**Bonus Effect**:\n"
    "- If this skill causes *Blind* ailment, then **for that hit only**, bonus:\n"
    "  - Base Skill Multiplier += (2 + baseDex / 100)\n\n"
    "**Buff Effect**:\n"
    "- Increases Accuracy by +(Skill Level² / 2 + 5 * Skill Level)\n"
    "- Duration: 10 seconds\n\n"
    "**Ailment: Blind**\n"
    "- Base Chance: 50% + (2 * Skill Level)%\n"
    "- Duration: 10 seconds\n"
    "- Resistance: None\n\n"
    "**Game Description**:\n"
    "“An attack with a smokescreen. Dark element attack. Dual Element with Arrow. Chance to inflict [Blind] on the target. Increases accuracy rate for a while.”\n\n"
    "**Bow bonus**:\n"
    "- Skill Multiplier +2\n"
    "- Blind Chance +20%\n\n"
    "**Bowgun bonus**:\n"
    "- Skill Multiplier +2.5\n"
    "- Blind Chance -20%"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084892577808394/smokedust.png?ex=68048261&is=680330e1&hm=ca78c269b78d4fda51be1406e93ea77f34720d911c7f08269024a5b4aaec5633&"
},
"Arm Break": {
  "title": "Arm Break",
  "description": (
    "**Lv 4 Skill**\n"
    "Bow/Bowgun/Arrow only\n"
    "**MP Cost**: 700\n"
    "**Damage Type**: Physical\n"
    "**Element**: Neutral (Dual Element – gains extra element from equipped Arrow)\n\n"
    "**Base Skill Multiplier**: 3 + 0.05 * Skill Level\n"
    "**Base Skill Constant**: 300 + 40 * Skill Level\n"
    "**Hit Count**: 1 hit\n"
    "**Max Cast Range**: 14m\n\n"
    "**Bonus Effect**:\n"
    "- If this skill causes *Lethargy* ailment, then **for that hit only**, bonus:\n"
    "  - Base Skill Multiplier += (1.3 + baseDex / 100)\n\n"
    "**Ailment: Lethargy**\n"
    "- Base Chance: 50% + (2 * Skill Level)%\n"
    "- Duration: 10 seconds\n"
    "- Resistance: None\n\n"
    "**Game Description**:\n"
    "“Attack a target's arm and reduce its attack power. The base element is Neutral and it has Dual Element (Arrow). Chance to inflict [Lethargy].”\n\n"
    "**Bow bonus**:\n"
    "- Lethargy Chance +20%\n\n"
    "**Bowgun bonus**:\n"
    "- Skill Multiplier +3.5\n"
    "- Lethargy Chance -20%"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084911288610846/armbreak.png?ex=68048265&is=680330e5&hm=3995c87cfe00e3f83e3457441d067368c5da48919ed0203c5a012aaa83da7ab6&"
},
"Shot Mastery": {
  "title": "Shot Mastery",
  "description": (
    "**Lv 1 Skill**\n"
    "Bow/Bowgun only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Weapon ATK +(3 * Skill Level)%\n"
    "- ATK Bonus:\n"
    "  - +1% (Levels 1–2)\n"
    "  - +2% (Levels 3–7)\n"
    "  - +3% (Levels 8–10)\n\n"
    "**Game Description**:\n"
    "“Get better at using bows and bowguns. ATK of Bows and Bowguns increases.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084940233490522/shotmastery.png?ex=6804826c&is=680330ec&hm=697191af448192f85f29ff9aac3af760e2ab2a53bbe0e3026f1948c331148eb7&"
},
"Sneak Attack": {
  "title": "Sneak Attack",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: None\n\n"
    "**Buff Effect**:\n"
    "- For the next **(Skill Level)** auto attacks and attacking skills, you will not gain aggro.\n"
    "- **Buff Duration**: Until **(Skill Level)** attacks/skills are consumed.\n\n"
    "**Important Notes**:\n"
    "- *Support* and *non-attacking skills* (including Sneak Attack itself) **will still generate aggro**.\n"
    "- However, they **will not consume** the count from the buff.\n\n"
    "**Game Description**:\n"
    "“Hide yourself and turn Aggro away. Certain attacks don't get Aggro after this skill.”\n\n"
    "**Bow bonus**:\n"
    "- MP Cost -200\n\n"
    "**Bowgun bonus**:\n"
    "- MP Cost -200"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084951876861972/sneakattack.png?ex=6804826f&is=680330ef&hm=7d11ed16629a67862a4f34a02b0ea5125a152b4dc7b8eb115fdfc00b0fca096c&"
},
"Long Range": {
    "title": "Long Range",
    "description": (
      "**Lv 2 Skill**\n"
      "No Limit\n"
      "**Passive Effect**: Increases the damage of all skills that have a Maximum Cast Range of 8m or higher by **(Skill Level)%**\n\n"
      "**Game Description**:\n"
      "“You become good at attacking from distance. Damage dealt from 8 meters or more increases.”\n\n"
      "*Some skills are unaffected*"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084991768895498/longrange.png?ex=68048278&is=680330f8&hm=51d222c0dd06fcec5a7d84113b1ec54c2e7f735e1dfe7b48d98103ec7ef5384a&"
  },
  "Quick Draw": {
    "title": "Quick Draw",
    "description": (
      "**Lv 3 Skill**\n"
      "No Limit\n"
      "**Passive Effect**: Whenever an attacking skill that consumes MP is used, you have a **(3 * Skill Level)%** chance to recover **100 MP**\n\n"
      "**Game Description**:\n"
      "“Quickly prepare for the next move. Chance to restore MP a little when succeeding in attacking with a skill.”\n\n"
      "**Important Notes**:\n"
      "- Support skills, non-attacking skills, and attacking skills that do not consume MP **will not activate** this skill.\n"
      "- This includes the effects of combo tags and MP Cost modifiers."
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869084964090695750/quickdraw.png?ex=68048272&is=680330f2&hm=66380d06f347a197b2fd5f5b6b0ca1997c99c9497b587f31a42d27edc515e265&"
  },
  "Decoy Shot": {
    "title": "Decoy Shot",
    "description": (
      "**Lv 4 Skill**\n"
      "No Limit\n"
      "**MP Cost**: 400\n"
      "**Maximum Cast Range**: Theoretically infinite (limited to 100m)\n"
      "**Base Cast Time**: 1 second; affected by Cast Speed\n\n"
      "**Skill Effect**:\n"
      "- Places a decoy that auto attacks as long as the main target is within its range.\n"
      "- Full Attack MP Recovery and Aggro applies, but the decoy doesn't prorate.\n"
      "- The decoy attacks based on your Attack Speed (minimum delay: 0.001s).\n"
      "- **Duration**: 10 + (Skill Level x Skill Level / 2) seconds. (At Lv10 = 60s)\n\n"
      "**Decoy Auto Stats**:\n"
      "- Damage Type: Neutral\n"
      "- Element: Neutral\n"
      "- Multiplier: 0.2 + 0.08 * Skill Level\n"
      "- Hit Count: 1\n"
      "- Hit Range: Defaults to the weapon's Auto Attack Max Range\n\n"
      "**Important Notes**:\n"
      "- Not affected by character's Motion Speed, but affected by combo tag **Swift**.\n"
      "- Game Description: “Generate a clone and make it attack. The clone attacks enemies attacking within the range. The clone's attack is normal attack but it has no proration.”\n"
      "- **Non-Bow/Bowgun Penalty**: If hit by AoE, decoy's delay increases by 1s per hit (max 3s).\n"
      "- Auto Multiplier is unaffected by auto attack damage increases.\n"
      "- Decoy is affected by Combo Tag effects if used in combo.\n"
      "- Dual Swords benefit from doubled AMPR on decoy, but damage scales with main hand ATK only.\n"
      "- Decoy only attacks the mob/boss you are targeting.\n"
      "- Skill and decoy bypass Sneak Attack’s effect.\n"
      "- **Power Wave** has no effect on decoy range.\n"
      "- Stats like AMPR, Crit Rate, etc. will affect decoy in real-time, but **Attack Speed changes** require re-casting.\n"
      "- Poison ailment will still drain HP when decoy attacks.\n"
      "- Decoy cannot inflict Neutral Proration.\n"
      "- This decoy can sync with **Cloning** from “Scroll Tree”.\n\n"
      "**Bug Note**:\n"
      "- This skill has an **AMPR bug**: Every time the decoy attacks, it gives **+100% base AMPR** to your next auto attack.\n"
      "- The decoy can keep this benefit without consuming it.\n"
      "- Bug condition is inconsistent: may trigger based on character/weapon switch or relogging.\n"
      "- Even if unintentional, the effect still happens. Either ignore it, pretend not to notice, or report it. *Evil laugh...*\n"
      "- Using the system like this is considered a bug. (I wish it wasn't, but it is.)"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869085007350730842/decoyshot.png?ex=6804827c&is=680330fc&hm=923a3470a31b0c21f8281ada57d7e3986e1dd79aa0a817d1a976cbb5ff13b7aa&"
  },
  "Fatal Shot": {
    "title": "Fatal Shot",
    "description": (
      "**Lv 3 Skill**\n"
      "Bow / Bowgun Only\n"
      "**MP Cost**: 200\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats**:\n"
      "- **Base Skill Multiplier**: 5 + 0.1 * Skill Level + TotalSTR / 200 + TotalDEX / 200\n"
      "- **Base Skill Constant**: 200\n"
      "- **Hit Count**: 1 hit\n"
      "- **Maximum Cast Range**: 14m\n\n"
      "**Skill Effect**:\n"
      "- Critical Rate of this skill increased by **+40** (estimated)\n"
      "- Accuracy of this skill decreased by **0** (still under investigation)\n"
      "- Can extend **tap break time** by: Floor(Skill Level / 2)\n"
      "- *Note*: If the skill **misses, is evaded, or grazed**, it **does not** extend break time\n\n"
      "**Game Description**:\n"
      "“A shot skill that pierces through a strong armor. It's a unique attack with a high critical rate, but low accuracy. If it hits the target right, the tap time to break monster's part will be extended.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869097124372033556/fatalshot.png?ex=68048dc5&is=68033c45&hm=42ef377d453551deb99b13fff617821dc38ec60214f2297bd135c79039f4df9f&"
  },
  "Vanquisher": {
    "title": "Vanquisher",
    "description": (
      "**Lv 5 Skill**\n"
      "Bow / Bowgun Only\n"
      "**MP Cost**: 1200\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats**:\n"
      "- **Base Skill Multiplier**: 5 + Skill Level + base DEX / 100\n"
      "- **Base Skill Constant**: 1200\n"
      "- **Hit Count**: 1 hit\n"
      "- **Maximum Cast Range**: 8m\n"
      "- **Hit Range**: 8m with 0.5m damage radius\n\n"
      "**Skill Effect**:\n"
      "- Removes **Ignite debuff** immediately upon use if you are affected.\n"
      "- Prevents **power dispersion** (split damage) to multiple targets within the area.\n"
      "- Grants **Perfect Aim**.\n"
      "- Damage scales based on whichever is higher: **SRD%** or **LRD%**.\n\n"
      "**Game Description**:\n"
      "“Delivers a powerful blow to a small area. The power gets dispersed if there are multiple targets within the area. If you have ignite debuff, activating the skill will remove it, prevent the power dispersion and guarantee hits.”\n\n"
      "**Weapon-Specific Effects**:\n"
      "- **Katana Penalty**:\n"
      "  - MP Cost -600\n"
      "  - Skill Constant -600\n"
      "  - Removes `base DEX / 100` from Skill Multiplier\n\n"
      "- **Bowgun Bonus**:\n"
      "  - Removes **Twin Storm cooldown** completely upon use (regardless of skill level)\n"
      "  - During **Twin Storm cooldown**, total damage (Skill Multiplier) is **doubled**\n\n"
      "- **MD Penalty**:\n"
      "  - Skill Constant -600\n"
      "  - Changes `base DEX / 100` in Skill Multiplier into `base INT / 200`"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967816735413645402/conquester.png?ex=680470d2&is=68031f52&hm=5bce26aef78cb34c7919107224a11b9505b91b86a2e6988e69c36145e38a2f99&"
  },
  "Twin Storm": {
    "title": "Twin Storm",
    "description": (
      "**Lv 5 Skill**\n"
      "Bowgun Only\n"
      "**MP Cost**: 200\n"
      "**Damage Type**: None\n\n"
      "**Auto Attack Modifiers**:\n"
      "- Auto Attack Skill Multiplier: **+1** *(stacks additively with other effects like Rampage, Kairiki, etc.)*\n"
      "- Auto Attack Skill Constant: **+0**\n"
      "- Auto Attack Hit Count: **2 hits** *(damage calculated once, then split)*\n\n"
      "**Skill Effect**:\n"
      "- Grants **(10 + 2 × Skill Level)** Twin stacks upon use.\n"
      "- Each stack converts 1 auto attack into 2 hits (2 stacks consumed per auto).\n\n"
      "**Buff Effect**:\n"
      "- **1.5× Movement Speed** while the buff is active.\n"
      "- **Total AMPR is doubled** during Twin Stack buff.\n"
      "- If **MP is full**, gain:\n"
      "  - Auto Attack Skill Multiplier **+(4 + 0.5 × Skill Level)**\n"
      "  - Auto Attack Skill Constant **+base DEX / 2**\n"
      "- **Buff Duration**: Permanent, until Twin stacks are depleted.\n\n"
      "**Cooldown**:\n"
      "- After buff ends: **(20 - Skill Level) seconds** cooldown before skill can be reused.\n"
      "- During cooldown:\n"
      "  - Auto Attack Skill Multiplier: **-(1 - 0.01 × Skill Level)**\n"
      "  - Total AMPR reduced by **(100 - 5 × Skill Level)%**, minimum 10% (estimate)\n\n"
      "**Game Description**:\n"
      "“Prepares 2 bowguns to enhance normal attack. The attack is enhanced further if MP is full. After a certain number of normal attacks, they’ll run out of bolts and normal attacks turn weaker for a certain period of time. Not usable while it is in effect.”\n\n"
      "**Weapon Bonuses**:\n"
      "- **Magic Device**:\n"
      "  - AMPR becomes **3× normal** during Twin buff\n\n"
      "- **Dagger**:\n"
      "  - If MP not full: Auto Attack Skill Multiplier **+(Dagger ATK / 100)**\n"
      "  - Cooldown auto attack damage reduction decreased to **(100 - 4 × Skill Level)%**\n\n"
      "- **Arrow**:\n"
      "  - Twin Stack gain **tripled**: **(30 + 6 × Skill Level) stacks**\n\n"
      "**Other Notes**:\n"
      "- **Power Wave** is not disabled; affects auto attack max range and damage modifier\n"
      "- **This skill cannot be put in a combo**"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967816734910320711/twinstorm.png?ex=680470d2&is=68031f52&hm=65cc09e30892b51a9951d4cc75a09b9777f13d4dff81fa001b05dd8becc2c08b&"
  },
  "Retrograde Shot": {
    "title": "Retrograde Shot",
    "description": (
      "**Lv 5 Skill**\n"
      "Bow Only\n"
      "**MP Cost**: 300\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats**:\n"
      "- **Base Skill Multiplier**: 5 + 0.5 × Skill Level + Base DEX / 100\n"
      "- **Base Skill Constant**: 300\n"
      "- **Hit Count**: 1 hit\n"
      "- **Maximum Cast Range**: 12m\n"
      "- **Hit Range**: 100m with 2.5m damage radius\n\n"
      "**Skill Effect**:\n"
      "- Launches a linear attack that marks the enemy with the **highest HP** (if multiple are hit).\n"
      "- **Marked target** lasts for **(10 + 2 × Skill Level)** seconds.\n"
      "- **Marked Effect**:\n"
      "  - Reduces **Dodge/Flee** of marked target by `((Total STR + Total DEX) × 0.04)%`\n"
      "  - Receives **Additional Damage** from *Shot* or *Hunter* skills\n"
      "  - The mark is **visible to party members**\n\n"
      "**Additional Damage Mechanics**:\n"
      "- Each hit with Shot/Hunter skills triggers 1 extra hit on marked target\n"
      "- Additional Damage per hit:\n"
      "  - **Multiplier**: Starts at 1\n"
      "  - **Constant**: 0\n"
      "- Each additional hit increases the next one's multiplier by:\n"
      "  `(Total DEX × Skill Level / 100)%`\n"
      "- Maximum stacks: **Floor(Skill Level / 4) + 3**\n"
      "- **Affected by**: SRD% / LRD% and Physical Proration\n"
      "- **Not affected by**: Long Range passive or Combo tag multipliers\n\n"
      "**Special Mechanics**:\n"
      "- **50% Physical Pierce** applies to the additional hit of this skill\n"
      "- **Movement Effect**:\n"
      "  - Normally moves user **5m backward** after use\n"
      "  - If casting while holding forward, **no movement occurs**\n"
      "- Grants **1-time iframe** (like Zantei) that reduces incoming damage to **0** during animation\n"
      "  - Works **even if dash is canceled** (i.e., no backward movement)\n"
      "- This skill **is not affected by motion speed**\n"
      "  - If dash is canceled, animation becomes **14 frames slower**\n\n"
      "**Game Description**:\n"
      "“A Technique of shooting enemies while moving backward. Attacks in a linear range and the target with the most HP that gets hit will be marked.”\n"
      "- *The mark lowers dodge and triggers growing additional damage from Shot/Hunter skills. Only the caster can trigger this effect.*"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967816735161991178/bodyturnshot.png?ex=680470d2&is=68031f52&hm=e2881ccbda8151178746284c4d5397346c217ee30d3b1e87f8adffaee862ef01&"
  },
  "Parabola Shot": {
    "title": "Parabola Shot",
    "description": (
      "**Lv 5 Skill**\n"
      "Bow / Bowgun / Arrow Only\n"
      "**MP Cost**: 400\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats**:\n"
      "- **Base Skill Multiplier**: 7.5 + 0.25 × Skill Level + Total DEX / 100\n"
      "- **Base Skill Constant**: 400\n"
      "- **Hit Count**: 1 hit\n"
      "- **Maximum Cast Range**: 24m\n"
      "- **Hit Radius**: (0.5 × Skill Level)m\n"
      "- **Landing Distance**:\n"
      "  - Based on Bow/Bowgun's auto attack max range\n"
      "  - Fixed to 12m if using Sub Arrow\n\n"
      "**Ailment**:\n"
      "- **Silence**\n"
      "  - **Chance**: 100%\n"
      "  - **Duration**: ~15 sec\n"
      "  - **Ailment Resistance**: None (needs confirmation)\n\n"
      "**Skill Effect**:\n"
      "- Launches the user upward and fires in a **parabolic arc**, direction affected by movement input\n"
      "- **For Bow/Bowgun**:\n"
      "  - If skill **misses target**, it will set a **Trap** at landing point\n"
      "    - Trap Multiplier: +5 more than normal hit\n"
      "    - Trigger Radius: 1m\n"
      "    - Trap Duration: 30 sec\n"
      "    - Trap disappears if hit by any AoE (even mid-air)\n"
      "    - Only **one trap** can exist at a time (new cast replaces old trap)\n"
      "- **Trap Homing Effect**:\n"
      "  - If the target has **Retrograde Mark**, Parabola Shot will always **home and land** on that target\n"
      "  - Homing effect is **only for Bow/Bowgun**\n"
      "  - Sub Arrow users do **not** get this homing behavior\n"
      "- **LRD% only** affects this skill, regardless of distance\n\n"
      "**Game Description**:\n"
      "“Attacks by firing a projectile that follows a parabolic path. The attack range is always the same, but the direction can be changed with the arrow keys when firing. Chance to inflict [Silence].”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967816734339903608/parabolacannon.png?ex=680470d2&is=68031f52&hm=972ed5c019e0c58e932fb0bb72e2fe7b846ef8467a01139b4945f6f94cde1d20&"
  },
  "Hunting Buddy": {
    "title": "Hunting Buddy",
    "description": (
      "**Tier 4 Skill**\n"
      "Bow / Bowgun Only — [Active Skill]\n"
      "**MP Cost**: 100 (summon), 0 (cancel summon)\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats**:\n"
      "- **Base Skill Multiplier**: 1 + Total DEX / 1000 + (0.1 × Skill Level × Stack) \n"
      "  - Max Stacks: 25 (No icon; calculated behind the scenes)\n"
      "- **Base Skill Constant**: 100\n\n"
      "**Stack Mechanic**:\n"
      "- Stacks are gained when the user hits the target with **Shot Skills**\n"
      "- Stacks **reset to 0** each time the dog attacks\n"
      "- **Auto Attack Multiplier boosters** (e.g., *Kairiki Ranshin*, *Berserk*, Power Wave/Mana Thrash regislets) are **added** to the base multiplier\n\n"
      "**Skill Behavior**:\n"
      "- Summons a dog companion that attacks the target every few seconds\n"
      "- The dog **returns to the user** after each attack before attacking again\n"
      "- Staying **far** or **running away** increases the delay between attacks\n"
      "- Uses **physical proration** and behaves like a **normal attack** (not skill proration)\n"
      "- **Affected by**: Short Range Damage (SRD), Awaken Element\n"
      "- **Not affected by**: Whack\n\n"
      "**Bow/Bowgun Bonus**:\n"
      "- When you are **knocked out**, the dog will use **First Aid** on you before disappearing (unless the whole party is wiped)\n"
      "- First Aid level equals the **Hunting Buddy Skill Level**\n\n"
      "**Game Description**:\n"
      "“Summons your companion to fight alongside you. It attacks every few seconds, causing normal attack proration. The effect that enhances your companion's next attack will stack when you hit the target with a Shot Skill.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/1343488198814466058/1349330595532115998/sprite_3.png?ex=680425cb&is=6802d44b&hm=1ae043b1ddff34159341bd626accd7d9908339a5d05f9db3cfe355d6b0889726&"
  },
  "Piercing Shot": {
    "title": "Piercing Shot",
    "description": (
      "**Tier 5 Skill**\n"
      "Bow / Bowgun Only — [Active Skill]\n"
      "**MP Cost**: 600\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats (per Hit)**:\n"
      "- **Base Skill Multiplier**: 10 + (0.25 × Skill Level) + Base DEX / 200\n"
      "- **Base Skill Constant**: 600 + Bonus (if not Graze)\n"
      "- **Bonus Skill Constant (based on hit #)**:\n"
      "  - 1st hit: Boss DEF × 0.25\n"
      "  - 2nd hit: Boss DEF × 0.5\n"
      "  - 3rd hit: Boss DEF × 0.75\n"
      "  - 4th–5th hits: Boss DEF × 1.0\n"
      "- **Hit Count**: 5 hits total (1 hit per charge level)\n"
      "- **Max Cast Range**: 24m\n"
      "- **Max Hit Range**: 45m (linear AOE)\n\n"
      "**Charge Mechanic**:\n"
      "- **Manual Charge Time**: 2 seconds per charge (10s for max 5 charges)\n"
      "- **Vs. Sleeping/Interrupted Targets**: 1s per charge (5s max)\n"
      "- **Combo Use**: Always 1 charge\n"
      "- **Quick Loader** applies to manual charge only\n"
      "- **Movement & Direction** can be adjusted with *Evasion*\n\n"
      "**MP Recovery**:\n"
      "- Recovers MP based on: AMPR × 1.5 × number of **non-graze** hits to the main target\n\n"
      "**Other Details**:\n"
      "- Affected by: Short Range / Long Range Damage %, Long Range Skill %, Physical Proration\n"
      "- Not affected by Motion Speed\n"
      "- **Graze Hits**: Deal less stable damage, give no bonus constant, and no MP recovery bonus\n"
      "- 🔧 *Bug*: Yellow graze hits appear as fake non-graze crits (visual only, mechanics unchanged)\n\n"
      "**Bowgun Bonus**:\n"
      "- Gains **1s invincibility** at the start or resumption of charging\n"
      "- Moving or using a skill (including Evasion) will **cancel** the invincibility\n\n"
      "**Game Description**:\n"
      "“An arrow that pierces even the strongest defense. Aims and attacks in a straight line with a Charge Skill (5 Levels). You can move and adjust the direction with Evasion. Each hit (except for Graze) increases its performance and slightly restores MP.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/1343488198814466058/1349330595838296118/sprite_6.png?ex=680425cb&is=6802d44b&hm=987b91a70bc8ecaf0fc467372e5587a6ff6682a12669490fa91ccbf84cec3808&"
  },
  "Spread Shot": {
    "title": "Spread Shot",
    "description": (
      "**Tier 5 Skill**\n"
      "Bow / Bowgun Only — [Active Skill]\n"
      "**MP Cost**: 200\n"
      "**Damage Type**: Physical\n\n"
      "**Skill Stats (per Hit)**:\n"
      "- **Base Skill Multiplier**: 2 + (0.1 × Skill Level)\n"
      "- **Base Skill Constant**: 200\n"
      "- **Ignore DEF**: (30 + 5 × Skill Level)% (separate from Physical Pierce and Armor Break)\n"
      "- **Hit Count**:\n"
      "  - **No Directional Key**: 5 Hits in fan-shaped AOE\n"
      "  - **Front/Back Key**:\n"
      "    - Bow: 5 Hits in linear spread\n"
      "    - Bowgun: 5 Hits like gatling gun (linear)\n"
      "  - **Left/Right Key**:\n"
      "    - 1st Hit ➜ Evasion (90° circle around target) ➜ 2nd Hit\n"
      "- **Max Cast Range**: 12m (AOE Skill)\n\n"
      "**Ailment Effect**:\n"
      "- **Element-based Ailments**:\n"
      "  - Neutral: None\n"
      "  - Fire: Ignite\n"
      "  - Water: Freeze\n"
      "  - Wind: Dazzled\n"
      "  - Earth: Poison\n"
      "  - Light: Weaken\n"
      "  - Dark: Curse\n"
      "- **Ailment Chance**: 1.2 × Skill Level % (per hit; stacks cumulatively on same target)\n"
      "  - Example: At Skill Lv10, 5 hits = 60% total base chance\n"
      "- **Bow Bonus**: Doubles ailment chance (e.g., 120% if all hits land)\n"
      "- **Ailment Resistance**: 10 seconds\n"
      "- **Special**:\n"
      "  - Element Starter skill allows 2 ailments if using different element on bow & arrow\n"
      "  - Regislets (Element Talent) override and enforce one specific element\n\n"
      "**Other Details**:\n"
      "- Not affected by Short/Long Range %\n"
      "- Not affected by Long Range Skill %\n"
      "- Uses and applies Physical Proration\n\n"
      "**Bowgun Bonus**:\n"
      "- Multiplier is **doubled** (×2) if you cast the skill with **left/right directional key**\n\n"
      "**Game Description**:\n"
      "“Attacks using 5 skillfully controlled arrows. Chance to inflict a status ailment (weapon element) on the target. Each hit on the same target slightly improves its performance. You can also change their direction the arrows are fired by using the directional keys.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/1343488198814466058/1349330595087646811/sprite_4.png?ex=680425cb&is=6802d44b&hm=db0d3b11e4686d327448ffb04d8e233ca019d6b4f93875aa989a5cab4c45c6bf&"
  },
  "Samurai Archery": {
    "title": "Samurai Archery",
    "description": (
      "**Level 5 Skill**\n"
      "Sub Katana Only — [Passive Skill]\n\n"
      "**Passive Effects**:\n"
      "- **Weapon ATK Boost**:\n"
      "  - + (Katana BaseWATK × 0.1 × Skill Level)\n"
      "  - But capped at: (Bow BaseWATK × Bow BaseStability × 0.1 × Skill Level)\n"
      "- **Stability Boost**:\n"
      "  - + (Katana Base Stability / 4)\n"
      "- **Accuracy Buff**:\n"
      "  - When you land a Normal Attack with Katana:\n"
      "    - Gain Accuracy buff: (Skill Level × Stack)%\n"
      "    - Buff duration: until the next skill is used\n"
      "    - Max Stacks: 10\n\n"
      "**Game Description**:\n"
      "“Slightly raises ATK and stability if a bow and a katana are equipped at the same time. If a normal attack is performed with the katana, the accuracy of the next skill used increases.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967816734700625980/samuraibowtechniques.png?ex=680470d2&is=68031f52&hm=16b523191686df1c78d7b768a358f163789a291a321972010817f7e7f59d7695&"
  },
  "Quick Loader": {
    "title": "Quick Loader",
    "description": (
      "**Tier 5 Skill**\n"
      "Bow / Bowgun Only — [Active Skill]\n"
      "**MP Cost**: 400\n\n"
      "**Buff Effect**:\n"
      "- Grants **3 Quick Loader Charges** (cannot be overwritten until expired)\n"
      "- **Bowgun Penalty**: Only 2 charges granted (loses 1 charge upon use)\n"
      "- Automatically consumes 1 charge to instantly increase **Cross Fire** charge by 1 level if it's not fully charged\n"
      "- If you’ve learned **Sneak Attack**, using Quick Loader will also grant Sneak Attack buff (level capped by Quick Loader level)\n"
      "- Buff Duration: **(120 - 6 × Skill Level) seconds**\n"
      "- Skill cast always has +50% Motion Speed\n\n"
      "**Game Description**:\n"
      "“Activates Cross Fire and increases its charge by 1 level if is not fully charged. This skill is not overwritten.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234852279514038362/quickloader.png?ex=6804478d&is=6802f60d&hm=07d642211a6fd8988958b849a58eafea6878b4a77904ab9f90d7d676824c1d97&"
  },
  "Element Starter": {
    "title": "Element Starter",
    "description": (
      "**Tier 5 Skill**\n"
      "Bow / Bowgun Only — [Passive Skill]\n\n"
      "**Passive Effects**:\n"
      "- Allows **non-dual element skills** to apply both:\n"
      "  - Main Weapon Element\n"
      "  - Arrow Element\n"
      "- If the skill has a **Fixed Element**, it will replace Arrow Element: becomes [Main Weapon + Fixed Element]\n"
      "- Enables interaction with **Elemental Weakness System**\n"
      "- When hitting with an element that is stronger than the enemy:\n"
      "  - Gain +1 Element Stack (up to 99 stacks)\n"
      "  - If you take damage:\n"
      "    - Recover HP = Floor(Skill Level × Max HP / 1000) × Stack\n\n"
      "**Game Description**:\n"
      "“The element of bow or bowgun will be activated at the same time as the arrow. *Not valid for dual element skills. Gets a small recovery barrier each time you deal damage to targets with the element you are weak to.”"
    ),
    "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/1234852279883137055/elementstarter.png?ex=6804478d&is=6802f60d&hm=1aee1b1dc3771e751cb21f7730e6a0c906b4fb266886715b96df385a6e5b0070&"
  }

}


###############################################################################################################################################################################

skillshalberd = {

"Flash Stab": {
  "title": "Flash Stab",
  "description": (
    "**Lv 1 Skill**\n"
    "One-Handed Sword / Halberd Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.05 * Skill Level\n"
    "- **Base Skill Constant**: 50 + 5 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n\n"
    "**Skill Effect**:\n"
    "- Motion Speed of this skill is boosted by **+50%**\n"
    "- *One-Handed Sword Penalty*: Motion Speed boost reduced by **-25%**\n\n"
    "**Game Description**:\n"
    "“Sharply attack an enemy with a quick movement.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175551762518056/flashstab.png?ex=68042e10&is=6802dc90&hm=81e3c1c62d78db12328032931b9ba45c03cafc4658716a9e8f70b8b723882bf9&"
},
"Cannon Spear": {
  "title": "Cannon Spear",
  "description": (
    "**Lv 1 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier (First Hit)**: 0.4 + 0.01 * Skill Level\n"
    "- **Base Skill Multiplier (Toss)**: 1.5 + 0.1 * Skill Level\n"
    "- **Base Skill Constant (First Hit)**: 100 + 10 * Skill Level\n"
    "- **Base Skill Constant (Toss)**: 0\n"
    "- **Hit Count**: 2 hits (each hit calculated separately)\n"
    "- **Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
    "- **Hit Range (Toss)**: \n"
    "  - Length: 8m (Lv 1-2), 9m (Lv 3-4), 10m (Lv 5-6), 11m (Lv 7-8), 12m (Lv 9-10)\n"
    "  - Radius: 1m (Lv 1-5), 2m (Lv 6-10); from caster's position\n\n"
    "**Skill Effect**:\n"
    "- Damage calculated for First Hit and Toss separately\n"
    "- *Note*: Triple Thrust's Skill Constant buff is **halved** when this skill is used\n\n"
    "**Game Description**:\n"
    "“Attack an enemy by throwing the halberd. The range increases as the skill levels up.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175565565960222/cannonspear.png?ex=68042e13&is=6802dc93&hm=35cb89c68c5895afe25d876368f3f5fc21decb5b71cfc752f12067c42471f627&"
},
"Dragon Tail": {
  "title": "Dragon Tail",
  "description": (
    "**Lv 2 Skill**\n"
    "Halberd Only\n"
    "**Type**: Active\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **First Hit**:\n"
    "  - **Multiplier**: 0.7 + 0.03 * Skill Level\n"
    "  - **Constant**: 100\n"
    "  - **Hit Range**: 1.5m (Lv 1–5), 2m (Lv 6–10)\n"
    "- **Second Hit**:\n"
    "  - **Multiplier**: 2 + 0.2 * Skill Level\n"
    "  - **Constant**: 50 + 15 * Skill Level\n"
    "  - **Hit Range**: 2.5m (Lv 1–3), 3m (Lv 4–6), 3.5m (Lv 7–9), 4m (Lv 10)\n"
    "- **Hit Count**: 2 hits (separate damage calculation per hit)\n"
    "- **Maximum Cast Range**: Theoretical infinite (must target something to cast)\n\n"
    "**Buff Effect**:\n"
    "- Reduces incoming damage while casting (does not reduce Fractional Damage)\n"
    "- If animation is at 1-hit: Receive 50% damage once\n"
    "- If animation is at 2-hit: Receive (100 - 10 * Skill Level)% damage once\n\n"
    "**Ailment**: Tumble (does not affect bosses)\n"
    "- **Chance**: 10 * Skill Level % (only mobs)\n"
    "- **Duration**: 3 seconds\n"
    "- **Ailment Resistance**: 3 seconds\n\n"
    "**Additional Info**:\n"
    "- Reduces **Triple Thrust**’s Skill Constant Buff effect by 50%\n\n"
    "**Game Description**:\n"
    "“Whirl around the Halberd and swipe enemies. Chance to inflict [Tumble]. Unable to inflict Tumble on boss monsters.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175574743097344/dragontail.png?ex=68042e15&is=6802dc95&hm=3a9620679ac771384bda7da2206288701ef8c55f68a2048e1ca766112ae565a5&"
},
"Dive Impact": {
  "title": "Dive Impact",
  "description": (
    "**Lv 3 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier (1st Hit)**: 2 + 0.2 * Skill Level + TotalSTR / 250\n"
    "- **Base Skill Multiplier (2nd Hit)**: 2 + 0.4 * Skill Level + TotalINT / 100\n"
    "- **Base Skill Constant (1st Hit)**: 200 + 20 * Skill Level\n"
    "- **Base Skill Constant (2nd Hit)**: 0\n"
    "- **Hit Count**: 2 hits\n"
    "- **Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
    "- **Hit Range (1st Hit)**: (2.5 + 0.25 * Skill Level)m around caster\n"
    "- **Hit Range (2nd Hit)**: (4.5 + 0.25 * Skill Level)m from caster's position at cast\n\n"
    "**Skill Effect**:\n"
    "- 2nd hit detonates **after 4 seconds**\n"
    "- 2nd hit may inflict **[Dazzled]**:\n"
    "  - Chance: (10 * Skill Level)%\n"
    "  - Duration: 10s\n"
    "  - Resistance: 30s\n"
    "- Grants **Invincibility** for 3s or until landing\n"
    "- Motion speed is **fixed** (not affected by Swift tags or Motion Speed%)\n"
    "- Affected by **Whack** on both hits\n"
    "- *Note*: Only 1st hit is affected by Short/Long Range Damage modifiers\n"
    "- *Triple Thrust's Skill Constant buff is halved* when used\n\n"
    "**Game Description**:\n"
    "“The thrust Halberd breaks the earth in time. Generate a mass explosion and deal additional damage after a while with a chance to inflict [Dazzled] when the skill is activated.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175584817815562/diveimpact.png?ex=68042e17&is=6802dc97&hm=5a72bc9dc4837a9b55eb11651e67b6ec2c6ca7ad49ad768985cf6de4c6dc9ee6&"
},
"Dragon Tooth": {
  "title": "Dragon Tooth",
  "description": (
    "**Lv 4 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier (1st Hit)**: 0.75 * Skill Level\n"
    "- **Base Skill Multiplier (2nd Hit)**: 7.5\n"
    "- **Base Skill Constant**: 0 (both hits)\n"
    "- **Hit Count**: 2 hits\n"
    "- **Maximum Cast Range**: 12m\n"
    "- **Hit Range**: Single target; radius of 0.5m + weapon’s Auto Attack Range, around caster’s landing position\n\n"
    "**Skill Effect**:\n"
    "- Caster jumps to enemy’s position and returns to original position\n"
    "- Jump speed depends on **Motion Speed** and distance\n"
    "- Grants immunity to **Flinch**, **Tumble**, and **Stun** during animation\n"
    "- Critical Rate **+65 + Skill Level**\n"
    "- Physical Pierce **+(10 * Skill Level)%**\n"
    "- *Note*: If jump distance exceeds (0.5m + auto attack range), this skill won’t deal damage\n\n"
    "**Game Description**:\n"
    "“Jump toward a target and attack. After using the skill, you will return to the original place. It has high Defense Ignorance and Critical Rate but it has no bonus on power.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175598596112424/dragontooth.png?ex=68042e1b&is=6802dc9b&hm=ada6034362d461fea7d25217fc9d2e8fd220bcf3753bb10ee8720c1bb2973381&"
},
"Deadly Spear": {
  "title": "Deadly Spear",
  "description": (
    "**Lv 1 Skill**\n"
    "One-Handed Sword / Halberd Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1.2 + 0.05 * Skill Level\n"
    "- **Base Skill Constant**: 80 + 3 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to the weapon's Auto Attack Max Range\n"
    "- **Base Charge Time**:\n"
    "  - 1.5s (Lv 1)\n"
    "  - 1s (Lv 2–4)\n"
    "  - 0.5s (Lv 5–7)\n"
    "  - None (Lv 8–10)\n\n"
    "**Skill Effect**:\n"
    "- Critical Rate **+300% Total Crit Rate** (4x of your total crit rate)\n"
    "- Physical Pierce:\n"
    "  - +10% (Lv 1–3)\n"
    "  - +15% (Lv 4–6)\n"
    "  - +20% (Lv 7–9)\n"
    "  - +25% (Lv 10)\n"
    "- If this skill **crits**, the **next skill’s MP cost is halved**\n"
    "- *One-Handed Sword Penalty*:\n"
    "  - Skill Multiplier: -0.2\n"
    "  - Critical Rate boost: -2.5\n\n"
    "**Game Description**:\n"
    "“Accurately thrust an enemy and deal fatal damage. It takes time to activate the skill, however, ignore certain amount of defense and have a high chance to inflict critical damage.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175617717940224/deadlyspear.png?ex=68042e1f&is=6802dc9f&hm=855872dc3f869a16d27bb535fb7aa5df85f2575f84df04dfbda738fcda059879&"
},
"Punish Ray": {
  "title": "Punish Ray",
  "description": (
    "**Lv 2 Skill**\n"
    "One-Handed Sword / Halberd Only\n"
    "**MP Cost**: 0\n"
    "**Damage Type**: Physical / Magical\n"
    "**Element**: Neutral\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 0.25 + 0.01 * (Skill Level)^2 + Total INT / 400\n"
    "- **Base Skill Constant**: 0\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: 12m\n"
    "- **Base Cast Time**: 2 seconds (affected by Cast Speed)\n\n"
    "**Skill Effect**:\n"
    "- Damage is calculated as Physical base, but rest uses Magic calculation\n"
    "- Magic Proration is applied\n"
    "- Cannot be used as the first skill in a combo\n\n"
    "**Buff Effect**:\n"
    "- Boosts Critical Rate of the next 3 skills:\n"
    "  - **+15 * Skill Level** for 1st skill\n"
    "  - **+10 * Skill Level** for 2nd skill\n"
    "  - **+5 * Skill Level** for 3rd skill\n"
    "- Buff Duration: Until a skill is used\n\n"
    "**Weapon Bonus/Penalty**:\n"
    "- *Halberd Bonus*: Skill Multiplier is doubled\n"
    "- *One-Handed Sword Penalty*:\n"
    "  - 1st Skill Crit Rate boost ÷ 1.5\n"
    "  - 2nd and 3rd Skill Crit Rate boost ÷ 2\n\n"
    "**Game Description**:\n"
    "“Cast a magic using the Halberd to resemble a staff. Deal magic damage affected by ATK. Critical Rate of the next skill increases.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175634889441304/punishray.png?ex=68042e23&is=6802dca3&hm=48ca7015ec7c1eba75cb69755f4dda157a2224932f2f575151c90bdd9143f321&"
},
"Strike Stab": {
  "title": "Strike Stab",
  "description": (
    "**Lv 3 Skill**\n"
    "One-Handed Sword / Halberd Only\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1.9 + 0.01 * Skill Level + Total STR / 500 (per hit)\n"
    "- **Ailment Bonus Multiplier**: 0.1 * Skill Level (added if target has ailment)\n"
    "- **Base Skill Constant**: 100 (per hit)\n"
    "- **Hit Count**: 3 hits (damage calculated once, copied to all hits)\n"
    "- **Maximum Cast Range**: Defaults to weapon's Auto Attack Max Range\n\n"
    "**Skill Effect**:\n"
    "- Base Crit Rate Penalty: (5 * Skill Level)%\n"
    "- Final Crit Rate Formula:\n"
    "  - (25 + CRT / 3.4) * (1 - Penalty%) * (1 + CritRate%) + FlatCrit\n"
    "- *One-Handed Sword Penalty*: Above formula divided by 2\n"
    "- If target has an ailment, Ailment Multiplier is added\n\n"
    "**Weapon Bonus/Penalty**:\n"
    "- *Halberd Bonus*: Ailment Multiplier x2, +100 Skill Constant\n\n"
    "**Game Description**:\n"
    "“Thrust an enemy with a quick movement. The damage increases if the target has a status ailment. Have a low chance to deal critical.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175647866605608/strikestab.png?ex=68042e26&is=6802dca6&hm=b61f142e060ac9eb2ddb26d2965b6bb97c59df935f0d3391dbec3c3b5d940739&"
},
"Chronos Drive": {
  "title": "Chronos Drive",
  "description": (
    "**Lv 4 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.5 * Skill Level (total of all hits)\n"
    "- **Base Skill Constant**: 40 * Skill Level\n"
    "- **Hit Count**: 3 hits (damage calculated once, spread evenly)\n"
    "- **Maximum Cast Range**: Defaults to weapon's Auto Attack Max Range\n\n"
    "**Skill Effect**:\n"
    "- Target receives additional hits over time\n"
    "- Effect Duration:\n"
    "  - 5s (Lv 1–2), 6s (Lv 3–4), 7s (Lv 5–6), 8s (Lv 7–8), 9s (Lv 9), 10s (Lv 10)\n"
    "- **Additional Damage**:\n"
    "  - **Type**: Physical/Magical (calculated as Magic Proration, but does not cause it)\n"
    "  - **Multiplier**: 0.4 + 0.01 * Skill Level + Total INT / 500\n"
    "  - **Constant**: 250 + 25 * Skill Level\n"
    "- **MP Recovery**: Recovers 30 MP per additional hit\n"
    "- **Additional Hit Timing**:\n"
    "  - Delay = Auto Attack Delay + 1.5 * Animation Time Modifier / 100\n"
    "  - Hit Count = Effect Duration / Delay\n"
    "- Additional hits copy crit/miss/graze/evasion from main hit\n\n"
    "**Notes**:\n"
    "- Additional hits not affected by Motion Speed, Combo Tags, Whack, SRD/LRD\n\n"
    "**Game Description**:\n"
    "“Repeat the fact that you penetrated a target. Add an effect that you deal additional damage for a few seconds.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175653671505960/chronosdrive.png?ex=68042e28&is=6802dca8&hm=53a55604a6f5727aaf24c3d79f5317a73a83c59034db4a2ca26781d30ed5d9d2&"
},
"Halberd Mastery": {
  "title": "Halberd Mastery",
  "description": (
    "**Lv 1 Skill**\n"
    "Halberd Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Weapon ATK + (3 * Skill Level)%\n"
    "- ATK Boost:\n"
    "  - +1% (Lv 1–2)\n"
    "  - +2% (Lv 3–7)\n"
    "  - +3% (Lv 8–10)\n\n"
    "**Game Description**:\n"
    "“Get better at using Halberds. ATK increases when you equip a Halberd.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175693588713472/halberdmastery.png?ex=68042e31&is=6802dcb1&hm=28605cadb6036479a59eac95a2bdf5b2f99d45ee365b00e05b7ec3a76d96b10c&"
},
"Critical Spear": {
  "title": "Critical Spear",
  "description": (
    "**Lv 3 Skill**\n"
    "Halberd Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- **Critical Rate %**:\n"
    "  - +0% (Lv 1)\n"
    "  - +1% (Lv 2–3)\n"
    "  - +2% (Lv 4–5)\n"
    "  - +3% (Lv 6–7)\n"
    "  - +4% (Lv 8–9)\n"
    "  - +5% (Lv 10)\n"
    "- **Flat Critical Rate**:\n"
    "  - +1 (Lv 1–2)\n"
    "  - +2 (Lv 3–4)\n"
    "  - +3 (Lv 5–6)\n"
    "  - +4 (Lv 7–8)\n"
    "  - +5 (Lv 9–10)\n\n"
    "**Game Description**:\n"
    "“Learn the mastery of Halberds. Critical Rate increases when you equip a Halberd.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175701952135188/criticalspear.png?ex=68042e33&is=6802dcb3&hm=74189544f1aa4a5c61a3a568d94325d8ea8a8f226e3f9fbe4b9681e4d05b2b4e&"
},
"Quick Aura": {
  "title": "Quick Aura",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 0\n"
    "**Damage Type**: None\n\n"
    "**Skill Effect**:\n"
    "- Consumes 15% of Max HP to activate\n"
    "- If HP is insufficient, user is left at 1 HP and buff is downgraded to Lv 1 effect\n\n"
    "**Buff Effect**:\n"
    "- Attack Speed: +(2.5 * Skill Level)% and +(50 * Skill Level)\n"
    "- Duration: 3 minutes\n\n"
    "**Weapon Bonus**:\n"
    "- *Halberd Bonus*: Max HP Consumption -5%\n"
    "- *Halberd Bonus*: Buff Duration +2 minutes\n\n"
    "**Game Description**:\n"
    "“Increase your speed with the fighting spirit. Activate skills by consuming HP instead of MP. Increase ASPD for a certain period of time.”\n"
    "**Notes**:\n"
    "- Cannot be used as the first skill in a combo"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175716678357012/quickaura.png?ex=68042e37&is=6802dcb7&hm=c4f8a18e10dcdaa35c31b5fccab48e4bb97346535c1907a0efacc01057e6cfbe&"
},
"War Cry of Struggle": {
  "title": "War Cry of Struggle",
  "description": (
    "**Lv 2 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: None\n\n"
    "**Base Charge Time**:\n"
    "- 5s (Lv 1–3)\n"
    "- 4s (Lv 4–6)\n"
    "- 3s (Lv 7–9)\n"
    "- 2s (Lv 10)\n\n"
    "**Skill Effect**:\n"
    "- Restores 120 MP on cast\n"
    "- Additional MP recovery based on current HP:\n"
    "  - HP ≤ 85%: +2 * Skill Level MP\n"
    "  - HP ≤ 70%: +4 * Skill Level MP\n"
    "  - HP ≤ 55%: +20 + (10 * Skill Level) MP\n"
    "- All effects stack\n\n"
    "**Weapon Bonus**:\n"
    "- *Halberd Bonus*: Charge Time -1 second\n\n"
    "**Game Description**:\n"
    "“The roar of life in a critical situation. Restore MP a little. The amount of the MP restoration increases as the current HP is low.”\n"
    "**Notes**:\n"
    "- Cannot be used in a combo"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175724727230525/warcryofstruggle.png?ex=68042e39&is=6802dcb9&hm=a070d70246e261575de1c9de7b9b5f9abe8042cfd9be9c3f8a48940f510077e4&"
},
"Godspeed Wield": {
  "title": "Godspeed Wield",
  "description": (
    "**Lv 4 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: None\n\n"
    "**Skill Effect**:\n"
    "- Every time you use the skill, you add a stack to the buff; the buff can have 3 stacks maximum\n\n"
    "**Buff Effect**:\n"
    "- Attack Speed **+ (30 * Skill Level * number of stacks)**\n"
    "- Motion Speed **+ (Skill Level * number of stacks)%**\n"
    "- Evasion Recharge **+ (Skill Level * number of stacks)%**\n"
    "- Max MP **- (100 * number of stacks)**\n"
    "- Physical Resistance and Magic Resistance **- ((100 - 3 * Skill Level) * number of stacks)%**\n\n"
    "**Buff Duration**: 10 + (2 * Skill Level) seconds\n\n"
    "**Game Description**:\n"
    "“Consume MaxMP and able to stack 3 times at most. Enhance ASPD/Action Speed/Evasion Recharge for a short period of time and greatly decrease Physical and Magic Resistance. The effect ends when taking damage.”\n\n"
    "**Halberd Bonus**:\n"
    "- Attack Speed of buff **+ (100 * number of stacks)**\n"
    "- Physical and Magical Resistance decrease of buff is reduced by **(45 * number of stacks)%**\n"
    "- Buff Duration **+30 seconds**"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175735632400404/godspeedwield.png?ex=68042e3b&is=6802dcbb&hm=2a307aa561974f1221a94b831cfc73058c44a1bfdb2691794aaa7c5ee41a37ee&"
},
"Buster Lance": {
  "title": "Buster Lance",
  "description": (
    "**Lv 3 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Constant**: 100\n"
    "- **Base Skill Multiplier**:\n"
    "  5 - Max[0, (distance - 6)] * (100 - Skill Level * 5)% + (TotalSTR + TotalAGI)/200\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: 12m\n"
    "- *Note*: distance = range between you and target when using this skill.\n"
    "  Max is highest value, e.g., Max[0, -4] = 0\n\n"
    "**Skill Effect**:\n"
    "- If you use this skill when you have **Punish Ray Buff**, then this skill will transform into **Grand Buster Lance**\n\n"
    "**Grand Buster Lance**:\n"
    "- This is a **magic skill** but uses **ATK** as base damage\n"
    "- Affected by **Concentrate**\n"
    "- Stab, hit, evasion, and damage calc checks are applied normally (like a physical skill)\n"
    "- **Damage Type**: Magic\n"
    "- **Base Skill Constant**: 200\n"
    "- **Base Skill Multiplier**:\n"
    "  5 + 0.1 * Punish Ray’s level - Max[0, (distance - 6)] * (60 - Skill Level * 4)% + (TotalSTR + TotalAGI)/200\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: 12m\n"
    "- *Note*: distance = range between you and target when using this skill\n\n"
    "**Skill Effect**:\n"
    "- Inflicts **Magic Proration**\n"
    "- Damage based on **Magic Proration**\n"
    "- Using Grand Buster Lance **refreshes Punish Ray stacks to 3**\n"
    "- **Leveling up Punish Ray** increases Grand Buster Lance's multiplier\n\n"
    "**Notes**:\n"
    "- Stability, hit, evasion, and damage calc are based on physical characteristics\n"
    "- Casted as **Buster Lance** first (physical skill), then transforms\n"
    "- Treated as a **magic skill**, so:\n"
    "  - Affected by **Concentrate**, not **Whack**\n"
    "  - Cannot be used under **Bleed** or **Silence** status\n\n"
    "**Game Description**:\n"
    "“Attack by throwing a spear from a distance. The further you are from the target, the weaker it is. The skill will change if certain conditions are met and the distance-based power depletion will also be minimized.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869175749607845908/busterlance.png?ex=68042e3f&is=6802dcbf&hm=469053b15efe082407142231321b844ae15fa7c1f96e635f797e1b9ef201b056&"
},
"Draconic Charge": {
  "title": "Draconic Charge",
  "description": (
    "**Lv 5 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical (First Hit) and Hybrid (Second Hit)\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier (First Hit)**: (5 + 0.5 * Skill Level) * (90% + Charge%)\n"
    "- **Base Skill Constant (First Hit)**: 300\n"
    "- **Base Skill Multiplier (Second AOE Hit)**: (5 + 0.5 * Skill Level) * (90% + Charge%)\n"
    "- **Base Skill Constant (Second AOE Hit)**: 0\n"
    "- **Hit Count**: 2 hits on the main target; 1 hit on all other targets (damage calculated individually)\n"
    "- **Maximum Cast Range**: Theoretically infinite (but needs target to cast)\n"
    "- **Second AOE Hit Range**: In front of the caster after dash, with 4m radius and 90° angle\n"
    "- **Teleport Distance**: 8m\n\n"
    "**Second AOE Hit Ailments**:\n"
    "- Neutral: None\n"
    "- Fire: Ignite\n"
    "- Water: Freeze\n"
    "- Wind: Slow\n"
    "- Earth: Poison\n"
    "- Light: Blind\n"
    "- Dark: Cursed\n"
    "- **Ailment Chance**: (Skill Level ^ 2)%\n"
    "- **Ailment Duration**: 10 sec\n"
    "- **Ailment Resistance**: None\n\n"
    "**Skill Effect**:\n"
    "- First Hit has **Perfect Aim**\n"
    "- Physical Pierce bonus = **+Floor(distance - 1m) * 10%**\n"
    "- Second AOE Hit is **Absolute Critical**\n"
    "- If 2nd AOE Hit is evaded:\n"
    "  - Normal evade = Yellow Crit → White (non-crit)\n"
    "  - Absolute evade (e.g., Evil Crystal Beast) = Still evaded\n"
    "- 2nd AOE Hit uses hybrid damage with physical characteristics (phy proration, crit rate, stability, etc.)\n"
    "- 2nd Hit formula: **(ATK + MATK/2 + Player Lvl - Enemy Lvl) * (100 - pres)% - MDEF**\n"
    "- **Magic Pierce affects 2nd Hit**, Physical Pierce does **not**\n\n"
    "**Manual Mode**:\n"
    "- Manual use enters **Charge Mode**\n"
    "- Gains **+20% Charge per 1 second** (unaffected by motion speed)\n"
    "- Skill auto-releases when moved or charge reaches 100%\n"
    "- Can manually release at 20%+\n"
    "- If enemy AOE is sensed during charge: **Instant 100% Charge release**\n"
    "*Note: You must begin charging before AOE appears to auto-trigger full charge.*\n\n"
    "**Combo Mode**:\n"
    "- When in combo (not opener), auto-charges and releases at 10%\n"
    "- Charge% based on combo slot:\n"
    "  - 2CC & 3CC: 10%\n"
    "  - 4CC: 15%\n"
    "  - 5CC: 20%\n"
    "  - 6CC: 25%\n"
    "  - Up to 10CC: 45%\n"
    "- Formula: **MIN(10%, (CC - 1) * 5%)**\n\n"
    "**Teleport Mechanics**:\n"
    "- After charge, teleport to **1m in front of main target**, max teleport range is 8m\n"
    "- Skill will **not deal damage** if 1st hit fails to reach (needs <=8m), or 2nd AOE exceeds its 12m requirement\n\n"
    "**Other Notes**:\n"
    "- Damage is affected by **srd% only** (not motion speed, etc.)\n"
    "- **Long Range shot skills** also apply\n"
    "- 2nd Hit now follows the **same proration** as 1st Hit\n\n"
    "**Game Description**:\n"
    "“Unleashes the rage of a dragon. Activates when it is full or when you move. Accumulates more rage if you sense danger from charging. Be careful not to miss as the range of the charge attack is only 8 meters.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967833235348398141/dragoniccharge.png?ex=68048030&is=68032eb0&hm=21ab130eaf4db9110a3834af16dd010fe74e34873123d028ab26656bd3ef06cc&"
},
"Infinite Dimension": {
  "title": "Infinite Dimension",
  "description": (
    "**Lv 5 Skill**\n"
    "Halberd Only\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 4 + BaseSTR / 1000 (per tick)\n"
    "- **Base Skill Constant**: 20 * Skill Level (per tick)\n"
    "- **Hit Count (Number of Ticks)**: 5 ticks (damage calculated for each tick)\n"
    "- **Hit Count (Hits per Tick)**: 2 hits (damage calculated once per tick, split evenly)\n"
    "- **Maximum Cast Range**: 12m\n"
    "- **Hit Range**: 6m radius around target's position when casted\n"
    "- **Interval Hit**: 1 tick = 2 hits every 1 second (unaffected by motion speed%, Swift, and Freeze)\n\n"
    "**Ailment Effect (per tick)**:\n"
    "- **Ailment**: Dazzled\n"
    "- **Base Chance**: (8 * Skill Level)%\n"
    "- **Duration**: 10 sec\n"
    "- **Ailment Resistance**: None\n\n"
    "**Skill Effect**:\n"
    "- This skill does **not inflict proration**, but damage is still based on **Physical Proration**\n"
    "- If **Chronos Drive** effect is active:\n"
    "  - Recovers **MP per tick = (Total AMPR / 10) * Skill Level**\n"
    "- Attack animation ends **immediately** when main target dies\n"
    "- Damage is **not affected by srd% or lrd%**\n\n"
    "**Game Description**:\n"
    "“Repeated spear attacks that transcend time and space. Repeatedly performs wide-ranging attacks around a target. Chance to inflict [Dazzled]. If Chronos Drive is in effect, extra MP will be recovered.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967833235096743998/dimensiontear.png?ex=68048030&is=68032eb0&hm=9f68ba34d717008a3083916736d7ac10ed786dd5b3eb00f02f40eb28b32423e2&"
},
"Tornado Lance": {
  "title": "Tornado Lance",
  "description": (
    "**Lv 5 Skill**\n"
    "Halberd Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Gain **1 Tornado Lance stack** each time you use a Halberd attacking skill that **does not miss or get evaded**\n"
    "- **Max Stack**: 10\n"
    "- Lose **half of your current stacks** when you get hit (even if dodged/missed by the enemy)\n"
    "- *Note*: Evasion (iframe) and invincibility **do not** cause stack loss; **dodged hits (miss)** still reduce stacks\n"
    "- **Buff Duration**: 100 seconds (refreshed on each valid halberd skill hit)\n\n"
    "**Buff Effects (per stack)**:\n"
    "- **+ (Skill Level / 5) Critical Damage**\n"
    "- **+10% Dodge / Flee**\n"
    "- **+ (2.5 * Stack * Skill Level / 10)% Chance to trigger Additional Melee/Magic**\n"
    "- **+ (8 * Stack * Skill Level / 10)% Graze Threshold**\n"
    "*Note: Halberd has 20% base Graze Threshold*\n\n"
    "**Special Effect**:\n"
    "- If the enemy is affected by **Dazzled**, then Hit Chance becomes:\n"
    "  - **MAX[(100 - (Enemy Flee - Player Accuracy) + MP / 10) ; Base Graze Threshold * 2]**\n"
    "- This Hit Chance calculation uses only the **base Graze Threshold** (Tornado Lance's bonus not included)\n\n"
    "**Other Notes**:\n"
    "- At maximum effect, this skill **reduces Graze Stability penalty** from -50% to -40%\n"
    "- With 100% Final Stability, damage fluctuation from graze is reduced to between **60% and 100%**\n\n"
    "**Game Description**:\n"
    "“Gains 1 unit of tornado power when a halberd skill hits. Your halberd gets stronger as you accumulate more tornado power. Half of the tornado will be lost if attacked.”\n"
    "Increases halberd’s critical damage, chance of additional attack and guaranteed hit as it accumulates. When the tornado power is lost due to getting attacked, dodge rate increases according to the value of power lost."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967833235843321886/tornadolance.png?ex=68048030&is=68032eb0&hm=ede3d9a10d792fa3882100ba9d6385f9b3df94b7e97c0e76d159a566a23807f5&"
},
"Almighty Wield": {
  "title": "Almighty Wield",
  "description": (
    "**Lv 5 Skill**\n"
    "Halberd Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Modifies **Godspeed Wield** mechanics:\n"
    "  - Chance to **lose only 1 stack instead of all** upon taking damage = **(10 * Skill Level)%**\n"
    "  - Reduces **Physical & Magic Resistance penalties** from Godspeed Wield by **(Skill Level / 2 * stack)%**\n\n"
    "**Halberd Bonus**:\n"
    "- Grants additional shortcut skills based on this skill's level:\n"
    "  - At **Level 1**: Unlocks **“Almighty Wield III”** → Instantly grants **3 GSW stacks**\n"
    "  - At **Level 5**: Unlocks **“Almighty Wield II”** → Instantly grants **2 GSW stacks**\n"
    "  - At **Level 10**: Unlocks **“Almighty Wield I”** → Instantly grants **1 GSW stack**\n"
    "*Note: GSW stack effects follow your current **Godspeed Wield** level*\n\n"
    "**Game Description**:\n"
    "“Alleviates the amount of each resistance decreased due to the skill “Godspeed Wield” and possibly lowers the buffs level by 1 to keep them active.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967833235608461352/godspeedwield.png?ex=68048030&is=68032eb0&hm=21b2018fc44666d9b33dcaaac6d77aa4c0b531d4e165b51ae7aa47e46cf86b37&"
},
"Blitz Spike": {
  "title": "Blitz Spike",
  "description": (
    "**T3 Skill**\n"
    "Halberd Only\n"
    "**Type**: Active\n"
    "**MP Cost**: 300\n\n"
    "**[Short Range Version] (0-7m Cast Range)**\n"
    "- **Damage Type**: Physical (uses ATK)\n"
    "- **Base Skill Multiplier**: 3 + 0.1 * Skill Level + 0.1 * Thor's Hammer Skill Level\n"
    "- **Base Skill Constant**: 300\n"
    "- **Hit Count**: 2 hits (damage calculated once, then divided evenly)\n"
    "- **Proration Type**: Magic Proration\n"
    "- **Affected by**: Short Range Damage%, Long Range Skill%\n\n"
    "**Ailment**: Paralysis\n"
    "- **Chance**: (5 * Skill Level + INT / 10)%\n"
    "- **Resistance Duration**: 10 seconds\n\n"
    "**Paralysis Additional Magic Damage** (Halberd Thunder)\n"
    "- **Damage Type**: Magic (uses MATK)\n"
    "- **Base Skill Multiplier**: 1 + 0.3 * Skill Level + 0.1 * Thor's Hammer Skill Level + Base INT / 200\n"
    "- **Base Skill Constant**: Total INT / 2\n"
    "- **Hit Count**: 1 hit (Absolute Critical)\n"
    "- **Proration Type**: Magic Proration\n"
    "- **Affected by**: Short Range Damage%, Long Range Skill%\n\n"
    "**[Long Range Version] (8-24m Cast Range)**\n"
    "- **Damage Type**: Physical (uses ATK)\n"
    "- **Base Skill Multiplier**: Total INT / 200\n"
    "- **Base Skill Constant**: Total INT\n"
    "- **Hit Count**: ROUNDUP(Skill Level / 3)\n"
    "- **MP Recovery**: 100% of character's AMPR per bullet\n"
    "- **Proration Type**: Normal Proration\n"
    "- **Not affected by**: Short/Long Range Damage% or Long Range Skill%\n\n"
    "**Game Description**:\n"
    "“A swift spear thrust wrapped in lightning. Chance to inflict [Paralysis] when activated near the target. "
    "If paralyzed, the target will take additional magic damage. When activated at a distance, lightning spears that "
    "automatically attack approaching enemies will be summoned.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1310475215893037069/1360086038378184714/sprite_9.png?ex=68046254&is=680310d4&hm=5ed8edc3126c6d8c60dfd426e698675c8bcf28c80566128a4f09668c4ad0a5c3&"
},
"Lightning Hail": {
  "title": "Lightning Hail",
  "description": (
    "**T4 Skill**\n"
    "Halberd Only\n"
    "**Type**: Active\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Magic (uses MATK - Halberd Thunder)\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.2 * ROUNDDOWN(Skill Level / 2) + Total INT / 1000\n"
    "- **Base Skill Constant**: 100 + 10 * Skill Level\n"
    "- **Hit Count**: 3 + ROUNDUP(Skill Level / 2)\n"
    "- **Invincibility Frame**: 2 seconds (ends when skill animation ends)\n"
    "- **Maximum Cast Range**: 18m\n"
    "- **Critical Type**: Absolute Critical\n\n"
    "**Skill Effect**:\n"
    "- Damage calculated separately per hit\n"
    "- Forced Long Range Skill\n"
    "- Affected by Long Range Damage% and Long Range Skill%\n"
    "- Uses and deals **Magic Proration**\n"
    "- Not affected by character's motion speed%, but **Swift** combo tag does affect it\n\n"
    "**Game Description**:\n"
    "“A spear technique that summons multiple lightning strikes from the sky. Generates multiple attacks that deal magic damage around the target. "
    "More likely to hit paralyzed targets. Grants invincibility to yourself when activated.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1310475215893037069/1360086047681286235/sprite_8.png?ex=68046256&is=680310d6&hm=5011f5aede94dcaca2fb33429b548639adadddd4b9b6565fe919a6f708d13c9c&"
},
"Thor's Hammer": {
  "title": "Thor's Hammer",
  "description": (
    "**T5 Skill**\n"
    "Halberd Only\n"
    "**Type**: Active\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Magic (uses MATK - Halberd Thunder)\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: (10 + 0.5 * Skill Level) / Target Count\n"
    "- **Base Skill Constant**: 400\n"
    "- **Hit Count**: 1 per target (split damage if multiple targets)\n"
    "- **Maximum Cast Range**: 12m\n"
    "- **Critical Type**: Absolute Critical\n"
    "- **Damage Calculation**: Separate per hit\n\n"
    "**Skill Effect**:\n"
    "- Not affected by short/long range damage or long range skill%\n"
    "- Uses and deals **Magic Proration**\n\n"
    "**Additional Magic Damage – Lightning Hail's Trail**:\n"
    "- **Base Constant**: Uses current Lightning Hail’s Base Constant\n"
    "- **Multiplier**: Lightning Hail’s Base Multiplier * Hit Order\n"
    "  - 1st hit = L.Hail Multiplier * 1\n"
    "  - 2nd hit = L.Hail Multiplier * 2\n"
    "  - 3rd hit = L.Hail Multiplier * 3\n"
    "  - ... up to 8th hit = L.Hail Multiplier * 8\n"
    "- Absolute Critical; not affected by SRD/LRD; uses magic proration; **does not inflict proration**\n\n"
    "**Buff Effect (12s * Skill Level or until immobilized)**:\n"
    "- **Additional Magic**: +10 * Skill Level %\n"
    "- **Magic Pierce**: +2 * Skill Level %\n"
    "- **Accuracy**: + (Base INT * Skill Level / 10)\n\n"
    "**Game Description**:\n"
    "“A spear technique that calls down a massive lightning strike. A magic attack with guaranteed critical, "
    "but the damage will be split among targets caught in the blast. Once activated, your Additional Magic, Magic Pierce, "
    "and Accuracy Rate will increase for a certain period of time. Halberd Bonus: Accuracy Rate increases according to INT. "
    "The skill 'Lightning Hail' will leave a lightning trail, and when Thor's Hammer is activated, additional magic damage will be generated.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1310475215893037069/1360086054341841049/sprite_12.png?ex=68046258&is=680310d8&hm=8c8ac51cc8f42835a994f71f4ae78af1b72731ec790fb22536d821a2faafa34f&"
}

}


#########################################################################################################################################################################################

skillsmartial = {
    "Smash": {
  "title": "Smash",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 0.5 + 0.02 * Skill Level\n"
    "- **Base Skill Constant**: 5 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n\n"
    "**Ailment**:\n"
    "- **Type**: Flinch\n"
    "- **Base Ailment Chance**: 50% (levels 1 to 5); 75% (levels 6 to 10)\n"
    "- **Ailment Duration**: 2 seconds\n"
    "- **Ailment Resistance**: 1 second (Easy and Normal); 3 seconds (Hard); 6 seconds (Nightmare); 9 seconds (Ultimate)\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +0.5\n"
    "- **Skill Constant**: +(25 + total AGI / 10)\n"
    "- **Flinch Chance**: +25%\n\n"
    "**Game Description**:\n"
    "“Strongly hit the target. Chance to inflict [Flinch] on target.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169697554309120/smash.png?ex=68057a1c&is=6804289c&hm=9c143a6b18d834664b3f8c32a8859d5f84fc68fdc1fbafb2868b3d11b6f2a95e&"
},
"Bash": {
  "title": "Bash",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.05 * Skill Level\n"
    "- **Base Skill Constant**: 10 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n\n"
    "**Ailment**:\n"
    "- **Type**: Stun\n"
    "- **Base Ailment Chance**: 25% (levels 1 to 5); 50% (levels 6 to 10)\n"
    "- **Ailment Duration**: 5 seconds\n"
    "- **Ailment Resistance**: 25 seconds (Easy, Normal, Hard and Nightmare); 30 seconds (Ultimate)\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +(1 + total AGI / 500)\n"
    "- **Skill Constant**: +(50 + total AGI / 5)\n"
    "- **Stun Chance**: +(25 + total AGI / 10)%\n\n"
    "**Game Description**:\n"
    "“Strike a heavy blow on the head. Chance to inflict [Stun] on the target.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169720891424808/bash.png?ex=68057a21&is=680428a1&hm=c729dfe1719efcae68b52f93b9b520f48361f254da2592ee30b39e8dd91390e3&"
},

"Shell Break": {
  "title": "Shell Break",
  "description": (
    "**Lv 2 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.05 * Skill Level\n"
    "- **Base Skill Constant**: 50 + 10 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n\n"
    "**Skill Effect**:\n"
    "- Physical Pierce: +(5 * Skill Level)%\n"
    "- MP Recovery: Recover 400 MP if this skill inflicts Armor Break\n\n"
    "**Ailment**:\n"
    "- **Type**: Armor Break\n"
    "- **Base Ailment Chance**: 10% + (1.5 * Skill Level)%\n"
    "- **Ailment Duration**: 5 seconds\n"
    "- **Ailment Resistance**: None\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +0.5\n"
    "- **Skill Multiplier**: +((target's DEF - target's Level) / 50); capped between -1 and 5\n"
    "- **Skill Constant**: +150\n"
    "- **Skill Constant**: +((target's DEF - target's Level) * 2); capped between -100 and 500\n\n"
    "**Knuckle Main Only Bonus**:\n"
    "- **Armor Break Chance**: +25%\n\n"
    "**Game Description**:\n"
    "“A straight punch that penetrates hard armor. The damage dealt increases as the target's DEF is higher. Low chance to inflict [Armor Break]. Recover MP if it succeeds.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169746963218462/shellbreak.png?ex=68057a28&is=680428a8&hm=0a0a464c3d16c2d694064321b7b88336ab7a15939957ea98f4b8d564cedb374d&"
},
"Heavy Smash": {
  "title": "Heavy Smash",
  "description": (
    "**Lv 3 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.15 * Skill Level\n"
    "- **Base Skill Multiplier (Additional Hit)**: 1 + 0.15 * Skill Level\n"
    "- **Base Skill Constant**: 100 + 10 * Skill Level (per hit)\n"
    "- **Hit Count**: 1 hit; 2 hits if the target has the Armor Break ailment\n"
    "- **Additional Hit Notes**: Dodge, Evasion, Guard, Anticipate, and Guard Break calculations are done for the first hit and copied to the second; rest of damage calculation is done per hit\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n\n"
    "**Skill Effect**:\n"
    "- Gains a second, always-critical hit if the target has Armor Break\n\n"
    "**Ailment**:\n"
    "- **Type**: Lethargy\n"
    "- **Base Ailment Chance**: 20% + (3 * Skill Level)%\n"
    "- **Ailment Duration**: 10 seconds\n"
    "- **Ailment Resistance**: None\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +1.5\n"
    "- **Skill Multiplier (Additional Hit)**: +5\n"
    "- **Skill Constant**: +100\n"
    "- **Lethargy Chance**: +50%\n\n"
    "**Other Effect**:\n"
    "- Triple Thrust's Skill Constant buff applies only to the first hit\n\n"
    "**Game Description**:\n"
    "“Hit the target very hard. Chance to inflict [Lethargy] on the target. Deal additional damage on the target that has [Armor Break].”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169757167951892/heavysmash.png?ex=68057a2a&is=680428aa&hm=603211459717bb9f72e972a71e7697e83e24b9ee7f4a768c6501afc638195f35&"
},

"Chariot": {
  "title": "Chariot",
  "description": (
    "**Lv 4 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 9.9 + 0.01 * Skill Level\n"
    "- **Base Skill Constant**: 50 + 20 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: 12m\n"
    "- **Hit Range**: Single target without Knuckles main/sub; AoE with Knuckles: height 12m, radius 0.75m from caster\n"
    "- **Base Charge Time**: 11s (Lv 1), 9s (Lv 2–3), 7s (Lv 4–5), 5s (Lv 6–7), 3s (Lv 8–9), 1s (Lv 10)\n\n"
    "**Ailment**:\n"
    "- **Type**: Fear\n"
    "- **Base Ailment Chance**: (5 * Skill Level)% (halved on bosses)\n"
    "- **Ailment Duration**: 10 seconds\n"
    "- **Ailment Resistance**: None\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +(2.5 + base AGI / 100)\n"
    "- **Skill Constant**: +250\n"
    "- **Fear Chance**: +50%\n"
    "- **Charge Time**: -1 second\n\n"
    "**Game Description**:\n"
    "“Shoot out the energy inside of the character. Chance to inflict [Fear] on the target. Charge Time is shortened depending on the skill level.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169781515878490/chariot.png?ex=68057a30&is=680428b0&hm=d5855197410502fd7c027f0772b39d2384c2abbbe1777db3670d3f3636dad573&"
},

"Sonic Wave": {
  "title": "Sonic Wave",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 0.75 + 0.025 * Skill Level\n"
    "- **Base Skill Constant**: 5 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: 4m (Lv 1–3); 8m (Lv 4–6); 12m (Lv 7–9); 16m (Lv 10)\n\n"
    "**Ailment**:\n"
    "- **Type**: Tumble\n"
    "- **Base Ailment Chance**: (5 * Skill Level)%\n"
    "- **Ailment Duration**: 3 seconds\n"
    "- **Ailment Resistance**: 3s (Easy/Normal); 6s (Hard); 12s (Nightmare); 18s (Ultimate)\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +0.25\n"
    "- **Skill Constant**: +25\n"
    "- **Tumble Chance**: +50%\n"
    "- **Maximum Cast Range**: +4m\n\n"
    "**Game Description**:\n"
    "“Attack with an impulsive wave. Chance to inflict [Tumble] on the target.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169798288908308/sonicwave.png?ex=68057a34&is=680428b4&hm=6e77ad0567cb6934c4aa812ff2937598bdc609a68ed1ec3eb9e602ce7fa3bb85&"
},
"Earthbind": {
  "title": "Earthbind",
  "description": (
    "**Lv 2 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.025 * Skill Level\n"
    "- **Base Skill Constant**: 5 * Skill Level\n"
    "- **Hit Count**: 1 hit\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n"
    "- **Hit Range**: 1m (Lv 1–2); 1.5m (Lv 3–5); 2m (Lv 6–8); 2.5m (Lv 9–10)\n\n"
    "**Skill Effect**:\n"
    "- For each target hit, recover 5% of Max HP (max 500 HP)\n\n"
    "**Ailment**:\n"
    "- **Type**: Stop\n"
    "- **Base Ailment Chance**: (5 * Skill Level)%\n"
    "- **Ailment Duration**: 10 seconds\n"
    "- **Ailment Resistance**: 50 seconds\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +(0.25 + total AGI / 500)\n"
    "- **Skill Constant**: +25\n"
    "- **Hit Range**: +1.5m\n"
    "- **HP Recovery Limit**: +500 HP\n"
    "- **Stop Chance**: +50%\n\n"
    "**Game Description**:\n"
    "“Attack enemies around you by shaking the ground. Chance to inflict [Stop] on the targets. Restore small amount of HP by hitting a target.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169812574707712/earthbind.png?ex=68057a37&is=680428b7&hm=6106b4783f9e03d8ccfd7ead681356f45b7bc7b56eede16fcf06da58db2f6084&"
},

"Triple Kick": {
  "title": "Triple Kick",
  "description": (
    "**Lv 3 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 1 + 0.1 * Skill Level (per hit)\n"
    "- **Base Skill Constant**: 25 + 2 * Skill Level (per hit)\n"
    "- **Hit Count**: 3 hits (individual damage calculations)\n"
    "- **Maximum Cast Range**: 3m\n\n"
    "**Skill Effect**:\n"
    "- Second hit: Critical Rate +(2 * Skill Level)\n"
    "- Third hit: Critical Rate +(4 * Skill Level)\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +1\n"
    "- **Critical Rate**: +50 for all hits\n\n"
    "**Game Description**:\n"
    "“Attack the target three times quickly. Critical rates are higher than normal attacks.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169850361200670/triplekick.png?ex=68057a40&is=680428c0&hm=aa6d48399750cc0824caa39bdbba40ef75968fea38eb49215fcdda7d9b207a59&"
},

"Rush": {
  "title": "Rush",
  "description": (
    "**Lv 4 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n\n"
    "**Skill Stats**:\n"
    "- **Base Skill Multiplier**: 3 + 0.4 * Skill Level (total across 4 hits)\n"
    "- **Base Skill Constant**: 20 * Skill Level (total across 4 hits)\n"
    "- **Hit Count**: 4 hits (damage divided evenly)\n"
    "- **Maximum Cast Range**: Defaults to Knuckle's Auto Attack Max Range if equipped on main weapon or sub weapon slot; 1m otherwise\n\n"
    "**Buff Effect**:\n"
    "- **Motion Speed**: +2% (Lv 1–3); +3% (Lv 4–6); +4% (Lv 7–9); +5% (Lv 10)\n"
    "- **Buff Activation**: Immediately, before skill is cast\n"
    "- **Buff Duration**: 10 seconds\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- **Skill Multiplier**: +(2 + base AGI / 50)\n"
    "- **Skill Constant**: +200\n"
    "- **Motion Speed Buff**: Doubled\n\n"
    "**Game Description**:\n"
    "“Quick consecutive attacks. Action Speed increases for a few seconds including Rush activated.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169863812329522/rush.png?ex=68057a43&is=680428c3&hm=eb409a7361612b1035534647525a841f0e1d306125b4ca337f4cf9c8777e7765&"
},
"Martial Mastery": {
  "title": "Martial Mastery",
  "description": (
    "**Lv 1 Skill**\n"
    "Knuckle Main only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- **Weapon ATK**: +(3 * Skill Level)%\n"
    "- **ATK**: +1% (Lv 1–2); +2% (Lv 3–7); +3% (Lv 8–10)\n\n"
    "**Game Description**:\n"
    "“—”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169890618146816/martialmastery.png?ex=68057a4a&is=680428ca&hm=2f72eac69bdade077d9c14991a75033992e85fa995e7afb7ef6514954e2cca58&"
},

"Martial Discipline": {
  "title": "Martial Discipline",
  "description": (
    "**Lv 3 Skill**\n"
    "Knuckle Main or Sub / Knuckle Main only (depends on effect)\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Increases the damage of Martial Skills by (1 * Skill Level)% (requires Knuckles equipped on Main or Sub)\n"
    "- Attack Speed +(Skill Level)% and +(10 * Skill Level) (only when Knuckles are Main weapon)\n\n"
    "**Game Description**:\n"
    "“Deepen understanding of Knuckles. Increases attack speed of Knuckles. Increases damage of Knuckle skills a little.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169900994846760/martialdiscipline.png?ex=68057a4c&is=680428cc&hm=938bf9524a546a344686acaea684ce2d607762454c6c6779d4e0601ee376d35a&"
},

"Chakra": {
  "title": "Chakra",
  "description": (
    "**Lv 4 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: None\n"
    "**Base Charge Time**: 3 seconds (affected by Cast Speed)\n\n"
    "**Skill Effect**:\n"
    "- Restores 50 MP to user and party members on successful cast\n\n"
    "**Buff Effect** (applies to party):\n"
    "- **Attack MP Recovery**: +(Skill Level + MAX(0, Skill Level - 5))\n"
    "- **Flat Skill Based Damage Reduction**: +0 (self), +(2 * base VIT) (others)\n"
    "- **Percentage Skill Based Damage Reduction**: +10% + (2 * Skill Level)%\n"
    "- **Buff Duration**: 10 + Skill Level seconds OR until caster is hit\n\n"
    "**Knuckle Main/Sub Bonus**:\n"
    "- MP Heal +50\n"
    "- Percentage Skill Based Damage Reduction +20%\n"
    "- Buff Duration +10 seconds\n\n"
    "**Game Description**:\n"
    "“Restore MP a little and add a buff to reduce the next damage for a few seconds. Increase Attack MP Recovery a little during the effect. Effective on party members.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169909224054784/chakra.png?ex=68057a4e&is=680428ce&hm=3ba349282290dffeccd12b6fe52ad974f104d5a1a4f533e9ffbd49e8e1224c2d&"
},

"Aggravate": {
  "title": "Aggravate",
  "description": (
    "**Lv 1 Skill**\n"
    "Knuckle Main only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- **Attack MP Recovery**: +(0.5 * Skill Level)\n"
    "- On successful auto attacks (not missed), chance to deal additional hit: (10 + 4 * Skill Level)%\n\n"
    "**Aggravate Hit Info**:\n"
    "- **Damage Type**: Neutral\n"
    "- **Element**: Neutral\n"
    "- **Skill Multiplier**: 0.05 * Skill Level (per hit)\n"
    "- **Hit Count**: Same as triggering auto attack (damage is divided evenly)\n"
    "- **Damage Formula**:\n"
    "  (Physical Base Damage - target's DEF) × Skill Multiplier × Stability × Neutral Proration × (1 - Gem Reduction%)\n"
    "- **Note**: Damage is calculated independently of the triggering auto attack; not affected by Guard\n\n"
    "**Ailment**:\n"
    "- **Type**: Armor Break\n"
    "- **Chance**: 0%\n\n"
    "**Other Notes**:\n"
    "- Not affected by Martial Discipline\n\n"
    "**Game Description**:\n"
    "“Keenly attack the target again. You have a chance to deal additional damage by normal attacks of Knuckles.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169928308150272/aggravate.png?ex=68057a53&is=680428d3&hm=2ba3f3a3b494bb37d4344a7d7f52f5c6b351f091c0a675f3118ddde18b5639b5&"
},
"Strong Chase Attack": {
  "title": "Strong Chase Attack",
  "description": (
    "**Lv 2 Skill**\n"
    "Knuckle Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Accuracy% + (Skill Level)% (default)\n\n"
    "**Main Knuckle Only Bonus**:\n"
    "- Aggravate Skill Multiplier + (0.05 * Skill Level)\n"
    "- Accuracy% boost is doubled → becomes (Skill Level * 2)%\n"
    "- Physical Pierce for Aggravate: *Still under investigation*\n\n"
    "**Game Description**:\n"
    "“Enhances the power of small attacks. Increases your accuracy and enhances the additional damage of [Aggravate].”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869169939372711966/strongchaseattack.png?ex=68057a55&is=680428d5&hm=102d853e530c5cd86724602eb6bf7f4bbee3c9ea4e8e706f62f1f6f0f2e74e90&"
},

"Abstract Arms": {
  "title": "Abstract Arms",
  "description": (
    "**Lv 5 Skill**\n"
    "Knuckle Only\n"
    "**Type**: Passive\n\n"
    "**Passive Effect**:\n"
    "- Allows **manual evasion dash during skill animations**.\n"
    "- Evasion cancels current skill animation, letting a **shadow/clone** perform the animation instead.\n"
    "- Skill cooldown:\n"
    "  • Main Knuckle: (10 - Skill Level) sec\n"
    "  • Sub Knuckle: (20 - Skill Level) sec\n"
    "- Cannot use again until the shadow finishes its animation.\n"
    "- Using this while in **Combo** cancels that Combo instantly.\n\n"
    "**Can be used with**:\n"
    "- All Martial skills **except** Slide, Energy Control, Asura Aura\n"
    "- Crusher skills: Breathworks, Combination, God Hand\n"
    "- Buff skills: MP Charge, War Cry, War Cry of Struggle, Quick Aura, Kairiki Ranshin, Guardian\n\n"
    "**Notes**:\n"
    "- Srd/Lrd% from Abstract Chariot is applied **when the clone deals damage**, not on cast.\n"
    "- Clone of Abstract God Hand does **not grant buff** when taking hits.\n\n"
    "**Game Description**:\n"
    "“Enables Evasion (Manual Only) while using certain Martial skills. After activating it, you need to wait before you can activate it again. Not available for some skills that perform special actions.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967826840192450650/psychothousandhands.png?ex=680522fc&is=6803d17c&hm=cae037e2d75a90b7cd9ff6e70d44f435e88df53a030b208134d338c4fc7fe29d&"
},

"Asura Aura": {
  "title": "Asura Aura",
  "description": (
    "**Lv 5 Skill**\n"
    "Knuckle Only\n"
    "**MP Cost**: 0\n"
    "**Type**: Toggle Buff\n\n"

    "**Punch Damage**:\n"
    "- Multiplier: 0.95 + (Base AGI / (2400 - Skill Level * 200))\n"
    "- Sub-Knuckle Penalty: 0.5 + (Base AGI / (2400 - Skill Level * 200))\n"
    "- Constant: 0\n"
    "- Hit Range: 2.5m\n"
    "- Interval: 1 hit per 0.25 sec (Unaffected by Motion Speed, Swift, Freeze)\n\n"

    "**Buff Effect (Asura Mode)**:\n"
    "- All skills except Martial/Crusher cost +100 MP (after combo tag reductions)\n"
    "- Gain 1 Asura Stack per 100 MP used\n"
    "- At 20+ Stacks: You lose 5% Max HP **per stack gained**\n"
    "- At 40 Stacks: Instant Death\n"
    "- Taking damage → Lose 100 MP to reduce damage by (MP * 5%) [max 95%] and gain 1 stack\n"
    "- No Attack MP Recovery (Decoy, auto attacks, etc.)\n"
    "- Actions like Burning Spirit or Manual Guard **still recover MP** based on AMPR\n"
    "- Skill Constant +20 * Skill Level (except for Asura punches); halved for sub-knuckle\n"
    "- [Main Knuckle] Damage Dealt +30% (multiplicative)\n"
    "- Flat Critical +7.5 * Skill Level; sub-knuckle = ÷3\n"
    "- Ailment Resistance: +1% per 10 MP (max 100%) [additive with MTL/equipment]\n\n"

    "**Auto Attack Effects in Asura Mode**:\n"
    "- Triggers **infinite punches** with Perfect Aim [Main Knuckle only]\n"
    "- Stops when target is too far, or you skill/manual guard/evasion\n"
    "- Does **not inflict prorate**, uses Physical Proration\n\n"

    "**Auto Attack with Asura Stacks (NOT in Asura Mode)**:\n"
    "- Triggers 1 punch per stack with Perfect Aim [Main Knuckle only]\n"
    "- Each punch can recover: (Total AMPR / 10) * Skill Level MP (halved on sub)\n"
    "- Missed hits do **not** recover MP (stack is still consumed)\n"
    "- Same cancel conditions as above\n"
    "- These also don’t inflict prorate, Physical Proration only\n\n"

    "**Partial Buffs when NOT in Asura Mode (but with ≥1 stack)**:\n"
    "- Flat Critical +7.5 * Skill Level; ÷3 if sub-knuck\n"
    "- Skill Constant +20 * Skill Level; halved if sub-knuck\n"
    "- [Main Knuckle] Damage Dealt +10% (additive)\n\n"

    "**Other Notes**:\n"
    "- Turning Asura ON resets stacks to 0 and gives 2 sec Iframe\n"
    "- Turning Asura OFF removes Iframe immediately if it's active\n"
    "- Stack MP recovery upon changing maps: stack * 50 MP (fixed)\n"
    "- Using this again toggles Asura Mode ON/OFF\n"
    "- Asura punches are **unaffected** by SRD/LRD, and still benefit from Brave Aura etc.\n"
    "- Game Description: “Unleashes the demon power that is hidden inside. While active, ATK increases and if you receive damage, MP will be used to mitigate the damage, but in exchange, you will lose Attack MP Recovery and MP cost will increase.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967826840393756672/asuraaura.png?ex=680522fc&is=6803d17c&hm=cdd07237a7e88dbe367e2774f7804b4377a0af9d385e39c9153a3faa20c904e3&"
},
"Flash Blink": {
  "title": "Flash Blink",
  "description": (
    "**Lv 5 Skill**\n"
    "Knuckle Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Max 6m\n\n"

    "**Damage**:\n"
    "- Base Skill Multiplier: 3 + 0.3 * Skill Level\n"
    "- [Main Knuckle Only] Additional Multiplier: + (Base AGI / 300)\n"
    "- Skill Constant: 100\n"
    "- Hit Count: 1 + Additional Hits based on Evasion Used\n\n"

    "**Additional Hits Mechanic**:\n"
    "- Total Add Hits = Max Evasion Stack - Current Evasion Stack\n"
    "- Add Hit Damage Scaling:\n"
    "  • 1st: 50% of Main Hit\n"
    "  • 2nd: 25%\n"
    "  • 3rd: 12.5%\n"
    "  • 4th: 6.25%\n"
    "  • ...continues halving\n"
    "- Damage is based on **Normal Auto Attack Proration**, and also inflicts it\n"
    "- **SRD% does not affect this skill**\n\n"

    "**Buff Effect**:\n"
    "- After using Flash Blink, your **next skill** gains +[Skill Level]% SRD%\n"
    "- Buff Duration: Until you use another skill\n\n"

    "Game Description: “Sends out a residual image to attack. The hit count increases according to the number of Evasions used. The power of the next close range attack increases.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967826840913858610/flasharts.png?ex=680522fc&is=6803d17c&hm=2ea1cf80a4a3affa8f00e16b80d91db8b42eba8d7b8c14723baec2ada31ff9bb&"
},
"Energy Control": {
  "title": "Energy Control",
  "description": (
    "**Lv 5 Skill**\n"
    "Knuckle Only\n"
    "**MP Cost**: 100\n\n"

    "**Skill Effect**:\n"
    "- Reduces **all incoming damage to 0** during animation\n"
    "- Successful parry grants **Chakra Buff (no MP recovery)**\n"
    "- Chakra Level granted = your current Chakra Level, capped at Energy Control Level\n"
    "- Grants Base Weapon ATK% and Stability buffs if parry successful\n"
    "- Cannot gain or keep Eburst stacks/buffs while this buff is active\n\n"

    "**Chakra Buff Effects**:\n"
    "- AMPR + (Chakra Level + MAX(0, Chakra Level - 5))\n"
    "- %Skill-Based Damage Reduction: 10% + 2% per Chakra Level\n"
    "- Buff Duration: 10 + Chakra Level seconds OR until hit\n"
    "- [Main Knuckle Only]: Extra +10s duration for Chakra buff\n"
    "- [Main Knuckle Only]: +20% to Skill-Based Damage Reduction\n\n"

    "**Base Weapon ATK% and Stability Buffs**:\n"
    "- +5% * Skill Level Weapon ATK (Main Knuckle only)\n"
    "- Caps at 50% total (combined with Annihilator)\n"
    "- Stability: +10% (all weapons)\n"
    "- Duration =\n"
    "  • Lv1: 30s\n"
    "  • Lv2: 32s\n"
    "  • Lv3: 35s\n"
    "  • Lv4: 40s\n"
    "  • Lv5: 45s\n"
    "  • Lv6: 50s\n"
    "  • Lv7: 60s\n"
    "  • Lv8: 70s\n"
    "  • Lv9: 80s\n"
    "  • Lv10: 90s\n\n"

    "Game Description: “Control the flow of energy and turns it aside. Nullifies the damage received while performing it and receives the buffs of Chakra except the MP Recovery effect. The level of Chakra that activates will not surpass the level of Energy Control acquired.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967826840620253224/dispersingforce.png?ex=680522fc&is=6803d17c&hm=577f3de5ceba50347b0cc60edf3c988136354997d3cf7ba67fc07d24f731cfaf&"
},
"Mountain Press": {
  "title": "Mountain Press",
  "description": (
    "**T5 Skill**\n"
    "Knuckles / Main Bare Hand Only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: 4m\n\n"

    "**Base Skill Multiplier**:\n"
    "- Knuckles: 7.5 + 0.25 * Skill Level\n"
    "- Barehand/Sub-weapon: 7.5 + 0.25 * Skill Level + (higher of DEX or AGI) / 100\n"
    "**Base Skill Constant**: 500\n\n"

    "**Ailment: Stun**\n"
    "- Chance: 100% (Knuckles), 10% * Skill Level (Barehand)\n"
    "- Duration: 5s\n"
    "- Resistance Cooldown: 30s (Easy~Nightmare), 35s (Ultimate)\n\n"

    "**Buff Effect**:\n"
    "- Aggravate extra hits become **Critical** if auto attack is Critical\n"
    "- Knuckle Main: Aggravate additional hit activation = **100%**\n"
    "- Aggravate gets +10% multiplier per successful activation during buff (max ×50; 5x multiplier)\n"
    "- Buff Duration: Equal to Stun Resistance Cooldown\n\n"

    "Notes:\n"
    "- Affected by Short Range Damage\n"
    "- Physical Proration\n\n"
    
    "Game Description: A powerful shoulder strike. Chance to inflict [Stun] on the target. "
    "*If the stun debuff is prevented due to active resistance, the buff effect from the skill \"Aggravate\" will be applied.*"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1343488332599922699/1348187339406573588/sprite_1.png?ex=6805430d&is=6803f18d&hm=76a9400619e764152a9e797f86c14e071587be5b465fec9514fac52023fb6ca9&"
},
"Seismic Stomp": {
  "title": "Seismic Stomp",
  "description": (
    "**T5 Skill**\n"
    "Knuckles / Main Bare Hand Only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: 2m\n\n"

    "**Base Skill Multiplier**:\n"
    "- Knuckles: 7.5 + 0.25 * Skill Level\n"
    "- Barehand/Sub-weapon: 7.5 + 0.25 * Skill Level + (higher of DEX or STR) / 100\n"
    "**Base Skill Constant**: 300\n\n"

    "**Ailment: Flinch**\n"
    "- Chance: 10% * Skill Level\n"
    "- Duration: 2s\n"
    "- Resistance Cooldown: 6s (Easy~Hard), 7s (NM), 10s (Ultimate)\n\n"

    "**MP Recovery Effect**:\n"
    "- 600 + (Total AMPR * 2)\n"
    "- Affected by Chakra, Aggravate, Quick Motion, Raving Storm, Ether Flame, Hidden Talent, Equipments, Crystas, Consumables, Infinity Gem, Stoodie Buff\n\n"

    "Notes:\n"
    "- Affected by Short Range Damage\n"
    "- Physical Proration\n\n"

    "Game Description: Throws your opponent off balance with a heavy stomp. Chance to inflict [Flinch] on the target. "
    "If successful, a large amount of MP will be restored."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1343488332599922699/1348187331928260662/sprite_2.png?ex=6805430c&is=6803f18c&hm=891ea5997ffd0c5d3b824b5ac0beca2ede26a0e73ac984d948f3d35e4bc11509&"
},
"Spin Sweep": {
  "title": "Spin Sweep",
  "description": (
    "**T5 Skill**\n"
    "Knuckles / Main Bare Hand Only\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: 2m\n\n"

    "**Base Skill Multiplier (Main Hit)**:\n"
    "- Knuckles: 2.5 + 0.25 * Skill Level\n"
    "- Barehand/Sub: 2.5 + 0.25 * Skill Level + (higher of AGI or STR)/100\n"
    "**Base Skill Constant**: 400\n\n"

    "**Additional Hit (Wheel Kick)**:\n"
    "- Knuckles: 5 + 0.5 * Skill Level + (Base AGI / 100)\n"
    "- Barehand: 5 + 0.5 * Skill Level\n"
    "- Constant: 400 + 40 * Skill Level\n\n"

    "**Ailment: Tumble**\n"
    "- Chance: 100%\n"
    "- Duration: 3s\n"
    "- Resistance Cooldown: 8s (Easy~Hard), 14s (NM), 20s (Ultimate)\n\n"

    "**Buff Effect**:\n"
    "- Immunity to: Suction, Slow, Stop\n"
    "- Evasion Recovery:\n"
    "  • Barehand/Sub-MD: +1\n"
    "  • Sub-Knuckles: +1.7\n"
    "  • Sub-Dagger: +2\n"
    "  • Main Knuckles: +3\n"
    "- Buff Duration: 2 + floor(Skill Level / 2)\n\n"

    "Notes:\n"
    "- Affected by Short Range Damage\n"
    "- Physical Proration\n\n"

    "Game Description: Trips your opponent with a leg sweep. Chance to inflict [Tumble] on the target. "
    "If successful, you will perform additional attacks and gain a buff for a few seconds. "
    "All Weapons Bonus: Evasion will be slightly restored when the buff is gained. The buff lasts for a few seconds and during this time, movement disruption due to [Slow], [Stop] and pull attacks will be prevented."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/1343488332599922699/1348187346876760084/sprite.png?ex=6805430f&is=6803f18f&hm=932bd3be328b35c5395b1fb5259a61a9afeca8802de6a995e2bc1e193e01d9f8&"
}

}





################################ KATANA #########################################



skillskatana = {
    
"Issen": {
  "title": "Issen",
  "description": (
    "**Lv 1 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n\n"

    "**Hit Count**: 2 hits\n"
    "- First Hit: Multiplier = 0.5 | Constant = 0\n"
    "- Second Hit: Multiplier = 1 + 0.05 * Skill Level | Constant = 50 + 5 * Skill Level\n\n"

    "**Skill Effects**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- Second Hit: **Critical Rate ×3** (200% boost)\n"
    "  → Effective Crit = Total Critical Rate * 3\n\n"

    "Game Description: Slash an enemy at a blinding speed. High Critical Rate at the second hit."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869209932795351050/issen.png?ex=68059f95&is=68044e15&hm=56c927dab3c399154c19cec7781d9e2533ada8351980051eabad83c0b0011a54&"
},
"Pulse Blade": {
  "title": "Pulse Blade",
  "description": (
    "**Lv 1 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: 12m\n\n"

    "**Hit Count**: 3 hits\n"
    "- First Hit Multiplier: 0.5\n"
    "- Second Hit: 0.5 + 0.05 * Skill Level\n"
    "- Third Hit: 0.5 + 0.1 * Skill Level\n"
    "- Constant for All Hits: 30 + Skill Level\n"
    "- Critical: Calculated once, applied to all 3 hits\n\n"

    "**Skill Effects**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- **Distance-based DEF penalty** applied to target:\n"
    "  → Penalty = (Distance - Katana Auto Range) * (11 - Skill Level)/100\n"
    "  → New Target DEF = Original DEF * (1 + Penalty), Penalty min = 0\n"
    "- If used **outside combo** or as the **last combo skill**, and user is not Slowed or Stopped:\n"
    "  → Allows **dash movement** using trackball during sheathing animation\n\n"

    "Game Description: Slash an enemy with an aerial slash at a distance. "
    "The damage decreases as you get further away from the target. "
    "You can move when sheathing the katana."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869209948033265664/pulseblade.png?ex=68059f98&is=68044e18&hm=871c31b0575cadd4fb747a7648e31be057ff10f2870341bd1810cf757f9d2527&"
},
"Triple Thrust": {
  "title": "Triple Thrust",
  "description": (
    "**Lv 2 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: 12m\n\n"

    "**Hit Count**: 3 hits (damage calculated once, split evenly)\n"
    "**Base Skill Multiplier**: 1.5 + 0.2 * Skill Level + (AGI / 500)\n"
    "**Base Skill Constant**: 0\n\n"

    "**Skill Effects**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- Movement: Moves you **behind** the target upon hit\n\n"

    "**Buff Effect**:\n"
    "- Boosts **Skill Constant** of next attack skill\n"
    "  → Constant Increase = Player Level / (11 - Skill Level)\n"
    "- Buff lasts **until a skill is used**\n\n"

    "Game Description: Quickly approach and thrust a target. Move behind a target when attacking. "
    "Increase the damage of the next skill a little."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869209966223970304/triplethrust.png?ex=68059f9d&is=68044e1d&hm=13a477fe73667b0069bc80b0adf44bfddcb27d94d0e13ea4a6cd3eef20ad35d9&"
},
"Hasso Happa": {
  "title": "Hasso Happa",
  "description": (
    "**Lv 3 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n"
    "**Hit Range**: \n"
    "- 2m (Lv 1–2), 3m (Lv 3–6), 4m (Lv 7–10) around caster\n\n"

    "**Hit Count**:\n"
    "- First Hit: Always 1 hit\n"
    "- Extra Hits: 0 (Lv 1–3), 1 (Lv 4–6), 2 (Lv 7–10)\n"
    "- Each hit has its own damage calculation\n\n"

    "**Multipliers**:\n"
    "- First Hit: 2.2 (Lv 1) → 6.0 (Lv 10)\n"
    "- Other Hits: Same as above except Lv 10 = 3.0 (not 6.0)\n"
    "- Constant: 130 + 2 × Skill Level\n\n"

    "**Skill Effects**:\n"
    "- Treated as **Unsheathe Attack**\n"
    "- Has **Perfect Aim**\n"
    "- Usable dash via trackball during sheathing animation if not Slowed/Stunned\n"
    "- [Main Katana Only] Enhanced version called **Sakura Ranman** triggers if used after **Kasumisetsu Getsuka** (requires 1 Sakura stack):\n"
    "  → Adds +1 + 0.5 + 0.5 multiplier to each hit compared to normal Hasso\n"
    "  → Recovers **+300 MP** per Sakura Ranman hit (max 600 MP per cast)\n\n"

    "**Combo Interaction**:\n"
    "- **Triple Thrust** Skill Constant buff is divided across hit count\n\n"
    "**Other Notes**:\n"
    "- Unaffected by Whack\n"
    "- Affected by **Short Range Damage** regardless of distance\n\n"

    "Game Description: Slash all enemies in a certain space. Deal damage to enemies around you without fail. You can move when sheathing the katana."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869209983663898674/hassohappa.png?ex=68059fa1&is=68044e21&hm=957602be86e2c71b51efd3b92d1d2d5821e19412acfb2887333a7c0362bf670f&"
},
"Tenryu Ransei": {
  "title": "Tenryu Ransei",
  "description": (
    "**Lv 4 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 300 (reduced to 100 after gaining stack)\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n\n"

    "**Hit Count**: 4 hits (damage spread evenly)\n"
    "**Multiplier**: 1.5 + 0.25 × Skill Level\n"
    "**Constant**: 10 × Skill Level\n"
    "**Stack Effect**:\n"
    "- Base multiplier × (1 + stack count), max 3 stacks\n"
    "- Accuracy +10 × (1 + stack count), max 3 stacks\n"
    "- Motion Speed: 125% - 15% × stack count (max 3 stacks)\n\n"

    "**Skill Effects**:\n"
    "- Treated as **Unsheathe Attack**\n"
    "- Doesn’t apply proration if it's the last skill used\n"
    "- Auto-attacks break this chain\n\n"

    "**Buff Mechanics**:\n"
    "- Gain 1 stack per use (max 4)\n"
    "- Buff lasts 10s from Tenryu, 30s from **Madagachi**/**Zantei Settetsu**, or extended via **Kasumisetsu Getsuka**\n"
    "- Using Madagachi/Zantei/Kasumisetsu while buff is active refreshes duration but **resets stacks**\n"
    "- Special mode: **Tenryu Ransei: Zannou/Zanyu** triggers under certain conditions\n"
    "- Auto attack delay = 0 (unless under Paralysis, Fear, etc.)\n\n"

    "**Limitations**:\n"
    "- Zantei version can't inflict Armor Break\n\n"

    "Game Description: Furiously slash consecutively. Power increases for a while every time you use the skill (4 times at most). "
    "Special attack is applied to Madagachi/Zantei Settetsu by meeting certain conditions and the buff duration increases."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210013200179240/tenryuransei.png?ex=68059fa8&is=68044e28&hm=09828d01dd06ef49f3dcb02e67c794942704a1fe507eb3aec6fec256744566a5&"
},
"Garyou Tensei": {
  "title": "Garyou Tensei",
  "description": (
    "**Lv 4 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n"
    "**Hit Count**: 1 hit\n"
    "**Not an Unsheathe Attack**\n\n"

    "**Damage Formula**:\n"
    "- Multiplier = MAX[0.2 × Skill Level; (0.2 × Skill Level + Stack Count ÷ 10) × Stack Count]\n"
    "- Constant: 100\n\n"

    "**Critical Penalty**:\n"
    "- Critical Rate = -(110 - 10 × Skill Level)\n"
    "- If **Kairiki Ranshin Buff** is active:\n"
    "  → Garyou removes the buff\n"
    "  → Gains +100 Flat Crit Rate and +100% Physical Pierce for this skill only\n\n"

    "**Bonus vs Armor Break**:\n"
    "- If the target has **Armor Break**, Garyou's constant ×10\n\n"

    "**Buff Aftercast**:\n"
    "- Gain Damage Reduction Buff: 5% × number of Garyou stacks\n"
    "- Buff duration = number of Garyou stacks (in seconds)\n\n"

    "**Divine Slash Condition**:\n"
    "- If using **Garyou Tensei Lv 10** with 10/10 stacks **during Shadowless Slash animation**, this skill becomes **Divine Slash**\n\n"

    "**Stack System**:\n"
    "- Gain 1 stack (max 10) for each:\n"
    "  → Mononofu skill used\n"
    "  → Dash-enhanced normal attack (main katana only)\n"
    "- Stacks expire upon using Garyou\n\n"

    "**Passive Effect**:\n"
    "- +2% damage to all Mononofu skills per stack (up to 10 = 20%)\n"
    "- After Garyou/Divine Slash, you always get +20% Mononofu damage **regardless of stack count** for the duration of the damage reduction buff\n\n"

    "Game Description: The ultimate slash. The power increases every time you use certain Mononofu Skills (10 times at Most). "
    "Power increases against targets inflicted with [Armor Break]. Critical Rate is extremely low."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210019932012614/garyoutensei.png?ex=68059fa9&is=68044e29&hm=429b1edb285741a21d345f1a12cd552fa79b8f3b9ca665648835ca95132c5bd0&"
},
"Pommel Strike": {
  "title": "Pommel Strike",
  "description": (
    "**Lv 1 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 200\n"
    "**Damage Type**: Physical\n"
    "**Element**: Neutral\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n"
    "**Hit Count**: 1 hit\n\n"

    "**Damage**:\n"
    "- Multiplier: 1 + 0.05 × Skill Level\n"
    "- Constant: 100 + 10 × Skill Level\n\n"

    "**Ailments**:\n"
    "- **Primary**: Paralysis\n"
    "  → Chance: 50% + (5 × Skill Level)%\n"
    "  → Duration: 10 seconds\n"
    "- **Secondary**: Stun (only if target is already Paralyzed)\n"
    "  → Chance: 5 × Skill Level%\n"
    "  → Duration: 5 seconds\n"
    "  → Resistance Duration: 25s (Easy–Nightmare); 30s (Ultimate)\n\n"

    "**Skill Effect**:\n"
    "- If the target already has **Paralysis**, this skill will inflict **Stun** instead\n"
    "- If using **Mind's Eye**, this skill will be stopped if the target has Paralysis\n\n"

    "Game Description: Strike an enemy with the pommel. Chance to inflict [Paralysis]. Chance to inflict [Stun] if the target is paralyzed."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210043122344006/pomelstrike.png?ex=68059faf&is=68044e2f&hm=ed7368978b902d71170c4d13ec8c0301cb4e407de16d881cef0f903e96a7a676&"
},
"Magadachi": {
  "title": "Magadachi",
  "description": (
    "**Lv 2 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n"
    "**Hit Count**: 1 hit\n\n"

    "**Damage**:\n"
    "- Base Multiplier: 2 + 0.3 × Skill Level\n"
    "- Constant: 100 + 10 × Skill Level\n"
    "- *Tenryu Ransei: Zannou* Multiplier: 13 + Floor((Tenryu Base Multiplier × 100 × Stack Count) ÷ 2) ÷ 100\n"
    "- *Tenryu Ransei: Zannou* Constant: 300\n\n"

    "**Skill Effect**:\n"
    "- If you don’t take damage before the katana lifting animation ends → normal damage dealt\n"
    "- If you take damage before it ends → animation changes and no damage is dealt\n"
    "- If used while Tenryu Ransei's buff is active and parry succeeds, you trigger **Tenryu Ransei: Zannou**\n"
    "  → Considered an Unsheathe Attack\n"
    "  → Grants **Perfect Aim** and **2s Invincibility** (or 0.5s after animation ends)\n\n"

    "**Buff Effects**:\n"
    "- Reduces **Physical & Fractional** damage taken by 90%\n"
    "- Reduces **Magic** damage taken by 45%\n"
    "- If damage would normally be fatal and you’re above 20% HP, you survive at **1 HP**\n"
    "- **Negates ailment** from the reduced hit\n"
    "- If damage is taken, **MP Recovery**: 100 + (10 × Skill Level); *-100 if used in combo*\n"
    "- Buff lasts until damage is taken or until animation ends\n\n"

    "**Notes**:\n"
    "- This skill **does not prorate** on parry\n"
    "- Triple Thrust’s constant boost applies to the normal attack, **not** to Tenryu Zannou\n\n"

    "Game Description: Parry an enemy's attack and reduce damage only once. Nullify ailments, recover MP a little, and remain at least 1 HP when taking fatal damage at certain amount of HP. Just deal damage if you don't parry."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210049363460096/magadachi.png?ex=68059fb0&is=68044e30&hm=f20a8924e39e03d7c4aef79794fdbdad2db1a5e86905f75ccf0bcd0c22f2acf7&"
},
"Zantei Settetsu": {
  "title": "Zantei Settetsu",
  "description": (
    "**Lv 3 Skill**\n"
    "Katana Main / Sub Only\n"
    "**MP Cost**: 400\n"
    "**Damage Type**: Physical\n"
    "**Cast Range**: Follows Katana Auto Attack Range\n"
    "**Hit Count**: 4 hits + 1 counter hit\n\n"

    "**Damage**:\n"
    "- Base Multiplier: 1 + 0.2 × Skill Level (total across all 4 hits)\n"
    "- Base Constant: 10 × Skill Level (total)\n"
    "- *Counter Multiplier*: 5 + 1 × Skill Level\n"
    "- *Counter Constant*: 30 × Skill Level\n"
    "- *Tenryu Ransei: Zannou* Multiplier: 13 + Floor((Tenryu Base Multiplier × 100 × Stack Count) ÷ 2) ÷ 100\n"
    "- *Tenryu Ransei: Zannou* Constant: 300\n\n"

    "**Skill Effect**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- If you take damage before the slashing animation ends → an **extra counter hit** triggers\n"
    "- If Tenryu Ransei buff is active during this, the counter becomes **Tenryu Ransei: Zannou**\n"
    "  → Unsheathe Attack, Perfect Aim, 2s Invincibility (or 0.5s after animation ends)\n"
    "  → Cannot inflict Armor Break\n\n"

    "**Buff Effects**:\n"
    "- Nullifies **1 instance of damage** (sets it to 0, but still considered “taken”)\n"
    "- Grants immunity to **Flinch, Tumble, Stun, Knockback** from that hit\n"
    "- Buff ends after 1 hit taken or animation ends\n\n"

    "**Counter Ailment**:\n"
    "- **Armor Break**\n"
    "  → Chance: 50% + (5 × Skill Level)%\n"
    "  → Duration: 5s\n"
    "  → No ailment resistance duration\n\n"

    "**Notes**:\n"
    "- Triple Thrust constant boost applies to first 4 hits\n"
    "- Does **not apply** to counter or Tenryu Ransei: Zannou\n\n"

    "Game Description: Furiously slash an enemy taking its attack. Nullify damage once and do additional attack. Chance to inflict [Armor Break] with it."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210055554256926/zanteisettetsu.png?ex=68059fb2&is=68044e32&hm=aad82b34753cd513326be635a8a2434ec0ff9f4b3b3e63f88c02c3be561bfa55&"
},
"Bushido": {
  "title": "Bushido",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit / Katana Main Only (depends on effect)\n"
    "**Type**: Passive Skill\n\n"

    "**Passive Effect**:\n"
    "- Max HP + (10 × Skill Level)\n"
    "- Max MP + (10 × Skill Level)\n"
    "- Accuracy + (Skill Level)\n"
    "- Weapon ATK + (3 × Skill Level)%\n"
    "- Additional ATK Bonus:\n"
    "  → +1% if Skill Level 1–2\n"
    "  → +2% if Skill Level 3–7\n"
    "  → +3% if Skill Level 8–10\n"
    "*Note: All ATK effects apply only when using **Katana** as Main Weapon*"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210066245537842/bushido.png?ex=68059fb4&is=68044e34&hm=bb2d99f3a71d0191f13aa660ab51b456b93f467c03b8ee9fae8a4e4ae6c440e0&"
},
"Two-Handed": {
  "title": "Two-Handed",
  "description": (
    "**Lv 1 Skill**\n"
    "No Limit / Katana Main Only (depends on effect)\n"
    "**Type**: Passive Skill\n\n"

    "**Passive Effect**:\n"
    "- Weapon ATK + (Skill Level)%\n"
    "- Accuracy + (Skill Level)%\n"
    "- Critical Rate + (Skill Level)\n"
    "- Stability + (Skill Level)%\n"
    "*These effects only apply if your **Sub Weapon slot is empty***\n\n"

    "**Conditional ATK Bonus**:\n"
    "- When using **Katana** as Main Weapon + no Sub Weapon (excluding **Ninjutsu Scroll + Ninja Spirit**):\n"
    "  → When you land a **Critical Auto Attack or Skill**, you gain:\n"
    "  → **Crit ATK Multiplier**: Total ATK × (1 + 0.05 × Skill Level)\n\n"

    "**Penalties (Non-Katana Main)**:\n"
    "- Critical Rate bonus: **halved**\n"
    "- Stability bonus: **halved**\n\n"

    "*Game Description is misleading — this does **not** increase critical damage directly*"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210098952708156/twohanded.png?ex=68059fbc&is=68044e3c&hm=38458ed9adc06d0532d5af973e79619450ea5d02925f773bf8bd8d2581b95602&"
},
"Meikyo Shishui": {
  "title": "Meikyo Shishui",
  "description": (
    "**Lv 2 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 200\n"
    "**Type**: Buff Skill (no direct damage)\n\n"

    "**Buff Effects**:\n"
    "- Critical Rate: +20 + (2 × Skill Level)\n"
    "- DEF: -100 × (11 - Skill Level)\n"
    "- MDEF: -100 × (11 × Skill Level)\n"
    "- Critical Damage: - (15 - Skill Level)%\n"
    "- Duration: 10s + (2 × Skill Level) OR until you use another skill\n"
    "- Buff applies only to the **next skill** after activation\n\n"

    "**Katana Main/Sub Bonuses**:\n"
    "- Critical Rate: +25 instead\n"
    "- No Critical Damage penalty\n"
    "- Buff duration is **doubled**\n\n"

    "**Special Interaction**:\n"
    "- If **Decoy** is cast immediately after Meikyo, the **crit rate bonus** persists throughout Decoy’s duration\n\n"

    "Game Description: Sharpen your focus. Critical Rate greatly increases for a short time and Critical Damage, DEF, and MDEF decrease. The effect ends when you use another skill."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210118057787392/meikyoshisui.png?ex=68059fc1&is=68044e41&hm=fd22500aea30af717c7087a156829af6f9f5b657be873a105847e3301b75d175&"
},
"Shukuchi": {
  "title": "Shukuchi",
  "description": (
    "**Lv 3 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 0\n"
    "**Type**: Passive/Dash Utility\n\n"

    "**Effect**:\n"
    "- When you use an auto attack or Mononofu attacking skill **out of range**, you will dash to the target (unless under [Slow] or [Stop])\n"
    "- The action is queued and performed after the dash animation ends\n"
    "- If it's an auto attack, it becomes an **Unsheathe Attack**\n\n"

    "**Buff Effect (upon dash)**:\n"
    "- Next auto attack's Skill Multiplier: +(0.05 × Skill Level)\n"
    "- Attack MP Recovery:\n"
    "  → Level 1: +0\n"
    "  → Level 2: +1\n"
    "  → Level 3: +2\n"
    "  → ... up to +25 at Level 10\n"
    "- Buff Duration: Until a skill or auto attack is executed\n\n"

    "**Katana Main Bonus**:\n"
    "- Attack MP Recovery is **doubled**\n\n"

    "**Notes**:\n"
    "- Works with **Rampage**: First 10 auto attacks get additive Skill Multiplier boost\n"
    "- Applies only to **main hand** in Dual Swords\n"
    "- Cancelling the dash removes the buff and Unsheathe effect\n"
    "- If the queued attack doesn’t connect, buff is lost"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210124219211786/shukuchi.png?ex=68059fc2&is=68044e42&hm=cfca15d166be1678ccf41cb240db0a8ed6c06ccb31d22dfe6c9654000fe3ba3d&"
},
"Kairiki Ranshin": {
  "title": "Kairiki Ranshin",
  "description": (
    "**Lv 4 Skill**\n"
    "No Limit\n"
    "**MP Cost**: 200\n"
    "**Type**: Buff\n\n"

    "**Effect**:\n"
    "- Inflicts [Ignite] on self\n"
    "- Duration depends on level:\n"
    "  → Level 1: 5s, Level 2–3: 6s, ..., Level 10: 10s\n"
    "- No resistance time\n\n"

    "**Buff Effects**:\n"
    "- ATK: +(10 × Skill Level)\n"
    "- Attack MP Recovery: up to +25 at Level 10\n"
    "- Auto Attack Skill Multiplier: +(0.05 × Skill Level)\n"
    "- Garyou Tensei:\n"
    "  → + (10 × Skill Level) Critical Rate\n"
    "  → + (10 × Skill Level)% Physical Pierce\n"
    "- Ends when you use **Garyou Tensei**\n\n"

    "**Katana Main/Sub Bonus**:\n"
    "- Auto Attack Multiplier bonus: +0.5\n"
    "- Buff Duration: **tripled**\n\n"

    "**Notes**:\n"
    "- Works with **Rampage**: Skill Multiplier boost applies to first 10 auto attacks\n"
    "- Only affects main hand for Dual Swords"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210132490379284/kairikiranshin.png?ex=68059fc4&is=68044e44&hm=ec9595c2c3b8890058dce6efe25f818b1f43071c1640612044e0947f87205e11&"
},
"Bouncing Blade": {
  "title": "Bouncing Blade",
  "description": (
    "**Lv 3 Skill**\n"
    "Katana Main Only\n"
    "**MP Cost**: 100\n"
    "**Damage Type**: Physical\n\n"

    "**Base Stats**:\n"
    "- Multiplier: 2 + (0.2 × Skill Level)\n"
    "- Constant: 100 × 10 × Skill Level\n"
    "- Hit Count: 1 hit\n"
    "- Range: Katana Auto Attack Range\n\n"

    "**Skill Effect**:\n"
    "- If you receive damage during the skill's animation:\n"
    "  → The skill triggers a **counterattack** and deals damage\n"
    "  → You gain **(current Garyou Stacks + 2)**\n"
    "- If you don't get hit: No damage, no proration\n"
    "- Immune to Flinch, Tumble, Stun **while waiting to receive damage**\n\n"

    "**Buff Effect (if damage is taken)**:\n"
    "- HP Recovery: + (Skill Level × 10)% of the damage taken\n"
    "- MP Cost of **next skill**: **Halved**\n"
    "- Accuracy Boost: (Base Accuracy × Weapon ATK × (0.05 + 0.02 × Skill Level)%)\n\n"

    "**Game Description**: A defensive scabbard technique. Counterattacks if hit once, heals HP, reduces next skill MP cost, and increases accuracy."
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/869210141868851251/bouncingblade.png?ex=68059fc6&is=68044e46&hm=3411c5908fb6d0925a747ddb22e9ba4b0fd860b7ccfd630fcebd3e815b8eeb3f&"
},
"Kasumisetsu Getsuka": {
  "title": "Kasumisetsu Getsuka",
  "description": (
    "**Lv 5 Skill**\n"
    "Main Katana Only\n"
    "**MP Cost**: 500\n"
    "**Damage Type**: Physical\n\n"

    "**First 4 Hits**:\n"
    "- Multiplier: 7.5 + (0.75 × Skill Level)\n"
    "- Constant: 500\n"
    "- Hit Count: 4 hits (calculated once and split evenly)\n\n"

    "**Last Hit (or Zanyu Variant)**:\n"
    "- Multiplier: 1 + (Total DEX ÷ 250)\n"
    "- Constant: 200\n"
    "- If Tenryu Ransei is active:\n"
    "  → Multiplier: (1.5 + 0.25 × Tenryu Skill Lv) × Tenryu Stack + TotalDEX / (50 × (5 − Stack))\n"
    "  → Constant: 200\n"
    "- Hit Count: 1 (evaluated independently)\n\n"

    "**Effect**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- If **Tenryu Ransei buff** is active:\n"
    "  → Last hit becomes **Tenryu Ransei: Zanyu**\n"
    "  → Buff duration refreshed: 10 + (10 × Stack) sec (Bowtana: −10s penalty)\n"
    "  → Consumes 3 stacks; **2 stacks** if you successfully parry with this skill\n"
    "- If no Tenryu stack: Skill still usable, but no buff refresh\n\n"

    "**Defense**:\n"
    "- Slight **Physical/Magic Damage Reduction** during animation:\n"
    "  → Reduction% = SkillLv × 9 − (max(0, SkillLv × 9 − 50) ÷ 2)\n"
    "- Immune to **Flinch**, **Tumble**, **Stun**, and **Knockback** (even absolute variants)\n\n"

    "**Main Katana Only Bonuses**:\n"
    "- Last Hit / Zanyu:\n"
    "  → + (Base STR ÷ 5) Critical Rate\n"
    "  → + (Base DEX ÷ 5)% Physical Pierce\n"
    "- Using **Hasso Happa** immediately after this skill triggers **Sakura Ranman** special action\n\n"

    "**Miscellaneous**:\n"
    "- Default cast range = Weapon’s auto attack range\n"
    "- If used with bow (Bowtana): cast range follows **bow**\n"
    "- Does **not** give Perfect Aim or invincibility (unlike Zannou or Zantei)\n\n"

    "**Game Description**:\n"
    "“Attacks the target with a series of slashes and slightly reduces the damage received while it is active. Performs a special attack if Tenryu Ransei is in effect, and the number of times it is used determines the duration of the power increase.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967838736916316250/kasumisetsugetsuka.png?ex=68052e10&is=6803dc90&hm=23fd9599b87dac3c0c529d7d1523d5f9d3040ce9ec50e55be8d14b785cda1774&"
},
"Shadowless Slash": {
  "title": "Shadowless Slash",
  "description": (
    "**Lv 5 Skill**\n"
    "Main Katana Only\n"
    "**MP Cost**: 300\n"
    "**Damage Type**: Physical\n\n"

    "**Base Damage**:\n"
    "- Multiplier (all 5 hits): 4 + (0.5 × Skill Lv) + (Base DEX ÷ 200) + (Base AGI ÷ 200)\n"
    "- Constant: 300\n"
    "- Hit Count: 5 (calculated once, split evenly)\n"
    "- Cast Range: Weapon’s Auto Attack Max Range (Bowtana: follows bow range)\n\n"

    "**Skill Effects**:\n"
    "- Treated as an **Unsheathe Attack**\n"
    "- Ignores **Short Range Damage%** scaling regardless of distance\n"
    "- **Grants +2 Garyou stacks** on use\n"
    "- **Accuracy Bonus**: +200 × Skill Level\n"
    "- Grants ability to dash post-cast; successful dash gives Enhanced Auto-Attack buff (Bowtana excluded)\n\n"

    "**Main Katana Bonus**:\n"
    "- If **Garyou Stack = 10/10** and Garyou skill at max level:\n"
    "  → Using Garyou during Shadowless animation triggers **Divine Slash** (must occur within the hit animation window)\n"
    "  → Skill usage between them is allowed, but **Divine Slash** must activate within Shadowless hit window\n"
    "- **Divine Slash** Properties:\n"
    "  → Damage Type: Physical, Unsheathe, SRD%-affected\n"
    "  → Has **Perfect Aim**, **2s Invincibility**, and **cannot be evaded** unless forced/absolute evasion\n"
    "  → Triggers **Kairiki Ranshin** effect (based on Kairiki skill level)\n"
    "  → Stats:\n"
    "    • Multiplier: 30 + (Base Weapon ATK ÷ 100)\n"
    "    • Constant: 500 (no Armor Break) / 1000 (with Armor Break)\n"
    "    • Hit Count: 1\n"
    "    • + (10 × Kairiki Lv) Critical Rate\n"
    "    • + (10 × Kairiki Lv)% Physical Pierce\n\n"

    "**Buff (After Divine Slash lands)**:\n"
    "- Unsheathe ATK + TRUNC((Total STR + Total DEX) ÷ 51)%\n"
    "- Duration: 10 seconds\n\n"

    "**Proration Behavior**:\n"
    "- Shadowless Slash uses physical proration **on cast**\n"
    "- Physical proration is **inflicted at the end** of the animation\n"
    "- Recasting Shadowless before damage log cancels previous proration\n"
    "- **Divine Slash** damage is calculated immediately when text appears, not on landing\n"
    "- Combo “Shadowless → Garyou”: Divine Slash inherits Shadowless proration (−2 physical total)\n\n"

    "**Game Description**:\n"
    "“Rapidly slashes the enemy. It’s so fast that even the enemy doesn’t know when the katana leaves its scabbard. Attacks with high accuracy and grants 2 of Garyou Tensei’s buffs. You can move when sheathing the katana.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967838737180528750/muezan.png?ex=68052e10&is=6803dc90&hm=c10af8e47fb5c3ee2df10d3fa366e38284df08615aee4070ed5fa8e16e80e3d8&"
},
"Nukiuchi Sennosen": {
  "title": "Nukiuchi Sennosen",
  "description": (
    "**Lv 5 Skill**\n"
    "Main Katana Only\n"
    "**Type**: Passive\n\n"

    "**Charge Mechanic**:\n"
    "- Passive activates after charging for **(12 − Skill Level)** seconds by **not using any attacks**\n"
    "- Performing a **Katana Dash** reduces the charge time by **1 second**\n"
    "- At **Level 10**, a single Katana Dash instantly activates the glowing state\n"
    "- If any attack (auto or skill) is used before the charge completes, the timer resets\n\n"

    "**Glowing Effect (Once Charged)**:\n"
    "- Replaces Shukuchi Auto Attack’s multiplier with **400% of its normal value**\n"
    "- **Constant** increases as HP decreases:\n"
    "  → Constant = 1000 × (100% − Current HP%)\n"
    "  → Example: At 25% HP → Constant = 1000 × (1 − 0.25) = 750\n"
    "- **Stacks additively** with:\n"
    "  • Kairiki Ranshin auto multiplier buff\n"
    "  • Berserk buff\n"
    "  • Other multipliers\n"
    "- If **Enhanced Auto-Attack buff** is active (from Shukuchi dash), it will **double** this Nukiuchi Auto’s total damage\n\n"

    "**Special Interaction**:\n"
    "- If used with **Pulse Blade**, this passive transforms it into **Swift Pulse Blade**\n"
    "  → Swift Pulse Blade deals **5x** the normal Pulse Blade damage\n"
    "  → Note: Swift Pulse Blade does **not** contribute to proration\n\n"

    "**Game Description**:\n"
    "“A sword-drawing technique that is like a miracle. When not attacking for a certain period of time, the normal attack with Shukuchi will be greatly enhanced. The less HP you have, the more powerful it is.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967838736522047548/shukuchi.png?ex=68052e10&is=6803dc90&hm=29e32d7020acc334372f20a9a3c532f18ab5fb94dfde66bac706da60f111868f&"
},
"Dauntless": {
  "title": "Dauntless",
  "description": (
    "**Lv 5 Skill**\n"
    "Main Katana Only\n"
    "**Type**: Passive\n\n"

    "**Dauntless Stack Mechanic**:\n"
    "- Gains **1 stack every (12 − Skill Level)** seconds when fighting miniboss/boss\n"
    "- Max stacks: **100**\n"
    "- If no miniboss or boss is present: **Lose 1 stack every 2 seconds**\n"
    "- **Parry skills** (Magadachi, Zantei Settetsu, Bouncing Blade) give **+2 stacks** per successful parry\n"
    "- Killing a miniboss: **Lose 10%** of current stacks\n\n"

    "**Stack Threshold Buffs**:\n"
    "• **10+ stacks**: Accuracy + (Stack/10 × 10)\n"
    "• **20+ stacks**: Flat Weapon ATK + (Stack/10 × 5)\n"
    "• **30+ stacks**: Unsheathe Damage + (Stack/10)%\n"
    "• **40+ stacks**: Motion Speed +12.5%\n"
    "• **50+ stacks**:\n"
    "  - Gain a one-time **iFrame during Katana slide animation** (similar to Zantei iFrame; prevents GSW/Aura cancel)\n"
    "  - **Kasumisetsu Getsuka** consumes 1 less Tenryu Stack\n"
    "  - **Tenryu Ransei Base Multiplier** +1\n"
    "• **60+ stacks**: Flat Base Weapon ATK + (Stack/10 × 5)\n"
    "• **70+ stacks**: Unsheathe Damage + (Stack/10)% (additional)\n"
    "• **80+ stacks**: Motion Speed +12.5% (additional)\n"
    "• **90+ stacks**: MP Cost of all Mononofu skills is **halved**\n"
    "• **100 stacks**: Weapon ATK % increased by **(2 × weapon refine value)%**\n\n"

    "**Game Description**:\n"
    "“A strong determination to confront the enemy. Dauntless automatically accumulates when fighting against a powerful enemy. Grants various buffs for every 10 Dauntless points accumulated. The effects end when the enemy is defeated.”"
  ),
  "image_url": "https://cdn.discordapp.com/attachments/614452674137686022/967838736714956891/futoufukutsu.png?ex=68052e10&is=6803dc90&hm=9868f9b6bbb91d12a085a93d94c31201f661c0cb78e826c336f0e6ea2a11cb24&"
}









}