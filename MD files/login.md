# Login Pseudo-Code

open database

create cursor

When user run ~login:

  alter table - add new column if not exists, and set default value to 0.

  if ((column exists) and (value = 0) and (time < 48)):
    update value

    if value < 8:
      update value

    else:
      update value to 1

  else:
    update value to 0 and reset timer
