alert=console.log

// use function to create class
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

delete chenhao['email']
chenhao.sayHello();
