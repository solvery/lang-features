alert=console.log
// "极简主义法"（minimalist approach）
// 这种方法不使用this和prototype
// 用一个对象模拟"类"。在这个类里面，定义一个构造函数createNew()，用来生成实例。

var Animal = {
createNew: function(){
			   var animal = {};
			   animal.sleep = function(){ alert("睡懒觉"); };
			   return animal;
		   }
};


var Cat = {
sound : "ha ha ha",
createNew: function(){
			   //var cat = {};
			   var cat = Animal.createNew();	// 继承 
			   var sound1 = "he he he";		// 私有属性
			   cat.makeSound = function(){ alert(Cat.sound); };
			   cat.changeSound = function(x){ Cat.sound = x; };
			   return cat;
		   }
};

var cat1 = Cat.createNew();
cat1.makeSound(); // 喵喵喵

var cat2 = Cat.createNew();
cat2.sleep(); // 睡懒觉

alert(cat2.sound1);
cat2.makeSound();
cat2.changeSound("he ha ha");
cat2.makeSound();

