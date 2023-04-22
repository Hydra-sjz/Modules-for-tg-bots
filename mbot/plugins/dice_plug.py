import re
from random import randint
from mbot.global_functions import log
from telethon import client, events, errors


@events.register(events.NewMessage(pattern=r"/roll(@\w+)?\s+((?:\d*d\d+\s*)+)$"))
async def on_roll(event):
    m = event.pattern_match

    ## check whether m.group(1) `(@\w+)` exists, and is the username of the bot
    usr_group = m.group(1)
    username = (await event.client.get_me()).username
    if usr_group and username not in usr_group:
        return


    dice_pattern = r"(\d*)d(\d+)" # the pattern to apply to m.group(2)
    dice_match = re.finditer(dice_pattern, m.group(2))

    outputs = list()
    total = int()
    output_strings = list()

    roll_limit = 0
    for d in dice_match:
        if roll_limit == 20: # cap the amount of dice/roll pairs at 20
            break

        ## set the amount of rolls to 1 if n in nd6 is not specified
        rolls = 1
        if d.group(1):
            rolls = int(d.group(1))

        sides = int(d.group(2)) # how many "sides" the dice has

        ## limit the amount of rolls and sides
        if rolls > 500 or sides > 100000:
            await event.respond("The maximum rolls is 500, and the maximum amount of sides is 100,000.")
            await log(event, info="Bad roll")
            return

        output_strings.append(f"**{rolls}d{sides}:**") # add the dice/roll pair to the output string

        ## quick maffs: sort each roll's result, and sum up all results
        val = list()
        for _ in range(0, rolls):
            r = randint(1, sides)
            val.append(str(r))
            total += r

        outputs.extend(val)
        output_strings.append(f"`{' '.join(val)}`") # add each result to the output string
        roll_limit += 1

    ## if there's more than one roll, reply with the total added to the end
    if len(outputs) > 1:
        output_strings.append(f"**=** `{total}`")

    output = "\n".join(output_strings)

    await log(event)    # Logs the event
    try:
        await event.respond(f"{output}")
    except errors.MessageTooLongError:
        await event.respond(f"**Total =** `{total}`\n"
                            + "Tip:  Message was too long, try rolling less dice next time")
