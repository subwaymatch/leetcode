import java.util.HashSet;
import java.util.Set;

class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> emailSet = new HashSet<String>();
        
        for (String email : emails) {
            StringBuffer sb = new StringBuffer();
            boolean isLocalName = true;
            boolean isLocalIgnored = false;
            
            for (char c : email.toCharArray()) {
                if (isLocalName) {
                    if (c == '@') {
                        sb.append("@");
                        isLocalName = false; 
                    }
                    
                    else if (isLocalIgnored || c == '.') 
                        continue;
                    else if (c == '+')
                        isLocalIgnored = true;
                    else
                        sb.append(c);
                }
                
                else
                    sb.append(c);
            }
            
            emailSet.add(sb.toString());
        }
        
        return emailSet.size();
    }
}
