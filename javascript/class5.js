alert=console.log

function Animal(){
	    this.species = "动物";
	  }

	function Cat(name,color){
		    this.name = name;
		    this.color = color;
		  }

function Cat(name,color){
	    Animal.apply(this, arguments);
	    this.name = name;
	    this.color = color;
	  }

	  var cat1 = new Cat("大毛","黄色");
	  alert(cat1.species); // 动物

Cat.prototype = new Animal(); //完全删除了prototype 对象原先的值，然后赋予一个新值。
  Cat.prototype.constructor = Cat;
  var cat1 = new Cat("大毛","黄色");
  alert(cat1.species); // 动物
alert(Cat.prototype.constructor == Animal); //true
alert(cat1.constructor == Cat.prototype.constructor); // true
alert(cat1.constructor == Animal); // true


function Animal(){ }
  Animal.prototype.species = "动物";

Cat.prototype = Animal.prototype;
  Cat.prototype.constructor = Cat;
  var cat1 = new Cat("大毛","黄色");
  alert(cat1.species); // 动物

Cat.prototype.constructor = Cat;
alert(Animal.prototype.constructor); // Cat


var F = function(){};
  F.prototype = Animal.prototype;
  Cat.prototype = new F();
  Cat.prototype.constructor = Cat;

alert(Animal.prototype.constructor); // Animal

function extend(Child, Parent) {

	    var F = function(){};
	    F.prototype = Parent.prototype;
	    Child.prototype = new F();
	    Child.prototype.constructor = Child;
	    Child.uber = Parent.prototype;
	  }

extend(Cat,Animal);
  var cat1 = new Cat("大毛","黄色");
  alert(cat1.species); // 动物

function extend2(Child, Parent) {
	    var p = Parent.prototype;
	    var c = Child.prototype;
	    for (var i in p) {
		      c[i] = p[i];
		      }
	    c.uber = p;
	  }

extend2(Cat, Animal);
  var cat1 = new Cat("大毛","黄色");
  alert(cat1.species); // 动物





