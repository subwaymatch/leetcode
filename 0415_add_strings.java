class Solution {
    public String addStrings(String num1, String num2) {
        String sNum = num1.length() > num2.length() ? num2 : num1;
        String lNum = sNum == num1 ? num2 : num1;
        
        int carry = 0;
        StringBuffer sb = new StringBuffer(); 
        
        for (int si = sNum.length() - 1, li = lNum.length() - 1; li >= 0; si--, li --) {
            int sum = (si >= 0) ? (sNum.charAt(si) + lNum.charAt(li) - ('0' * 2) + carry) : (lNum.charAt(li) - '0' + carry);
            carry = sum / 10;
            sum %= 10; 
            
            sb.append(String.valueOf(sum));
        }
        
        if (carry > 0) sb.append("1"); 
        
        return sb.reverse().toString();
    }
}
