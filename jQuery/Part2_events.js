$("h1").click(function() {
    $(this).text("I was changed!");
})

$("li").click(function() {
    console.log("Any li was clicked!");
})

// KEY PRESS
$("input").eq(0).keypress(function(event) {
    if (event.which === 13) { // 13 is "Enter" button
        $("h3").toggleClass("turnBlue");
    }
    console.log(event);
})

// on()
$("h1").on("dblclick", function() {
    $(this).toggleClass("turnBlue");
})

$("h1").on("mouseenter", function() {
    $(this).toggleClass("turnBlue");
})

$("input").eq(1).on("click", function() {
    $(".container").fadeOut(3000);
})

$("input").eq(1).on("click", function() {
    $(".container").slideUp(3000);
})
