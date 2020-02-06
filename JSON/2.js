var obj = {name :"rajinikanth", age : 33, hasPets : false};
var t=[]
function printAllKeys(obj) {
    Object.entries(obj).forEach(([key,val])=>{
        t.push(key);
    });
  console.log(t)
  t.forEach((item,index)=>{
      console.log(item);
  });
   }
