var obj = {name :"rajinikanth", age : 33, hasPets : false};
var t=[]

function printAllValues(obj) {
Object.entries(obj).forEach(([key,val])=>{
      t.push(val);
  });
console.log(t)
t.forEach((item,index)=>{
    console.log(item);
}); 
}
