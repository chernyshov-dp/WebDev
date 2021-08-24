var player1 = prompt("Player One: Enter Your Name , you will be Blue");
var player1Color = "rgb(86, 151, 255)";

var player2 = prompt("Player Two: Enter Your Name, you will be Red");
var player2Color = "rgb(237, 45, 73)";

var table = $("table tr");

var turn = 1;
var cell = 0;

function reportWin(rowNum, colNum) {
    console.log(`You won! row: ${rowNum} col: ${colNum}`);
}

function changeColor(rowIndex, colIndex, color) {
    return table.eq(rowIndex).find("td").eq(colIndex).find("button").css("background-color", color);
}

function returnColor(rowIndex, colIndex) {
    return table.eq(rowIndex).find("td").eq(colIndex).find("button").css("background-color");
}

function checkBottom(colIndex) {
    var colorReport = returnColor(5, colIndex);
    for (var row = 0; row > -1; row--) {
        colorReport = returnColor(row, colIndex);
        if (colorReport === "rgb(128, 128, 128)") {
            return row;
        }
    }
}

function colorMatchCheck(one, two, three, four) {
    return (one === two && obe === three && one === four && one !== "rgb(128, 128, 128)" && one !== undefined);
}

function horizontalWinCheck(){
    return 0;
}

function VerticalWinCheck() {
    return 0;
}

function diagonalWinCheck(p) {
    return 0;
}