
def pCons(list: List[Int]): String = list match {  
	case Nil => "nil"
	case x::xs => "(" + x + "." + pCons(xs) + ")"
} 
