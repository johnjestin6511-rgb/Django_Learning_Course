var FirstName = prompt("Hello and welocome please enter your first Name")
var SecondName = prompt("Hello and welocome please enter your Second Name")
var Age = prompt("Hpw old are you?")
var Height = prompt("What is your height in cm?")
var Pet = prompt("What is your pet's name?")
alert("Thank you so much for the information.")

if (FirstName[0]===SecondName[0] && Age>20 && Age<30 && Height>170 && Pet[Pet.length-1]==="y"){
    console.log("Welcome Spy");
}
else {
    console.log("Nothing to see here");
}