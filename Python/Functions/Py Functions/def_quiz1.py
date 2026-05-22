### TEST ZERO
demo_course_score = 80.6

def convert_score_to_letter(course_score):
    if course_score >= 90:
      return "A"
    elif course_score >= 80:
      return "B"
    elif course_score >= 70:
      return "C"
    elif course_score >= 60:
      return "D"
    else: 
      return "F"
    
print(convert_score_to_letter(demo_course_score))


### TEST ONE
demo_grades = {'NB0':100, 'NB1':87.5, 'NB2':100, 'NB4':75, 'NB5':70, 'NB7':100, 'NB9':50, 'NB10':100, 'NB11':77.5,
               'NB12':56.25, 'NB13':100, 'NB14':100, 'NB15':100, 'MT1':75, 'MT2':85, 'Final':85, 'Extra Credit':66.667}

demo_weights = [('NB0',2), ('NB1',4), ('NB2',4), ('NB4',4), ('NB5',4), ('NB7',4), ('NB9',4), ('NB10',4), ('NB11',4),
               ('NB12',4), ('NB13',4), ('NB14',4), ('NB15',4), ('MT1',10), ('MT2',15), ('Final',25), ('Extra Credit',3)]

def overall_grade(grades, weights):
    total_score = 0 
    # 'weight' represents the individual weight(s) in the tuple
    for weight in weights:
    # 'assignment' represents the first value in the tuple -- as the [key] for dictionary
      assignment = weight[0]
    # 'total_score' the sum of (grade * weight) / 100 iterated in the 'for' loop
      total_score += (grades[assignment] * weight[1]) / 100
    # 'return' the final sum (not indented) -- round 2 decimal places
    return (round(total_score, 2))

print(overall_grade(demo_grades, demo_weights))


### TEST TWO
demo_syllabus_words = ['the', 'a', 'utc', 'it', 'frequently', 'piazza', 'is', 'for', 'notebook', 'vocareum']
demo_important_words = {'utc', 'autograder', 'vocareum', 'notebook', '48-hour extension', 'proctored exams', 'piazza'}

def syllabus_words_importance(syllabus_words, important_words):
  words_list = []

  for words in syllabus_words:
      if words in important_words:
        words_list = words_list + [words]
      final_list = sorted(words_list)  
  return final_list[:3]
       
print(syllabus_words_importance(demo_syllabus_words, demo_important_words))


### TEST THREE
demo_exam_guidelines = {'Allowed': {'Online Resources': ['Google', 'Practice Exam Solutions'],
                                    'Physical Resources': ['Snacks'],
                                    'Technology': ['One Computer'],
                                   'Environment': ['Cats Making Noise', 'Music With Headphones'],
                                   'Misc': ['Short Breaks']},
                        'Not Allowed': {'Online Resources': ['ChatGPT', 'GitHub Copilot'],
                                       'Technology': ['Multiple Computer Screens'],
                                       'Environment': ['Talking with Friends or Family']}}

def find_guidelines(exam_guidelines):
    from collections import defaultdict
    guidelines = defaultdict(list)

    for outer in exam_guidelines:
        permission = exam_guidelines[outer]
        for types in permission:
            category = permission[types]
            for item in category:
                guidelines[types].append({item:outer})

    return dict(guidelines)

print(find_guidelines(demo_exam_guidelines))


### TEST FOUR
demo_distorted_str = '''Hi fam! Welcome to CSE 6040, no cap. I hope this course hits different, and you have
a total glow up from learning new data analysis techniques periodt. Don't @ me, but I think our team of TAs
slaps and will help you W the course.'''

demo_translation_dict = {'cowboy': {'Howdy': 'Hi', 'partners!': 'class!', 'Ah': 'I', 'wanna': 'want to',
                                    'extey-nd': 'extend', 'grand': 'very', 'ole': 'warm', 'ta': 'to', 'thuh': 'the',
                                    'ya': 'you', 'programmin': 'programming', 'ave': 'have', 'all-fired': 'great',
                                    'awf': 'of', 'eend': 'and', 'ahr': 'are', 'hair': 'here'},
                         'gen_z': {'fam!': 'class!', 'no': 'we are so glad', 'cap.': 'to have you.',
                                   'hits': 'challenges', 'different,': 'you,', 'total': 'great', 'glow': 'time',
                                   'up': 'as', 'from': 'you', 'learning': 'learn', 'periodt.': 'throughout the semester.',
                                   "Don't": 'I', '@': 'might be', 'me,': 'biased,', 'slaps': 'are fantastic',
                                   'W': 'succeed in'},
                         'shakespearean': {'Good': 'Greetings', 'morrow': 'new', 'class!': 'students!', 'wanteth': 'wanted',
                                           'extendeth': 'extend', 'warmeth': 'warm', 'welcometh': 'welcome',
                                           'desire': 'hope', 'thee': 'you', 'learneth': 'learn', "f'r": 'for',
                                           "has't": 'have', 'most': 'absolute', 'wondrous': 'best', 'Wondrous': 'Best',
                                           "instructeth'rs": 'instructors', 'art': 'are', "h're": 'here',
                                           'holp': 'help', 'succeedeth': 'succeed'}
                              }

demo_msg_style = 'gen_z'

def translate_msg(distorted_str, msg_style, translation_dict):
    translate_str = ''''''
    word_list = distorted_str.split()

    for word in word_list:
        try:
            translate_str += ' ' + translation_dict[msg_style][word]
        except:
            translate_str += ' ' + word

    return translate_str.strip()


print(translate_msg(demo_distorted_str, demo_msg_style, demo_translation_dict))


### PERSONAL TEST
list_one = [.10,.15,.20,.25,.30,.35,.40,.45,.50]
dict_one = {'A':10.99, 'B':5.65,'C':7.00,'D':9.89}

def markup_category(lists, dicts):
    final_dict = {}
    for item in dicts:
        price = dicts[item]
        markups = []
        for markup_per in lists:
            markup_price = round(price + (markup_per * price), 4)
            # adding to list of markup values
            markups.append(markup_price)
            # assigning items to markup values
        final_dict[item] = markups 
    return final_dict
    
print(markup_category(list_one, dict_one))