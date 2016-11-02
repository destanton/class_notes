console.log("Getting Started with JS");

var myNumber = 10 / 90;
console.log(myNumber);

var myArray = [10, "joel", [90, 23, 10], "peanut"];
console.log(myArray[2][1]);

// for counter, item in enumerate(array): in python

for (var i = 0 ; i < myArray.length ; i++){
    // var item = myArray[i];
    console.log(myArray[i]);

} // don't need semicolon on for loop

var myObject = {
  "myName": "danielle",
  "myAge": 29

};

console.log(myObject["myName"]);
console.log(myObject.myName);

// def blahblah(): in python
// js functions

var myFunc = function(x, y) {
  return x * y;
};
console.log(myFunc(9, 4)); // positional arguments

var sillyArray = [9, 4, 5, 3];

var loopFunc = function(item) {
  console.log(item);
}; // not doing much, just printing, but going to be used below

sillyArray.forEach(loopFunc); // for each item in sillyarray vall loopfunc. different way to do a for loop, but doesn't look like a for loop

sillyArray.forEach(function(item){ // has no name, cannot be reused.
  console.log(item);
});
