alert=console.log

//创建对象
var chenhao = Object.create(null);
 
//设置一个属性
 Object.defineProperty( chenhao,
                'name', { value:  'Chen Hao',
                          writable:     true,
                          configurable: true,
                          enumerable:   true });
 
//设置多个属性
Object.defineProperties( chenhao,
    {
        'email'  : { value:  'haoel@hotmail.com',
                     writable:     true,
                     configurable: true,
                     enumerable:   true },
        'website': { value: 'http://coolshell.cn',
                     writable:     true,
                     configurable: true,
                     enumerable:   true }
    }
);

// Get/Set 访问器
var  age = 0;
Object.defineProperty( chenhao,
            'age', {
                      get: function() {return age+1;},
                      set: function(value) {age = value;},
                      enumerable : true,
                      configurable : true
                    }
);
chenhao.age = 100; //调用set
alert(chenhao.age); //调用get 输出101（get中+1了）;

// 利用已有的属性(age)通过get和set构造新的属性(birth_year)：

Object.defineProperty( chenhao,
            'birth_year',
            {
                get: function() {
                    var d = new Date();
                    var y = d.getFullYear();
                    return ( y - this.age );
                },
                set: function(year) {
                    var d = new Date();
                    var y = d.getFullYear();
                    this.age = y - year;
                }
            }
);

alert(chenhao.birth_year);
chenhao.birth_year = 2000;
alert(chenhao.age);

//列出对象的属性.
function listProperties(obj)
{
    var newLine = "";
    var names = Object.getOwnPropertyNames(obj);
    for (var i = 0; i < names.length; i++) {
        var prop = names[i];
        alert(prop + newLine);

        // 列出对象的属性配置（descriptor）动用getOwnPropertyDescriptor函数。
        var descriptor = Object.getOwnPropertyDescriptor(obj, prop);
        for (var attr in descriptor) {
            alert("..." + attr + ': ' + descriptor[attr]);
            alert(newLine);
        }
        alert(newLine);
    }
}

listProperties(chenhao);




