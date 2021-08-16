var x = 0;

while (x < 5 ){
    console.log("x is currently: " + x);
    
    if (x === 3){
        console.log("X IS EQUAL TO THREE");
        break;
    }

    console.log("x is still less than 5, adding 1 to x");
    x++;
}

// Write a while loop that prints out
// only the even numberrs from 1 to 10

var y = 1;

while (y < 11){
    if (y%2 === 0){
        console.log(y);
    }
    y++;
}
