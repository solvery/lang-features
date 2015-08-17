alert=console.log

var Chinese = {
nation:'中国'
};
var Doctor ={
career:'医生'
}

function object(o) {
	function F() {}
	F.prototype = o;
	return new F();
}

var Doctor = object(Chinese);
Doctor.career = '医生';

alert(Doctor.nation); //中国

function extendCopy(p) {
	var c = {};
	for (var i in p) { 
		c[i] = p[i];
	}
	c.uber = p;
	return c;
}
var Doctor = extendCopy(Chinese);
Doctor.career = '医生';
alert(Doctor.nation); // 中国

// 浅拷贝
Chinese.birthPlaces = ['北京','上海','香港'];
var Doctor = extendCopy(Chinese);
Doctor.birthPlaces.push('厦门');
alert(Doctor.birthPlaces); //北京, 上海, 香港, 厦门
alert(Chinese.birthPlaces); //北京, 上海, 香港, 厦门

// 深拷贝
function deepCopy(p, c) {
	var c = c || {};
	for (var i in p) {
		if (typeof p[i] === 'object') {
			c[i] = (p[i].constructor === Array) ? [] : {};
			deepCopy(p[i], c[i]);
		} else {
			c[i] = p[i];
		}
	}
	return c;
}

var Doctor = deepCopy(Chinese);
Chinese.birthPlaces = ['北京','上海','香港'];
Doctor.birthPlaces.push('厦门');
alert(Doctor.birthPlaces); //北京, 上海, 香港, 厦门
alert(Chinese.birthPlaces); //北京, 上海, 香港

