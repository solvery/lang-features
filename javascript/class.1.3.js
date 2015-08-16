// http://coolshell.cn/articles/6668.html

function Base() {
	this.id = "base"
}

// var obj = new Base();
// 等于下面的代码
var obj  = {};
obj.__proto__ = Base.prototype;
Base.call(obj);

Base.prototype.toString = function() {
	return this.id;
}

// new 继承
function Derive(id) {
	this.id = id;
}
Derive.prototype = new Base();
Derive.prototype.test = function(id){
	return this.id === id;
}
var newObj = new Derive("derive");

// create 继承
// ECMAScript V5

function object(old) {
   function F() {};
   F.prototype = old;
   return new F();
}
var newObj = object(oldObject);

var base ={
  id:"base",
  toString:function(){
          return this.id;
  }
};
var derive = object(base);


