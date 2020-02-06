var array = [[["firstName", "Vasanth"], ["lastName", "Raja"], ["age", 24], ["role", "JSWizard"]], [["firstName","Sri"], ["lastName", "Devi"], ["age", 28], ["role", "Coder"]]];
 function transformEmployeeData(array) {
    var list= [];
    var d={}
    for(i=0;i<array.length;i++)
    {
        d={};
        for(j=0;j<array[i].length;j++)
        {
            d[array[i][j][0]]=array[i][j][1];
        }
        list.push(d);
        
    }    
    
    return list;
   }
console.log(transformEmployeeData(array));
