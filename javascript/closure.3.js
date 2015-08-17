alert=console.log

// 1 匿名自执行函数
var datamodel = {  
    table : [],  
    tree : {}  
};  
   
(function(dm){  
    for(var i = 0; i < dm.table.rows; i++){  
       var row = dm.table.rows[i];  
       for(var j = 0; j < row.cells; i++){  
           drawCell(i, j);  
       }  
    }  
     
    //build dm.tree    
})(datamodel); 

// 2缓存
function SearchBox() {};
var CachedSearchBox = (function(){  
    var cache = {},  
       count = [];  
    return {  
       attachSearchBox : function(dsid){  
           if(dsid in cache){//如果结果在缓存中  
              return cache[dsid];//直接返回缓存中的对象  
           }  
           var fsb = new SearchBox(dsid);//新建  
           cache[dsid] = fsb;//更新缓存  
           if(count.length > 100){//保正缓存的大小<=100  
              delete cache[count.shift()];  
           }  
           return fsb;        
       },  
   
       clearSearchBox : function(dsid){  
           if(dsid in cache){  
              cache[dsid].clearSelection();    
           }  
       }  
    };  
})();  
   
CachedSearchBox.attachSearchBox("input1");  

// 3 实现封装
var person = function(){  
    //变量作用域为函数内部，外部无法访问  
    var name = "default";     
     
    return {  
       getName : function(){  
           return name;  
       },  
       setName : function(newName){  
           name = newName;  
       }  
    }  
}();  
   
alert(person.name);//直接访问，结果为undefined  
alert(person.getName());  
person.setName("abruzzi");  
alert(person.getName());  
 
// 提供类的模板机制
function Person(){  
    var name = "default";     
     
    return {  
       getName : function(){  
           return name;  
       },  
       setName : function(newName){  
           name = newName;  
       }  
    }  
};  
   
   
var john = Person();  
alert(john.getName());  
john.setName("john");  
alert(john.getName());  
   
var jack = Person();  
alert(jack.getName());  
jack.setName("jack");  
alert(jack.getName());  
 

