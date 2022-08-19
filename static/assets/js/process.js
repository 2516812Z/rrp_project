$(".step01").click( function() {
    $(".discovery").addClass("active").siblings().removeClass("active");
});

$(".step02").click( function() {
    $(".strategy").addClass("active").siblings().removeClass("active");
});

$(".step03").click( function() {
    $(".creative").addClass("active").siblings().removeClass("active");
});

$(".step04").click( function() {
    $(".production").addClass("active").siblings().removeClass("active");
});

$(".step05").click( function() {
    $(".analysis").addClass("active").siblings().removeClass("active");
});

$("#color").click( function() {
    $("body").toggleClass("blue")
});