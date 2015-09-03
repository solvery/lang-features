// http//blog.csdn.net/g9yuayon/article/details/1271319

alert=console.log

function fact(n){
	if(n == 0){
		return 1;
	}

	if(n > 0){
		return n * fact(n - 1);
	}
}

fact3 = function(himself, n){
	if( n < 2 ){
		return 1;
	}

	return n * himself(himself, n-1);
}

r=fact3(fact3, 3) 
alert(r)

//
	fact4 = function(himself){
		return function(n){
			if( n < 2 ){
				return 1;
			}

			return n * himself(himself)(n-1);
		}
	}

function f(q){
	return function(n){
		if(n < 2){
			return 1;
		}

		return n * q(n-1);
	}
}

function fact5(h){
	return function(n){
		return f(h(h))(n);
	}
}

function Y(f){
	g = function(h){
		return function(x){
			return f(h(h))(x);
		}
	}

	return g(g);
}

//
fact6 = Y(
		function(h){
		return function(n){
		if(n < 2){
		return 1;
		}

		return n * h(n-1);
		}
		}
		); 


