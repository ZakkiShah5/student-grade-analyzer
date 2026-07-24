

students = [
    {"name": "Ana", "score": 85},
    {"name": "Bob", "score": 45},
    {"name": "Cid", "score": 92},
    {"name": "Dan", "score": 60},
    {"name": "Eve", "score": 73}
]

score_list = []
at_risk = []
grade_count = {}

def get_grade(score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

max_score = {}
min_score = {}
for s in students:
    score = s['score']
    name = s['name']
    score_list.append(score)   
    print(f'{name} scored {score} with {get_grade(score)} grade')
    if score < 60:
        at_risk.append(name)
    grade = get_grade(score)
    grade_count[grade] = grade_count.get(grade, 0) + 1
    
    
for s in students:
    score = s['score']
    name = s['name']
    if max(score_list) == score:
        print(f'{name} got the highest grade with score: {score}')
        max_score['name'] = name 
        max_score['score'] = score 
    elif min(score_list) == score:
        print(f'{name} got the lowest grade with score: {score}')
        min_score['name'] = name
        min_score['score'] = score




class_avg = sum(score_list)/len(score_list)
print(f'Class average score is {class_avg}.')
print(f'These students are at risk: {at_risk}')
print(grade_count)


print('---- Class Summary ----')
print(f'Average: {class_avg}')
print(f'Highest: {max_score['name']} ({max_score['score']})')
print(f'Lowest: {min_score['name']} ({min_score['score']})')
print(f'Grade Distribution: {grade_count}')
print(f'At risk: {at_risk}')