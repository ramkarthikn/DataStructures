class TrieNode:
    def __init__(self,letter):
        self.letter = letter 
        self.children= {} 
        self.is_end_of_word= False
class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    def add_word(self,word):
        cur_node = self.root 
        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter]= TrieNode(letter)
            cur_node = cur_node.children[letter]
        cur_node.is_end_of_word = True 
    def does_word_exist(self,word):
        if word =="":
            return True 
        curr_node= self.root 
        for letter in word:
            if letter not in curr_node.children:
                return False 
            curr_node= curr_node.children[letter]
        return curr_node.is_end_of_word

trie = Trie()
trie.add_word("karthik")
trie.add_word("karthi")
print(trie.does_word_exist("karthi"))