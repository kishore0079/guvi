var obj = {name: "ISRO", age: 35, role: "Scientist"};
  var m=[]
  function convertListToObject(obj) {
   Object.entries(obj).forEach(([key,value])=>
   {
        m.push([key,value])
   });
  }
  convertListToObject(obj);
console.log(m)
