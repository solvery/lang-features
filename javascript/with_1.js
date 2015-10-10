
function A() {
	this.v1 = 1;
}
var oa = new A();
with (oa) {
	// 直接访问属性
	v1 = 2;
} 


