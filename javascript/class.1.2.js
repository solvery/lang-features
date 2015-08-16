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
