// Simple Number Guessing Game

let randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

function checkGuess() {
    const userInput = document.getElementById("guessInput").value;
    const result = document.getElementById("result");

    attempts++;

    if (userInput == randomNumber) {
        result.innerHTML = `🎉 Correct! You guessed the number in ${attempts} attempts.`;
        result.style.color = "green";
    }
    else if (userInput > randomNumber) {
        result.innerHTML = "📈 Too High! Try Again.";
        result.style.color = "orange";
    }
    else {
        result.innerHTML = "📉 Too Low! Try Again.";
        result.style.color = "red";
    }
}

function restartGame() {
    randomNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;

    document.getElementById("guessInput").value = "";
    document.getElementById("result").innerHTML = "Game Restarted! Start Guessing.";
}
