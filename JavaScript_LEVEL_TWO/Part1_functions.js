function helloYou(name) {
    console.log("Hello, " + name + "!");
}

function addNum(num1, num2) { 
    console.log(num1 + num2);
}

// addNum("2", 2); -> 22

function helloSomeone(name="Frankie") {
    console.log("Hello, " + name);
}


// Let's use return
function formal(name="Sam", title="Sir") {
    return title + " " + name;
}

function timesFive(numInput) {
    // Local scope to the function
    var result = numInput * 5;
    return result;
}

// Global scope
var v = "GLOBAL V";
var stuff = "GLOBAL STUFF";

function fun(stuff) {
    console.log(v);
    stuff = "Reassign stuff inside func";
    console.log(stuff);
}

fun();
console.log(stuff);
