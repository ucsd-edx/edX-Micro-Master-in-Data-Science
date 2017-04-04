def U_matching_subexpressions(params):
  """ Written by yfreund Tue Oct 13 2015 20:00:50 GMT-0700 (PDT)
  Finds matching subexpressions and reports them.
  """
  matches=find_matches(params)
  hint=''
  for item in matches:
    if item[0]=='R':
      continue
    value=item[1]
    if value >20 or int(value)!=value:
      hint+='The subexpression %s is correct'%item[3]
      if item[2]!=item[3]:
      	hint+=', it can also be written as %s'%item[2]
      hint+='\n'
      #print hint,
  return hint
