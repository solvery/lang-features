
var chenhao = {
    name: "Chen Hao",
    email: "haoel@hotmail.com",
    website: "http://coolshell.cn",
    age: 100,
    get birth_year() {
        var d = new Date();
        var y = d.getFullYear();
        return ( y - this.age );
    },
    set birth_year(year) {
        var d = new Date();
        var y = d.getFullYear();
        this.age = y - year;
    }

};
alert(chenhao.birth_year);
chenhao.birth_year = 2000;
alert(chenhao.age);

