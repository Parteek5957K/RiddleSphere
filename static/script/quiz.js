let currentPuzzleNumber = 1;

function loadPuzzle(direction) {
    if (direction === 'forward') {
        currentPuzzleNumber += 1;
    } else if (direction === 'backward') {
        currentPuzzleNumber -= 1;
    }
    if (currentPuzzleNumber < 1) {
        currentPuzzleNumber = 5;
    } else if (currentPuzzleNumber > 5) {
        currentPuzzleNumber = 1;
    }

    fetch(`/puzzle/${currentPuzzleNumber}/`)
        .then(response => response.text())
        .then(data => {
            document.getElementById('puzzle-content').innerHTML = data;
        })
        .catch(error => console.error('Error fetching puzzle:', error));
}

let answers = 0;

function checkAnswer() {

    const userAnswer = document.getElementById('answer').value;

    fetch('/bunker-room/get_answer/')
        .then(response => response.json())
        .then(data => {
            const expectedAnswers = data.answers;
            const correctAnswer = expectedAnswers[currentPuzzleNumber - 1];
            if (String(userAnswer) === correctAnswer) {
                answers += 1;
                alert('Correct answer!');
            } else {
                alert('Incorrect answer. Try again.');
            }
            if (answers > 4) {
                window.parent.toggleDisplay();
            }
        })
        .catch(error => console.error('Error fetching answers:', error));
}

document.getElementById('answer').addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
        checkAnswer();
      }
    });
document.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowLeft') {
        loadPuzzle('backward');
      }
    });
document.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight') {
        loadPuzzle('forward');
      }
    });