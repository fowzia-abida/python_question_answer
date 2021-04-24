from app import Questions

question_paper= [
    "(1)what is the color of the sky \n a)blue  b)green  c)yellow\n",
    "(2)what is the closesz planet to Earth? \n a)mars  b)marcury  c)venus\n"
]

question_solve_object = [
   Questions(question_paper[0], "a"),
    Questions(question_paper[1], "b")



]

def run_function(question_solve_object):
    score= 0
    for new in question_solve_object:
        users_answer = input(new.show_ques)
        if users_answer== new.show_ans:
              score += 1
    print(f'you got {score}/{len(question_solve_object)}')
run_function(question_solve_object)