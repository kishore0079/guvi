var expected = {foo: 5,bar: 6};
var actual = {foo: 5, bar: 6}
function assertObjectsEqual(actual, expected){
    
    var eq=JSON.stringify(actual) === JSON.stringify(expected) 
 if(eq)
 {
     return true;
 }
 else{
     return false;
 }
}
console.log(assertObjectsEqual(actual, expected));
console.log(Object.keys(expected).length)
