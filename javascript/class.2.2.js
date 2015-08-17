alert=console.log

function Cat(name,color){
	this.name=name;
	this.color=color;
}
var cat1 = new Cat("大毛","黄色");
var cat2 = new Cat("二毛","黑色");

console.log(cat1.name); // 大毛
console.log(cat1.color); // 黄色

console.log((cat1.constructor == Cat));
alert(cat2.constructor == Cat); //true

alert(cat1 instanceof Cat);
alert(cat2 instanceof Cat);
