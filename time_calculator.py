def add_time(start, duration, *day):

    # I started with parsing the datetime in order to separate hours from minutes
      statement = ''
      start = start.rstrip()
      duration = duration.rstrip()
      s = start.split(' ')
      h = s[0].split(':')
      d = duration.split(':')

      if (not h[0].isnumeric() or not h[1].isnumeric()) or (not d[0].isnumeric() or not d[1].isnumeric()):
        return 'We only accept digits.'

      # I'll use this variable to convert later on to 24h format
      merid = s[1]
    
      # start hours and minutes
      hs = int(h[0])
      ms = int(h[1])
    
      # duration hours and minutes
      hd = int(d[0])
      md = int(d[1])

      # the list have been used to get the right index based on how many days
      check_day = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']

      # changing AM/PM format to 24h in order to have a easy calculation
      if merid == 'PM':
          hs += 12

      # doing the maths and converting it in a 24h plus increasing days when applicable
      new_hours = hs + hd
      new_minutes = ms + md
      if new_minutes > 60:
          new_hours += 1
          new_minutes -= 60

      new_day = 0
      if new_hours > 24:
          new_day += int(new_hours // 24)
          new_hours = new_hours % 24
          if new_day == 1:
              statement = '(next day)'
          if new_day > 1:
              statement = f'({new_day} days later)'

      # back again to AM/PM form as challenge required
      if new_hours > 0 and new_hours < 12:
          mer = 'AM'
      elif new_hours == 12:
          mer = 'PM'
      elif new_hours > 12:
          mer = 'PM'
          new_hours -= 12
      else:
          mer = 'AM'
          new_hours += 12

      # z.fill() helps to add a 0 if minutes are < 9 and make it as 01, 02, 03 instead 1, 2, 3 and so on.
      new_minutes = str(new_minutes).zfill(2)

      # if day should provided we can add it and change it using index() based on how many days are past, we basically shift the actually index based on new_day
      if day:
          day = day[0].lower().capitalize()
          i = check_day.index(day)
          # [(i+new_day)%7] this will make sure to loop over the list at the right index
          if i == 0:
              return f'{new_hours}:{new_minutes} {mer}, {check_day[i]}{statement}'
          return f'{new_hours}:{new_minutes} {mer}, {check_day[(i+new_day)%7]} {statement}'

    # make sure this part is out from the loop, this part is the case when *day is not provided
    if new_day == 0:
        return f'{new_hours}:{new_minutes}, {mer}'
    else:
        return f'{new_hours}:{new_minutes}, {mer} {statement}'
       
