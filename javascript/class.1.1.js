
//我们可以看到， 其用function来做class。
var Person = function(name, email, website){
	this.name = name;
	this.email = email;
	this.website = website;

	this.sayHello = function(){
		var hello = "Hello, I'm "+ this.name  + ", \n" +
			"my email is: " + this.email + ", \n" +
			"my website is: " + this.website;
		alert(hello);
	};
};

var chenhao = new Person("Chen Hao", "haoel@hotmail.com",
		"http://coolshell.cn");
chenhao.sayHello();
