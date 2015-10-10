alert=console.log

// 严格模式
// www.ruanyifeng.com/blog/2013/01/javascript_strict_mode.html

'use strict';


function strict(){
    "use strict";
    v2 = 1; 
    return "这是严格模式。";
}

function notStrict() {
    return "这是正常模式。";
}
//
// 全局变量必须显式声明
/// v1 = 1; 

// 静态绑定
// no with
function A() {
}
var oa = new A();
/// with (oa) { } 

var x = 2;
alert(eval("var x=5; x"))
alert(x);

