alert=console.log

// 作用

// 闭包中局部变量是引用而非拷贝
function say667() {
    // Local variable that ends up within closure
    var num = 666;
    var sayAlert = function() { alert(num); }
    num++;
    return sayAlert;
}

var sayAlert = say667();
sayAlert()

// 多个函数绑定同一个闭包，因为他们定义在同一个函数内。
function setupSomeGlobals() {
    // Local variable that ends up within closure
    var num = 666;
    // Store some references to functions as global variables
    gAlertNumber = function() { alert(num); }
    gIncreaseNumber = function() { num++; }
    gSetNumber = function(x) { num = x; }
}
setupSomeGlobals(); // 为三个全局变量赋值
gAlertNumber(); //666
gIncreaseNumber();
gAlertNumber(); // 667
gSetNumber(12);//
gAlertNumber();//12

// 当在一个循环中赋值函数时，这些函数将绑定同样的闭包
function buildList(list) {
    var result = [];
    for (var i = 0; i < list.length; i++) {
        var item = 'item' + list[i];
        result.push( function() {alert(item + ' ' + list[i])} );
    }
    return result;
}

function testList() {
    var fnlist = buildList([1,2,3]);
    // using j only to help prevent confusion - could use i
    for (var j = 0; j < fnlist.length; j++) {
        fnlist[j]();
    }
}

// 外部函数所有局部变量都在闭包内，即使这个变量声明在内部函数定义之后。
function sayAlice() {
    var sayAlert = function() { alert(alice); }
    // Local variable that ends up within closure
    var alice = 'Hello Alice';
    return sayAlert;
}
var helloAlice=sayAlice();
helloAlice();

// 每次函数调用的时候创建一个新的闭包

function newClosure(someNum, someRef) {
    // Local variables that end up within closure
    var num = someNum;
    var anArray = [1,2,3];
    var ref = someRef;
    return function(x) {
        num += x;
        anArray.push(num);
        alert('num: ' + num +
        '\nanArray ' + anArray.toString() +
        '\nref.someVar ' + ref.someVar);
    }
}
closure1=newClosure(40,{someVar:'closure 1'});
closure2=newClosure(1000,{someVar:'closure 2'});

closure1(5); // num:45 anArray[1,2,3,45] ref:'someVar closure1'
closure2(-10);// num:990 anArray[1,2,3,990] ref:'someVar closure2'

// Singleton 单件：

var singleton = function () {
    var privateVariable;
    function privateFunction(x) {
        //...privateVariable...
    }

    return {
        firstMethod: function (a, b) {
            //...privateVariable...
        },
        secondMethod: function (c) {
            //...privateFunction()...
        }
    };
}();


