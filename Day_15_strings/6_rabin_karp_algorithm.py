'''
###################### Repeated String Match ######################
Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.

Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".


leetcode : https://leetcode.com/problems/repeated-string-match/

'''


# it can be solved with the help of Rabin Karp algorithm.
# Rabin Karp algorithm : It is used to find the pattern in the text.
# youtube : https://www.youtube.com/watch?v=qQ8vS2btsxIs


# solution
# solution written in C++
'''
class Solution {
private:
    int BASE = 1000000;
public:
    int repeatedStringMatch(string A, string B) {
        if(A == B) return 1;
        int count = 1;
        string source = A;
        while(source.size() < B.size()){
            count++;
            source+=A;
        }
        if(source == B) return count;
        if(Rabin_Karp(source,B) != -1) return count;
        if(Rabin_Karp(source+A,B) != -1) return count+1;
        return -1;
    }


    int Rabin_Karp(string source, string target){
        if(source == "" or target == "") return -1;
        int m = target.size();
        int power = 1;
        for(int i = 0;i<m;i++){
            power = (power*31)%BASE;
        }
        int targetCode = 0;
        for(int i = 0;i<m;i++){
            targetCode = (targetCode*31+target[i])%BASE;
        }
        int hashCode = 0;
        for(int i = 0;i<source.size();i++){
            hashCode = (hashCode*31 + source[i])%BASE;
            if(i<m-1) continue;
            if(i>=m){
                hashCode = (hashCode-source[i-m]*power)%BASE;
            }
            if(hashCode<0)
                hashCode+=BASE;
            if(hashCode == targetCode){
                if(source.substr(i-m+1,m) == target)
                    return i-m+1;
            }
        }
        return -1;
    }
};

'''