var Person = Object.create(null);

Object.defineProperties
(
    Person,
    {
        'name'  : {  value: 'Chen Hao'},
        'email'  : { value : 'haoel@hotmail.com'},
        'website': { value: 'http://coolshell.cn'}
    }
);

Person.sayHello = function () {
    var hello = "<p>Hello, I am "+ this.name  + ", <br>" +
                "my email is: " + this.email + ", <br>" +
                "my website is: " + this.website;
    document.write(hello + "<br>");
}

var Student = Object.create(Person);
Student.no = "1234567"; //学号
Student.dept = "Computer Science"; //系

//使用Person的属性
document.write(Student.name + ' ' + Student.email + ' ' + Student.website +'<br>');

//使用Person的方法
Student.sayHello();

//重载SayHello方法
Student.sayHello = function (person) {
    var hello = "<p>Hello, I am "+ this.name  + ", <br>" +
                "my email is: " + this.email + ", <br>" +
                "my website is: " + this.website + ", <br>" +
                "my student no is: " + this. no + ", <br>" +
                "my departent is: " + this. dept;
    document.write(hello + '<br>');
}
//再次调用
Student.sayHello();

//查看Student的属性（只有 no 、 dept 和 重载了的sayHello）
document.write('<p>' + Object.keys(Student) + '<br>');

Student.name = 'aaa';

//输出 aaa
document.write('<p>' + Student.name + '</p>');

//输出 Chen Hao
document.write('<p>' +Object.getPrototypeOf(Student).name + '</p>');

//新版的重载SayHello方法
Student.sayHello = function (person) {
    Object.getPrototypeOf(this).sayHello.call(this);
    var hello = "my student no is: " + this. no + ", <br>" +
                "my departent is: " + this. dept;
    document.write(hello + '<br>');
}

function Composition(target, source)
{
    var desc  = Object.getOwnPropertyDescriptor;
    var prop  = Object.getOwnPropertyNames;
    var def_prop = Object.defineProperty;

    prop(source).forEach(
        function(key) {
            def_prop(target, key, desc(source, key))
        }
    )
    return target;
}

//艺术家
var Artist = Object.create(null);
Artist.sing = function() {
    return this.name + ' starts singing...';
}
Artist.paint = function() {
    return this.name + ' starts painting...';
}

//运动员
var Sporter = Object.create(null);
Sporter.run = function() {
    return this.name + ' starts running...';
}
Sporter.swim = function() {
    return this.name + ' starts swimming...';
}

Composition(Person, Artist);
document.write(Person.sing() + '<br>');
document.write(Person.paint() + '<br>');

Composition(Person, Sporter);
document.write(Person.run() + '<br>');
document.write(Person.swim() + '<br>');

//看看 Person中有什么？（输出：sayHello,sing,paint,swim,run）
document.write('<p>' + Object.keys(Person) + '<br>');
