function isOperator(v) {
	return ['+', '-', '*', '/'].includes(v); 
}

/**
 * @param {string[]} tokens
 * @return {number}
 */
function evalRPN(tokens) {
	var operandsStack = []; 
	var result = null; 

	tokens.forEach(function(v) {
		if (isOperator(v)) {
			var right = operandsStack.pop();
			var left = operandsStack.pop();

			switch(v) {
				case '+':
					operandsStack.push(left + right); 
					break; 
				case '-':
					operandsStack.push(left - right);
					break;
				case '*':
					operandsStack.push(left * right); 
					break; 
				case '/':
					operandsStack.push(Math.trunc(left / right)); 
					break; 
				default:
					break; 
			}
		} else {
			operandsStack.push(parseInt(v)); 
		}
	});

	return operandsStack.pop(); 
}
