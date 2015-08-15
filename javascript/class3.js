alert=console.log
　　function Cat(name,color){
	　　　　this.name = name;
	　　　　this.color = color;
	　　　　this.type = "猫科动物";
	　　　　this.eat = function(){alert("吃老鼠");};
	　　}
	　　var cat1 = new Cat("大毛","黄色");
	　　var cat2 = new Cat ("二毛","黑色");
	　　alert(cat1.type); // 猫科动物
	　　cat1.eat(); // 吃老鼠
	alert(cat1.eat == cat2.eat); //false
