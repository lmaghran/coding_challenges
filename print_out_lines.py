string_list= ['Hello,', 'world!', 'I', 'love', 'Python', 'and', 'Hackbright']

def recursive_sum(string_list, printed_words=""):
  if string_list==[]:
    return

  else:
    printed_words=printed_word_pre_pop+ string_list.pop(0)
    if len(printed_words)>=10:
      print(printed_word_pre_pop)

    else:
      recursive_sum(string_list, printed_word_pre_pop)

recursive_sum(string_list)