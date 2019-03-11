/**
 * @param {string} s
 * @return {boolean}
 */
function isPalindrome(s) {
	if (s.length <= 1) return true; 

	let loopUntil = Math.floor(s.length / 2)

	var s = s.toLowerCase(); 
	var left = 0; 
	var right = s.length - 1; 

	while (left < right) {
		if (!isAlphaNumeric(s[left])) {
			left++;
			continue; 
		}
		else if (!isAlphaNumeric(s[right])) {
			right--; 
			continue; 
		}
		else if (s[left] == s[right]) {
			left++; 
			right--; 
			continue; 
		}
		else {
			return false; 
		}
	}

	return true; 
}

function isAlphaNumeric(c) {
	return ((c >= 'a' && c <= 'z') || (c >= '0' && c <= '9'));
}
