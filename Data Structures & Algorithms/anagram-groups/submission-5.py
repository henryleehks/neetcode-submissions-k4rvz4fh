class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        return_list = []
        
        for i in range(len(strs)):
            word = strs[i]
            sorted_word = ''.join(letter for letter in sorted(word))
            if sorted_word in hashmap:
                hashmap[sorted_word].append(i)
            else:
                hashmap[sorted_word] = [i]
        
        for k in hashmap:
            v = hashmap[k]
            words_list = []
            for i in v:
                words_list.append(strs[i])
            return_list.append(words_list)
        
        return return_list