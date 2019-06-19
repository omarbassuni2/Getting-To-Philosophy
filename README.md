# Getting-To-Philosophy
This is a script that plays the Getting To Philosophy
It tries to reach: https://en.wikipedia.org/wiki/Philosophy
It starts with a random wiki page using: https://en.wikipedia.org/wiki/Special:Random
It has Two functions:

find_first()
  Which scrapes the HTML and gets all paragraphs p then searches in each one of them
  for a link a tag, and returns the first it encounters

continue_crawling()
  checks if we're stuck in a loop or reached our destination
