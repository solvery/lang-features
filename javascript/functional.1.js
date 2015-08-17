// coolshell/10169.html

// pair
function make_pair(x, y) {
    // 返回一个支持get_left和get_right操作的闭包(Closure)
    return {
        get_left : function() { return x },
        get_right : function() { return y }
    }
}
function get_left(pair) {
    return pair.get_left();
}
function get_right(pair) {
    return pair.get_right();
}
// Test case
console.log(get_left(make_pair(1, 2))) //1
console.log(get_right(make_pair(1, 2))) //2

// stack
function make_stack() {
    return null
}
function push(stack, x) {
    return {
        top : function() { return x },
        pop : function() { return stack }
    }
}
function top(stack) {
    return stack.top()
}
function pop(stack) {
    return stack.pop()
}
// Test case
var stack = make_stack()
stack = push(stack, 1)
stack = push(stack, 2)
stack = push(stack, 3)
console.log(top(stack)) //3
stack = pop(stack)
console.log(top(stack)) //2
stack = push(stack, 4)
console.log(top(stack)) //4

//// list
function empty() {
    return null
}
function singleton(e) {
    return {
        first: function() { return e },
        rest: function() { return null }
    }
}
function first(list) {
    return list.first()
}
function rest(list) {
    return list.rest()
}
function append(list1, list2) {
    if (null == list1) return list2
    if (null == list2) return list1

    return {
        first : function() { return first(list1) },
        rest : function() { return append(rest(list1), list2) }
    }
}

// 二叉树迭代器：

function make_binary_tree_iterator(node) {
    return {
        first : function() {
            return null != node.left ? first(make_binary_tree_iterator(node.left)) : node
        },
        rest : function() {
            var left_it = (null == node.left ? null : make_binary_tree_iterator(node.left))
            var root_it = singleton(node)
            var right_it = (null == node.right ? null : make_binary_tree_iterator(node.right))
            var it = append(append(left_it, root_it), right_it)
            return rest(it)
        }
    }
}
//======== Test case ========
var tree = {
    value : 1,
        left : {
            value : 2,
            left : { value : 4, left : null, right : null },
            right : null
        },
        right : {
            value : 3,
            left : null,
            right : { value : 7, left : null, right : null }
    }
}
for (var it = make_binary_tree_iterator(tree); null != it; it = rest(it)) {
    console.log(first(it).value)
}


