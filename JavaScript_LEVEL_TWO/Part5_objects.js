// PART 1
var carInfo = {make: "Toyota", year: 1990, model: "Camry"};
carInfo;
carInfo["make"];

var myNewO = {a: "hello", b: [1, 2, 3], c: {inside: ["a", "b"]}};
myNewO["a"];
myNewO["b"][1];
myNewO["c"]["inside"][1];

carInfo["year"] = 2006;
carInfo["year"] += 1;
carInfo["year"];

// The way to see all the properties of a specified JavaScript object
// in console by which the developer can easily get the properties of the object.
console.dir(carInfo);

// There is no specific order in the object
for (key in carInfo){
    console.log(key);
    console.log(carInfo[key]);
}


// PART 2
var myObj = {
    prop: 37,
    reportProp: function() {
        return this.prop;
    }
}
console.log(myObj.reportProp());

var simple = {
    prop: "Hello",
    myMethod: function() {
        console.log("The myMethob was called");
    }
}
simple;
console.dir(simple);
simple.myMethod();

var myNewObj = {
    name: "Daniil",
    greet: function () {
        console.log("Hello, " + this.name + "!");
    }
}
myNewObj.greet();
