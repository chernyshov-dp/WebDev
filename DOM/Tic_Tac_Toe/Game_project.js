var restartButton = document.querySelector("#restart")
var squares = document.querySelectorAll("td")

function clearTable() {
    for (var i = 0; i < squares.length; i++) {
        squares[i].textContent = "";
    }
}

restartButton.addEventListener("click", clearTable)

function changeMarker() {
    if (this.textContent == "") {
        this.textContent = "X";
    } else if (this.textContent == "X") {
        this.textContent = "O";
    } else {
        this.textContent = "";
    }
}

for (var i = 0; i < squares.length; i++){
    squares[i].addEventListener("click", changeMarker)
}
