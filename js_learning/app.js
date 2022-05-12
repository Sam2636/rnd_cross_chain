
//list--------------------------------> accessing
var myData = []; 

myData.push(1); // add at the end 
console.log(myData); // prints [1] 

myData.unshift(2); // add to the top 
console.log(myData); // prints [2,1] 

// Arrays are zero index based: 
console.log(myData[0]); // prints 2 


//example------------------------------>2
var arr2 = [];
s=arr2.length;
console.log(s);
var arr3 = [ 'cat', 'rat', 'bat' ];
console.log(arr3.length);


//examle------------------------------------>3

var arr3 = [ 'cat', 'rat', 'bat' ];
for (var i = 0; i < arr3.length; i++) {
    console.log(arr3[i]);
}

//example--------------------------------->4
console.log('splice')
console.log('removes --->item')

var arr3 = [ 'cat', 'rat', 'bat', 'cat', 'rat', 'bat' ];
arr3.splice(1, 1);
console.log(arr3);
console.log(arr3.length);

console.log('--------------------------------')
console.log('mapping')
//example ------------------------------->mappinf
const numbers = [65, 44, 12, 4];
const newArr = numbers.map(myFunction)

function myFunction(num) {
  console.log( num +1);
}

console.log('------------------------------')
console.log('foreach')
const fruits = ["apple", "orange", "cherry"];
fruits.forEach(function(item){console.log(item)})



console.log('------------------------------')
console.log('sorting----')
const fruit = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits.sort());
console.log(fruits.reverse());