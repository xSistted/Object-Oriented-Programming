def add_score(subject_score, subject, score):
    for count in range(0, len(score)):
        subject_score[subject[count]] = score[count]
    return subject_score

def turn_to_list(all_subject_score, list_of_subject, list_of_score):
    for value in all_subject_score:
        if value == "{}":
            continue
        elif value.startswith("{"):
            value = value.replace("{", "").replace("}","")
            subject_scores = value.split(",")
            for subject_score in subject_scores:
                subject, score = subject_score.split(":")
                subject = subject.replace("'","")
                list_of_subject.append(subject)
                list_of_score.append(int(score))
        else:
            if not value.isdigit():
                value = value.replace("'", "")
                list_of_subject.append(value)
            else:
                list_of_score.append(int(value))

def new_dict(dict_of_score):
    return {key: value for key, value in dict_of_score.items() if key != "" and value >= 0}

def calc_average_score(dict_of_score):
    sum = 0
    for value in dict_of_score.values():
        sum += value
    average = sum / len(dict_of_score)
    return "%.2f" % average

dict_of_score = {}
list_of_subject = []
list_of_score = []
average = 0.00

all_subject_score = input()
all_subject_score = all_subject_score.replace(' ','').split('|')

turn_to_list(all_subject_score, list_of_subject, list_of_score)

dict_of_score = add_score(dict_of_score, list_of_subject, list_of_score)

dict_of_score = new_dict(dict_of_score)

if dict_of_score != {}:
    average = calc_average_score(dict_of_score)
    print(f"{dict_of_score}, Average score: {average}")
else:
    print(f"{dict_of_score}, Average score: {average}")
