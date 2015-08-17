alert=console.log

function Cat(name,color){
	this.name = name;
	this.color = color;
}
Cat.prototype.type = "猫科动物";
Cat.prototype.eat = function(){alert("吃老鼠")};

var cat1 = new Cat("大毛","黄色");
var cat2 = new Cat("二毛","黑色");
alert(cat1.type); // 猫科动物
cat1.eat(); // 吃老鼠

alert(cat1.eat == cat2.eat); //true

alert(Cat.prototype.isPrototypeOf(cat1)); //true
alert(Cat.prototype.isPrototypeOf(cat2)); //true

alert(cat1.hasOwnProperty("name")); // true
alert(cat1.hasOwnProperty("type")); // false

alert("name" in cat1); // true
alert("type" in cat1); // true

for(var prop in cat1) { alert("cat1["+prop+"]="+cat1[prop]); }

