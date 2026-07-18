from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# This updated list holds question types, answer choices, and image filenames
LOVE_QUESTIONS = [
    {
        "id": 1,
        "type": "multiple_choice",
        "q": "When was our very first met?",
        "options": ["A coffee shop", "University campus", "Visa consulate office", "Dorm canteen"],
        "correct": "Visa consulate office",
        "hint": "Think passport...",
        "image": "us1.jpg"
    },
    {
        "id": 2,
        "type": "text",
        "q": "What was my dress colour when I sing 'Love Story' with you?",
        "correct": "white",
        "hint": "the colour I wear many times!",
        "image": "us2.jpg"
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "q": "Do you think I'm your soulmate forever?",
        "options": ["Yes, absolutely!", "Yes, a thousand times!", "Of course!", "All of the above"],
        "correct": "All of the above",
        "hint": "There are no wrong answers here, but one choice is perfect.",
        "image": "us3.jpg"
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "q": "What did we eat after coming back from visa office?",
        "options": ["螺蛳粉", "老友粉", "桂林米粉", "炒饭"],
        "correct": "螺蛳粉",
        "hint": "Think spicy and hot...",
        "image": "us4.jpg"
    },
    {
        "id": 5,
        "type": "text",
        "q": "What is my favorite Vietnamese dish?",
        "correct": "Bun Cha",
        "hint": "Think delicious Vietnamese grilled pork and noodles",
        "image": "us5.jpg"
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "q": "What is the day we go 'Guangxi Wonderful camp'?",
        "options": ["Dec 06,2025", "Nov 6th-10th,2025", "Oct 20th,2025", "Nov 3rd,2025"],
        "correct": "Nov 6th-10th,2025",
        "hint": "We became closer on those days!",
        "image": "us6.jpg"
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "q": "How many days did I come to Hanoi?",
        "options": ["5 days", "6 days", "8 days", "7 days"],
        "correct": "7 days",
        "hint": "It was more than a few days!",
        "image": "us7.jpg"
    },
    {
        "id": 8,
        "type": "text",
        "q": "What nickname do I call you the most?",
        "correct": "little dragon",
        "hint": "It's the English translation of your name!",
        "image": "us8.jpg"
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "q": "The date you proposed me",
        "options": ["Nov 15th,2025", "Oct 15th,2025", "Nov 10th,2025", "Dec 31st,2025"],
        "correct": "Nov 15th,2025",
        "hint": "It's sure before I gave you my answer back.",
        "image": "us9.jpg"
    }, # <-- Added the missing closing brace and comma here!
    {
        "id": 10,
        "type": "text",
        "q": "Will you be my future husband? Yes or No",
        "correct": "Yes",
        "hint": "Yes only, if 'No' I will kill you",
        "image": "us10.jpg"
    }
] # <-- Added the missing closing square bracket here!


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/question/<int:q_id>', methods=['GET', 'POST'])
def question(q_id):
    q_idx = q_id - 1
    if q_idx < 0 or q_idx >= len(LOVE_QUESTIONS):
        return redirect(url_for('victory'))

    current_q = LOVE_QUESTIONS[q_idx]
    error = None

    if request.method == 'POST':
        user_answer = request.form.get('answer', '').strip()

        if current_q['type'] == 'text':
            is_correct = user_answer.lower() in current_q['correct'].lower() or current_q['correct'].lower() in user_answer.lower()
        else:
            is_correct = user_answer == current_q['correct']

        if is_correct:
            next_id = q_id + 1
            if next_id > len(LOVE_QUESTIONS):
                return redirect(url_for('victory'))
            return redirect(url_for('question', q_id=next_id))
        else:
            error = "Oops! That's not it, try again my love! 💕"

    return render_template('question.html', question=current_q, total=len(LOVE_QUESTIONS), error=error)


@app.route('/victory')
def victory():
    return render_template('victory.html')

@app.route('/letter')
def letter():
    return render_template('letter.html') # This loads the separate letter page!

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)