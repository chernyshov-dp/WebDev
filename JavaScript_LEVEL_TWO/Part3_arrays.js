var country1 = "Russia";
var country2 = "USA";
var country3 = "China";
var countries = ["Russia", "USA", "China"];

countries[0];
countries[1];

countries[2] = "France";
countries;

var mixed = [true, 20, "string"];
mixed.length;

// pop()
var myArr = ["one", "two", "three"];
var lastItem = myArr.pop(); // "three"
myArr; // ["one", "two"]

// push()
myArr.push("new_item");
myArr; // ["one", "two", "new_item"]

myArr[myArr.length - 1];

// Nested arrays
var matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];

// Array iteration
var arr = ["A", "B", "C"];
for(var i = 0; i < arr.length; i++){
    console.log(arr[i]);
}

for (letter of arr){
    console.log(letter);
}

for (letter of arr){
    alert(letter);
}

arr.forEach(alert);

function addAwesome(name) {
    console.log(name + " is awesome!");
}

var topics = ["python", "django", "science"];
topics.forEach(addAwesome);
